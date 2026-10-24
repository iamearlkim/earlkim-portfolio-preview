"""Docs-site tour: square video composed from high-res captures.
usage: python3 compose.py OUTDIR [t1,t2,...]"""
import json, sys, os
from PIL import Image, ImageDraw

R = json.load(open('rects.json'))
OUT, FPS, SRC = 1440, 30, 2
IMG = {}
def img(name):
    if name not in IMG:
        IMG[name] = Image.open(name + '.png').convert('RGB')
    return IMG[name]

def ease(x):
    x = max(0.0, min(1.0, x)); return 4*x*x*x if x < .5 else 1 - pow(-2*x + 2, 3) / 2
def keys(k, t):
    if t <= k[0][0]: return k[0][1:]
    for a, b in zip(k, k[1:]):
        if a[0] <= t <= b[0]:
            p = ease((t - a[0]) / (b[0] - a[0] or 1)); return [a[i] + (b[i] - a[i]) * p for i in range(1, len(a))]
    return k[-1][1:]

bx, by = R['browse']; ix, iy = R['input']; fx, fy = R['filter']; ex, ey = R['exec']
mx, my, mw, mh = R['modal']
# scene: (start, end, image-swaps [(t, name)], camera keys [(t, cx, cy, side)], cursor keys [(t, x, y)], clicks, page height)
SC = [
    (0.0, 3.0, [(0, 'home0'), (1.15, 'home1')], [(0, 720, 450, 900), (1.1, 720, 450, 900), (2.6, 720, 600, 760)],
     [(0.35, 980, 760), (0.95, ix + 40, iy + 4), (1.4, ix + 40, iy + 4), (2.45, bx + 10, by + 4), (3.0, bx + 10, by + 4)], [1.0, 2.6], 900),
    (3.0, 6.2, [(0, 'skills')], [(3.0, 560, 450, 900), (3.6, 560, 450, 900), (6.0, 560, 1250, 900)], [], [], R['skillsDoc']['h']),
    (6.2, 9.6, [(0, 'lib0'), (7.7, 'lib1')], [(6.2, 545, 560, 900), (7.9, 545, 560, 900), (9.0, 520, 650, 800)],
     [(6.75, 760, 980), (7.5, fx + 2, fy + 2), (7.7, fx + 2, fy + 2), (8.9, 640, 720), (9.6, 640, 720)], [7.6], 2266),
    (9.6, 12.6, [(0, 'ondoc')], [(9.6, 706, 450, 900), (10.2, 706, 450, 900), (11.2, 706, 780, 900), (12.3, 706, 840, 720)], [], [], R['docDoc']['h']),
    (12.6, 16.2, [(0, 'detail0'), (14.15, 'detail1')], [(12.6, 560, 450, 900), (14.3, 560, 450, 900), (15.1, mx + mw / 2, my + mh / 2, 720)],
     [(13.1, 760, 860), (13.95, ex + 10, ey + 4), (14.3, ex + 10, ey + 4), (14.9, mx + mw - 120, my + mh - 30), (16.2, mx + mw - 120, my + mh - 30)], [14.05], 900),
]
DUR = SC[-1][1]
TR = 0.5  # slide transition length, overlapping the start of the next scene

ARROW = [(0, 0), (0, 21), (5, 16.5), (8.6, 24.5), (12, 23), (8.6, 15.4), (15.2, 15.4)]

def scene_frame(sc, t, with_cursor=True):
    st, en, swaps, cam, cur, clicks, ph = sc
    name = [n for (ts, n) in swaps if t - st >= ts or ts == 0 or t >= ts][-1]
    # swaps are absolute times except the 0 entry
    name = swaps[0][1]
    for ts, n in swaps[1:]:
        if t >= ts: name = n
    cx, cy, side = keys(cam, t)
    side = min(side, 900)
    x0 = min(max(cx - side / 2, 0), 1440 - side); y0 = min(max(cy - side / 2, 0), ph - side)
    im = img(name).crop(tuple(int(round(v * SRC)) for v in (x0, y0, x0 + side, y0 + side))).resize((OUT, OUT), Image.LANCZOS)
    if with_cursor and cur and cur[0][0] <= t <= cur[-1][0] + 0.2:
        k = OUT / side
        px, py = keys(cur, t)
        a = min(1, (t - cur[0][0]) / 0.25, max(0, (en - t) / 0.25))
        layer = Image.new('RGBA', (OUT, OUT), (0, 0, 0, 0)); d = ImageDraw.Draw(layer)
        sx, sy = (px - x0) * k, (py - y0) * k
        for ct in clicks:
            rp = (t - ct) / 0.5
            if 0 <= rp < 1:
                r = (14 + 46 * rp) * k / 1.6
                d.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(26, 115, 232, int(90 * (1 - rp) * a)))
        pr = 0.85 if any(0 <= t - ct < 0.15 for ct in clicks) else 1.0
        s = 1.55 * pr * k / 1.6
        d.polygon([(sx + x * s, sy + y * s) for x, y in ARROW], fill=(32, 33, 36, int(255 * a)), outline=(255, 255, 255, int(255 * a)), width=max(2, int(2 * s)))
        im = Image.alpha_composite(im.convert('RGBA'), layer).convert('RGB')
    return im

def render(t):
    for i, sc in enumerate(SC):
        if sc[0] <= t < sc[1] or (i == len(SC) - 1 and t >= sc[0]):
            cur = scene_frame(sc, t)
            if i > 0 and t < sc[0] + TR:
                p = ease((t - sc[0]) / TR)
                prev = scene_frame(SC[i - 1], SC[i - 1][1] - 0.001, with_cursor=False)
                out = Image.new('RGB', (OUT, OUT), (0, 0, 0))
                off = int(OUT * p)
                out.paste(prev, (-off, 0)); out.paste(cur, (OUT - off, 0))
                return out
            return cur
    return scene_frame(SC[-1], t)

if __name__ == '__main__':
    od = sys.argv[1]; os.makedirs(od, exist_ok=True)
    if len(sys.argv) > 2:
        for v in map(float, sys.argv[2].split(',')): render(v).save(f'{od}/s{v}.png')
    else:
        n = int(DUR * FPS)
        for i in range(n): render(i / FPS).save(f'{od}/f{i:04d}.png')
        print('frames', n)
