from pathlib import Path
import os

PROJECT_ROOT = Path(__file__).resolve().parents[3]
MODEL_PATH = Path(os.getenv("EGG_MODEL_PATH", str(PROJECT_ROOT / "models" / "best.pt")))
MAX_IMAGE_BYTES = int(os.getenv("EGG_MAX_IMAGE_BYTES", "10485760"))
MAX_PIXELS = int(os.getenv("EGG_MAX_PIXELS", "25000000"))
ALLOWED_ORIGINS = [s.strip() for s in os.getenv("EGG_CORS_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173").split(',') if s.strip()]
CLASSES = ['large', 'medium', 'small']
