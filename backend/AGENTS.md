# Backend AGENTS.md

Inherit all root [agent rules](../AGENTS.md). Keep `backend/app/main.py` with routers from `api/routes/{health,predict}.py`, configuration in `core/config.py`, inference in `inference/yolo.py` and Pydantic contract in `schemas/prediction.py`. The `services/` directory is reserved but contains no service code in the audited repository.

**Trusted checkpoint:** only load local `models/best.pt` from the user's validated Kaggle artifacts; never auto-download arbitrary `.pt` files, use untrusted weights, or report fake detections. Expected `model.names`: `large`, `medium`, `small`. Endpoint health=API liveness; ready=checkpoint load status; predict=real YOLO. Handle JPEG/PNG/WEBP, ≤10 MiB, and 25 MP pixel limit. Keep HTTP 415/413/422/503 meaningful, no debug stack traces in public responses. Actual YOLO `.predict(device='cpu')` in existing code; do not claim CUDA.

**Quality gate:** `python -m pip check`, `python -m pytest backend/tests -v`, and actual POST image with verified return schema and known label; a four-test contract suite is not a model-accuracy suite. No auth, rate-limit or production server hardening exists. Document any additions and update bilingual API docs. Never change report metrics or raw dataset as side effect of backend work.
