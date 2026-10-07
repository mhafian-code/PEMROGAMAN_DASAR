"""
tipe data python - number
=========================

materi ini mengikuti slide "Python Number" (slide 12-20):
number, verifikasi type(), int, float, complex, konversi tipe,
fungsi matematika, random, dan trigonometri.

number adalah tipe data yang tidak berubah (immutable). mengubah nilainya
akan menghasilkan objek baru yang dialokasikan ulang. objek number dibuat
saat pertama kali kita memberikan nilai.
"""

import math
import random


# ------------------------------------------------------------------ type()
# slide 13: untuk memverifikasi tipe objek, gunakan fungsi type()
def verifikasi_tipe():
    print("=== verifikasi tipe dengan type() ===")

    angka = 100
    desimal = 3.14
    kompleks = 2 + 5j
    teks = "halo"

    print(f"nilai {angka!r} bertipe {type(angka)}")
    print(f"nilai {desimal!r} bertipe {type(desimal)}")
    print(f"nilai {kompleks!r} bertipe {type(kompleks)}")
    print(f"nilai {teks!r} bertipe {type(teks)}")

    # bool adalah turunan dari int di python, jadi type() nya bool
    benar = True
    print(f"nilai {benar!r} bertipe {type(benar)}")


# ------------------------------------------------------------------ int
# slide 14: integer, positif maupun negatif, tanpa desimal, panjang tak terbatas
def tipe_int():
    print("\n=== int ===")

    positif = 20
    negatif = -7
    nol = 0
    besar = 123456789012345678901234567890  # panjang tak terbatas

    print(f"positif   {positif} -> {type(positif)}")
    print(f"negatif   {negatif} -> {type(negatif)}")
    print(f"nol       {nol} -> {type(nol)}")
    print(f"besar     {besar}")
    print(f"besar + 1 {besar + 1}   # tidak overflow")

    # basis lain
    print(f"binair    0b1010 -> {0b1010}")
    print(f"oktal     0o17   -> {0o17}")
    print(f"heksa     0xFF   -> {0xFF}")


# ------------------------------------------------------------------ float
# slide 15: angka dengan satu atau lebih desimal, bisa scientific dengan 'e'
def tipe_float():
    print("\n=== float ===")

    desimal = 3.14
    negatif = -0.5
    scientific_kecil = 1.5e3      # 1.5 x 10^3
    scientific_besar = 1.5e-3     # 1.5 x 10^-3

    print(f"desimal        {desimal} -> {type(desimal)}")
    print(f"negatif        {negatif}")
    print(f"1.5e3          {scientific_kecil}")
    print(f"1.5e-3         {scientific_besar}")

    # membagi dua int selalu menghasilkan float, termasuk yang|genzahl|
    print(f"10 / 3         {10 / 3}   -> {type(10 / 3)}")
    print(f"10 / 4         {10 / 4}")
    print(f"10 // 4        {10 // 4}  -> {type(10 // 4)}  # pembagian bulat")


# ------------------------------------------------------------------ complex
# slide 16: complex ditulis dengan 'j' sebagai bagian imaginary
def tipe_complex():
    print("\n=== complex ===")

    a = 2 + 5j
    b = -3j
    c = complex(4, 7)   # cara lain: real 4, imaginary 7

    print(f"{a} -> {type(a)}")
    print(f"real part     {a.real}")
    print(f"imaginary     {a.imag}")
    print(f"hanya imajiner {b}")
    print(f"dibuat fungsi {c}")
    print(f"{a} + {a} = {a + a}")


# ------------------------------------------------------------------ konversi
# slide 17: int(x), float(x), complex(x), complex(x, y)
def konversi_tipe():
    print("\n=== konversi tipe ===")

    teks_angka = "42"
    desimal = 3.99
    bilangan = 7

    print(f"int('{teks_angka}')        -> {int(teks_angka)}")
    print(f"int({desimal})           -> {int(desimal)}   # bagian desimal dibuang")
    print(f"int({desimal}) dibulatkan  -> {round(desimal)}")
    print(f"float({bilangan})          -> {float(bilangan)}")
    print(f"float('{teks_angka}')      -> {float(teks_angka)}")
    print(f"complex({bilangan})         -> {complex(bilangan)}")
    print(f"complex({bilangan}, 5)      -> {complex(bilangan, 5)}")


# ------------------------------------------------------------------ matematika
# slide 18: fungsi matematika
def fungsi_matematika():
    print("\n=== fungsi matematika (math) ===")

    x = 16

    print(f"sqrt({x})      {math.sqrt(x)}")
    print(f"pow(2, 10)    {math.pow(2, 10)}")
    print(f"floor(3.7)    {math.floor(3.7)}   # bulatkan ke bawah")
    print(f"ceil(3.2)     {math.ceil(3.2)}    # bulatkan ke atas")
    print(f"fabs(-5.5)    {math.fabs(-5.5)}")
    print(f"factorial(5)  {math.factorial(5)}")
    print(f"gcd(12, 18)   {math.gcd(12, 18)}")
    print(f"pi            {math.pi}")
    print(f"e             {math.e}")


# ------------------------------------------------------------------ random
# slide 19: fungsi random
def fungsi_random():
    print("\n=== fungsi random ===")

    random.seed(42)   # biar hasilnya konsisten tiap program dijalankan

    print(f"random()            {random.random()}          # float 0.0 sampai 1.0")
    print(f"randint(1, 6)       {random.randint(1, 6)}       # integer, termasuk batas")
    print(f"randrange(0, 10, 2) {random.randrange(0, 10, 2)}  # 0, 2, 4, 6, 8")
    print(f"choice([1,2,3,4])   {random.choice([1, 2, 3, 4])}")
    print(f"shuffle demo        lihat di bawah")

    angka = [1, 2, 3, 4, 5]
    random.shuffle(angka)
    print(f"setelah shuffle     {angka}")
    print(f"sample(range(1,50),5) {random.sample(range(1, 50), 5)}")


# ------------------------------------------------------------------ trigonometri
# slide 20: fungsi trigonometri
def fungsi_trigonometri():
    print("\n=== fungsi trigonometri (math) ===")

    sudut = math.pi / 4   # 45 derajat dalam radian

    print(f"45 derajat = {sudut} radian")
    print(f"sin(45)    {math.sin(sudut):.6f}")
    print(f"cos(45)    {math.cos(sudut):.6f}")
    print(f"tan(45)    {math.tan(sudut):.6f}")
    print(f"degrees(pi/4)  {math.degrees(sudut)}")
    print(f"radians(45)     {math.radians(45):.6f}")

    # semua fungsi ini menerima radian, bukan derajat
    print(f"sin(0) = {math.sin(0)}   sin(pi/2) = {math.sin(math.pi / 2)}")


# ------------------------------------------------------------------
# catatan: python TIDAK punya tipe data long seperti di slide 17.
# slide menyebut long(x) sebagai fungsi konversi, tapi di python 3
# long sudah tidak ada; int() sudah menangani bilangan bulat tak terbatas.
def catatan_long():
    print("\n=== catatan tentang long() ===")
    print("python 3 tidak punya long(). int() sudah cukup untuk")
    print("bilangan bulat tak terbatas, jadi tidak perlu long(x).")


if __name__ == "__main__":
    verifikasi_tipe()
    tipe_int()
    tipe_float()
    tipe_complex()
    konversi_tipe()
    fungsi_matematika()
    fungsi_random()
    fungsi_trigonometri()
    catatan_long()
