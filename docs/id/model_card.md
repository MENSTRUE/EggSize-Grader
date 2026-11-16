# Model Card — EggSizeGrader

**EggSizeGrader** merupakan proyek hari ke-38 dari portofolio [100 Days of Projects](https://github.com/MENSTRUE). Sistem mendeteksi kotak objek dan kategori anotasi (`large`, `medium`, `small`) pada foto telur menggunakan checkpoint YOLOv8n yang dipilih melalui validasi. Proyek memadukan eksperimen Kaggle dengan audit kebocoran data, inferensi FastAPI lokal, serta antarmuka React/TypeScript. **Sistem tidak mengukur diameter atau berat fisik dan bukan sistem grading komersial resmi.**

## 5. Objectives and research questions

Apakah YOLOv8n tiga kelas dapat mengenali objek telur pada held-out test berbasis grup? Seberapa berisiko overlap identitas sumber Roboflow pada split asli? Apakah checkpoint asli dapat melayani unggahan lokal?

## 6. Scope and non-goals

Cakupan: bounding box, label, confidence, jumlah, inferensi lokal, evaluasi sadar kebocoran. Tidak mencakup gram, milimeter, kalibrasi, keamanan pangan, grade regulasi, atau produksi industri.

## 8. Implementation status

**Diverifikasi dari repository:** sumber kode, 4 tes kontrak API, metrik JSON, screenshot, contoh gambar. **Dilaporkan dari lokal:** pytest 4/4 lulus, dependency terpasang, screenshot inferensi. **Belum diverifikasi:** deployment publik, benchmark banyak perangkat, keandalan produksi.

## 18. Duplicate and leakage assessment

Audit split asli menemukan **12 source key pada lintas split** dan **0 hash SHA-256 identik lintas split**. Penggabungan identitas nama asal dan hash menghasilkan **153 grup konservatif**. GroupShuffleSplit (seed 42) menjaga seluruh anggota grup pada satu split baru. Metode ini tidak menutup kemungkinan gambar mirip yang bernama atau ber-hash berbeda.

## 23. Validation and final held-out metrics

| Metric | Validation (41 images) | Frozen held-out test (50 images) |
|---|---:|---:|
| Precision | 89.81% | 83.60% |
| Recall | 82.31% | 86.64% |
| mAP@50 | 90.99% | 91.13% |
| mAP@50–95 | 83.53% | 84.28% |
| AP@50–95 large | 77.32% | 77.01% |
| AP@50–95 medium | 89.27% | 89.84% |
| AP@50–95 small | 84.00% | 85.99% |


## 24. Per-class behavior and confusion matrix

Pada held-out test, kelas **large** memiliki AP@50–95 terendah (77,01%); medium 89,84%, small 85,99%. **Aset confusion matrix test tidak ditemukan dalam audit repository** sehingga nilainya tidak diklaim. Error deteksi perlu pencocokan berbasis IoU, bukan akurasi klasifikasi saja.

## 29. Repository layout

Mempertahankan root: `README.md`, `AGENTS.md`, `LICENSE`, `.env.example`, `.gitignore`; `notebooks/`, `models/`, `reports/`, `assets/{plots,examples,screenshots,diagrams}`, `backend/`, `frontend/`, `docs/`, `scripts/`. Lihat [arsitektur](architecture.md). Dataset mentah dan bobot `.pt` tidak dimasukkan Git.

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

## 37. Security and privacy

API memeriksa tipe konten, jumlah byte dan decode Pillow; gambar diolah dalam memori. Jangan memuat bobot `.pt` sembarangan (risiko pickle PyTorch). Jangan menganggap browser/log jaringan tidak mencatat data. Tidak tersedia autentikasi dan kontrol akses pengguna.

## Sumber dan verifikasi

Semua hasil numerik di atas berasal dari laporan eksperimen dalam repository, bukan hasil hitung ulang pada perubahan dokumentasi ini. Studi hanya menggunakan satu arsitektur; screenshot gambar lokal merupakan demonstrasi, bukan bukti kebenaran ukuran fisik.

[README utama](../../README.md) · [reports](../../reports/README.md) · [notebook](../../notebooks/eggsizegrader.ipynb)
