# Frontend — EggSizeGrader

React 18, TypeScript, Vite and lucide-react. No fabricated UI predictions; predictions come exclusively from FastAPI `POST /api/v1/predict`. Start backend first, then from project root:

```powershell
cd frontend
npm install
npm run dev
```

Open http://127.0.0.1:5173. Vite proxies `/api` to localhost:8000. `npm run build` performs TypeScript checks and creates dist/. If backend is offline or checkpoint missing the UI shows an error/unavailable state. Drag-and-drop or browse a JPEG/PNG/WEBP (max 10MB). Once real inference succeeds, export an annotated image or detection CSV. Research evaluation figures shown on Overview/Insights are historical held-out metrics, not live upload results.

This interface and endpoint are intended for local research. Before deployment add appropriate security, privacy, rate limiting, file type inspection, and production hosting configuration.
