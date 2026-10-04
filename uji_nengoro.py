"""tes nengoro_angin.py: cek slot lirik, penulisan naskah, dan pembacaan melodi."""
import os
import tempfile

import nengoro_angin as na

# 1. template harus punya slot kosong untuk tiap bagian
data = na.buat_template()
assert set(data) == {nama for nama, _ in na.BAGIAN}, "nama bagian tidak lengkap"
for nama, isi in data.items():
    assert len(isi["lirik"]) == na.JUMLAH_BARIS, f"jumlah baris {nama} salah"
    assert all(b == "" for b in isi["lirik"]), f"{nama} harus mulai kosong"
    assert len(isi["kord"]) == na.JUMLAH_BARIS, f"jumlah kord {nama} salah"
print("1. template        ok")

# 2. slot lirik dan kord harus bisa diisi terpisah
data["verse1"]["lirik"][0] = "baris uji"
data["verse1"]["kord"][0] = "Am"
assert data["verse1"]["lirik"][0] == "baris uji"
assert data["verse1"]["kord"][0] == "Am"
assert data["verse1"]["lirik"][1] == "", "mengisi satu baris tidak boleh mengubah baris lain"
print("2. isi slot        ok")

# 3. naskah.txt harus ditulis, kord di atas baris lirik
nama_file = os.path.join(tempfile.mkdtemp(), "naskah.txt")
isi = na.buat_template()
isi["verse1"]["lirik"][0] = "baris uji"
isi["verse1"]["kord"][0] = "Am"
na.cetak_naskah(isi, nama_file)

with open(nama_file, encoding="utf-8") as f:
    baris = f.read().splitlines()

i = baris.index("baris uji")
assert baris[i - 1].strip() == "Am", f"kord harus tepat di atas lirik, dapat {baris[i-1]!r}"
assert baris[0] == "nengoro angin"
print("3. tulis naskah    ok")

# 4. pembacaan melodi: abaikan komentar dan baris kosong, buang nada tak dikenal
nama_melodi = os.path.join(tempfile.mkdtemp(), "melody.txt")
with open(nama_melodi, "w", encoding="utf-8") as f:
    f.write("# komentar\n\nC4\n  d4  \nZ9\nE4\n\n")

nada = na.baca_melodi(nama_melodi)
assert nada == ["C4", "D4", "E4"], f"melodi salah dibaca: {nada}"
print("4. baca melodi     ok")

# 5. semua nada harus ada di tabel frekuensi
for n in nada:
    assert n in na.NOTA_HZ, f"nada {n} tidak punya frekuensi"
print("5. tabel frekuensi ok")

# 6. pemutar nada harus jalan tanpa error
if os.name == "nt":
    na.mainkan(["C4", "E4", "G4"], durasi=10)
print("6. bunyikan        ok")

print("\nsemua tes lulus")