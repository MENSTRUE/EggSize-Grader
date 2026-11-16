# Model Card — EggSizeGrader

**EggSizeGrader** is Day 38 of the [100 Days of Projects](https://github.com/MENSTRUE) portfolio. It detects bounding boxes and annotated classes (`large`, `medium`, `small`) in egg photographs using a validation-selected YOLOv8n checkpoint. The project joins a leakage-aware Kaggle experiment, local FastAPI inference, and a React/TypeScript analysis interface. **It does not measure physical diameter or weight and is not an official commercial grading system.**

## 5. Objectives and research questions

Can a three-class YOLOv8n detector identify the annotated egg objects on held-out grouped samples? How sensitive are the benchmark splits to shared Roboflow source identifiers? Does the real checkpoint serve live local uploads?

## 6. Scope and non-goals

In scope: bounding boxes, class labels, confidence, counts, local inference, leakage-aware evaluation. Out of scope: grams, millimetres, calibration, food safety, regulatory grades, industrial production.

## 8. Implementation status

**Verified from repository:** source code, 4 API contract tests, metrics JSON, screenshots, image examples. **Reported locally:** 4/4 pytest passed, dependencies installed, screenshot of successful inference. **Not verified:** hosted deployment, cross-device benchmark, repeated production reliability.

## 18. Duplicate and leakage assessment

Original split inspection found **12 source keys crossing original splits** and **0 identical SHA-256 hashes crossing splits**. A union of source-name and byte-hash identities produced **153 conservative groups**. GroupShuffleSplit (seed 42) placed each group entirely within one new split. This does not exclude visually similar images having different filenames/hashes.

## 23. Validation and final held-out metrics

| Metric | Validation (41 images) | Frozen held-out test (50 images) |
|---|---:|---:|
| Precision | 89.81% | 83.60% |
| Recall | 82.31% | 86.64% |
| mAP@50 | 90.99% | 91.13% |
| mAP@50–95 | 83.53% | 84.28% |
| AP@50–95 large | 77.32% | 77.01% |
| AP@50–95 medium | 89.27% | 89.84% |
| AP@50–95 small | 84.00% | 85.99% |


## 24. Per-class behavior and confusion matrix

On held-out test, **large** has the lowest AP@50–95 (77.01%); medium reaches 89.84% and small 85.99%. **No test confusion-matrix asset exists in the audited repository**; therefore, no confusion-matrix values are claimed. Object detection errors require IoU-based matching, not classification-only accuracy.

## 29. Repository layout

Preserves existing root: `README.md`, `AGENTS.md`, `LICENSE`, `.env.example`, `.gitignore`; `notebooks/`, `models/`, `reports/`, `assets/{plots,examples,screenshots,diagrams}`, `backend/`, `frontend/`, `docs/`, `scripts/`. See [architecture](architecture.md). Raw datasets and `.pt` weights are deliberately excluded.

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

## 37. Security and privacy

The API checks content type, byte count and Pillow decode; it processes uploaded images in memory. Do not accept arbitrary `.pt` weights (PyTorch pickle risk). Do not assume local browser/network logs leave no trace. No authentication and no per-user access control are present.

## Source material and verification

All numeric results above originate from the checked-in experiment reports, not from new computation in this documentation update. The original study includes a single architecture; the local image screenshot is a demonstration, not evidence of physical-size correctness.

[Repository README](../../README.md) · [reports](../../reports/README.md) · [notebook](../../notebooks/eggsizegrader.ipynb)
