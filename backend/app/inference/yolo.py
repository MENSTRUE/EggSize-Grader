import io
import threading
import time
from PIL import Image, ImageOps, UnidentifiedImageError
from fastapi import HTTPException
from backend.app.core.config import MODEL_PATH, MAX_PIXELS, CLASSES

class EggDetector:
    def __init__(self):
        self._model = None
        self._lock = threading.Lock()
        self.load_error = None

    @property
    def ready(self):
        return self._model is not None

    def load(self):
        if self._model is not None:
            return
        with self._lock:
            if self._model is not None:
                return
            try:
                if not MODEL_PATH.is_file():
                    raise FileNotFoundError(f"Checkpoint missing: {MODEL_PATH}")
                from ultralytics import YOLO
                model = YOLO(str(MODEL_PATH)) # trusted, local checkpoint only
                raw = model.names
                names = [str(raw[i]).strip().lower() for i in range(len(raw))] if isinstance(raw,dict) else [str(n).strip().lower() for n in raw]
                if names != CLASSES:
                    raise ValueError(f"Expected {CLASSES}, checkpoint provides {names}")
                self._model=model
                self.load_error=None
            except Exception as exc:
                self.load_error=f"{type(exc).__name__}: {exc}"
                raise

    def predict(self, data: bytes, conf: float, iou: float):
        try:
            Image.MAX_IMAGE_PIXELS = MAX_PIXELS
            with Image.open(io.BytesIO(data)) as raw:
                raw.verify()
            with Image.open(io.BytesIO(data)) as raw:
                if raw.width*raw.height>MAX_PIXELS:
                    raise ValueError('Image too large in pixels')
                image=ImageOps.exif_transpose(raw).convert('RGB')
        except (UnidentifiedImageError,ValueError,OSError,Image.DecompressionBombError) as exc:
            raise HTTPException(status_code=422,detail=f"Invalid image: {exc}")
        try:
            self.load()
        except Exception:
            raise HTTPException(status_code=503,detail='Model is unavailable; check server logs and checkpoint')
        start=time.perf_counter()
        # Guard inference on the single loaded model
        with self._lock:
            result=self._model.predict(source=image, conf=conf, iou=iou, verbose=False, device='cpu')[0]
        elapsed=(time.perf_counter()-start)*1000
        detections=[]; counts={name:0 for name in CLASSES}
        for b in result.boxes:
            cid=int(b.cls[0].item()); label=CLASSES[cid]
            detections.append({'class_id':cid,'label':label,'confidence':round(float(b.conf[0].item()),5),'box_xyxy':[round(float(v),2) for v in b.xyxy[0].tolist()]})
            counts[label]+=1
        return {'model':'YOLOv8n / best.pt','image_width':image.width,'image_height':image.height,'detections':detections,'counts':counts,'total':len(detections),'inference_ms':round(elapsed,2)}

detector=EggDetector()
