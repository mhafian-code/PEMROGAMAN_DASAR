"""
tipe data python - string
==========================

materi ini mengikuti slide "Python String" (slide 21-25):
membuat string, mencetak, mengakses substring dengan kurung siku,
meng-update string, fungsi-fungsi string, dan input dari command line.


catatan penting
---------------
string di python itu immutable (tidak bisa diubah). "meng-update" string
di slide berarti menugaskan ulang variabelnya dengan nilai baru, bukan
mengubah isi string yang sudah ada. jadi kode seperti ini salah:

    s = "halo"
    s[0] = "H"      # TypeError: 'str' object does not support item assignment

yang benar adalah menugaskan ulang:

    s = "H" + s[1:]
"""

import textwrap


# ------------------------------------------------------------------ membuat
# slide 21: string dibuat dengan melampirkan karakter dalam tanda kutip.
# tanda kutip tunggal dan ganda dianggap sama.
def membuat_string():
    print("=== membuat string ===")

    tunggal = 'halo'
    ganda = "halo"
    campuran = 'kata "berkutip" di dalam'
    multiline = """baris pertama
baris kedua
baris ketiga"""

    print(f"tunggal        {tunggal!r}")
    print(f"ganda          {ganda!r}")
    print(f"sama?          {tunggal == ganda}")
    print(f"campuran       {campuran}")
    print(f"multiline      {multiline!r}")
    print(f"dicetak ke layar dengan print():")
    print(multiline)


# ------------------------------------------------------------------ accessing
# slide 22: untuk mengakses substring, gunakan tanda kurung siku
def akses_substring():
    print("\n=== akses substring (kurung siku) ===")

    s = "Programming"

    print(f"s         = {s!r}")
    print(f"s[0]      {s[0]!r}    # karakter pertama")
    print(f"s[-1]     {s[-1]!r}   # karakter terakhir")
    print(f"s[0:5]    {s[0:5]!r}  # potong dari 0 sampai sebelum 5")
    print(f"s[4:]     {s[4:]!r}   # dari indeks 4 sampai akhir")
    print(f"s[:6]     {s[:6]!r}")
    print(f"s[::2]    {s[::2]!r}   # langkah 2, ambil huruf ganjil")

    # s[awal:akhir:langkah] - "akhir" tidak ikut, dan boleh dikosongkan


def update_string():
    print("\n=== meng-update string ===")

    # string immutable, jadi "update" = tugas ulang
    s = "halo dunia"
    print(f"sebelum  {s!r}")
    s = "H" + s[1:]        # ganti huruf pertama jadi kapital
    print(f"setelah  {s!r}")

    s = s.upper()
    print(f"upper()  {s!r}")

    # kode berikut akan error kalau dijalankan:
    # s[0] = "H"         # TypeError: 'str' object does not support item assignment


# ------------------------------------------------------------------ fungsi
# slide 23: strip(), len(), lower(), upper()
def fungsi_dasar():
    print("\n=== fungsi dasar string ===")

    teks = "   Programming Essentials   "

    print(f"asli   {teks!r}")
    print(f"strip() {teks.strip()!r}      # buang whitespace kiri & kanan")
    print(f"len()    {len(teks)}              # panjang string, spasi ikut dihitung")
    print(f"len tanpa spasi {len(teks.strip())}")
    print(f"lower()  {'PYTHON'.lower()!r}")
    print(f"upper()  {'python'.upper()!r}")


# slide 24: replace(), split()
def fungsi_ganti_dan_pisah():
    print("\n=== replace() dan split() ===")

    # replace()
    teks = "saya belajar python di kelas"
    print(f"asli        {teks!r}")
    print(f"replace     {teks.replace('python', 'java')!r}")
    print(f"replace 2x  {teks.replace('saya', 'kita', 2)!r}   # 2 = berapa kali")

    # split()
    kalimat = "saya, belajar, python, di kelas"
    kata = kalimat.split(", ")
    print(f"\nasli   {kalimat!r}")
    print(f"split  {kata}")
    print(f"tipe   {type(kata)}   # hasilnya list")

    # split tanpa separator memisah per spasi
    print(f"split()   {'a b  c'.split()}   # spasi berurutan jadi satu")

    # splitlines untuk teks multiline
    bait = """baris satu
baris dua
baris tiga"""
    print(f"splitlines {bait.splitlines()}")


# ------------------------------------------------------------------ input
# slide 25: proses input string pakai fungsi input()
# CATATAN: input() selalu mengembalikan string, meskipun user mengetik angka.
def input_string():
    print("\n=== input dari command line ===")
    print("(tekan enter saja untuk memakai nilai bawaan)")

    nama = input("Nama Anda    : ") or "Hafian"
    umur_teks = input("Umur Anda    : ") or "19"

    print(f"\nnama    = {nama!r}  -> {type(nama)}")
    print(f"umur    = {umur_teks!r}  -> {type(umur_teks)}")
    print("lihat, umur masih string walau user mengetik angka")

    # konversi ke int supaya bisa dipakai buat hitung-hitungan
    umur_int = konversi_ke_int(umur_teks)
    if umur_int is None:
        print(f"\n{umur_teks!r} bukan angka, dilewati")
        return

    print(f"\nsetelah int(): {umur_int!r}  -> {type(umur_int)}")
    print(f"tahun depan: {umur_int + 1}")


def konversi_ke_int(teks):
    """mengubah teks jadi int, atau None kalau bukan angka."""
    try:
        return int(teks)
    except ValueError:
        return None


# ------------------------------------------------------------------
# catatan: slide menyebut "mengupdate string dengan menugaskan kembali
# variable". ini bukan ciri khusus python, berlaku juga di bahasa lain,
# karena memang tidak ada string yang bisa diubah isinya.
def ringkasan():
    print("=== ringkasan ===")
    print(textwrap.dedent("""
        - string dibuat dengan tanda kutip tunggal atau ganda, keduanya sama
        - kurung siku untuk akses: s[0], s[-1], s[0:5], s[::2]
        - string immutable, jadi "update" berarti tugas ulang variabel
        - strip() buang whitespace, len() panjang, lower() upper() ubah case
        - replace() ganti, split() pecah jadi list
        - input() selalu menghasilkan string, konversi manual kalau butuh angka
    """).strip())


if __name__ == "__main__":
    membuat_string()
    akses_substring()
    update_string()
    fungsi_dasar()
    fungsi_ganti_dan_pisah()
    input_string()
    ringkasan()
