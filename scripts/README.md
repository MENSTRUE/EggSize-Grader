# Scripts — status and conventions

The repository currently tracks `scripts/.gitkeep` **only**; there is no executable script under `scripts/` to document as implemented. Do not invent commands or file paths.

Existing entrypoints are:
- Kaggle training and export: `notebooks/eggsizegrader.ipynb`.
- Backend: `python -m uvicorn backend.app.main:app --reload --port 8000` from project root.
- Tests: `python -m pytest backend/tests -v`.
- Frontend: `npm run dev` and `npm run build` from `frontend/`.

If future utilities are added in this folder, use descriptive names and document purpose, args, OS requirements, reproducibility, safe I/O, relative root paths and tests. Do not add scripts that download or overwrite checkpoints or datasets without an explicit provenance and integrity check. Preserve source-of-truth reports and frozen evaluation membership.
