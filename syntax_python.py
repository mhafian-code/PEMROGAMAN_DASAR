"""
syntax python
=============

materi ini mengikuti slide "Syntax Python" (slide 5-9): cara menjalankan,
indentasi, comment, docstring, dan case sensitivity.


indentasi
---------
di bahasa lain indentasi cuma untuk keterbacaan kode. di python indentasi
sangat penting: python memakainya untuk menentukan awal dan akhir blok.
melewatkan indentasi akan menghasilkan IndentationError.


comment
-------
comment dimulai dengan #, python mengabaikan sisa baris setelah tanda itu.
biasanya comment diberi warna berbeda di editor.


docstring
---------
dokumentasi yang lebih lengkap dari comment. ditulis dengan tiga tanda
kutip di awal dan akhir (tanda kutip tiga), di awal dan akhir
fungsi/kelas/modul, dan bisa satu baris atau multiline. nilainya bisa
diakses lewat __doc__.
"""


# ------------------------------------------------------------------ indentasi
def contoh_indentasi():
    """fungsi ini menunjukkan kalau blok ditandai indentasi."""
    nilai = 10

    if nilai > 5:
        # dua baris di dalam if harus indentasi sama
        hasil = "lebih besar dari 5"
        print(hasil)

    # baris ini kembali ke indentasi fungsi
    return hasil


def indentasi_wrong():
    """contoh kode yang salah, sengaja tidak dijalankan."""
    kode = """
if True:
print("baris ini harus indentasi")
    """
    print(kode.strip())


# ------------------------------------------------------------------ comment
# comment satu baris
x = 10  # comment di belakang kode juga boleh

# comment bisa
# ditulis beberapa baris
# tanpa baris kosong di antaranya

y = 20  # y bernilai 20


def fungsi_dengan_comment():
    """docstring fungsi ini"""

    # nilai awal
    awal = 5

    # dikalikan dua
    return awal * 2


# ------------------------------------------------------------------ docstring
def docstring_satu_baris():
    """mengembalikan kuadrat dari sebuah angka."""
    return 7 ** 2


def docstring_multiline():
    """
    Menghitung luas lingkaran.

    Parameter:
        jari_jari (float): jari-jari lingkaran.

    Return:
        float: luas lingkaran.

    Contoh:
        >>> luas_lingkaran(3)
        28.274333882308138
    """
    jari_jari = 3
    return 3.141592653589793 * jari_jari ** 2


# ------------------------------------------------------------------ case sensitivity
def case_sensitivity():
    """python membedakan huruf besar dan huruf kecil."""
    print("=== case sensitivity ===")

    print("print()  berhasil:")
    print("halo")
    print("Print()  dan  PRINT()  akan error:")

    for salah in ("Print('halo')", "PRINT('halo')"):
        try:
            exec(salah)
        except NameError:
            print(f"  {salah:<18} -> NameError, fungsi tidak ditemukan")

    namaVariabel = 1
    namavariabel = 2
    print(f"\nnamaVariabel != namavariabel: {namaVariabel} != {namavariabel} "
          f"-> {namaVariabel == namavariabel}")


# ------------------------------------------------------------------ ringkasan
def ringkasan():
    """menampilkan ringkasan aturan syntax python."""
    print("\n=== ringkasan ===")
    print("""
indentasi   menentukan blok, pakai 4 spasi. lewati = IndentationError
comment    # sampai akhir baris, tidak dieksekusi
docstring  tiga tanda kutip di awal dan akhir, menyimpan dokumentasi
            fungsi/kelas/modul
case       print() bisa, Print() dan PRINT() error
baris baru python selesai di baris baru, tanpa titik koma
    """.strip())


if __name__ == "__main__":
    print("=== indentasi ===")
    print(f"hasil    {contoh_indentasi()}")
    indentasi_wrong()

    print("\n=== comment ===")
    print(f"x       {x}")
    print(f"y       {y}")
    print(f"fungsi  {fungsi_dengan_comment()}")

    print("\n=== docstring ===")
    print(f"satu baris   {docstring_satu_baris()}")
    print(f"multiline    {docstring_multiline():.4f}")
    print(f"\n__doc__ fungsi pertama:")
    print(f"  {contoh_indentasi.__doc__}")

    case_sensitivity()
    ringkasan()
