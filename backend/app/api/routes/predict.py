from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from backend.app.core.config import MAX_IMAGE_BYTES
from backend.app.inference.yolo import detector
from backend.app.schemas.prediction import PredictionResponse

router=APIRouter(tags=['inference'])

@router.post('/predict',response_model=PredictionResponse)
async def predict(file: UploadFile=File(...),confidence:float=Form(0.35,ge=0.05,le=0.95),iou:float=Form(0.5,ge=0.1,le=0.9)):
    if file.content_type not in ('image/jpeg','image/png','image/webp'):
        raise HTTPException(status_code=415,detail='Use JPEG, PNG or WEBP')
    data=await file.read(MAX_IMAGE_BYTES+1)
    if len(data)>MAX_IMAGE_BYTES:
        raise HTTPException(status_code=413,detail=f'Max upload size is {MAX_IMAGE_BYTES} bytes')
    if not data:
        raise HTTPException(status_code=422,detail='Empty file')
    return detector.predict(data,confidence,iou)
