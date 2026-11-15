# Backend agent rules
- Keep the root layout fixed. Never overwrite model, notebook or scientific reports.
- Source of truth: `models/best.pt`, `reports/heldout_test_metrics.json`, `reports/dataset_provenance.json`.
- Reject invalid uploads; never return fabricated predictions when checkpoint unavailable.
- Run `python -m pytest backend/tests -q` and validate one real image with actual checkpoint before claiming full integration.
- Untrusted `.pt` files must never be loaded. Retain class order: large, medium, small.
- No public-facing farm-grade or physical-size claims.
