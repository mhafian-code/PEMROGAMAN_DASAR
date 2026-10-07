"""
tipe data python - collections
==============================

materi ini mengikuti slide "Python Collections (Arrays)" (slide 26-45).

ada 4 tipe collection di python:

    list       -> runtut (ordered), dapat diubah, izinkan member ganda
    tuple      -> runtut, TIDAK dapat diubah, izinkan member ganda
    set        -> tidak runtut, tidak berindeks, tidak izinkan member ganda
    dictionary -> tidak runtut, dapat diubah, berindeks, kunci unik

memilih tipe collection yang tepat berarti perlu tahu sifat masing-masing.
"""


# ================================================================== list
# slide 27-31: list ditulis dengan square bracket []
def list_dasar():
    print("=== list ===")

    buah = ["apel", "jeruk", "mangga"]
    angka = [1, 2, 3]
    campuran = [1, "dua", 3.0, True]      # python tidak mewajibkan satu tipe
    kosong = []                             # list kosong

    print(f"buat list  {buah}")
    print(f"angka     {angka}")
    print(f"campuran  {campuran}")
    print(f"kosong    {kosong}")

    # akses item dengan index
    print(f"\n[0]  {buah[0]}   # index mulai dari 0")
    print(f"[-1] {buah[-1]}  # index negatif dari belakang")
    print(f"[0:2] {buah[0:2]}")

    # ubah nilai item dengan index
    buah[1] = "lemon"
    print(f"\nsetelah buah[1] = 'lemon'  {buah}")

    # list bisa diubah isinya
    buah.append("anggur")
    print(f"setelah append()            {buah}")


# slide 28: 'in' untuk cek, len() panjang, append(), insert()
def list_cek_dan_tambah():
    print("\n=== list: cek dan tambah ===")

    buah = ["apel", "jeruk", "mangga"]

    # cek apakah item ada
    print(f"'jeruk' in buah   {'jeruk' in buah}")
    print(f"'durian' in buah  {'durian' in buah}")

    # panjang list = banyak item
    print(f"len()   {len(buah)}")

    # menambah item di akhir
    buah.append("anggur")
    print(f"append()          {buah}")

    # menambah item di indeks tertentu
    buah.insert(1, "nanas")
    print(f"insert(1, nanas)  {buah}")

    # menambah beberapa item sekaligus
    buah.extend(["salak", "rambutan"])
    print(f"extend()          {buah}")


# slide 29: remove(), pop(), del()
def list_hapus():
    print("\n=== list: hapus ===")

    buah = ["apel", "jeruk", "mangga", "anggur"]

    # hapus berdasarkan nilai
    buah.remove("jeruk")
    print(f"remove('jeruk')   {buah}")

    # hapus berdasarkan index, dan nilainya dikembalikan
    diambil = buah.pop(0)
    print(f"pop(0) -> {diambil!r}  sisa {buah}")

    # hapus berdasarkan index dengan del
    del buah[0]
    print(f"del buah[0]       {buah}")

    # kosongkan
    buah.clear()
    print(f"clear()           {buah}   len = {len(buah)}")

    # del juga bisa menghapus seluruh list
    angka = [1, 2, 3]
    del angka
    try:
        angka
    except NameError:
        print("del angka         list-nya benar-benar hilang, nama tidak dikenal lagi")


# slide 30: clear() dan list() konstruktor
def list_konstruktor():
    print("\n=== list: konstruktor ===")

    dari_kurung = list([1, 2, 3])
    dari_string = list("abc")
    dari_range = list(range(5))
    dari_tuple = list((7, 8, 9))
    duplikat = list(range(10, 15))

    print(f"list([1,2,3])      {dari_kurung}")
    print(f"list('abc')        {dari_string}   # string dipecah per karakter")
    print(f"list(range(5))     {dari_range}")
    print(f"list((7,8,9))      {dari_tuple}")
    print(f"list(range(10,15)) {duplikat}")


# slide 31: list method
def list_method():
    print("\n=== list: method ===")

    x = [5, 3, 9, 1, 7]
    y = [5, 3, 9, 1, 7]

    x.append(6)
    print(f"append(6)    {x}")

    y.sort()
    print(f"sort()       {y}")            # mengurutkan, mengubah list itu sendiri

    z = [5, 3, 9, 1, 7]
    z.sort(reverse=True)
    print(f"sort(reverse) {z}")

    w = [1, 2, 3, 4, 5]
    w.reverse()
    print(f"reverse()    {w}")

    angka = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"asli         {angka}")
    print(f"count(1)     {angka.count(1)}")      # berapa kali nilai 1 muncul
    print(f"index(4)     {angka.index(4)}")      # posisi pertama nilai 4
    print(f"copy()       {angka.copy()}")
    print(f"max/min      {max(angka)} / {min(angka)}")
    print(f"sum()        {sum(angka)}")

    # sorted() tidak mengubah list asli
    belum = [3, 1, 2]
    urut = sorted(belum)
    print(f"\nbelum       {belum}")
    print(f"sorted()    {urut}   # list asli tidak berubah")


# ================================================================== tuple
# slide 32-34: tuple ditulis dengan round bracket ()
def tuple_dasar():
    print("\n=== tuple ===")

    buah = ("apel", "jeruk", "mangga")
    angka = (1, 2, 3)
    satu = (5,)                      # koma wajib supaya ini tuple, bukan int

    print(f"buat tuple {buah}  -> {type(buah)}")
    print(f"angka     {angka}")
    print(f"satu      {satu}  -> {type(satu)}  (koma wajib)")

    # akses item, sama seperti list
    print(f"\n[0]  {buah[0]}")
    print(f"[-1] {buah[-1]}")

    # cek dan panjang
    print(f"\n'jeruk' in buah  {'jeruk' in buah}")
    print(f"len()            {len(buah)}")

    # tuple tidak bisa diubah
    print("\ncoba ubah isi tuple:")
    try:
        buah[1] = "lemon"
    except TypeError:
        print("  TypeError: 'tuple' object does not support item assignment")
    print("  tuple immutable, jadi harus buat tuple baru:")
    baru = buah[:1] + ("lemon",) + buah[2:]
    print(f"  {baru}")


# slide 34: tuple() konstruktor dan method
def tuple_konstruktor_method():
    print("\n=== tuple: konstruktor dan method ===")

    dari_list = tuple([1, 2, 3])
    dari_string = tuple("ab")
    dari_range = tuple(range(4))

    print(f"tuple([1,2,3])   {dari_list}")
    print(f"tuple('ab')      {dari_string}")
    print(f"tuple(range(4))  {dari_range}")

    x = (1, 3, 5, 3, 7, 3)
    print(f"\nasli      {x}")
    print(f"count(3)  {x.count(3)}")
    print(f"index(3)  {x.index(3)}  # posisi pertama")

    # tuple bisa dipakai untuk tukar nilai (swap) tanpa variabel bantu
    a, b = 1, 2
    a, b = b, a
    print(f"\nswap tanpa variabel bantu: a={a}, b={b}")


# ================================================================== set
# slide 35-39: set ditulis dengan curly bracket {}
def set_dasar():
    print("\n=== set ===")

    buah = {"apel", "jeruk", "mangga", "apel"}   # 'apel' duplikat, otomatis hilang
    angka = {1, 2, 3, 2, 1}
    kosong = set()                              # {} itu dictionary kosong, bukan set!

    print(f"buat set   {buah}  -> {type(buah)}")
    print(f"duplikat hilang, jumlah item: {len(buah)}")
    print(f"angka      {angka}")
    print(f"set()      {kosong}  -> {type(kosong)}")

    print("\nset tidak berindeks, jadi tidak bisa pakai [0]:")
    try:
        buah[0]
    except TypeError:
        print("  TypeError: 'set' object is not subscriptable")

    print("tapi bisa diiterasi dengan for loop:")
    for item in sorted(buah):       # diurutkan supaya output-nya konsisten
        print(f"  - {item}")

    print("\nset tidak bisa diubah nilainya, tapi boleh ditambah:")
    buah.add("anggur")
    print(f"add()      {sorted(buah)}")
    print(f"add() dua kali 'mangga' -> jumlah tetap {len(buah)}")


# slide 36: add(), update(), remove(), discard(), pop(), clear()
def set_ubah_dan_hapus():
    print("\n=== set: tambah dan hapus ===")

    s = {1, 2, 3}

    # tambah
    s.add(4)
    print(f"add(4)      {sorted(s)}")
    s.update([5, 6])
    print(f"update([5,6]) {sorted(s)}")

    # hapus
    s.remove(6)
    print(f"remove(6)   {sorted(s)}")

    # discard() lebih aman: tidak error kalau nilainya tidak ada
    s.discard(100)
    print(f"discard(100) {sorted(s)}   # tidak error")

    print("\ncoba remove() nilai yang tidak ada:")
    try:
        s.remove(100)
    except KeyError:
        print("  KeyError. makanya pakai discard() kalau nilai bisa jadi tidak ada")

    # pop() mengambil sembarang item dari set
    print(f"\npop()       {s.pop()!r}   -> sisanya {sorted(s)}")

    s.clear()
    print(f"clear()      {s}   len = {len(s)}")


def set_konstruktor():
    print("\n=== set: konstruktor ===")

    dari_list = set([1, 2, 2, 3])
    dari_string = set("banana")
    dari_range = set(range(6))

    print(f"set([1,2,2,3])  {sorted(dari_list)}   # duplikat hilang")
    print(f"set('banana')    {sorted(dari_string)}   # huruf unik")
    print(f"set(range(6))   {sorted(dari_range)}")


# slide 39: set method
def set_method():
    print("\n=== set: operasi himpunan ===")

    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}

    print(f"a = {sorted(a)}")
    print(f"b = {sorted(b)}")
    print(f"irisan / a & b   {sorted(a & b)}")
    print(f"gabungan / a|b   {sorted(a | b)}")
    print(f"selisih / a - b   {sorted(a - b)}")
    print(f"simetris / a ^ b {sorted(a ^ b)}")
    print(f"a.issubset(b)    {a.issubset({1, 2, 3})}")
    print(f"union            {sorted(a.union(b))}")
    print(f"intersection     {sorted(a.intersection(b))}")
    print(f"difference       {sorted(a.difference(b))}")
    print(f"issubset a <= a  {a.issubset(a)}")


# ================================================================== dict
# slide 40-45: dictionary ditulis dengan curly bracket, punya kunci dan nilai
def dict_dasar():
    print("\n=== dictionary ===")

    siswa = {
        "nama": "Hafian",
        "nim": "12345",
        "umur": 19,
    }

    print(f"buat dict {siswa}  -> {type(siswa)}")
    print(f"kunci    {list(siswa.keys())}")
    print(f"nilai    {list(siswa.values())}")
    print(f"item     {list(siswa.items())}")

    # akses item mengacu pada kunci
    print(f"\n['nama']  {siswa['nama']}")
    print(f".get()    {siswa.get('alamat', 'tidak ada')}")   # aman kalau kunci tidak ada

    # cek kunci ada atau tidak
    print(f"\n'nama' in siswa   {'nama' in siswa}")
    print(f"'alamat' in siswa {'alamat' in siswa}")
    print(f"len()             {len(siswa)}")

    # ubah nilai mengacu pada kunci
    siswa["umur"] = 20
    print(f"\nsetelah siswa['umur'] = 20  {siswa}")

    # kunci baru otomatis ditambah
    siswa["prodi"] = "Informatika"
    print(f"tambah kunci baru           {siswa}")


# slide 42: pop(), popitem(), del()
def dict_hapus():
    print("\n=== dictionary: hapus ===")

    siswa = {"nama": "Hafian", "nim": "12345", "umur": 19}

    # pop() menghapus berdasarkan kunci, nilainya dikembalikan
    nim = siswa.pop("nim")
    print(f"pop('nim') -> {nim!r}   sisa {siswa}")

    # popitem() menghapus pasangan terakhir yang dimasukkan
    pasangan = siswa.popitem()
    print(f"popitem() -> {pasangan!r}   sisa {siswa}")

    # hapus berdasarkan kunci dengan del
    siswa = {"nama": "Hafian", "nim": "12345", "umur": 19}
    del siswa["nim"]
    print(f"del siswa['nim']            {siswa}")

    # hapus seluruh dictionary
    siswa = {"nama": "Hafian", "nim": "12345"}
    del siswa
    print("del siswa                  dictionary-nya hilang dari namespace")

    # kosongkan
    siswa = {"nama": "Hafian", "nim": "12345"}
    siswa.clear()
    print(f"clear()                    {siswa}   len = {len(siswa)}")


# slide 44: dict() konstruktor
def dict_konstruktor():
    print("\n=== dictionary: konstruktor ===")

    dari_kv = dict(nama="Hafian", nim="12345")
    dari_list = dict([("a", 1), ("b", 2)])
    dari_dict = dict({"x": 10, "y": 20})

    print(f"dict(nama=..., nim=...)  {dari_kv}")
    print(f"dict([('a',1),...])     {dari_list}")
    print(f"dict({{'x':10,...}})     {dari_dict}")


# slide 45: dictionary method
def dict_method():
    print("\n=== dictionary: method ===")

    d = {"a": 1, "b": 2, "c": 3}

    print(f"asli        {d}")
    print(f"keys()      {list(d.keys())}")
    print(f"values()    {list(d.values())}")
    print(f"items()     {list(d.items())}")
    print(f"get('a')    {d.get('a')}")
    print(f"get('z', 0) {d.get('z', 0)}   # nilai bawaan kalau kunci tidak ada")

    salinan = d.copy()
    print(f"copy()      {salinan}")

    d.update({"d": 4})
    print(f"update()    {d}")

    # setdefault: isi kalau belum ada
    d.setdefault("e", 5)
    d.setdefault("a", 99)     # 'a' sudah ada, jadi tidak berubah
    print(f"setdefault {d}")

    # loop untuk iterasi
    print("\niterasi:")
    for kunci, nilai in d.items():
        print(f"  {kunci} = {nilai}")


# ================================================================== ringkasan
def ringkasan():
    print("\n=== ringkasan perbandingan ===")
    print(f"{'tipe':<12} {'rurut':<7} {'bisa diubah':<13} {'duplikat':<10} {'indeks'}")
    print("-" * 58)
    print(f"{'list':<12} {'ya':<7} {'ya':<13} {'boleh':<10} {'ya'}")
    print(f"{'tuple':<12} {'ya':<7} {'tidak':<13} {'boleh':<10} {'ya'}")
    print(f"{'set':<12} {'tidak':<7} {'nilai tidak':<13} {'tidak':<10} {'tidak'}")
    print(f"{'dict':<12} {'tidak':<7} {'ya':<13} {'kunci unik':<10} {'lewat kunci'}")
    print("\npilihan tipe:")
    print("  - butuh urutan dan boleh diubah      -> list")
    print("  - butuh urutan tapi tidak boleh diubah -> tuple")
    print("  - butuh cek keanggotaan cepat, tanpa duplikat -> set")
    print("  - butuh pasangan kunci-nilai         -> dict")


if __name__ == "__main__":
    list_dasar()
    list_cek_dan_tambah()
    list_hapus()
    list_konstruktor()
    list_method()

    tuple_dasar()
    tuple_konstruktor_method()

    set_dasar()
    set_ubah_dan_hapus()
    set_konstruktor()
    set_method()

    dict_dasar()
    dict_hapus()
    dict_konstruktor()
    dict_method()

    ringkasan()
