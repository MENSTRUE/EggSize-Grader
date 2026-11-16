# Dataset Provenance — EggSizeGrader

**EggSizeGrader** merupakan proyek hari ke-38 dari portofolio [100 Days of Projects](https://github.com/MENSTRUE). Sistem mendeteksi kotak objek dan kategori anotasi (`large`, `medium`, `small`) pada foto telur menggunakan checkpoint YOLOv8n yang dipilih melalui validasi. Proyek memadukan eksperimen Kaggle dengan audit kebocoran data, inferensi FastAPI lokal, serta antarmuka React/TypeScript. **Sistem tidak mengukur diameter atau berat fisik dan bukan sistem grading komersial resmi.**

## 11. End-to-end workflow

Penemuan sumber Kaggle → audit anotasi/duplikat → pembagian ulang berbasis identitas → latih YOLOv8n → pilih `best.pt` menggunakan validasi → evaluasi held-out satu kali → salin checkpoint tepercaya ke lokal → POST gambar → validasi FastAPI → inferensi YOLO → overlay dan ekspor.

## 12. Dataset and provenance

Input yang benar-benar dipakai adalah `/kaggle/input/datasets/loliwibu/eggsizegrader-dataset`, dengan kelas `large`, `medium`, `small`. Sumber dalam YAML: [Roboflow EGGS SIZES FINAL v2](https://universe.roboflow.com/abegaille-jean-lapiz/eggs-sizes-final/dataset/2), workspace `abegaille-jean-lapiz`. Sumber dua kelas lainnya tidak dicampur. Provenance tercatat 15 November 2026 UTC.

## 13. Dataset license and attribution

YAML dataset **menyatakan** `CC BY 4.0`, tetapi izin sumber perlu diverifikasi terpisah. Atribusi proyek Roboflow dipertahankan. File `LICENSE` repository justru menyatakan **lisensi belum dipilih**, sehingga tidak ada klaim lisensi kode permisif. Lisensi Ultralytics, bobot, dan dependency perlu diperiksa sebelum distribusi.

## 14. Discovery and data audit

318 pasangan gambar/label diaudit; split sumber train 262, valid 38, test 18. Label YOLO diperiksa untuk ID kelas dan koordinat normalisasi bounding box. Tidak tercatat contoh background. Lihat `reports/source_inventory.csv` serta `reports/annotation_issues.csv`.

## 15. Classes and annotation definition

ID kelas 0=`large`, 1=`medium`, 2=`small`. Tiap anotasi YOLO memuat `class_id cx cy width height` dalam koordinat normalisasi. Nama tersebut merupakan label gambar dari anotator, bukan hasil instrumen ukur.

## 16. Cleaning and preprocessing

Gambar rusak, label hilang, ID kelas tak valid, atau bounding box di luar rentang harus menghentikan proses. Sufiks nama `.rf.*` dinormalisasi menjadi identitas sumber konservatif; hash SHA-256 dihitung. Penyiapan data menyalin pasangan gambar/label tervalidasi ke direktori kerja Kaggle.

## 17. Split and distribution

| Split | Images | Large boxes | Medium boxes | Small boxes |
|---|---:|---:|---:|---:|
| Train | 227 | 524 | 689 | 561 |
| Validation | 41 | 146 | 64 | 101 |
| Held-out test | 50 | 136 | 131 | 112 |
| **Total** | **318** | **806** | **884** | **774** |


## Sumber dan verifikasi

Semua hasil numerik di atas berasal dari laporan eksperimen dalam repository, bukan hasil hitung ulang pada perubahan dokumentasi ini. Studi hanya menggunakan satu arsitektur; screenshot gambar lokal merupakan demonstrasi, bukan bukti kebenaran ukuran fisik.

[README utama](../../README.md) · [reports](../../reports/README.md) · [notebook](../../notebooks/eggsizegrader.ipynb)
