from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.core.config import ALLOWED_ORIGINS
from backend.app.api.routes import health, predict

app=FastAPI(title='EggSizeGrader API',version='0.1.0',description='Research-only object detection for three annotated egg-size categories.')
app.add_middleware(CORSMiddleware,allow_origins=ALLOWED_ORIGINS,allow_credentials=False,allow_methods=['GET','POST'],allow_headers=['*'])
app.include_router(health.router,prefix='/api/v1')
app.include_router(predict.router,prefix='/api/v1')
