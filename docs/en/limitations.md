# Limitations — EggSizeGrader

**EggSizeGrader** is Day 38 of the [100 Days of Projects](https://github.com/MENSTRUE) portfolio. It detects bounding boxes and annotated classes (`large`, `medium`, `small`) in egg photographs using a validation-selected YOLOv8n checkpoint. The project joins a leakage-aware Kaggle experiment, local FastAPI inference, and a React/TypeScript analysis interface. **It does not measure physical diameter or weight and is not an official commercial grading system.**

## 5. Objectives and research questions

Can a three-class YOLOv8n detector identify the annotated egg objects on held-out grouped samples? How sensitive are the benchmark splits to shared Roboflow source identifiers? Does the real checkpoint serve live local uploads?

## 8. Implementation status

**Verified from repository:** source code, 4 API contract tests, metrics JSON, screenshots, image examples. **Reported locally:** 4/4 pytest passed, dependencies installed, screenshot of successful inference. **Not verified:** hosted deployment, cross-device benchmark, repeated production reliability.

## 13. Dataset license and attribution

The dataset YAML **declares** `CC BY 4.0`; upstream permission must be checked separately. Attribution to the named Roboflow project is retained. `LICENSE` in this repo expressly says **license not yet selected**, so no blanket permissive source-code license is claimed. Ultralytics, weights, and any third-party dependencies require their own license review for distribution.

## 17. Split and distribution

| Split | Images | Large boxes | Medium boxes | Small boxes |
|---|---:|---:|---:|---:|
| Train | 227 | 524 | 689 | 561 |
| Validation | 41 | 146 | 64 | 101 |
| Held-out test | 50 | 136 | 131 | 112 |
| **Total** | **318** | **806** | **884** | **774** |


## 25. Error analysis and interpretation

The moderate relative weakness of `large` warrants qualitative review of missed boxes and class confusion. The saved test prediction grid provides visual examples, but the repository does not present a quantitative FP/FN breakdown by cause. Domain shift between cameras and lighting is not measured.

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

## 37. Security and privacy

The API checks content type, byte count and Pillow decode; it processes uploaded images in memory. Do not accept arbitrary `.pt` weights (PyTorch pickle risk). Do not assume local browser/network logs leave no trace. No authentication and no per-user access control are present.

## Source material and verification

All numeric results above originate from the checked-in experiment reports, not from new computation in this documentation update. The original study includes a single architecture; the local image screenshot is a demonstration, not evidence of physical-size correctness.

[Repository README](../../README.md) · [reports](../../reports/README.md) · [notebook](../../notebooks/eggsizegrader.ipynb)
