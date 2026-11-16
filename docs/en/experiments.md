# Experiments — EggSizeGrader

**EggSizeGrader** is Day 38 of the [100 Days of Projects](https://github.com/MENSTRUE) portfolio. It detects bounding boxes and annotated classes (`large`, `medium`, `small`) in egg photographs using a validation-selected YOLOv8n checkpoint. The project joins a leakage-aware Kaggle experiment, local FastAPI inference, and a React/TypeScript analysis interface. **It does not measure physical diameter or weight and is not an official commercial grading system.**

## 18. Duplicate and leakage assessment

Original split inspection found **12 source keys crossing original splits** and **0 identical SHA-256 hashes crossing splits**. A union of source-name and byte-hash identities produced **153 conservative groups**. GroupShuffleSplit (seed 42) placed each group entirely within one new split. This does not exclude visually similar images having different filenames/hashes.

## 19. Model architecture

Ultralytics **YOLOv8n** object detector (reported 3,011,433 parameters with detection head adapted from 80 to 3 classes). The saved PyTorch checkpoint is `models/best.pt` locally; `.pt` is Git-ignored. Inference is forced to CPU in `backend/app/inference/yolo.py`.

## 20. Experiment and baseline

One pretrained architecture was trained; there is no cross-architecture controlled comparison. An always-no-boxes sanity baseline yields zero recall on annotated samples, but **was not given a fabricated mAP**. Design is single-model research proof of concept.

## 21. Training setup

Seed=42, pretrained `yolov8n.pt`, 60 epochs configured, patience=15, image size=640, batch=16, optimizer=`auto`, GPU device index 0 on Kaggle. Selection follows Ultralytics validation fitness. Exact effective completed epochs should be checked against the captured training log if asserted.

## 22. Champion selection

`best.pt` was chosen by the training framework from **validation**, not test. `reports/model_selection.json` lists one architecture and explicitly records `test_used_for_selection: false`. Any future threshold tuning should use validation, not the frozen test.

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


## 25. Error analysis and interpretation

The moderate relative weakness of `large` warrants qualitative review of missed boxes and class confusion. The saved test prediction grid provides visual examples, but the repository does not present a quantitative FP/FN breakdown by cause. Domain shift between cameras and lighting is not measured.

## 26. Model artifacts and contracts

Model loader checks file existence and expects exact ordered classes `large`, `medium`, `small`. `POST /api/v1/predict` returns model, original image width/height, list of detections with class id/label/confidence/XYXY pixel coordinates, class counts, total, latency, and research warning. File is decoded with Pillow and EXIF orientation applied.

## Source material and verification

All numeric results above originate from the checked-in experiment reports, not from new computation in this documentation update. The original study includes a single architecture; the local image screenshot is a demonstration, not evidence of physical-size correctness.

[Repository README](../../README.md) · [reports](../../reports/README.md) · [notebook](../../notebooks/eggsizegrader.ipynb)
