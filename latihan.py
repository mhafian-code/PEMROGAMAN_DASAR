import math

# Latihan 1: Konversi suhu Celcius menjadi Reamur dan Fahrenheit
# Input: suhu dalam Celcius
# Proses: R = 4/5 * C dan F = 9/5 * C + 32
# Output: suhu dalam Reamur dan Fahrenheit
def latihan1():
    print("--- Latihan 1: Konversi Celcius ke Reamur & Fahrenheit ---")
    c = float(input("Masukkan suhu dalam Celcius: "))
    r = 4/5 * c
    f = 9/5 * c + 32
    print(f"Suhu dalam Reamur: {r}")
    print(f"Suhu dalam Fahrenheit: {f}")


# Latihan 2: Sisi miring segitiga siku-siku
# Input: a dan b (sisi pembentuk sudut siku-siku)
# Proses: c = sqrt(a^2 + b^2)
# Output: sisi miring (c)
def latihan2():
    print("--- Latihan 2: Sisi Miring Segitiga Siku-siku ---")
    a = float(input("Masukkan panjang sisi a: "))
    b = float(input("Masukkan panjang sisi b: "))
    c = math.sqrt(a**2 + b**2)
    print(f"Sisi miring (c) adalah: {c}")


# Latihan 3: Menghitung usia berdasarkan tahun lahir dan tahun sekarang
# Input: Tahun lahir (tl), Tahun sekarang (ts)
# Proses: Umur = ts - tl
# Output: Cetak Umur
def latihan3():
    print("--- Latihan 3: Menghitung Usia ---")
    tl = int(input("Masukkan tahun lahir (tl): "))
    ts = int(input("Masukkan tahun sekarang (ts): "))
    umur = ts - tl
    print(f"Usia anda saat ini adalah: {umur} tahun")


# Latihan 4: Menguji apakah suhu (Celcius) adalah beku, cair, gas
# Input: suhu dalam celcius (bil bulat)
# Proses: jika < 0 = beku, 0-100 = cair, dan > 100 = gas
# Output: beku, cair, gas
def latihan4():
    print("--- Latihan 4: Beku / Cair / Gas ---")
    suhu = int(input("Masukkan suhu dalam Celcius: "))
    if suhu < 0:
        status = "beku"
    elif suhu <= 100:
        status = "cair"
    else:
        status = "gas"
    print(f"Status air pada suhu {suhu} derajat adalah: {status}")


# Latihan 5: Mengetahui bilangan terbesar dari n buah bilangan
# Input: bilangan-bilangan sebanyak n kali
# Proses: simpan nilai masing-masing bil yang diinputkan user,
#   jika bil pertama, langsung catat bahwa bil itu maksimum,
#   kemudian bandingkan dengan bil yang lainnya,
#   jika ada yang lebih besar dari maksimum, jadikan bil itu maksimumnya
# Output: bil maksimum
def latihan5():
    print("--- Latihan 5: Bilangan Terbesar dari n Bilangan ---")
    n = int(input("Masukkan jumlah bilangan (n): "))
    maksimum = None
    for i in range(1, n + 1):
        bil = float(input(f"Masukkan bilangan ke-{i}: "))
        if i == 1:
            maksimum = bil
        elif bil > maksimum:
            maksimum = bil
    print(f"Bilangan maksimum adalah: {maksimum}")


# Latihan 6: Menentukan bilangan genap atau ganjil
# Input: suatu bilangan
# Output: genap / ganjil / nol
def latihan6():
    print("--- Latihan 6: Genap / Ganjil / Nol ---")
    bilangan = int(input("Masukkan suatu bilangan: "))
    if bilangan == 0:
        print("Output: nol")
    elif bilangan % 2 == 0:
        print("Output: genap")
    else:
        print("Output: ganjil")


# Latihan 7: Menghitung akar-akar persamaan kuadrat
# D = B^2 - 4*A*C
# Jika D < 0 maka didapat akar imajiner
# Jika D = 0 maka X1 = X2 yang didapat dari -B / (2*A)
# Jika D > 0 maka ada dua akar:
#   X1 = (-B + sqrt(D)) / (2*A) dan X2 = (-B - sqrt(D)) / (2*A)
def latihan7():
    print("--- Latihan 7: Akar Persamaan Kuadrat Ax^2 + Bx + C = 0 ---")
    a = float(input("Masukkan nilai A: "))
    b = float(input("Masukkan nilai B: "))
    c = float(input("Masukkan nilai C: "))

    if a == 0:
        print("Bukan persamaan kuadrat (A tidak boleh 0)")
        return

    d = (b ** 2) - (4 * a * c)
    print(f"Nilai diskriminan (D) = {d}")

    if d < 0:
        print("Output: didapat akar imajiner")
    elif d == 0:
        x1 = -b / (2 * a)
        x2 = x1
        print(f"Output: X1 = X2 = {x1}")
    else:  # d > 0
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print("Output: memiliki dua akar real yang berbeda")
        print(f"X1 = {x1}")
        print(f"X2 = {x2}")


if __name__ == "__main__":
    while True:
        print("\n=== Menu Latihan ===")
        print("1. Konversi Celcius ke Reamur & Fahrenheit")
        print("2. Sisi miring segitiga siku-siku")
        print("3. Menghitung usia")
        print("4. Beku / Cair / Gas")
        print("5. Bilangan terbesar dari n bilangan")
        print("6. Genap / Ganjil / Nol")
        print("7. Akar persamaan kuadrat")
        print("0. Keluar")
        pilih = input("Pilih latihan (0-7): ")

        if pilih == "1":
            latihan1()
        elif pilih == "2":
            latihan2()
        elif pilih == "3":
            latihan3()
        elif pilih == "4":
            latihan4()
        elif pilih == "5":
            latihan5()
        elif pilih == "6":
            latihan6()
        elif pilih == "7":
            latihan7()
        elif pilih == "0":
            print("Selesai.")
            break
        else:
            print("Pilihan tidak valid.")
