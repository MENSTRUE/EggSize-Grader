# Dokumentasi teknis Bahasa Indonesia — EggSizeGrader

**EggSizeGrader** merupakan proyek hari ke-38 dari portofolio [100 Days of Projects](https://github.com/MENSTRUE). Sistem mendeteksi kotak objek dan kategori anotasi (`large`, `medium`, `small`) pada foto telur menggunakan checkpoint YOLOv8n yang dipilih melalui validasi. Proyek memadukan eksperimen Kaggle dengan audit kebocoran data, inferensi FastAPI lokal, serta antarmuka React/TypeScript. **Sistem tidak mengukur diameter atau berat fisik dan bukan sistem grading komersial resmi.**

## Indeks dokumen

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
