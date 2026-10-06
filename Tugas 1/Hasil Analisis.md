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

## Pitfall 2: [nama pitfall] — ditulis oleh [nama]

**Bukti di skenario:** [kutip/paraphrase bagian skenario]

**Kenapa ini keliru:** [penjelasan]

**Dampak ke FoodGo:** [mekanisme kegagalan konkret]

**Solusi desain awal:** [usulan solusi]

**Trade-off:** [apa yang dikorbankan/risiko dari solusi ini]


---

## Pitfall 3: [nama pitfall] — ditulis oleh [nama]

(ulangi struktur di atas)

---

## Kesimpulan Kelompok

[Ringkasan: jika FoodGo memperbaiki ketiga pitfall ini, apa arsitektur yang disarankan secara garis besar? Kaitkan dengan Tugas 2.]
