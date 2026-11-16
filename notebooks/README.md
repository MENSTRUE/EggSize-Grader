# Experiment notebook — Day 38

Main notebook: [`eggsizegrader.ipynb`](eggsizegrader.ipynb). The experiment used Kaggle input `/kaggle/input/datasets/loliwibu/eggsizegrader-dataset`, originally YOLO train/valid/test folders. Source YAML was strictly verified for `large`, `medium`, `small` (IDs 0,1,2). The unrelated two-class Roboflow archive was excluded.

## Execution and lineage
1. Inspect Kaggle environment, input and YAML provenance.
2. Pair all 318 images to YOLO labels; validate dimensions, normalized XYWH and class IDs. Record issue CSV.
3. Strip Roboflow `.rf.*` augmentation suffixes, compare SHA-256, derive unioned source groups, detect original split overlap.
4. GroupShuffleSplit with seed 42; build new image/label splits: train 227, validation 41, test 50. Write `reports/split_membership.csv` and distribution.
5. EDA, real GT visual, zero-box sanity baseline, trained YOLOv8n with pretrained weights.
6. Select best weights via validation and evaluate held-out test once. Save metrics, class AP and predictions.
7. Export model/report/visual artifact ZIP and integrity checks. ONNX export was optional and is not documented as a released model.

## Reproduce
Enable Kaggle GPU and Internet if needed for Ultralytics/weights, attach the dataset, open/import notebook, run sequentially and **Save Version** only after outputs complete. Notebook as checked into Git is executable study logic; results in `reports/` derive from an actual run. The original training environment used Kaggle Python 3.13.16, Ultralytics 8.4.213 on Tesla T4. Fixed seed improves, but does not guarantee byte-identical deep learning results across versions. Keep held-out membership frozen; record experiment version if re-training.

## Outputs, constraints and interpretation
Expected outputs under `/kaggle/working/EggSizeGrader_Day38/` include `models/best.pt`, audit JSON/CSV, metrics JSON, GT and held-out prediction figures, model card, and ZIP. Inspect exact outputs before copying; local checkpoint is Git-ignored. Do not turn source image labels into mass/diameter claims; test-set results apply only to this grouped dataset. See [methods](../docs/en/methodology.md) and [reproducibility](../docs/en/reproducibility.md).
