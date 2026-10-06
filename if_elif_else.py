"""
Instruksi if-elif-else
======================

sintaks dasar:

    if ekspresi:
        statement(s)

kalau ekspresi boolean bernilai TRUE, blok statement di dalam
dieksekusi. kalau FALSE, blok itu dilewati dan program lanjut ke
baris berikutnya di luar blok.

indentasi penting. python pakai indentasi (biasanya 4 spasi) untuk
menandai awal dan akhir blok, bukan kurung kurawal seperti di C atau Java.


contoh dari slide
-----------------
var1 = 100
if var1:
    print ("1 - Got a true expression value")
    print (var1)

var2 = 0
if var2:
    print ("2 - Got a true expression value")
    print (var2)
print ("Good bye!")

keluaran:
    1 - Got a true expression value
    100
    Good bye!

kenapa "2 - Got a true expression value" tidak muncul?
karena var2 bernilai 0, dan di python 0 dianggap FALSE. nilai
numerik yang lain dianggap TRUE. jadi blok kedua dilewati, lalu
program langsung ke print ("Good bye!").

arti nilai "benar" di python:

    0        -> False
    angka    -> True (selain 0)
    ""       -> False (string kosong)
    teks     -> True (selain string kosong)
    [] {} () -> False (koleksi kosong)
    None     -> False

jadi `if var1:` setara dengan `if var1 != 0:` untuk angka.
"""


# --------------------------------------------------------------- contoh 1
# persis seperti di slide
def contoh_if_saja():
    print("--- contoh 1: if saja ---")

    var1 = 100
    if var1:
        print("1 - Got a true expression value")
        print(var1)

    var2 = 0
    if var2:
        print("2 - Got a true expression value")
        print(var2)

    print("Good bye!")


# --------------------------------------------------------------- contoh 2
# kalau({}, kalau tidak, kalau tidak juga)
def contoh_if_elif_else(nilai):
    print(f"\n--- contoh 2: if-elif-else, nilai = {nilai} ---")

    if nilai > 80:
        predikat = "A"
    elif nilai > 70:
        predikat = "B"
    elif nilai > 60:
        predikat = "C"
    else:
        predikat = "D"

    print(f"nilai {nilai} mendapat predikat {predikat}")
    return predikat


# --------------------------------------------------------------- contoh 3
#elif bisa berupa banyak kondisi, tidak harus tiga
def konversi_suhu(celsius):
    print(f"\n--- contoh 3: elif banyak, celsius = {celsius} ---")

    if celsius < 0:
        status = "beku"
    elif celsius == 0:
        status = "titik beku"
    elif celsius < 100:
        status = "cair"
    elif celsius == 100:
        status = "titik didih"
    else:
        status = "gas/uap"

    print(f"{celsius} derajat -> {status}")
    return status


# --------------------------------------------------------------- contoh 4
# elif dieksekusi hanya sampai yang pertama bernilai TRUE
def nilai_rantai(nilai):
    print(f"\n--- contoh 4: rantai elif, nilai = {nilai} ---")

    if nilai < 0:
        hasil = "negatif"
    elif nilai == 0:
        hasil = "nol"
    elif nilai < 10:
        hasil = "satu digit"
    elif nilai < 100:
        hasil = "dua digit"
    else:
        hasil = "besar"

    print(f"{nilai} -> {hasil}")
    return hasil


if __name__ == "__main__":
    contoh_if_saja()

    for n in [90, 75, 65, 50]:
        contoh_if_elif_else(n)

    for s in [-5, 0, 25, 100, 150]:
        konversi_suhu(s)

    for n in [-3, 0, 7, 42, 500]:
        nilai_rantai(n)
