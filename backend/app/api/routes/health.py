from fastapi import APIRouter
from backend.app.inference.yolo import detector
from backend.app.core.config import MODEL_PATH, CLASSES

router=APIRouter(tags=['system'])
@router.get('/health')
def health():
    return {'status':'ok','model_loaded':detector.ready}

@router.get('/ready')
def ready():
    if not detector.ready:
        try: detector.load()
        except Exception: pass
    return {'ready':detector.ready,'checkpoint_exists':MODEL_PATH.is_file(), 'classes':CLASSES,'error':detector.load_error}

@router.get('/model')
def model():
    return {'name':'EggSizeGrader YOLOv8n','task':'object-detection','classes':CLASSES, 'checkpoint_exists': MODEL_PATH.is_file(),'measurement':'relative labeled categories, not weight or dimensions'}
