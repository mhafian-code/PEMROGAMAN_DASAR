"""
Generator flowchart untuk 7 soal latihan (latihan.py).
Menghasilkan file flowchart.html berisi diagram alur (SVG) untuk nomor 1-7.

Simbol:
  - Terminal (bulgat)      : mulai / selesai
  - Persegi panjang        : proses
  - Belah ketupat          : input / output
  - Belah ketupat (diamond): percabangan / kondisi
"""

from html import escape

# ukuran dalam piksel
W_PROS = 240      # lebar proses / input / output
H_TERM = 46       # tinggi terminal
H_DIA = 90        # tinggi decision
R_MERGE = 6       # jari-jari titik gabung

FONT = "Segoe UI, Arial, sans-serif"


def _esc(t):
    return escape(t)


class Node:
    def __init__(self, cx, cy, lines, kind="proses", w=None):
        self.cx = cx
        self.cy = cy
        self.lines = lines if isinstance(lines, (list, tuple)) else [lines]
        self.kind = kind
        if kind == "decision":
            self.w, self.h = 220, H_DIA
        elif kind == "terminal":
            self.w, self.h = 200, H_TERM
        elif kind == "merge":
            self.w = self.h = 2 * R_MERGE
        else:
            self.w = w or W_PROS
            self.h = 30 + 20 * len(self.lines)

    @property
    def top(self):
        return self.cy - self.h / 2

    @property
    def bottom(self):
        return self.cy + self.h / 2

    @property
    def left(self):
        return self.cx - self.w / 2

    @property
    def right(self):
        return self.cx + self.w / 2

    def svg(self):
        s = []
        if self.kind == "merge":
            s.append(f'<circle cx="{self.cx}" cy="{self.cy}" r="{R_MERGE}" fill="#33415c"/>')
            return "".join(s)

        fill = {"terminal": "#dbeafe", "proses": "#ffffff",
                "input": "#ecfdf5", "output": "#fef3c7",
                "decision": "#fee2e2"}[self.kind]

        if self.kind == "decision":
            pts = (f"{self.cx},{self.top} {self.right},{self.cy} "
                   f"{self.cx},{self.bottom} {self.left},{self.cy}")
            s.append(f'<polygon points="{pts}" fill="{fill}" stroke="#33415c" stroke-width="1.6"/>')
        elif self.kind == "terminal":
            s.append(f'<rect x="{self.left}" y="{self.top}" width="{self.w}" height="{self.h}" '
                     f'rx="{self.h/2}" fill="{fill}" stroke="#33415c" stroke-width="1.6"/>')
        elif self.kind in ("input", "output"):
            s.append(f'<polygon points="{self.left+18},{self.top} {self.right},{self.top} '
                     f'{self.right-18},{self.bottom} {self.left},{self.bottom}" '
                     f'fill="{fill}" stroke="#33415c" stroke-width="1.6"/>')
        else:
            s.append(f'<rect x="{self.left}" y="{self.top}" width="{self.w}" height="{self.h}" '
                     f'rx="4" fill="{fill}" stroke="#33415c" stroke-width="1.6"/>')

        n = len(self.lines)
        for i, line in enumerate(self.lines):
            y = self.cy - (n - 1) * 10 + i * 20
            s.append(f'<text x="{self.cx}" y="{y}" font-family="{FONT}" font-size="14" '
                     f'fill="#111827" text-anchor="middle" dominant-baseline="middle">'
                     f'{_esc(line)}</text>')
        return "".join(s)


def edge(points, label=None, lpos=None):
    pts = " ".join(f"{x},{y}" for x, y in points)
    s = (f'<polyline points="{pts}" fill="none" stroke="#33415c" stroke-width="1.6" '
         f'stroke-linejoin="round" marker-end="url(#arrow)"/>')
    if label and lpos:
        s += (f'<text x="{lpos[0]}" y="{lpos[1]}" font-family="{FONT}" font-size="12" '
              f'font-weight="bold" fill="#b91c1c" text-anchor="middle" '
              f'dominant-baseline="middle">{_esc(label)}</text>')
    return s


CHARTS = []   # (judul, nodes, edges, width, height) untuk keperluan validasi


def chart(title, nodes, edges, width, height, subtitle=""):
    CHARTS.append((title, nodes, edges, width, height))
    body = [n.svg() for n in nodes] + edges
    sub = f'<div class="sub">{_esc(subtitle)}</div>' if subtitle else ""
    return f"""
<section class="card">
  <h2>{_esc(title)}</h2>
  {sub}
  <svg viewBox="0 0 {width} {height}" width="{width}" height="{height}">
    <defs>
      <marker id="arrow" markerWidth="9" markerHeight="9" refX="8" refY="3.2" orient="auto">
        <path d="M0,0 L0,6.4 L8,3.2 z" fill="#33415c"/>
      </marker>
    </defs>
    {''.join(body)}
  </svg>
</section>
"""


# ----------------------------------------------------------------- chart 1
def chart1():
    a = Node(380, 30, "MULAI", "terminal")
    b = Node(380, 100, "Input suhu Celcius (C)", "input")
    c = Node(380, 180, ["R = 4/5 * C", "F = 9/5 * C + 32"], "proses")
    d = Node(380, 285, "Output: Reamur & Fahrenheit", "output")
    e = Node(380, 355, "SELESAI", "terminal")
    edges = [
        edge([(380, a.bottom), (380, b.top)]),
        edge([(380, b.bottom), (380, c.top)]),
        edge([(380, c.bottom), (380, d.top)]),
        edge([(380, d.bottom), (380, e.top)]),
    ]
    return chart("1. Konversi Celcius ke Reamur dan Fahrenheit", [a, b, c, d, e], edges,
                 900, 400, "Input: suhu Celcius  |  Proses: R = 4/5*C, F = 9/5*C + 32  |  Output: R dan F")


# ----------------------------------------------------------------- chart 2
def chart2():
    a = Node(380, 30, "MULAI", "terminal")
    b = Node(380, 100, "Input panjang sisi a", "input")
    c = Node(380, 165, "Input panjang sisi b", "input")
    d = Node(380, 245, "c = sqrt(a^2 + b^2)", "proses")
    e = Node(380, 320, "Output: sisi miring (c)", "output")
    f = Node(380, 390, "SELESAI", "terminal")
    edges = [
        edge([(380, a.bottom), (380, b.top)]),
        edge([(380, b.bottom), (380, c.top)]),
        edge([(380, c.bottom), (380, d.top)]),
        edge([(380, d.bottom), (380, e.top)]),
        edge([(380, e.bottom), (380, f.top)]),
    ]
    return chart("2. Sisi Miring Segitiga Siku-siku", [a, b, c, d, e, f], edges,
                 900, 430, "Input: a dan b  |  Proses: c = sqrt(a^2 + b^2)  |  Output: sisi miring (c)")


# ----------------------------------------------------------------- chart 3
def chart3():
    a = Node(380, 30, "MULAI", "terminal")
    b = Node(380, 100, "Input tahun lahir (tl)", "input")
    c = Node(380, 165, "Input tahun sekarang (ts)", "input")
    d = Node(380, 245, "Umur = ts - tl", "proses")
    e = Node(380, 320, "Output: cetak umur", "output")
    f = Node(380, 390, "SELESAI", "terminal")
    edges = [
        edge([(380, a.bottom), (380, b.top)]),
        edge([(380, b.bottom), (380, c.top)]),
        edge([(380, c.bottom), (380, d.top)]),
        edge([(380, d.bottom), (380, e.top)]),
        edge([(380, e.bottom), (380, f.top)]),
    ]
    return chart("3. Menghitung Usia", [a, b, c, d, e, f], edges,
                 900, 430, "Input: tahun lahir (tl), tahun sekarang (ts)  |  Proses: Umur = ts - tl")


# ----------------------------------------------------------------- chart 4
def chart4():
    a = Node(380, 30, "MULAI", "terminal")
    b = Node(380, 100, "Input suhu Celcius (bil bulat)", "input")
    c = Node(380, 195, "suhu < 0 ?", "decision")
    d = Node(140, 300, "status = beku", "proses")
    e = Node(380, 300, "0 <= suhu <= 100 ?", "decision")
    f = Node(680, 300, "status = cair", "proses")
    g = Node(380, 425, "status = gas", "proses")
    m = Node(380, 520, "", "merge")
    h = Node(380, 575, "Output: beku / cair / gas", "output")
    i = Node(380, 650, "SELESAI", "terminal")
    edges = [
        edge([(380, a.bottom), (380, b.top)]),
        edge([(380, b.bottom), (380, c.top)]),
        edge([(c.left, c.cy), (140, c.cy), (140, d.top)], "Ya", (205, c.cy - 14)),
        edge([(380, c.bottom), (380, e.top)], "Tidak", (400, (c.bottom + e.top) / 2)),
        edge([(e.right, e.cy), (f.left - 6, e.cy)], "Ya", (522, e.cy - 14)),
        edge([(380, e.bottom), (380, g.top)], "Tidak", (400, (e.bottom + g.top) / 2)),
        edge([(140, d.bottom), (140, m.cy), (m.left - 6, m.cy)]),
        edge([(680, f.bottom), (680, m.cy), (m.right + 6, m.cy)]),
        edge([(380, g.bottom), (380, m.top)]),
        edge([(380, m.bottom), (380, h.top)]),
        edge([(380, h.bottom), (380, i.top)]),
    ]
    return chart("4. Menguji Suhu: Beku / Cair / Gas", [a, b, c, d, e, f, g, m, h, i], edges,
                 900, 690, "Input: suhu Celcius  |  < 0 = beku, 0-100 = cair, > 100 = gas")


# ----------------------------------------------------------------- chart 5
def chart5():
    a = Node(390, 30, "MULAI", "terminal")
    b = Node(390, 100, "Input n (jumlah bilangan)", "input")
    c = Node(390, 165, "maksimum = None", "proses")
    d = Node(390, 230, "i = 1", "proses")
    e = Node(390, 320, "i <= n ?", "decision")
    f = Node(390, 445, "Input bilangan ke-i", "input")
    g = Node(390, 560, "i == 1 ?", "decision")
    h = Node(200, 675, "maksimum = bil", "proses")
    i = Node(730, 560, "bil > maksimum ?", "decision")
    j = Node(730, 675, "maksimum = bil", "proses")
    m = Node(390, 800, "", "merge")
    k = Node(390, 880, "i = i + 1", "proses")
    o = Node(390, 1000, "Output: bilangan maksimum", "output")
    p = Node(390, 1080, "SELESAI", "terminal")
    edges = [
        edge([(390, a.bottom), (390, b.top)]),
        edge([(390, b.bottom), (390, c.top)]),
        edge([(390, c.bottom), (390, d.top)]),
        edge([(390, d.bottom), (390, e.top)]),
        edge([(390, e.bottom), (390, f.top)], "Ya", (412, (e.bottom + f.top) / 2)),
        edge([(390, f.bottom), (390, g.top)]),
        edge([(g.left, g.cy), (200, g.cy), (200, h.top)], "Ya", (240, g.cy - 14)),
        edge([(g.right, g.cy), (i.left - 6, g.cy)], "Tidak", (557, g.cy - 14)),
        edge([(730, i.bottom), (730, j.top)], "Ya", (752, (i.bottom + j.top) / 2)),
        edge([(i.right, i.cy), (890, i.cy), (890, k.cy), (k.right + 6, k.cy)], "Tidak", (890, i.cy - 14)),
        edge([(200, h.bottom), (200, m.cy), (m.left - 6, m.cy)]),
        edge([(730, j.bottom), (730, m.cy), (m.right + 6, m.cy)]),
        edge([(390, m.bottom), (390, k.top)]),
        edge([(k.left, k.cy), (40, k.cy), (40, e.cy), (e.left - 6, e.cy)]),
        edge([(e.right, e.cy), (550, e.cy), (550, o.cy), (o.right + 6, o.cy)], "Tidak", (530, e.cy - 14)),
        edge([(390, o.bottom), (390, p.top)]),
    ]
    return chart("5. Bilangan Terbesar dari n Bilangan", [a, b, c, d, e, f, g, h, i, j, m, k, o, p],
                 edges, 940, 1140,
                 "Input: n bilangan  |  bil pertama jadi maksimum, lalu bandingkan dengan bilangan berikutnya")


# ----------------------------------------------------------------- chart 6
def chart6():
    a = Node(380, 30, "MULAI", "terminal")
    b = Node(380, 100, "Input suatu bilangan", "input")
    c = Node(380, 200, "bilangan == 0 ?", "decision")
    d = Node(150, 320, "Output: nol", "output", w=200)
    e = Node(380, 320, "bilangan % 2 == 0 ?", "decision")
    f = Node(680, 440, "Output: genap", "output")
    g = Node(380, 440, "Output: ganjil", "output")
    m = Node(380, 520, "", "merge")
    h = Node(380, 600, "SELESAI", "terminal")
    edges = [
        edge([(380, a.bottom), (380, b.top)]),
        edge([(380, b.bottom), (380, c.top)]),
        edge([(c.left, c.cy), (150, c.cy), (150, d.top)], "Ya", (210, c.cy - 14)),
        edge([(380, c.bottom), (380, e.top)], "Tidak", (402, (c.bottom + e.top) / 2)),
        edge([(e.right, e.cy), (f.left - 6, e.cy)], "Ya", (522, e.cy - 14)),
        edge([(380, e.bottom), (380, g.top)], "Tidak", (402, (e.bottom + g.top) / 2)),
        edge([(150, d.bottom), (150, m.cy), (m.left - 6, m.cy)]),
        edge([(680, f.bottom), (680, m.cy), (m.right + 6, m.cy)]),
        edge([(380, g.bottom), (380, m.top)]),
        edge([(380, m.bottom), (380, h.top)]),
    ]
    return chart("6. Menentukan Genap / Ganjil / Nol", [a, b, c, d, e, f, g, m, h], edges,
                 900, 660, "Input: suatu bilangan  |  Output: genap / ganjil / nol")


# ----------------------------------------------------------------- chart 7
def chart7():
    a = Node(420, 30, "MULAI", "terminal")
    b = Node(420, 95, "Input A", "input")
    c = Node(420, 160, "Input B", "input")
    d = Node(420, 225, "Input C", "input")
    e = Node(420, 325, "A == 0 ?", "decision")
    f = Node(170, 395, ["Output: bukan", "persamaan kuadrat"], "output")
    g = Node(420, 460, "D = B^2 - 4*A*C", "proses")
    h = Node(420, 565, "D < 0 ?", "decision")
    i = Node(170, 680, "Output: akar imajiner", "output")
    j = Node(420, 680, "D == 0 ?", "decision")
    k = Node(750, 800, "X1 = X2 = -B / (2*A)", "proses")
    l = Node(420, 800, ["X1 = (-B + sqrt(D)) / (2*A)", "X2 = (-B - sqrt(D)) / (2*A)"], "proses")
    m = Node(420, 880, "", "merge")
    n = Node(420, 960, "SELESAI", "terminal")
    edges = [
        edge([(420, a.bottom), (420, b.top)]),
        edge([(420, b.bottom), (420, c.top)]),
        edge([(420, c.bottom), (420, d.top)]),
        edge([(420, d.bottom), (420, e.top)]),
        edge([(e.left, e.cy), (170, e.cy), (170, f.top)], "Ya", (240, e.cy - 14)),
        edge([(420, e.bottom), (420, g.top)], "Tidak", (440, (e.bottom + g.top) / 2)),
        edge([(420, g.bottom), (420, h.top)]),
        edge([(h.left, h.cy), (170, h.cy), (170, i.top)], "Ya", (240, h.cy - 14)),
        edge([(420, h.bottom), (420, j.top)], "Tidak", (440, (h.bottom + j.top) / 2)),
        edge([(j.right, j.cy), (750, j.cy), (750, k.top)], "Ya", (640, j.cy - 14)),
        edge([(420, j.bottom), (420, l.top)], "Tidak", (440, (j.bottom + l.top) / 2)),
        edge([(170, i.bottom), (170, m.cy), (m.left - 6, m.cy)]),
        edge([(750, k.bottom), (750, m.cy), (m.right + 6, m.cy)]),
        edge([(420, l.bottom), (420, m.top)]),
        edge([(f.left, f.cy), (25, f.cy), (25, n.cy), (n.left - 6, n.cy)]),
        edge([(420, m.bottom), (420, n.top)]),
    ]
    return chart("7. Akar-akar Persamaan Kuadrat", [a, b, c, d, e, f, g, h, i, j, k, l, m, n],
                 edges, 920, 1020, "D = B^2 - 4*A*C  |  D < 0 = akar imajiner, D = 0 = akar kembar, D > 0 = dua akar")


LEGEND = """
<div class="legend">
  <span><svg width="90" height="34"><rect x="5" y="4" width="80" height="26" rx="13" fill="#dbeafe" stroke="#33415c" stroke-width="1.6"/><text x="45" y="18" font-size="12" text-anchor="middle" dominant-baseline="middle" font-family="Segoe UI">Mulai/Selesai</text></svg></span>
  <span><svg width="90" height="34"><rect x="5" y="4" width="80" height="26" rx="4" fill="#fff" stroke="#33415c" stroke-width="1.6"/><text x="45" y="18" font-size="12" text-anchor="middle" dominant-baseline="middle" font-family="Segoe UI">Proses</text></svg></span>
  <span><svg width="90" height="34"><polygon points="20,4 85,4 70,30 5,30" fill="#ecfdf5" stroke="#33415c" stroke-width="1.6"/><text x="45" y="18" font-size="12" text-anchor="middle" dominant-baseline="middle" font-family="Segoe UI">Input</text></svg></span>
  <span><svg width="90" height="34"><polygon points="20,4 85,4 70,30 5,30" fill="#fef3c7" stroke="#33415c" stroke-width="1.6"/><text x="45" y="18" font-size="12" text-anchor="middle" dominant-baseline="middle" font-family="Segoe UI">Output</text></svg></span>
  <span><svg width="90" height="34"><polygon points="45,3 86,17 45,31 4,17" fill="#fee2e2" stroke="#33415c" stroke-width="1.6"/><text x="45" y="18" font-size="12" text-anchor="middle" dominant-baseline="middle" font-family="Segoe UI">Kondisi</text></svg></span>
</div>
"""

HTML = f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="utf-8">
<title>Flowchart Latihan 1-7</title>
<style>
  body {{ font-family: {FONT}; background: #f4f5fb; margin: 0; padding: 28px; color: #111827; }}
  h1 {{ text-align: center; color: #4c1d95; }}
  .sub {{ text-align: center; color: #4b5563; font-size: 14px; margin-bottom: 10px; }}
  .legend {{ display: flex; gap: 14px; justify-content: center; flex-wrap: wrap;
             background: #fff; padding: 12px 18px; border-radius: 10px; max-width: 900px;
             margin: 0 auto 24px; box-shadow: 0 1px 4px rgba(0,0,0,.08); }}
  .card {{ background: #fff; border-radius: 12px; padding: 18px; margin: 0 auto 28px;
           max-width: 940px; box-shadow: 0 1px 6px rgba(0,0,0,.1); page-break-inside: avoid; }}
  .card h2 {{ margin: 0 0 4px; font-size: 19px; color: #4c1d95; }}
  svg {{ display: block; margin: 0 auto; }}
  @media print {{ body {{ background: #fff; padding: 0; }} .card {{ box-shadow: none; border: 1px solid #ddd; }} }}
</style>
</head>
<body>
<h1>Flowchart Latihan Algoritma (Nomor 1 - 7)</h1>
{LEGEND}
{chart1()}
{chart2()}
{chart3()}
{chart4()}
{chart5()}
{chart6()}
{chart7()}
</body>
</html>
"""

if __name__ == "__main__":
    with open("flowchart.html", "w", encoding="utf-8") as f:
        f.write(HTML)
    print("flowchart.html berhasil dibuat")
