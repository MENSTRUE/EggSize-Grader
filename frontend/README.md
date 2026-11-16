# Frontend — React + TypeScript + Vite

## Purpose
A local research dashboard for live three-class egg detection. React 18, TypeScript, Vite 6 and lucide-react; no router or state-management library. `src/pages/App.tsx` owns UI state and view tabs; `src/hooks/useModelStatus.ts` retrieves readiness, `src/services/api.ts` sends multipart requests, `src/types/index.ts` models response, `src/components/ResultCanvas.tsx` overlays XYXY pixel boxes on HTML canvas, `src/styles/index.css` controls visual layout.

## UI workflow
1. Start FastAPI on port 8000. 2. `cd frontend; npm install; npm run build; npm run dev`. 3. Open `http://127.0.0.1:5173`, confirm Model online from `/ready`. 4. In Grade analysis browse or drag/drop JPEG/PNG/WEBP up to 10 MiB. 5. Set confidence 0.05–0.95, IoU 0.10–0.90. 6. Generate detections; inspect real boxes, per-class counts and inference latency; export Annotated PNG or Results CSV. 7. Model insights shows **historical** report metrics, not live prediction scoring.

## Navigation and state
Three tabs (`overview`, `analyze`, `insights`) switch client-side, with no deep-link routing. `file`, `preview`, `result`, `busy`, `error`, `conf`, `iou` are local state. A loading indicator accompanies API calls; unavailable model or invalid upload displays a warning/error. Blank result means no image or no successful call, not an asserted negative grading decision.

## API and build
Dev Vite proxy in `vite.config.ts` forwards `/api` to `http://127.0.0.1:8000`; optional `VITE_API_BASE_URL` overrides API base in `src/services/api.ts`. Real payload uses `FormData` file+confidence+iou to `/api/v1/predict`; backend is source of detections. Run `npm run build` for TypeScript + Vite output `dist/` (Git ignored). The repo contains a checked-in `tsconfig.tsbuildinfo` file, which is a generated build artifact; review cleanup separately, do not assume all generated files are ignored.

## Screenshots, performance and limitations
![Local inference UI](../assets/screenshots/Screenshot%202026-11-16%20135615.png)

The recorded browser demo shows **13 objects labeled medium**, about **2,869 ms** on a single run; labels are model predictions and do not establish classification correctness. Browser E2E automation, auth, internationalization, server-side routing, production deployment and real-time video are not implemented. `npm run build` success should be verified on the developer machine before release. See [architecture](../docs/en/architecture.md), [evaluations](../docs/en/evaluation.md).
