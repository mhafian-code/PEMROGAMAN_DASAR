"""Validasi geometri flowchart.html: cek node keluar kanvas, node saling
tumpang tindih, dan garis panah yang menembus kotak lain."""
import buat_flowchart as bf


def overlap(a, b, pad=0.0):
    return not (a.right + pad <= b.left or b.right + pad <= a.left
                or a.bottom + pad <= b.top or b.bottom + pad <= a.top)


def point_in(p, n, pad=0.0):
    x, y = p
    return (n.left - pad <= x <= n.right + pad) and (n.top - pad <= y <= n.bottom + pad)


def seg_points(pts, step=4):
    out = []
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        d = max(abs(x2 - x1), abs(y2 - y1))
        n = max(1, int(d // step))
        for k in range(n + 1):
            out.append((x1 + (x2 - x1) * k / n, y1 + (y2 - y1) * k / n))
    return out


def near(p, q, d=14):
    return abs(p[0] - q[0]) <= d and abs(p[1] - q[1]) <= d


problems = 0
for title, nodes, edges, w, h in bf.CHARTS:
    boxes = [n for n in nodes if n.kind != "merge"]

    for n in nodes:
        if n.left < 0 or n.top < 0 or n.right > w or n.bottom > h:
            print(f"[{title}] node di luar kanvas: {n.lines} "
                  f"({n.left:.0f},{n.top:.0f})-({n.right:.0f},{n.bottom:.0f}) vs {w}x{h}")
            problems += 1

    # perkiraan lebar teks (Segoe UI 14px ~ 7.4px per karakter)
    for n in boxes:
        for line in n.lines:
            need = len(line) * 7.4 + 10
            avail = n.w if n.kind != "decision" else n.w * 0.8
            if need > avail:
                print(f"[{title}] teks mungkin kepanjangan: '{line}' "
                      f"butuh {need:.0f}px, kotak {avail:.0f}px")
                problems += 1

    for i, a in enumerate(boxes):
        for b in boxes[i + 1:]:
            if overlap(a, b, -1):
                print(f"[{title}] node tumpang tindih: {a.lines} <-> {b.lines}")
                problems += 1

    for e in edges:
        poly = e.split('points="')[1].split('"')[0]
        pts = [tuple(float(v) for v in p.split(",")) for p in poly.split()]
        for p in seg_points(pts):
            # ujung panah sengaja menyentuh kotak, jadi abaikan_itu
            if near(p, pts[0]) or near(p, pts[-1]):
                continue
            for n in boxes:
                if point_in(p, n, 2):
                    print(f"[{title}] garis {pts} menembus node {n.lines} di {p}")
                    problems += 1
                    break

print("MASALAH:", problems)
