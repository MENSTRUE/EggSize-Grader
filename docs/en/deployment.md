# Deployment — EggSizeGrader

**EggSizeGrader** is Day 38 of the [100 Days of Projects](https://github.com/MENSTRUE) portfolio. It detects bounding boxes and annotated classes (`large`, `medium`, `small`) in egg photographs using a validation-selected YOLOv8n checkpoint. The project joins a leakage-aware Kaggle experiment, local FastAPI inference, and a React/TypeScript analysis interface. **It does not measure physical diameter or weight and is not an official commercial grading system.**

## 24. Per-class behavior and confusion matrix

On held-out test, **large** has the lowest AP@50–95 (77.01%); medium reaches 89.84% and small 85.99%. **No test confusion-matrix asset exists in the audited repository**; therefore, no confusion-matrix values are claimed. Object detection errors require IoU-based matching, not classification-only accuracy.

## 25. Error analysis and interpretation

The moderate relative weakness of `large` warrants qualitative review of missed boxes and class confusion. The saved test prediction grid provides visual examples, but the repository does not present a quantitative FP/FN breakdown by cause. Domain shift between cameras and lighting is not measured.

## 29. Repository layout

Preserves existing root: `README.md`, `AGENTS.md`, `LICENSE`, `.env.example`, `.gitignore`; `notebooks/`, `models/`, `reports/`, `assets/{plots,examples,screenshots,diagrams}`, `backend/`, `frontend/`, `docs/`, `scripts/`. See [architecture](architecture.md). Raw datasets and `.pt` weights are deliberately excluded.

## 30. System requirements

Windows PowerShell example uses Python 3.11, pip, Node.js/npm and local CPU inference; GPU not required for the current backend. Training used Kaggle T4. Downloading dependencies may be heavy on slow networks.

## 31. Setup and installation

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

## 32. Run and usage examples

Open API docs at `http://127.0.0.1:8000/docs`. Check `/api/v1/ready`: `ready=true` means a model was loaded and classes validated. Browse/select a test image, choose thresholds, click Generate detections, inspect boxes and counts, then download annotated PNG or CSV.

## 33. End-to-end testing

Local user-reported test: `4 passed, 1 warning` under pytest on Windows/Python 3.11; tests cover health, model contract, MIME rejection, corrupt image. The attached screenshot indicates successful **one real local inference**: 13 medium boxes, about 2,869 ms. It does not establish correctness for all boxes. No automated E2E browser suite is present.

## 34. Reproducibility and lineage

Notebook `notebooks/eggsizegrader.ipynb` encodes dataset audit, split seed 42, 60-epoch configuration, evaluation and artifact ZIP creation. `reports/` preserves split membership and SHA-256 source inventory. The runtime was Kaggle Python 3.13.16 with Ultralytics 8.4.213; local installation log showed Python 3.11.9 and a later package version. Dependency ranges are not byte-identical environment locking.

## 35. Visual evidence

![Original annotation examples](../../assets/examples/ground_truth_samples.png)
*Ground-truth YOLO boxes from the training examples; not model predictions.*

![Dataset EDA](../../assets/plots/dataset_eda.png)
*Recorded split/class distribution and boxes per image.*

![Held-out prediction grid](../../assets/plots/heldout_prediction_grid.png)
*Saved prediction visualization from the experiment; the grid is qualitative rather than a statistical accuracy measurement.*

![Local application with detections](../../assets/screenshots/Screenshot%202026-11-16%20135615.png)
*Local browser screenshot: 13 detected objects, all displayed as `medium`, around 2,869 ms inference on that particular run. A successful inference demonstration, not an independent ground-truth correctness check.*

## 36. Deployment readiness

**Research-local only.** Vite dev proxy, unrestricted local upload endpoint and CPU performance are not deployment certification. Require auth, rate limits, HTTPS, file and decompression limits, privacy review, packaging of trusted weights, logging/monitoring and a production service configuration.

## Source material and verification

All numeric results above originate from the checked-in experiment reports, not from new computation in this documentation update. The original study includes a single architecture; the local image screenshot is a demonstration, not evidence of physical-size correctness.

[Repository README](../../README.md) · [reports](../../reports/README.md) · [notebook](../../notebooks/eggsizegrader.ipynb)
