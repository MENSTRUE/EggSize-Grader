# Model registry — EggSizeGrader

## Trusted model and storage
Local `models/best.pt` is the checkpoint selected from Ultralytics YOLOv8n **validation**. Because the root `.gitignore` excludes `*.pt`, model absence from GitHub is expected. The checkpoint must be obtained from the original saved Kaggle artifact and its trust/source verified, not from third-party arbitrary downloads. The model is run on CPU in `backend/app/inference/yolo.py`.

## Metadata and classes
- Task: object detection, YOLOv8n, 3 class head; large ID0, medium ID1, small ID2.
- Pretrained initial weights: `yolov8n.pt`; configured training size 640, 60 epochs, patience 15, batch 16, seed 42, `optimizer=auto`.
- Inference input: uploaded RGB Pillow image after EXIF normalization, forwarded to Ultralytics; no fixed explicit frontend resize. Detection output: pixel XYXY, label, score, counts.
- Comparison/selection: only **one architecture**, validation-selected best checkpoint; test never used for model selection (per `reports/model_selection.json`).

## Held-out evidence
| Metric | Validation (41 images) | Frozen held-out test (50 images) |
|---|---:|---:|
| Precision | 89.81% | 83.60% |
| Recall | 82.31% | 86.64% |
| mAP@50 | 90.99% | 91.13% |
| mAP@50–95 | 83.53% | 84.28% |
| AP@50–95 large | 77.32% | 77.01% |
| AP@50–95 medium | 89.27% | 89.84% |
| AP@50–95 small | 84.00% | 85.99% |


These are object-detection dataset metrics, not egg weight/diameter accuracy. No calibration, external-camera test or guaranteed real-world grading reliability is established. 

## Verify locally
```powershell
Test-Path .\models\best.pt
python -m uvicorn backend.app.main:app --reload --port 8000
```
Call `/api/v1/ready` for loaded state and class check. An absent/untrusted `.pt` must not be auto-replaced. `reports/export_verification.json` describes the Kaggle-side artifact verification; no ONNX export is represented as shipped. Attribution/licenses must be reviewed before model redistribution.
