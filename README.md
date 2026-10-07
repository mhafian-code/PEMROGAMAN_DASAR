# Pemrograman Dasar — Latihan Python

Kumpulan materi dan latihan Python: 7 soal latihan algoritma beserta
flowchart-nya, materi pemrograman dasar (tipe data, variabel, operator,
syntax), dan materi instruksi percabangan.

Butuh Python 3 saja, tidak ada dependensi eksternal.

## Daftar Isi

### Latihan Algoritma

| No. | Judul | Input | Proses | Output |
|-----|-------|-------|--------|--------|
| 1 | Konversi suhu Celcius ke Reamur dan Fahrenheit | suhu Celcius | `R = 4/5 * C` dan `F = 9/5 * C + 32` | suhu Reamur dan Fahrenheit |
| 2 | Sisi miring segitiga siku-siku | panjang sisi `a` dan `b` | `c = sqrt(a^2 + b^2)` | sisi miring (`c`) |
| 3 | Menghitung usia | tahun lahir (`tl`), tahun sekarang (`ts`) | `Umur = ts - tl` | cetak umur |
| 4 | Menguji status air | suhu Celcius (bilangan bulat) | `< 0` = beku, `0-100` = cair, `> 100` = gas | beku / cair / gas |
| 5 | Bilangan terbesar dari n bilangan | `n` buah bilangan | bandingkan tiap bilangan dengan maksimum saat ini | bilangan maksimum |
| 6 | Genap, ganjil, atau nol | suatu bilangan | cek `== 0`, lalu `% 2 == 0` | genap / ganjil / nol |
| 7 | Akar-akar persamaan kuadrat | `A`, `B`, `C` | `D = B^2 - 4*A*C`, lalu periksa tanda `D` | akar real atau akar imajiner |

## Materi Pemrograman Dasar

| File | Isi |
|------|-----|
| `syntax_python.py` | indentasi, comment, docstring, case sensitivity |
| `tipe_data.py` | number: int, float, complex, `type()`, konversi, `math`, random, trigonometri |
| `tipe_string.py` | membuat string, kurung siku, `strip`/`len`/`lower`/`upper`/`replace`/`split`, `input()` |
| `tipe_collection.py` | list, tuple, set, dictionary beserta method-nya |
| `variabel_operator.py` | variabel dinamis, aturan nama, output, operator aritmatika sampai bitwise |
| `if_elif_else.py` | instruksi `if`, `elif`, `else` |

```bash
python syntax_python.py       # atau file materi lain, semua bisa dijalankan langsung
```

Tiap modul berisi fungsi per topik dan bisa dijalankan langsung untuk
melihat hasilnya.

### Catatan tentang materi

Beberapa hal di slide perlu disesuaikan dengan Python 3:

- `long(x)` tidak ada di Python 3. `int()` sudah menangani bilangan bulat
  tak terbatas, jadi tidak perlu fungsi terpisah.
- String itu immutable. "Meng-update string" di slide berarti menugaskan
  ulang variabelnya, bukan mengubah isi string yang sudah ada.
- `input()` selalu mengembalikan `str`, даже kalau user mengetik angka.
  Perlu `int()` atau `float()` kalau mau dipakai buat hitung-hitungan.
- `{}` adalah dictionary kosong, bukan set kosong. Set kosong pakai `set()`.

## Latihan Algoritma

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
latihan.py                 # 7 latihan algoritma, masing-masing satu fungsi
if_elif_else.py            # materi percabangan if-elif-else
syntax_python.py           # materi syntax dasar
tipe_data.py               # materi number, konversi, math, random, trigonometri
tipe_string.py             # materi string
tipe_collection.py         # materi list, tuple, set, dict
variabel_operator.py       # materi variabel dan operator
flowchart.html             # flowchart nomor 1 sampai 7
nengoro_angin.py           # penyusun naskah interaktif + pemutar nada
melody.txt                 # contoh nada, bukan melodi asli lagu
index.html

uji_if_elif_else.py        # tes untuk if_elif_else.py
uji_pemrograman_dasar.py   # tes untuk 5 modul materi dasar
uji_nengoro.py             # tes untuk nengoro_angin.py
```

## Menjalankan Tes

```bash
python uji_pemrograman_dasar.py
python uji_if_elif_else.py
python uji_nengoro.py
```

Setiap modul materi sudah dipanggil oleh tesnya dengan output ditahan,
lalu hasilnya dicocokkan. Untuk modul yang butuh input user
(`tipe_string.input_string`) fungsinya dilewati oleh tes dan perlu
dijalankan manual.

## Catatan

- `index.html` masih halaman kosong bawaan, belum dipakai
- `melody.txt` masih berisi nada contoh. Kalau diisi melodi lengkap,
  tambahkan ke `.gitignore` karena itu juga hak cipta
