# Evidence registry — `reports/`

Files are preserved experiment evidence; documentation should not edit metrics or source membership. Values below are read from the checked-in JSON/CSV outputs, with different source roles.

## Dataset and audit evidence
| File | Role |
|---|---|
| `dataset_provenance.json` | Kaggle path, Roboflow project/version, source YAML declared license, access time |
| `source_inventory.csv` | Per-image source, dimensions, box counts and SHA-256 source inventory |
| `annotation_issues.csv` | Invalid/missing annotation audit; only header in current artifact |
| `duplicate_label_conflicts.json` | Exact duplicate annotation disagreement report (empty list) |
| `leakage_audit.json` | 318 images, 153 groups, original split source overlap 12, exact-hash overlap 0 |
| `split_membership.csv` | Frozen group-disjoint split membership; includes source image paths from Kaggle |
| `clean_split_distribution.csv` | New split images and per-class box counts |

| Split | Images | Large boxes | Medium boxes | Small boxes |
|---|---:|---:|---:|---:|
| Train | 227 | 524 | 689 | 561 |
| Validation | 41 | 146 | 64 | 101 |
| Held-out test | 50 | 136 | 131 | 112 |
| **Total** | **318** | **806** | **884** | **774** |


## Experiment and evaluation
| File | Role |
|---|---|
| `experiment_config.json` | Seed 42, YOLOv8n, size 640, 60 epochs, batch 16, patience 15 |
| `baseline.json` | Predict-zero-box sanity baseline, not a fabricated comparable mAP |
| `model_selection.json` | Best checkpoint from validation; no test-tuning |
| `validation_metrics.json` | Validation precision/recall/mAP and per-class AP |
| `heldout_test_metrics.json` | Frozen test: 50 images in 23 groups |
| `heldout_per_class_ap.csv` | Large/medium/small AP@50–95 |
| `prediction_examples.csv` | Saved per-image prediction examples |
| `export_verification.json` | Export/smoke verification metadata |
| `artifact_manifest.json` | Recorded artifact checksums/manifest |

| Metric | Validation (41 images) | Frozen held-out test (50 images) |
|---|---:|---:|
| Precision | 89.81% | 83.60% |
| Recall | 82.31% | 86.64% |
| mAP@50 | 90.99% | 91.13% |
| mAP@50–95 | 83.53% | 84.28% |
| AP@50–95 large | 77.32% | 77.01% |
| AP@50–95 medium | 89.27% | 89.84% |
| AP@50–95 small | 84.00% | 85.99% |


## Visual interpretation and caution
Plots and original YOLO annotations reside in `assets/`; see [asset catalog](../assets/README.md). Test `large` AP@50–95 is 77.01%, below medium 89.84%; this is class-specific AP, not a direct classification confusion count. No **held-out confusion-matrix plot** is present in the audited repository. The saved `prediction_examples.csv` and screenshots are qualitative unless matched to ground truth. `source_inventory.csv` and `split_membership.csv` may contain Kaggle absolute file paths; these are historical provenance, not portable path references.
