# Latihan Algoritma — Pemrograman dan Struktur Data

Kumpulan 7 soal latihan algoritma beserta flowchart-nya.

Berisi kode Python (`latihan.py`) dan diagram alur SVG (`flowchart.html`).

## Daftar Isi

| No. | Judul | Input | Proses | Output |
|-----|-------|-------|--------|--------|
| 1 | Konversi suhu Celcius ke Reamur dan Fahrenheit | suhu Celcius | `R = 4/5 * C` dan `F = 9/5 * C + 32` | suhu Reamur dan Fahrenheit |
| 2 | Sisi miring segitiga siku-siku | panjang sisi `a` dan `b` | `c = sqrt(a^2 + b^2)` | sisi miring (`c`) |
| 3 | Menghitung usia | tahun lahir (`tl`), tahun sekarang (`ts`) | `Umur = ts - tl` | cetak umur |
| 4 | Menguji status air | suhu Celcius (bilangan bulat) | `< 0` = beku, `0-100` = cair, `> 100` = gas | beku / cair / gas |
| 5 | Bilangan terbesar dari n bilangan | `n` buah bilangan | bandingkan tiap bilangan dengan maksimum saat ini | bilangan maksimum |
| 6 | Genap, ganjil, atau nol | suatu bilangan | cek `== 0`, lalu `% 2 == 0` | genap / ganjil / nol |
| 7 | Akar-akar persamaan kuadrat | `A`, `B`, `C` | `D = B^2 - 4*A*C`, lalu periksa tanda `D` | akar real atau akar imajiner |

## Cara Menjalankan

Butuh Python 3, tidak ada dependensi eksternal.

```bash
python latihan.py
```

Program menampilkan menu, masukkan nomor latihan (1-7) atau `0` untuk keluar.
Semua nilai diambil dari input user, termasuk tahun sekarang dan jumlah
bilangan.

## Flowchart

Buka `flowchart.html` di browser. Tiap soal ada di kotak terpisah lengkap
dengan legenda simbol, dan siap dicetak ke PDF lewat `Ctrl+P`.

Diagram digambar sebagai SVG langsung di dalam `flowchart.html`, tidak ada
library atau dependensi tambahan.

## Struktur File

```
latihan.py       # 7 latihan, masing-masing satu fungsi
flowchart.html   # flowchart nomor 1 sampai 7
index.html
```

## Catatan

- repo ini belum punya unit test, verifikasi dilakukan dengan memanggil
  tiap latihan memakai input yang diketahui lalu mencocokkan hasilnya secara manual
- `index.html` masih halaman kosong bawaan, belum dipakai
