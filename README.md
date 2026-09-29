# Latihan Algoritma — Pemrograman dan Struktur Data

Kumpulan 7 soal latihan algoritma beserta flowchart-nya.

Repo ini berisi dua bagian: kode Python (`latihan.py`) dan diagram alur
SVG (`flowchart.html`) yang dihasilkan oleh script terpisah.

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

```bash
python buat_flowchart.py   # menulis flowchart.html
```

Buka `flowchart.html` di browser. Tiap soal ada di kotak terpisah lengkap
dengan legenda simbol, dan siap dicetak ke PDF lewat `Ctrl+P`.

Untuk memvalidasi geometri diagram (node keluar kanvas, node tumpang tindih,
garis panah yang menembus kotak, teks yang melebihi ukuran kotak):

```bash
python cek_flowchart.py   # harus keluar "MASALAH: 0"
```

## Struktur File

```
latihan.py         # 7 latihan, masing-masing satu fungsi
buat_flowchart.py  # generator flowchart.html (SVG, tanpa dependensi)
cek_flowchart.py   # pemeriksa geometri diagram
flowchart.html     # hasil generate, 7 diagram
index.html
```

### Cara flowchart dibuat

Koordinat tiap bentuk dihitung di `buat_flowchart.py`. Kelas `Node`
menggambar satu simbol flowchart dan menyimpan koordinat sisinya (`top`,
`bottom`, `left`, `right`), sehingga pemanggilan berikutnya cukup
menghitung titik sambung antar simbol:

```python
a = Node(380, 30, "MULAI", "terminal")
b = Node(380, 100, "Input suhu Celcius (C)", "input")
edge([(380, a.bottom), (380, b.top)])
```

Jenis simbol yang tersedia: `terminal` (mulai / selesai), `proses`,
`input`, `output`, `decision` (percabangan), dan `merge` (titik gabung
untuk cabang yang berakhir pada output yang sama).

## Catatan

- repo ini belum punya unit test, verifikasi dilakukan dengan memanggil
  tiap latihan memakai input yang diketahui lalu mencocokkan hasilnya secara manual
- `index.html` masih halaman kosong bawaan, belum dipakai
