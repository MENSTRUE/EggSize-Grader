from pydantic import BaseModel, Field

class Detection(BaseModel):
    class_id: int
    label: str
    confidence: float
    box_xyxy: list[float] = Field(min_length=4,max_length=4)

class PredictionResponse(BaseModel):
    model: str
    image_width: int
    image_height: int
    detections: list[Detection]
    counts: dict[str,int]
    total: int
    inference_ms: float
    warning: str = "Image-based labels are not calibrated physical measurements."
