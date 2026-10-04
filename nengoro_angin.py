"""
latihan nengoro angin
=====================

program untuk menyusun naskah lirik "nengoro angin" sekaligus,
opsional, membunyikan melodi yang sudah kamu isi sendiri.

kenapa program ini tidak memuat lirik jadi?
--------------------------------------------
lirik lagu berhak cipta, jadi liriknya tidak ditanam di sini.
yang ditanam hanya kerangkanya: urutan bait, slot kord, dan tempat
untuk melodi. kamu isi sendiri lewat menu interaktif, hasilnya
ditulis ke file naskah.

cara pakai
----------
python nengoro_angin.py           -> menu interaktif
python nengoro_angin.py --template -> cetak template naskah saja
python nengoro_angin.py --mainkan  -> bunyikan melodi dari melody.txt
"""

import sys

# ------------------------------------------------------------------ struktur

# urutan bagian lagu. ganti jumlah bait sesuai naskah yang kamu pakai.
BAGIAN = [
    ("verse1", " bait 1 "),
    ("verse2", " bait 2 "),
    ("refrain", " refrain "),
]

# jumlah baris lirik per bagian
JUMLAH_BARIS = 4

# kordon yang lazim dipakai untuk lagu rakyat jawa barat di key c.
# ini cadangan umum, bukan transkripsi melodi lagu ini - sesuaikan
# dengan sumber notasi yang kamu pakai.
KORD_C = ["C", "Am", "F", "G"]
KORD_G = ["G", "Em", "C", "D"]

# ------------------------------------------------------------------ template


def buat_template(key="C"):
    """mengembalikan dict berisi slot lirik kosong per bagian."""
    kord = KORD_C if key == "C" else KORD_G
    return {
        nama: {
            "lirik": [""] * JUMLAH_BARIS,
            "kord": [kord[i % len(kord)] for i in range(JUMLAH_BARIS)],
        }
        for nama, _ in BAGIAN
    }


# ------------------------------------------------------------------ tampilan


def cetak_template(data):
    """mencetak naskah dalam bentukAligned berbaris, siap disalin."""
    lebar = max(len(nama) for nama, _ in BAGIAN)

    print()
    print("=" * (lebar + 24))
    print("nengoro angin - template naskah")
    print("=" * (lebar + 24))
    print()

    for nama, judul in BAGIAN:
        isi = data[nama]
        print(f"-- {judul.strip()} " + "-" * (lebar + 10))
        for baris, kord in zip(isi["lirik"], isi["kord"]):
            print(f"| {baris:<40} |   {kord}")
        print()


def cetak_naskah(data, judul_teks="naskah.txt"):
    """menulis naskah ke file, kord diletakkan di atas baris liriknya."""
    with open(judul_teks, "w", encoding="utf-8") as f:
        f.write("nengoro angin\n")
        f.write("=" * 40 + "\n\n")

        for nama, judul in BAGIAN:
            isi = data[nama]
            f.write(f"{judul.strip()}\n")
            for baris, kord in zip(isi["lirik"], isi["kord"]):
                f.write(f"{kord:>6}\n")
                f.write(f"{baris}\n")
            f.write("\n")

    print(f"naskah tersimpan di {judul_teks}")


# ------------------------------------------------------------------ pengisian


def isi_interaktif(data):
    """meminta user mengetik lirik tiap baris. enter saja berarti dilewati."""
    for nama, judul in BAGIAN:
        isi = data[nama]
        print()
        print(f"== {judul.strip()} " + "=" * 30)
        for i in range(JUMLAH_BARIS):
            nomor = i + 1
            try:
                ketik = input(f"  baris {nomor} > ").strip()
            except EOFError:
                ketik = ""
            isi["lirik"][i] = ketik
            if ketik:
                try:
                    kustom = input(f"    kord baris ini [{isi['kord'][i]}] > ").strip()
                except EOFError:
                    kustom = ""
                if kustom:
                    isi["kord"][i] = kustom.upper()
        print()

    return data


# ------------------------------------------------------------------ pemutar


# not -> frekuensi dalam hz. dipakai buat membunyikan nada di windows.
NOTA_HZ = {
    "C4": 262, "D4": 294, "E4": 330, "F4": 349, "G4": 392,
    "A4": 440, "B4": 494,
    "C5": 523, "D5": 587, "E5": 659, "F5": 698, "G5": 784,
    "A5": 880, "B5": 988, "C6": 1047,
    "RE": 294, "MI": 330, "FA": 349, "SOL": 392, "LA": 440, "SI": 494,
}


def baca_melodi(nama_file="melody.txt"):
    """
    membaca melodi dari file teks. satu nada per baris.
    baris kosong dan yang diawali # diabaikan.

    contoh isi melody.txt:
        C4
        D4
        E4
        C4
    """
    nada = []
    with open(nama_file, encoding="utf-8") as f:
        for baris in f:
            baris = baris.strip()
            if not baris or baris.startswith("#"):
                continue
            nada.append(baris.upper())

    salah = [n for n in nada if n not in NOTA_HZ]
    if salah:
        print(f"nada tidak dikenal, dilewati: {sorted(set(salah))}")

    return [n for n in nada if n in NOTA_HZ]


def mainkan(daftar, durasi=350):
    """membunyikan deretan nada. hanya jalan di windows."""
    if sys.platform != "win32":
        print("pemutar nada hanya jalan di windows")
        return

    try:
        import winsound
    except ImportError:
        print("modul winsound tidak tersedia")
        return

    for nada in daftar:
        print(nada, end=" ", flush=True)
        winsound.Beep(NOTA_HZ[nada], durasi)
    print("\nselesai")


# ------------------------------------------------------------------ main


def main():
    argumen = sys.argv[1:]

    if "--mainkan" in argumen:
        try:
            nada = baca_melodi()
        except FileNotFoundError:
            print("file melody.txt belum ada")
            print("isi dulu satu nada per baris, contoh: C4, D4, E4")
            return
        if not nada:
            print("melodi kosong")
            return
        mainkan(nada)
        return

    if "--template" in argumen:
        cetak_template(buat_template())
        return

    print("nengoro angin")
    print()
    print("[1] lihat template naskah")
    print("[2] isi lirik lalu simpan ke naskah.txt")
    print("[3] bunyikan melody.txt")
    print("[0] keluar")

    while True:
        try:
            pilih = input("\npilih > ").strip()
        except EOFError:
            break
        except KeyboardInterrupt:
            print()
            break

        if pilih == "0":
            print("sampai jumpa")
            break

        elif pilih == "1":
            cetak_template(buat_template())

        elif pilih == "2":
            data = isi_interaktif(buat_template())
            cetak_template(data)
            cetak_naskah(data)
            print()
            print("ingat: yang masuk ke file ini cuma lirik yang kamu ketik sendiri")

        elif pilih == "3":
            try:
                mainkan(baca_melodi())
            except FileNotFoundError:
                print("file melody.txt belum ada")
                print("isi dulu satu nada per baris, contoh: C4, D4, E4")

        else:
            print("pilihan tidak dikenal")

    print("selesai")


if __name__ == "__main__":
    main()