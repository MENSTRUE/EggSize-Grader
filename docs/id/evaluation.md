# Evaluation — EggSizeGrader

**EggSizeGrader** merupakan proyek hari ke-38 dari portofolio [100 Days of Projects](https://github.com/MENSTRUE). Sistem mendeteksi kotak objek dan kategori anotasi (`large`, `medium`, `small`) pada foto telur menggunakan checkpoint YOLOv8n yang dipilih melalui validasi. Proyek memadukan eksperimen Kaggle dengan audit kebocoran data, inferensi FastAPI lokal, serta antarmuka React/TypeScript. **Sistem tidak mengukur diameter atau berat fisik dan bukan sistem grading komersial resmi.**

## 16. Cleaning and preprocessing

Gambar rusak, label hilang, ID kelas tak valid, atau bounding box di luar rentang harus menghentikan proses. Sufiks nama `.rf.*` dinormalisasi menjadi identitas sumber konservatif; hash SHA-256 dihitung. Penyiapan data menyalin pasangan gambar/label tervalidasi ke direktori kerja Kaggle.

## 17. Split and distribution

| Split | Images | Large boxes | Medium boxes | Small boxes |
|---|---:|---:|---:|---:|
| Train | 227 | 524 | 689 | 561 |
| Validation | 41 | 146 | 64 | 101 |
| Held-out test | 50 | 136 | 131 | 112 |
| **Total** | **318** | **806** | **884** | **774** |


## 21. Training setup

Seed=42, bobot awal `yolov8n.pt`, konfigurasi 60 epoch, patience=15, ukuran gambar=640, batch=16, optimizer=`auto`, GPU Kaggle indeks 0. Pemilihan mengikuti fitness validasi Ultralytics. Jumlah epoch yang benar-benar selesai harus dicek dari log pelatihan sebelum diklaim.

## 22. Champion selection

`best.pt` dipilih oleh framework dari **validasi**, bukan test. `reports/model_selection.json` mencatat satu arsitektur dan `test_used_for_selection: false`. Penyetelan threshold berikutnya harus memakai validasi, bukan held-out test.

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

## 25. Error analysis and interpretation

Kelemahan relatif kelas `large` perlu telaah false negative dan kekeliruan kelas. Grid prediksi test menyediakan contoh visual, tetapi repository belum menyediakan perincian FP/FN kuantitatif per penyebab. Pergeseran domain antar kamera/cahaya belum diukur.

## 26. Model artifacts and contracts

Loader mengecek keberadaan checkpoint dan urutan kelas `large`, `medium`, `small`. `POST /api/v1/predict` mengembalikan model, dimensi gambar, deteksi (ID/label/confidence/koordinat XYXY piksel), hitungan per kelas, total, latensi, serta peringatan penelitian. Berkas didekode Pillow dengan orientasi EXIF.

## 27. Backend capabilities

Endpoint FastAPI: `GET /api/v1/health` (liveness); `GET /api/v1/ready` (mencoba load model); `GET /api/v1/model` (metadata); `POST /api/v1/predict` (deteksi asli). MIME JPEG/PNG/WEBP, maksimal 10 MiB dan 25 megapiksel. Tipe salah 415, gambar invalid 422, terlalu besar 413, checkpoint tidak tersedia 503.

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
