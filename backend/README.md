# Backend — FastAPI + trusted YOLOv8n

## Purpose and implementation
Local research inference. API code lives in `app/main.py`, `app/api/routes/health.py` and `predict.py`; `app/core/config.py` configures model path and upload limits; `app/inference/yolo.py` validates images and synchronizes model inference; `app/schemas/prediction.py` defines response. `app/services/` currently contains only `__init__.py` and is not a feature.

## Run (project root)
```powershell
cd "D:\porto\100 day\day 38"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r backend\requirements.txt
python -m pytest backend\tests -v
python -m uvicorn backend.app.main:app --reload --port 8000
```
Open a **second** PowerShell terminal:
```powershell
cd "D:\porto\100 day\day 38\frontend"
npm install
npm run build
npm run dev
```
API `http://127.0.0.1:8000/docs`; UI `http://127.0.0.1:5173`. Local checkpoint `models/best.pt` must be supplied from the saved Kaggle artifact because `.gitignore` excludes `*.pt`.

## Routes and contracts
| Method | Route | Real behavior |
|---|---|---|
| GET | `/api/v1/health` | Liveness, reports whether model already loaded; **does not load it** |
| GET | `/api/v1/ready` | Attempts trusted checkpoint load, returns `ready`, `checkpoint_exists`, classes, load error |
| GET | `/api/v1/model` | Model metadata; **not readiness** |
| POST | `/api/v1/predict` | Multipart image upload and real CPU YOLO inference |

### Predict input
`file`: JPEG, PNG or WEBP, up to **10 MiB**; `confidence`: default 0.35, `[0.05,0.95]`; `iou`: default 0.50, `[0.10,0.90]`. Pillow verifies image and enforces 25 MP. EXIF orientation is applied. Neither arbitrary URLs nor batch uploads are supported.

### Response
```json
{"model":"YOLOv8n / best.pt","image_width":640,"image_height":480,"detections":[],"counts":{"large":0,"medium":0,"small":0},"total":0,"inference_ms":0.0,"warning":"Image-based labels are not calibrated physical measurements."}
```
**Contract illustration only; not an inference result.** Real detections have `class_id`, `label`, `confidence` in `[0,1]`, `box_xyxy` (4 pixel values). Error statuses: 413 excessive bytes; 415 media type; 422 invalid/empty image; 503 unavailable model. A 200 response with 0 objects is possible.

## Configuration and security
Actual config names: `EGG_MODEL_PATH`, `EGG_MAX_IMAGE_BYTES` (default 10485760), `EGG_MAX_PIXELS` (default 25000000), `EGG_CORS_ORIGINS` (localhost/127.0.0.1:5173). `MODEL_PATH` defaults to root `models/best.pt`; note root `.env.example` contains `MODEL_PATH` but this is **not read** by current backend. Run at project root. Only trusted local PyTorch checkpoints should be loaded. No auth, per-user quota, rate limit, TLS termination or production deployment is implemented.

## Testing and troubleshooting
`python -m pytest backend/tests -v`: four contract/negative tests. User-reported local run: 4 passed, 1 `StarletteDeprecationWarning`. Verify `GET /api/v1/ready` and a real image separately; tests don't grade box correctness. `Torch ... +cpu` and `CUDA=False` are expected for the installed CPU environment; inference is coded with `device='cpu'`. HTTP 503 means missing/incompatible model; see checkpoint on disk and `classes`. See [full deployment guidance](../docs/en/deployment.md) and [Indonesian troubleshooting](../docs/id/troubleshooting.md).
