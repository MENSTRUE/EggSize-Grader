# AGENTS.md — EggSizeGrader operating rules

## Mission and hierarchy
Maintain Day 38 as a reproducible, evidence-driven three-class egg object detector; do not turn visual labels into physical grading. Priority: actual implementation and captured `reports/` evidence > executable notebook > local verified test logs/screenshots > explanatory docs > assumptions. If they disagree, audit and flag rather than silently reconcile.

## Immutable repository invariants
Keep root `README.md`, `AGENTS.md`, `LICENSE`, `.env.example`, `.gitignore`, `notebooks/`, `models/`, `reports/`, `assets/{plots,examples,screenshots,diagrams}`, `backend/`, `frontend/`, `docs/`, `scripts/`. Do not add a tracked `datasets/` folder or change root names. Never delete research artifacts or overwrite `best.pt` without explicit direction. `.gitignore` excludes `.pt`; model availability is local, not GitHub evidence.

## Before–Now–Next
**Before:** separate upstream datasets, 3-class selection, 318 images, source overlaps. **Now:** validation-selected YOLOv8n, 227/41/50 grouped splits, held-out report, FastAPI/React local demo. **Next:** systematic correctness review, external generalization, API hardening, CI; not yet production.

## Scientific integrity
Use `reports/dataset_provenance.json` and original Roboflow YAML for sourcing; verify CC BY 4.0 declaration upstream. Preserve `large`, `medium`, `small` indices 0,1,2. Audit missing labels, invalid boxes, source suffixes/byte hashes. Keep group identities disjoint. Select checkpoints/thresholds on validation; never use held-out test for optimization after viewing metrics. One model architecture is not a benchmark of multiple architectures. No fabricated metric/confusion matrix, no physical diameter/mass claims. Document seed, split, dependencies, checksums and test-set reuse status.

## Backend requirements
Follow FastAPI's existing `backend/app/{api/routes,core,inference,schemas,services}` layout. `/health` is liveness, `/ready` verifies the trusted checkpoint, `/predict` is genuine model inference. Validate MIME, file length, decompression limits, class schema and errors; no mock responses presented as model predictions. Never load untrusted `.pt` weights. No authentication exists, so never claim internet-safe production. Test API and at least one **real labeled image** before claiming full E2E correctness.

## Frontend requirements
Preserve React + Vite + TypeScript architecture. API is source of live inference; JSON reports are source for historical metrics. Use explicit loading, unavailable, empty and error states. Keep upload ≤10 MiB and three classes. Never invent confidence or boxes. Run `npm run build` and test a real file against FastAPI. Canvas labels are visualization, not ground truth.

## Documentation and assets
Root README must reflect current status. Maintain equivalent substantive English `docs/en` and Indonesian `docs/id` pages, plus relevant component READMEs. Render existing visuals by relative paths; never invent training plots or screenshots. Update docs when API or metric contracts change. Preserve license placeholders until verified permissions are chosen. Audit broken links and image names before commit.

## Testing and Definition of Done
1. `python -m pip check` and `python -m pytest backend/tests -v` pass; record warnings.
2. `GET /api/v1/ready` indicates loaded trusted checkpoint.
3. Real `POST /api/v1/predict` returns dimensions/counts/boxes; compare against annotation before correctness claim.
4. `npm run build` and browser upload/export checked on targeted environment.
5. Documentation and actual model/report files cross-checked; Git diff inspected; no secret, raw dataset, `.venv`, `node_modules`, `dist` or unlicensed binary committed.

## Git hygiene and prohibitions
Use scoped commits (`docs(day38): ...`, `feat(day38): ...`). Do not force-push, delete code, re-run training needlessly, manufacture metrics, alter held-out splits without a new experiment, or silently change repository structure. Review `git status`, `git diff --check`, links, screenshots and license status before pushing.
