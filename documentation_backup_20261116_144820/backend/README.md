# Backend — EggSizeGrader

FastAPI service using the **actual local trusted** `models/best.pt` YOLOv8n checkpoint. From project root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r backend\requirements.txt
python -m uvicorn backend.app.main:app --reload --port 8000
```

API: `GET /api/v1/health`, `/ready`, `/model`, `POST /api/v1/predict` (multipart `file`, `confidence` 0.05–0.95, `iou` 0.1–0.9). Documentation at `http://127.0.0.1:8000/docs`. `/ready` loads and validates the model; `/health` only checks server liveness. Inference uses CPU for portability; change device after benchmarking if desired. An unavailable checkpoint results in 503, never a mock prediction.

`python -m pytest backend/tests -q` runs contract and upload-validation tests; integration testing with the true checkpoint must also be run locally. Do not expose this development service to the public without authentication, rate limits, reverse proxy, upload hardening and a security review. Images are processed in memory and not intentionally stored; server/network logs remain environment-dependent.
