# Experiments — EggSizeGrader

**EggSizeGrader** merupakan proyek hari ke-38 dari portofolio [100 Days of Projects](https://github.com/MENSTRUE). Sistem mendeteksi kotak objek dan kategori anotasi (`large`, `medium`, `small`) pada foto telur menggunakan checkpoint YOLOv8n yang dipilih melalui validasi. Proyek memadukan eksperimen Kaggle dengan audit kebocoran data, inferensi FastAPI lokal, serta antarmuka React/TypeScript. **Sistem tidak mengukur diameter atau berat fisik dan bukan sistem grading komersial resmi.**

## 18. Duplicate and leakage assessment

Audit split asli menemukan **12 source key pada lintas split** dan **0 hash SHA-256 identik lintas split**. Penggabungan identitas nama asal dan hash menghasilkan **153 grup konservatif**. GroupShuffleSplit (seed 42) menjaga seluruh anggota grup pada satu split baru. Metode ini tidak menutup kemungkinan gambar mirip yang bernama atau ber-hash berbeda.

## 19. Model architecture

Detektor objek Ultralytics **YOLOv8n** (tercatat 3.011.433 parameter; head disesuaikan dari 80 menjadi 3 kelas). Checkpoint PyTorch tersimpan lokal sebagai `models/best.pt`, sementara `.pt` diabaikan Git. Inferensi pada `backend/app/inference/yolo.py` menggunakan CPU.

## 20. Experiment and baseline

Satu arsitektur pralatih dilatih; tidak ada perbandingan terkontrol antarsitektur. Baseline selalu tanpa prediksi kotak mempunyai recall nol pada data beranotasi, namun **tidak diberi mAP buatan**. Studi ini merupakan proof-of-concept satu model.

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


## 25. Error analysis and interpretation

Kelemahan relatif kelas `large` perlu telaah false negative dan kekeliruan kelas. Grid prediksi test menyediakan contoh visual, tetapi repository belum menyediakan perincian FP/FN kuantitatif per penyebab. Pergeseran domain antar kamera/cahaya belum diukur.

## 26. Model artifacts and contracts

Loader mengecek keberadaan checkpoint dan urutan kelas `large`, `medium`, `small`. `POST /api/v1/predict` mengembalikan model, dimensi gambar, deteksi (ID/label/confidence/koordinat XYXY piksel), hitungan per kelas, total, latensi, serta peringatan penelitian. Berkas didekode Pillow dengan orientasi EXIF.

## Sumber dan verifikasi

Semua hasil numerik di atas berasal dari laporan eksperimen dalam repository, bukan hasil hitung ulang pada perubahan dokumentasi ini. Studi hanya menggunakan satu arsitektur; screenshot gambar lokal merupakan demonstrasi, bukan bukti kebenaran ukuran fisik.

[README utama](../../README.md) · [reports](../../reports/README.md) · [notebook](../../notebooks/eggsizegrader.ipynb)
