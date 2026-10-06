"""tes if_elif_else.py"""
import io
import contextlib

import if_elif_else as m


def tangkap(fungsi, *args):
    """menjalankan fungsi sambil menahan print, biar hasil bisa dicek diam-diam."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        hasil = fungsi(*args)
    return hasil


# 1. contoh 1 harus menghasilkan dua dari tiga print
keluaran = tangkap(m.contoh_if_saja)
assert keluaran is None
print("1. contoh if     ok")

# 2. predikat if-elif-else
assert tangkap(m.contoh_if_elif_else, 90) == "A"
assert tangkap(m.contoh_if_elif_else, 81) == "A"
assert tangkap(m.contoh_if_elif_else, 80) == "B"   # batas: 80 bukan A
assert tangkap(m.contoh_if_elif_else, 71) == "B"
assert tangkap(m.contoh_if_elif_else, 70) == "C"
assert tangkap(m.contoh_if_elif_else, 61) == "C"
assert tangkap(m.contoh_if_elif_else, 60) == "D"   # batas: 60 bukan C
assert tangkap(m.contoh_if_elif_else, 0) == "D"
assert tangkap(m.contoh_if_elif_else, -1) == "D"
print("2. predikat      ok")

# 3. konversi suhu, termasuk nilai batas
assert tangkap(m.konversi_suhu, -1) == "beku"
assert tangkap(m.konversi_suhu, 0) == "titik beku"
assert tangkap(m.konversi_suhu, 1) == "cair"
assert tangkap(m.konversi_suhu, 99) == "cair"
assert tangkap(m.konversi_suhu, 100) == "titik didih"
assert tangkap(m.konversi_suhu, 101) == "gas/uap"
print("3. konversi suhu ok")

# 4. rantai elif
for nilai, harus in [(-3, "negatif"), (0, "nol"), (7, "satu digit"),
                     (42, "dua digit"), (500, "besar"), (99, "dua digit")]:
    assert tangkap(m.nilai_rantai, nilai) == harus, f"{nilai} != {harus}"
print("4. rantai elif   ok")

# 5. hanya satu cabang yang jalan per panggilan
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    m.nilai_rantai(42)
baris = [b for b in buf.getvalue().splitlines() if b.strip()]
assert len(baris) == 2, f"harusnya 2 baris, dapat {len(baris)}"
assert baris[0] == "--- contoh 4: rantai elif, nilai = 42 ---"
assert baris[1] == "42 -> dua digit"
print("5. satu cabang   ok")

# 6. elif pertama yang TRUE menang, elif setelahnya diabaikan
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    m.konversi_suhu(150)
assert "gas/uap" in buf.getvalue()
assert "cair" not in buf.getvalue()
print("6. elseif unik   ok")

print("\nsemua tes lulus")