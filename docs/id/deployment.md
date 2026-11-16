# Deployment — EggSizeGrader

**EggSizeGrader** merupakan proyek hari ke-38 dari portofolio [100 Days of Projects](https://github.com/MENSTRUE). Sistem mendeteksi kotak objek dan kategori anotasi (`large`, `medium`, `small`) pada foto telur menggunakan checkpoint YOLOv8n yang dipilih melalui validasi. Proyek memadukan eksperimen Kaggle dengan audit kebocoran data, inferensi FastAPI lokal, serta antarmuka React/TypeScript. **Sistem tidak mengukur diameter atau berat fisik dan bukan sistem grading komersial resmi.**

## 24. Per-class behavior and confusion matrix

Pada held-out test, kelas **large** memiliki AP@50–95 terendah (77,01%); medium 89,84%, small 85,99%. **Aset confusion matrix test tidak ditemukan dalam audit repository** sehingga nilainya tidak diklaim. Error deteksi perlu pencocokan berbasis IoU, bukan akurasi klasifikasi saja.

## 25. Error analysis and interpretation

Kelemahan relatif kelas `large` perlu telaah false negative dan kekeliruan kelas. Grid prediksi test menyediakan contoh visual, tetapi repository belum menyediakan perincian FP/FN kuantitatif per penyebab. Pergeseran domain antar kamera/cahaya belum diukur.

## 29. Repository layout

Mempertahankan root: `README.md`, `AGENTS.md`, `LICENSE`, `.env.example`, `.gitignore`; `notebooks/`, `models/`, `reports/`, `assets/{plots,examples,screenshots,diagrams}`, `backend/`, `frontend/`, `docs/`, `scripts/`. Lihat [arsitektur](architecture.md). Dataset mentah dan bobot `.pt` tidak dimasukkan Git.

## 30. System requirements

Contoh Windows PowerShell menggunakan Python 3.11, pip, Node.js/npm dan inferensi CPU lokal; backend saat ini tidak membutuhkan GPU. Training memakai GPU T4 Kaggle. Unduhan dependency dapat berat pada koneksi lambat.

## 31. Setup and installation

```powershell
cd "D:\porto\100 day\day 38"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r backend\requirements.txt
python -m pytest backend\tests -v
python -m uvicorn backend.app.main:app --reload --port 8000
```
Buka terminal PowerShell **kedua**:
```powershell
cd "D:\porto\100 day\day 38\frontend"
npm install
npm run build
npm run dev
```
API `http://127.0.0.1:8000/docs`; UI `http://127.0.0.1:5173`. Checkpoint lokal `models/best.pt` harus disalin dari artefak Kaggle karena `.gitignore` mengabaikan `*.pt`.

## 32. Run and usage examples

Buka dokumentasi API `http://127.0.0.1:8000/docs`. Cek `/api/v1/ready`: `ready=true` berarti model berhasil dimuat dan kelas diverifikasi. Pilih gambar uji, atur threshold, klik Generate detections, tinjau kotak/hitungan lalu unduh PNG anotasi atau CSV.

## 33. End-to-end testing

Laporan pengujian lokal: `4 passed, 1 warning` di Windows/Python 3.11; tes mencakup health, kontrak model, penolakan MIME, gambar invalid. Screenshot menunjukkan **satu inferensi lokal nyata**: 13 kotak medium, sekitar 2.869 ms. Hal ini tidak membuktikan semua kotak benar. Belum ada suite E2E browser otomatis.

## 34. Reproducibility and lineage

Notebook `notebooks/eggsizegrader.ipynb` mencatat audit, seed split 42, konfigurasi 60 epoch, evaluasi dan pembuatan ZIP artefak. Folder `reports/` menyimpan keanggotaan split dan inventaris SHA-256. Runtime Kaggle menggunakan Python 3.13.16 dan Ultralytics 8.4.213; lokal memakai Python 3.11.9 dengan versi paket lebih baru. Rentang dependency bukan environment lock identik.

## 35. Visual evidence

![Contoh anotasi asli](../../assets/examples/ground_truth_samples.png)
*Kotak ground truth YOLO pada contoh pelatihan, bukan prediksi model.*

![Dataset EDA](../../assets/plots/dataset_eda.png)
*Distribusi split/kelas serta kotak per gambar berdasarkan artefak.*

![Grid prediksi held-out](../../assets/plots/heldout_prediction_grid.png)
*Visualisasi prediksi tersimpan; bersifat kualitatif, bukan ukuran akurasi statistik.*

![Aplikasi lokal dengan deteksi](../../assets/screenshots/Screenshot%202026-11-16%20135615.png)
*Screenshot browser lokal: 13 objek terdeteksi, semuanya tampil sebagai `medium`, dengan sekitar 2.869 ms inferensi pada satu eksekusi. Bukti aplikasi berjalan, bukan pengujian kebenaran anotasi independen.*

## 36. Deployment readiness

**Hanya riset lokal.** Proxy Vite dev, endpoint unggah tanpa autentikasi, dan performa CPU bukan bukti kesiapan deployment. Produksi memerlukan autentikasi, rate limit, HTTPS, pembatasan dekompresi, tinjauan privasi, distribusi bobot tepercaya, logging/monitoring dan konfigurasi layanan.

## Sumber dan verifikasi

Semua hasil numerik di atas berasal dari laporan eksperimen dalam repository, bukan hasil hitung ulang pada perubahan dokumentasi ini. Studi hanya menggunakan satu arsitektur; screenshot gambar lokal merupakan demonstrasi, bukan bukti kebenaran ukuran fisik.

[README utama](../../README.md) · [reports](../../reports/README.md) · [notebook](../../notebooks/eggsizegrader.ipynb)
