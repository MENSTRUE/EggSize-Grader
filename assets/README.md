# Assets — visual evidence inventory

Every existing visual below is a saved repository file; none is generated for decorative purposes in this documentation.

## Plots
- [`plots/dataset_eda.png`](plots/dataset_eda.png): histogram of boxes per image and grouped split/class distribution; evidence of dataset composition.
- [`plots/heldout_prediction_grid.png`](plots/heldout_prediction_grid.png): saved multiple model predictions from the held-out experiment; **qualitative** examples, not a substitute for mAP calculations.

## Examples
- [`examples/ground_truth_samples.png`](examples/ground_truth_samples.png): drawn **ground-truth bounding boxes**, not an inference result.
- `examples/pred_*.png`: 12 saved individual inference images recorded in repository; file names retain input provenance fragments, avoid confusing them with curated ground truth. Verify image ownership/licensing before redistribution.

## Screenshots
- [`screenshots/Screenshot 2026-11-16 135615.png`](screenshots/Screenshot%202026-11-16%20135615.png): local UI test, 13 detections displayed as medium with around 2,869 ms inference. Demonstrates a successful application run, **not verified physical-size labels or aggregate test performance**.

## Diagrams
`diagrams/` has `.gitkeep` only in audited repo. README and architecture docs use source-controlled Mermaid rather than fabricated rendered diagram images.

## Usage and licensing
All relative image references are intended for GitHub Markdown rendering. Visuals inherit the source-image attribution obligations; Kaggle dataset source YAML declares CC BY 4.0 but rights remain subject to upstream verification. Avoid re-saving edited results as if they were raw model outputs. New figures must name experiment/split/model and be linked to metrics source.
