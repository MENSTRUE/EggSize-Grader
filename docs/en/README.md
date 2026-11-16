# English technical documentation — EggSizeGrader

**EggSizeGrader** is Day 38 of the [100 Days of Projects](https://github.com/MENSTRUE) portfolio. It detects bounding boxes and annotated classes (`large`, `medium`, `small`) in egg photographs using a validation-selected YOLOv8n checkpoint. The project joins a leakage-aware Kaggle experiment, local FastAPI inference, and a React/TypeScript analysis interface. **It does not measure physical diameter or weight and is not an official commercial grading system.**

## Document index

- [Dataset Provenance](dataset_provenance.md)
- [Methodology](methodology.md)
- [Experiments](experiments.md)
- [Model Card](model_card.md)
- [Evaluation](evaluation.md)
- [Limitations](limitations.md)
- [Architecture](architecture.md)
- [Reproducibility](reproducibility.md)
- [Deployment](deployment.md)
- [Troubleshooting](troubleshooting.md)

## Source of truth / Sumber kebenaran

1. `reports/*.json` and `reports/*.csv` for recorded dataset/method/metrics.
2. `notebooks/eggsizegrader.ipynb` for executable experiment design.
3. `backend/app/`, `frontend/src/` for app implementation.
4. `assets/` for saved figures/screenshots, which are qualitative unless separately quantified.
5. GitHub repository state, not an assumption about unpublished local files.

**Checkpoint note / Catatan checkpoint:** `models/best.pt` is required locally but Git excludes `*.pt`. The screenshot is local-run evidence, not a reproducible checkpoint distribution record.
