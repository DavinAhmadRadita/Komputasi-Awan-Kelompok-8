# Jurnal 5

## Implementasi Bully
- Kendala saat mengerjakan: Mengalami kesulitan dalam memahami alur komunikasi antar-node, terutama saat mengirim pesan ELECTION

## Skenario 1: Start normal
- Leader yang terpilih: Node 3
  
- Log/observasi
  
  <img width="617" height="201" alt="Screenshot 2026-11-03 213907" src="https://github.com/user-attachments/assets/88947ec0-979f-4e95-b35f-ee8000cba3cd" />
  <img width="646" height="176" alt="image" src="https://github.com/user-attachments/assets/de7e7e31-703f-4bbf-9794-513e30d6e903" />
  <img width="663" height="754" alt="image" src="https://github.com/user-attachments/assets/1204744c-33d1-4af5-b4a4-404373bcf49a" />



## Seknario 2: Leader dimatikan
- Leader yang terpilih: Node 2
- Berapa lama waktu sampai leader baru terdeteksi: waktu yang di dapatkan adalah 8,51 detik

  
  <img width="311" height="490" alt="image" src="https://github.com/user-attachments/assets/7947d76a-bae2-4e21-bad5-878cd42dded9" />


> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 3/11/2026 | gemini | TODO 1 sampai 4 apa saja yang di kerjakan | Memahami fungsi setiap pesan dan menyesuaikannya dengan alur komunikasi antar-node. Menerapkan proses election dengan mengirim pesan ke node yang memiliki ID lebih tinggi. Menyesuaikan kode untuk menetapkan leader dan mengirim pemberitahuan ke semua node. Menerapkan pengecekan kondisi leader secara berkala dan memulai election jika leader tidak merespons. | Memahami fungsi setiap bagian, kemudian menerapkannya ke dalam kode Python sesuai alur kerja Bully Algorithm dan melakukan pengujian menggunakan 3 node |
