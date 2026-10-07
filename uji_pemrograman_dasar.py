"""
tes untuk materi pemrograman dasar
==================================

menjalankan tiap modul dan mengecek hasilnya. setiap fungsi dibungkus supaya
print di dalamnya tertahan, sehingga yang dicek cuma nilai balik.

jalankan: python uji_pemrograman_dasar.py
"""

import contextlib
import io

import syntax_python
import tipe_collection
import tipe_data
import tipe_string
import variabel_operator


def diamkan(fungsi, *args, **kwargs):
    """jalankan fungsi sambil menahan output print."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        hasil = fungsi(*args, **kwargs)
    return hasil


# ================================================================== tipe_data
def tes_tipe_data():
    print("[1] tipe_data")

    # type() harus sesuai
    assert type(100) is int
    assert type(3.14) is float
    assert type(2 + 5j) is complex
    assert type("halo") is str
    assert type(True) is bool
    print("    type() benar")

    # int tanpa batas
    besar = 123456789012345678901234567890
    assert besar + 1 == 123456789012345678901234567891
    print("    int panjang tak terbatas")

    # float
    assert 1.5e3 == 1500.0
    assert 1.5e-3 == 0.0015
    print("    float scientific")

    # pembagian int selalu float, // tetap int
    assert type(10 / 3) is float
    assert type(10 // 3) is int
    assert 10 // 3 == 3
    print("    pembagian dan //")

    # complex
    a = 2 + 5j
    assert a.real == 2.0 and a.imag == 5.0
    assert complex(4, 7) == complex(4, 7)
    print("    complex .real .imag")

    # konversi
    assert int("42") == 42
    assert int(3.99) == 3
    assert round(3.99) == 4
    assert float(7) == 7.0
    assert complex(7, 5) == complex(7, 5)
    print("    konversi tipe")

    # math
    import math
    assert math.sqrt(16) == 4.0
    assert math.floor(3.7) == 3
    assert math.ceil(3.2) == 4
    assert math.gcd(12, 18) == 6
    print("    fungsi matematika")

    # trigonometri pakai radian
    assert abs(math.sin(math.pi / 2) - 1.0) < 1e-9
    assert math.degrees(math.pi) == 180.0
    print("    trigonometri")

    # random harus dalam rentang yang benar
    import random
    random.seed(1)
    for _ in range(50):
        assert 0.0 <= random.random() < 1.0
    for _ in range(50):
        assert 1 <= random.randint(1, 6) <= 6
    print("    random dalam rentang")

    # semua modul harus bisa dijalankan tanpa error
    for nama in ("verifikasi_tipe", "tipe_int", "tipe_float", "tipe_complex",
                 "konversi_tipe", "fungsi_matematika", "fungsi_random",
                 "fungsi_trigonometri", "catatan_long"):
        diamkan(getattr(tipe_data, nama))
    print("    semua fungsi jalan")


# ================================================================== tipe_string
def tes_tipe_string():
    print("[2] tipe_string")

    # input_string() tidak dipanggil di sini karena butuh ketikan dari user
    for nama in ("membuat_string", "akses_substring", "update_string",
                 "fungsi_dasar", "fungsi_ganti_dan_pisah", "ringkasan"):
        diamkan(getattr(tipe_string, nama))
    print("    semua fungsi jalan (input_string dilewati, butuh input user)")

    # kutip tunggal dan ganda sama
    assert 'halo' == "halo"

    # slicing
    s = "Programming"
    assert s[0] == "P"
    assert s[-1] == "g"
    assert s[0:5] == "Progr"
    assert s[4:] == "ramming"
    assert s[::2] == "Pormig"
    print("    slicing kurung siku")

    # string immutable
    try:
        s[0] = "X"
        assert False, "harus error"
    except TypeError:
        print("    string immutable")

    # konversi aman
    assert tipe_string.konversi_ke_int("19") == 19
    assert tipe_string.konversi_ke_int("bukan angka") is None
    print("    konversi_ke_int aman")


# ================================================================== collection
def tes_collection():
    print("[3] tipe_collection")

    for nama in ("list_dasar", "list_cek_dan_tambah", "list_hapus",
                 "list_konstruktor", "list_method", "tuple_dasar",
                 "tuple_konstruktor_method", "set_dasar", "set_ubah_dan_hapus",
                 "set_konstruktor", "set_method", "dict_dasar", "dict_hapus",
                 "dict_konstruktor", "dict_method", "ringkasan"):
        diamkan(getattr(tipe_collection, nama))
    print("    semua fungsi jalan")

    # list bisa diubah
    x = [1, 2, 3]
    x[0] = 99
    assert x == [99, 2, 3]
    x.append(4)
    assert len(x) == 4
    x.insert(0, 0)
    assert x[0] == 0
    assert 2 in x
    x.remove(2)
    assert 2 not in x
    assert x.pop(0) == 0
    x.clear()
    assert x == []
    print("    list")

    # list("abc") memecah per karakter
    assert list("abc") == ["a", "b", "c"]
    assert list(range(3)) == [0, 1, 2]

    # sorted() tidak mengubah list asli
    asli = [3, 1, 2]
    assert sorted(asli) == [1, 2, 3]
    assert asli == [3, 1, 2]
    print("    sorted() tidak mengubah asli")

    # tuple immutable
    t = (1, 2, 3)
    try:
        t[0] = 99
        assert False, "harus error"
    except TypeError:
        print("    tuple immutable")

    assert (5,) != 5            # koma wajib
    assert type((5,)) is tuple
    assert 2 in t and len(t) == 3
    print("    tuple")

    # set unik dan tanpa indeks
    s = {1, 2, 2, 3}
    assert len(s) == 3
    try:
        s[0]
        assert False, "harus error"
    except TypeError:
        print("    set tanpa indeks")

    assert set() != {}          # set() kosong, {} itu dict
    s.discard(99)               # discard aman kalau nilai tidak ada
    print("    set() bukan {}")

    # dict
    d = {"a": 1, "b": 2}
    assert d["a"] == 1
    assert d.get("z", 0) == 0
    assert "a" in d and "z" not in d
    d["c"] = 3
    assert len(d) == 3
    assert d.pop("c") == 3
    d.clear()
    assert d == {}
    print("    dict")


# ================================================================== variabel
def tes_variabel_operator():
    print("[4] variabel_operator")

    for nama in ("variabel_dasar", "variabel_dinamis", "aturan_nama",
                 "output_variabel", "plus_v_salah", "operator_aritmetik",
                 "operator_penugasan", "operator_perbandingan", "operator_logika",
                 "operator_identitas", "operator_keanggotaan", "operator_bitwise"):
        diamkan(getattr(variabel_operator, nama))
    print("    semua fungsi jalan")

    # variabel dinamis
    y = 10
    y = "str"
    assert type(y) is str
    print("    variabel dinamis")

    # aritmetika
    assert 12 + 5 == 17
    assert 12 - 5 == 7
    assert 12 * 5 == 60
    assert 12 / 5 == 2.4
    assert 12 // 5 == 2
    assert 12 % 5 == 2
    assert 2 ** 10 == 1024
    assert -12 == -12
    assert 2 ** 3 ** 2 == 512
    assert (2 ** 3) ** 2 == 64
    print("    aritmetika")

    # penugasan
    z = 10
    z += 5
    assert z == 15
    z *= 2
    assert z == 30
    a = b = c = 7
    assert a == b == c == 7
    print("    penugasan")

    # perbandingan
    assert (10 == 10) and (10 != 5) and (10 > 5) and (10 < 50)
    assert (10 >= 10) and (10 <= 10)
    assert 1 < 2 < 3
    assert not (3 < 2 < 1)
    print("    perbandingan")

    # logika
    assert True and True
    assert not (True and False)
    assert True or False
    assert not (False or False)
    assert not True is False
    print("    logika")

    # identitas dan keanggotaan
    assert None is None
    assert [1, 2] == [1, 2]
    assert [1, 2] is not [1, 2]
    assert "jeruk" in ["apel", "jeruk"]
    assert "durian" not in ["apel"]
    assert "gram" in "programming"
    print("    identitas dan keanggotaan")

    # bitwise
    assert 12 & 10 == 8
    assert 12 | 10 == 14
    assert 12 ^ 10 == 6
    assert ~12 == -13
    assert 12 << 1 == 24
    assert 12 >> 2 == 3
    print("    bitwise")

    # string + int harus error
    try:
        "5" + 5
        assert False, "harus error"
    except TypeError:
        print("    str + int error")


# ================================================================== syntax
def tes_syntax():
    print("[5] syntax_python")

    assert diamkan(syntax_python.contoh_indentasi) == "lebih besar dari 5"
    assert diamkan(syntax_python.docstring_satu_baris) == 49
    assert abs(diamkan(syntax_python.docstring_multiline) - 28.274333882308138) < 1e-9
    assert diamkan(syntax_python.fungsi_dengan_comment) == 10
    for nama in ("indentasi_wrong", "case_sensitivity", "ringkasan"):
        diamkan(getattr(syntax_python, nama))
    print("    semua fungsi jalan")

    # docstring harus ada di __doc__
    assert syntax_python.contoh_indentasi.__doc__ is not None
    assert "kuadrat" in syntax_python.docstring_satu_baris.__doc__
    print("    __doc__ terisi")

    # indentasi salah harus IndentationError
    try:
        compile("if True:\nprint(1)", "<uji>", "exec")
        assert False, "harus error"
    except IndentationError:
        print("    indentasi salah terdeteksi")


if __name__ == "__main__":
    print("=== tes pemrograman dasar ===\n")
    tes_tipe_data()
    tes_tipe_string()
    tes_collection()
    tes_variabel_operator()
    tes_syntax()
    print("\nsemua tes lulus")
