"""
variabel dan operator python
============================

materi ini mengikuti slide "Variable Python" (slide 46-49) dan
"Operator Python" (slide 50-57).


variabel bersifat dinamis
-------------------------
python tidak perlu deklarasi tipe data. variabel dibuat begitu ada nilai
yang ditugaskan ke dalamnya, dan tipenya bisa berubah saat program berjalan:

    x = 10        # x jadi int
    x = "halo"    # sekarang x jadi str, tidak ada error


aturan penamaan variabel (slide 47)
------------------------------------
- karakter pertama harus huruf atau garis bawah ( _ )
- karakter berikutnya boleh huruf, garis bawah, atau angka
- case-sensitive: umur dan Umur itu dua variabel berbeda
- hindari nama yang bentrok dengan keyword python (if, class, dll)
"""


# ------------------------------------------------------------------ variabel
# slide 46: variabel adalah lokasi memori untuk menyimpan nilai
def variabel_dasar():
    print("=== variabel ===")

    nama = "Hafian"          # str
    umur = 19                # int
    tinggi = 1.72            # float
    aktif = True             # bool
    hobbi = ["baca", "koding"]   # list

    print(f"nama    {nama!r}    -> {type(nama)}")
    print(f"umur    {umur!r}       -> {type(umur)}")
    print(f"tinggi  {tinggi!r}     -> {type(tinggi)}")
    print(f"aktif   {aktif!r}     -> {type(aktif)}")
    print(f"hobbi   {hobbi}      -> {type(hobbi)}")


def variabel_dinamis():
    print("\n=== sifat dinamis variabel ===")

    x = 10
    print(f"x = 10          tipe {type(x)}")

    x = 3.14
    print(f"x = 3.14        tipe {type(x)}   # tipe berubah, tidak perlu deklarasi")

    x = "sekarang string"
    print(f"x = 'string'    tipe {type(x)}")

    print("\nsatu variabel bisa dipakai ulang untuk tipe berbeda,")
    print("tapi lebih baik pakai nama berbeda supaya kode enak dibaca.")


# slide 47: aturan penamaan
def aturan_nama():
    print("\n=== aturan nama variabel ===")

    # valid
    nama = "Hafian"
    _privat = "okay mulai garis bawah"
    _nama2 = "garis bawah + angka"
    namaPanjang = "camelCase"

    print(f"nama          {nama}")
    print(f"_privat       {_privat}")
    print(f"_nama2        {_nama2}")
    print(f"namaPanjang   {namaPanjang}")

    # case-sensitive
    umur = 19
    Umur = 20
    print(f"\numur = {umur}")
    print(f"Umur = {Umur}   # dua variabel berbeda")

    # invalid
    print("\ncoba nama yang tidak valid:")
    try:
        exec("2nilai = 10")
    except SyntaxError:
        print("  2nilai = 10      -> SyntaxError, tidak boleh mulai angka")
    try:
        exec("nama tengah = 10")
    except SyntaxError:
        print("  'nama tengah'    -> SyntaxError, tidak boleh ada spasi")
    try:
        exec("class = 10")
    except SyntaxError:
        print("  class = 10       -> SyntaxError, 'class' itu keyword python")


# slide 48: output variabel, print(), dan operator +
def output_variabel():
    print("\n=== output variabel ===")

    # print menerima banyak argumen, dipisah spasi
    print("nilai a =", 5, "dan b =", 3)

    # menggabungkan teks dan variabel dengan +
    nama = "Hafian"
    umur = 19
    print("halo, nama saya " + nama + ", umur " + str(umur) + " tahun")

    # + bisa menyambung dari variabel ke variabel
    depan = "belajar"
    belakang = "python"
    print(depan + " " + belakang)

    # cara lain yang lebih rapi: f-string
    print(f"halo, nama saya {nama}, umur {umur} tahun")


# slide 49: untuk angka, + itu operator matematika. string + angka = error
def plus_v_salah():
    print("\n=== + antara string dan angka ===")

    x = 5
    y = 3
    print(f"x + y = {x + y}   # angka + angka = penjumlahan")

    s = "5"
    print(f"s = {s!r}")
    print("s + x:")
    try:
        s + x
    except TypeError:
        print("  TypeError: can only concatenate str (not \"int\") to str")
    print("solusinya: ubah ke string dulu pakai str() atau f-string")
    print(f"  s + str(x) = {s + str(x)}")
    print(f"  f-string    = {s}{x}")


# ------------------------------------------------------------------ operator
# slide 51: arithmetic
def operator_aritmetik():
    print("\n=== operator aritmatika ===")

    a = 12
    b = 5

    print(f"a = {a}, b = {b}")
    print(f"a + b   = {a + b}     # penjumlahan")
    print(f"a - b   = {a - b}     # pengurangan")
    print(f"a * b   = {a * b}     # perkalian")
    print(f"a / b   = {a / b}      # pembagian, hasilnya float")
    print(f"a // b  = {a // b}     # pembagian bulat")
    print(f"a % b   = {a % b}     # sisa pembagian (modulo)")
    print(f"a ** b  = {a ** b}    # pangkat")
    print(f"-a      = {-a}      # unary negatif")

    # urutannya penting, ** paling kuat
    print(f"\n2 ** 3 ** 2     = {2 ** 3 ** 2}   # dihitung dari kanan")
    print(f"(2 ** 3) ** 2   = {(2 ** 3) ** 2}   # pakai kurung untuk memaksa kiri")
    print(f"10 / 3 * 3      = {10 / 3 * 3}     # kiri ke kanan")


# slide 52: assignment
def operator_penugasan():
    print("\n=== operator penugasan ===")

    x = 10
    print(f"x = 10      -> {x}")

    x += 5      # x = x + 5
    print(f"x += 5      -> {x}")
    x -= 3
    print(f"x -= 3      -> {x}")
    x *= 2
    print(f"x *= 2      -> {x}")
    x /= 4
    print(f"x /= 4      -> {x}")
    x //= 3
    print(f"x //= 3     -> {x}")
    x **= 3
    print(f"x **= 3     -> {x}")
    x %= 50
    print(f"x %= 50     -> {x}")

    # assignment berantai
    a = b = c = 7
    print(f"\na = b = c = 7   -> a={a}, b={b}, c={c}")


# slide 53: comparison
def operator_perbandingan():
    print("\n=== operator perbandingan ===")

    a = 10
    b = 5

    print(f"a = {a}, b = {b}")
    print(f"a == b    {a == b}     # sama dengan")
    print(f"a != b    {a != b}     # tidak sama dengan")
    print(f"a > b     {a > b}     # lebih besar")
    print(f"a < b     {a < b}     # lebih kecil")
    print(f"a >= b    {a >= b}    # lebih besar sama dengan")
    print(f"a <= b    {a <= b}    # lebih kecil sama dengan")

    # mengurutkan dengan berantai
    print(f"\n1 < 2 < 3     {1 < 2 < 3}   # bisa dirantai")
    print(f"3 < 2 < 1     {3 < 2 < 1}")

    # perbandingan string
    print(f"\n'apel' < 'jeruk'   {'apel' < 'jeruk'}   # ikut urutan alfabet")


# slide 54: logical
def operator_logika():
    print("\n=== operator logika ===")

    a = 10
    b = 5

    print(f"a = {a}, b = {b}")
    print(f"a > 5 and b > 3     {a > 5 and b > 3}")
    print(f"a > 5 and b > 10    {a > 5 and b > 10}")
    print(f"a > 15 or b > 3     {a > 15 or b > 3}")
    print(f"a > 15 or b > 10    {a > 15 or b > 10}")
    print(f"not (a > 5)         {not (a > 5)}")

    # short-circuit: python tidak mengevaluasi bagian kanan kalau tidak perlu
    print("\nshort-circuit:")
    print(f"  False and print()  -> {False and print('tidak dicetak')}")
    print(f"  True or print()    -> {True or print('tidak dicetak')}")


# slide 55: identity
def operator_identitas():
    print("\n=== operator identitas (is / is not) ===")

    a = 100
    b = 100
    c = [1, 2, 3]
    d = [1, 2, 3]

    print(f"a = {a}, b = {b}")
    print(f"a is b              {a is b}    # objek kecil di-cache python")

    print(f"\nc = {c}, d = {d}   # isi sama tapi objek berbeda")
    print(f"c is d              {c is d}")
    print(f"c == d              {c == d}    # nilainya sama")
    print(f"c is not d          {c is not d}")

    print("\ncatatan: pakai is hanya untuk None, True, False.")
    print("untuk perbandingan nilai biasa, pakai == .")
    print(f"  x = None; x is None   {None is None}   # ini yang benar")
    print(f"  x = None; x == None   {None == None}   # kebetulan sama juga")


# slide 56: membership
def operator_keanggotaan():
    print("\n=== operator keanggotaan (in / not in) ===")

    buah = ["apel", "jeruk", "mangga"]
    teks = "programming"

    print(f"buah    = {buah}")
    print(f"'jeruk' in buah      {'jeruk' in buah}")
    print(f"'durian' in buah     {'durian' in buah}")
    print(f"'durian' not in buah {'durian' not in buah}")

    print(f"\nteks    = {teks!r}")
    print(f"'gram' in teks       {'gram' in teks}")
    print(f"'xyz' in teks        {'xyz' in teks}")

    print(f"\nbisa dipakai juga untuk dict, dicek terhadap kunci:")
    siswa = {"nama": "Hafian", "nim": "12345"}
    print(f"'nama' in siswa      {'nama' in siswa}")


# slide 57: bitwise
def operator_bitwise():
    print("\n=== operator bitwise (bit per bit) ===")

    a = 12   # 1100
    b = 10   # 1010

    print(f"a = {a}  -> {a:04b}")
    print(f"b = {b}  -> {b:04b}")
    print(f"a & b   {a & b}  -> {a & b:04b}   # AND, 1 hanya kalau dua-duanya 1")
    print(f"a | b   {a | b}  -> {a | b:04b}   # OR, 1 kalau salah satunya 1")
    print(f"a ^ b   {a ^ b}  -> {a ^ b:04b}   # XOR, 1 kalau berbeda")
    print(f"~a      {~a}  -> {~a:04b}  # NOT, balik semua bit")

    print(f"\nshift:")
    print(f"a << 1  {a << 1}   # geser kiri 1 bit, sama dengan kali 2")
    print(f"a >> 2  {a >> 2}   # geser kanan 2 bit, sama dengan bagi 4")

    print("\npenggunan:")
    print(f"  cek genap    x % 2 == 0")
    print(f"  cek ganjil   x % 2 == 1")


if __name__ == "__main__":
    variabel_dasar()
    variabel_dinamis()
    aturan_nama()
    output_variabel()
    plus_v_salah()

    operator_aritmetik()
    operator_penugasan()
    operator_perbandingan()
    operator_logika()
    operator_identitas()
    operator_keanggotaan()
    operator_bitwise()
