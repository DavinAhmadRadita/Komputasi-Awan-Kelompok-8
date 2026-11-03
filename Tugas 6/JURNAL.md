# Jurnal Proses — Tugas 6

## Implementasi find_successor
- Kesalahan pertama yang ditemui (mis. lupa wrap-around di ring): Pada awal implementasi, saya masih perlu memahami cara menentukan node successor pada ring, terutama ketika tidak ada node dengan ID yang lebih besar atau sama dengan hash key.
- Cara memperbaikinya: Saya mengurutkan node_id menggunakan sorted(), kemudian mencari node pertama yang memiliki node_id >= key_hash. Jika tidak ditemukan, digunakan node_ids[0] sebagai wrap-around ke node dengan ID terkecil.

## Skenario join/leave
- Hasil sebelum & sesudah node baru bergabung: Sebelum node baru bergabung terdapat 4 node, yaitu node dengan ID hash 40, 102, 136, dan 177. Kemudian node-medan-1 bergabung dengan ID hash 123. Node baru tersebut masuk di antara node 102 dan 136 pada ring. Program menampilkan simulasi perpindahan tanggung jawab data ke node baru.
- Hasil sebelum & sesudah node keluar: Sebelum perubahan terdapat node dengan ID hash 177 (node-jakarta-1). Setelah node tersebut keluar, node 177 dihapus dari ring dan successor baru ditentukan, yaitu node dengan ID hash 40. Program menampilkan simulasi perpindahan tanggung jawab data dari node yang keluar ke successor baru. Hasil lookup kurir-001 dan kurir-002 tetap dapat menemukan alamat IP masing-masing.
  
- Tugas ini sudah sesuai dengan syarat yang diberikan

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 11/3/2026 | ChatGPT | apakah codingan ini sudah sesuai dengan tugas yang diberikan? | Secara keseluruhan sudah benar | Tugas ini sudah sesuai dengan syarat yang diberikan |
