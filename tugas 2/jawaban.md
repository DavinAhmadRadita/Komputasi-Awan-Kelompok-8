# Tugas 2 (Pekan 2) — Perancangan Arsitektur untuk FoodGo

**Materi terkait:** Architectural style (Layered, SOA, Peer-to-Peer, Publish-Subscribe).
| Nama | NIM |
|---|---|
| Davin Ahmad Radita | 103072400055 |
| Nazriel Irham Pratama Putra | 103072400062 |
| Gevin Shinarsa Pratama | 103072400080 | 
| Yoga Krisna Putra | 103072400104 |

## Studi Kasus

Melanjutkan Tugas 1: FoodGo butuh sistem yang **decoupled** agar tim kurir dan tim resto tidak saling mengganggu ketika salah satu modul diperbarui/deploy ulang. Saat ini semua modul (pesanan, pembayaran, notifikasi kurir, katalog resto) berjalan sebagai satu aplikasi monolitik — sekali deploy, semua modul ikut restart dan berisiko downtime total.

## Tugas Kelompok

1. Pilih **satu** gaya arsitektur utama: **Service-Oriented Architecture (SOA)** atau **Publish-Subscribe**. Boleh dikombinasikan (mis. SOA untuk service inti + Pub-Sub untuk notifikasi), tapi harus dijustifikasi kenapa kombinasi ini yang dipilih.
2. Gambarkan minimal 4 komponen berikut dan interaksinya: modul Pesanan, modul Pembayaran, modul Kurir/Notifikasi, modul Katalog Resto (dan message broker/API gateway jika relevan).
3. Jelaskan alur satu skenario penuh secara end-to-end di diagram (misalnya: pelanggan buat pesanan → bayar → resto terima notifikasi → kurir ditugaskan) — tunjukkan komponen mana berkomunikasi dengan siapa, dan **jenis komunikasinya** (sinkron/asinkron, request-response/event).
4. Analisis tertulis: kenapa gaya ini mengatasi masalah *coupling* dari Tugas 1, dan apa trade-off-nya (mis. Pub-Sub menambah kompleksitas debugging karena alur tidak linear).

# Jawaban
## 1. Pemilihan Gaya Arsitektur

FoodGo menggunakan gabungan arsitektur SOA (*Service-Oriented Architecture*) dan *Publish-Subscribe* supaya sistemnya lebih teratur dan setiap bagian tidak terlalu bergantung satu sama lain. Dengan SOA, fitur-fitur FoodGo dibagi menjadi beberapa layanan, seperti layanan pesanan, pembayaran, katalog restoran, dan notifikasi kurir. Setiap layanan memiliki tugas masing-masing, sehingga jika ada perubahan pada satu layanan, layanan lainnya tidak harus ikut diubah atau di-deploy ulang.

Sementara itu, *Publish-Subscribe* digunakan untuk mengirimkan informasi antar-layanan melalui *message broker*. Contohnya, ketika pembayaran berhasil, sistem akan mengirimkan event yang bisa diterima oleh layanan pesanan untuk memperbarui status dan layanan notifikasi untuk memberi tahu pihak restoran atau kurir. Jadi, layanan yang mengirim informasi tidak perlu menghubungi setiap layanan lain secara langsung.

Kombinasi kedua arsitektur ini dipilih karena FoodGo membutuhkan sistem yang bisa menangani banyak pesanan sekaligus tanpa membuat semua fitur saling mengganggu. Komunikasi sinkron digunakan untuk proses yang membutuhkan jawaban langsung, seperti pengecekan menu dan harga. Sementara itu, komunikasi asinkron digunakan untuk proses yang tidak harus langsung selesai, seperti pengiriman notifikasi dan pembaruan status pesanan. Dengan cara ini, FoodGo lebih mudah dikembangkan dan diperbarui, serta risiko gangguan pada satu layanan memengaruhi seluruh sistem dapat dikurangi.

