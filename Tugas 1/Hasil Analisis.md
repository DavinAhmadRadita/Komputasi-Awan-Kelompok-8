# Tugas 1 — Analisis Pitfall FoodGo

**Kelompok:** [nama kelompok]

| Nama | NIM | Kontribusi |
|---|---|---|
| Davin Ahmad Radita | 103072400055 | Pitfall 1 |
| Nazriel Irham Pratama Putra | 103072400062 | [pitfall/bagian yang dikerjakan] |
| Gevin Shinarsa Pratama | 103072400080 | pitfall 2 |
| Yoga Krisna Putra | 103072400104 | [pitfall/bagian yang dikerjakan] |

## Pitfall 1: The Network Is Reliable — ditulis oleh Davin Ahmad Radita

**Bukti di skenario:** Tim engineering FoodGo menulis asumsi “network is always reliable, no need for retry”

**Kenapa ini keliru:** Ketika modul Pesanan berkomunikasi dengan modul Pembayaran dan terjadi gangguan jaringan, request dapat gagal. Karena FoodGo tidak memiliki mekanisme retry, proses pembayaran atau pemesanan dapat terganggu dan menyebabkan request pengguna gagal

**Dampak ke FoodGo:** Ketika modul Pesanan berkomunikasi dengan modul Pembayaran dan terjadi gangguan jaringan, request dapat gagal. Karena FoodGo tidak memiliki mekanisme retry, proses pembayaran atau pemesanan dapat terganggu dan menyebabkan request pengguna gagal

**Solusi desain awal:** Menerapkan timeout dan retry dengan exponential backoff pada komunikasi antar-service. Selain itu, dapat digunakan circuit breaker untuk menghentikan sementara request ke service yang sedang mengalami gangguan

**Trade-off:** Retry dapat membantu mengatasi kegagalan sementara, tetapi jika service sedang overload, retry yang terlalu banyak justru dapat menambah beban dan menyebabkan cascading failure. Karena itu jumlah retry harus dibatasi

---

## Pitfall 2: Latency Is Zero — ditulis oleh Gevin Shinarsa Pratama

**Bukti di skenario:** Modul Pesanan memanggil modul Pembayaran dan menunggu tanpa batas waktu karena tidak terdapat timeout pada komunikasi antar-service.

**Kenapa ini keliru:** Dalam sistem terdistribusi, komunikasi antar-service selalu membutuhkan waktu. Latency juga dapat meningkat ketika trafik sedang tinggi atau service yang dituju sedang mengalami beban berat. Jadi, respons dari service tidak dapat dianggap selalu datang dengan cepat.

**Dampak ke FoodGo:** Saat terjadi lonjakan pesanan, modul Pembayaran menjadi lambat. Modul Pesanan yang menunggu respons tanpa batas waktu menyebabkan banyak request tertahan. Akibatnya resource server semakin banyak digunakan, aplikasi menjadi lambat, request mengalami timeout, dan pada kondisi tertentu server dapat crash.

**Solusi desain awal:** Memberikan timeout pada setiap komunikasi antar-service. Jika proses tidak harus mendapatkan respons secara langsung, FoodGo juga dapat menggunakan message queue dan asynchronous processing.

**Trade-off:** Timeout dapat membuat request lebih cepat dihentikan ketika service lambat, tetapi proses yang sebenarnya masih berjalan mungkin dianggap gagal oleh sistem. Penggunaan message queue juga membuat arsitektur menjadi lebih kompleks.


---

## Pitfall 3: Single Point of Failure — ditulis oleh Yoga Krisna Putra

**Bukti di skenario:**
Satu server menangani seluruh modul FoodGo, yaitu pesanan, pembayaran, dan notifikasi kurir dalam satu proses monolitik yang sama.

**Kenapa ini keliru:**
Ketika semua fungsi bergantung pada satu server dan satu proses, server tersebut menjadi single point of failure. Jika server mengalami overload atau crash, seluruh fungsi aplikasi dapat ikut berhenti.

**Dampak ke FoodGo:**
Ketika trafik meningkat pada jam makan siang atau saat promo besar, satu server harus menangani banyak request dari berbagai modul. Server akhirnya kewalahan dan dapat crash total, sehingga layanan pesanan, pembayaran, dan notifikasi kurir ikut terganggu dan membutuhkan restart manual.

**Solusi desain awal:**
Memisahkan modul menjadi beberapa service, misalnya Order Service, Payment Service, dan Notification Service. Setiap service dapat dijalankan pada beberapa instance dan menggunakan load balancer sehingga beban tidak hanya ditanggung oleh satu server.

**Trade-off:**
Memisahkan sistem menjadi beberapa service meningkatkan skalabilitas dan reliability, tetapi membuat sistem lebih kompleks. FoodGo harus menangani komunikasi antar-service, deployment yang lebih banyak, monitoring, serta kemungkinan kegagalan jaringan antar-service.
---

## Kesimpulan Kelompok

[Ringkasan: jika FoodGo memperbaiki ketiga pitfall ini, apa arsitektur yang disarankan secara garis besar? Kaitkan dengan Tugas 2.]
