# Jurnal Proses — Tugas 3

## Percobaan tanpa Lock
- Hasil `processed_count` yang didapat:
- 
  <img width="548" height="167" alt="image" src="https://github.com/user-attachments/assets/34f27a2a-6e6b-45e7-9572-9c5b2285cc19" />

- Kenapa bisa meleset: jumlah pesanan yang berhasil diproses selalu kurang dari 100. terjadi karena beberapa thread mengakses dan mengubah variabel `processed_count` secara bersamaan tanpa adanya pengamanan. Misalnya, dua thread membaca nilai counter yang sama, kemudian keduanya menambahkan angka 1. Akibatnya, salah satu perubahan tertimpa oleh thread lainnya (*lost update*). Inilah yang menyebabkan jumlah pesanan yang tercatat tidak sesuai dengan jumlah pesanan sebenarnya.

## Percobaan dengan Lock
- Hasil `processed_count` setelah perbaikan:

<img width="530" height="55" alt="image" src="https://github.com/user-attachments/assets/8d875027-20a3-47e6-a278-c4d79fceda95" />


## Kendala Docker
- Error yang ditemui saat `docker build`/`docker run` dan cara memperbaikinya:
**Kendala Docker**

pertama kali run perintah `docker build`, terjadi error karena penulisan versi Python pada Dockerfile masih menggunakan `__ISI_VERSI__`. Akibatnya, Docker tidak dapat menemukan image Python yang akan digunakan.

Untuk mengatasinya, bagian tersebut diganti menjadi:

```dockerfile
FROM python:3.12-slim
```

Setelah itu, proses build berhasil dilakukan menggunakan perintah:

```bash
docker build -t foodgo-order-sim .
```

Kemudian program berhasil dijalankan menggunakan:

```bash
docker run --rm foodgo-order-sim
```

Setelah perbaikan, program dapat berjalan dengan baik di dalam Docker container.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 03/11/2026 | ChatGPT | Mengapa penggunaan mekanisme Lock diperlukan dalam proses multithreading ketika beberapa thread mengakses variabel counter yang sama? | Lock digunakan untuk mengatur akses terhadap variabel bersama agar tidak terjadi perubahan nilai secara bersamaan yang dapat menyebabkan race condition. | Memahami fungsi Lock dan membandingkan hasil counter sebelum dan sesudah menggunakan mekanisme sinkronisasi. |
| 03/11/2026 | ChatGPT | 	Bagaimana peran Dockerfile dalam proses pembuatan image dan menjalankan aplikasi Python di dalam container? | Dockerfile berisi instruksi untuk menentukan image dasar, direktori kerja, menyalin file program, dan menjalankan aplikasi di dalam container. | Mempelajari fungsi setiap instruksi Dockerfile dan menerapkannya pada simulasi pesanan FoodGo. |
