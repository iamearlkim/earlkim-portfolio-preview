"""Compose the square console video from the slowed, timestamped recording.
usage: python3 compose.py OUTDIR [t1,t2,...]   (times = output seconds; omit for all frames)"""
import json, sys, os, math
from PIL import Image, ImageDraw

D = json.load(open('rec/log.json'))
LOG, EV = D['log'], D['ev']
OUT = 1440           # square output px
FPS = 30
SRC = 2              # recording device scale factor (css -> px)

def ease(x):
    x = max(0.0, min(1.0, x))
    return 4*x*x*x if x < .5 else 1 - pow(-2*x + 2, 3) / 2

# --- time remap: output seconds -> demo seconds (piecewise linear) ---
c1, c2, dn = EV['clickLink'], EV['clickRun'], EV['done']
REMAP = [
    (0.0, 0.55),
    (2.5, EV['step1done'] + 0.05),   # typing + error, a bit faster than real time
    (3.3, c1),                        # cursor travels to the link
    (4.5, c2),                        # panel slides in, cursor to Run skill
    (8.3, dn),                        # skill run, ~2.3x speed
    (10.3, dn + 1.45),                # hold on Done / verification
]
DUR = REMAP[-1][0]

def demo_t(v):
    for (a, ta), (b, tb) in zip(REMAP, REMAP[1:]):
        if a <= v <= b:
            return ta + (tb - ta) * (v - a) / (b - a)
    return REMAP[-1][1]

# --- camera: (output s, cx, cy, side) in css px of the 1440x900 page ---
CAM = [
    (0.0, 520, 430, 760),
    (2.1, 520, 430, 760),
    (2.8, 560, 580, 640),
    (3.35, 560, 580, 640),
    (4.15, 1130, 560, 660),
    (4.7, 1130, 560, 660),
    (5.5, 1060, 520, 760),
    (8.2, 1060, 520, 760),
    (9.0, 1190, 640, 520),
    (DUR, 1190, 640, 520),
]

def cam(v):
    for a, b in zip(CAM, CAM[1:]):
        if a[0] <= v <= b[0]:
            p = ease((v - a[0]) / (b[0] - a[0] or 1))
            return [a[i] + (b[i] - a[i]) * p for i in (1, 2, 3)]
    return CAM[-1][1:]

# --- cursor path in css px: (output s, x, y) ---
lx, ly = EV['link']['x'], EV['link']['y']
rx, ry = EV['run']['x'], EV['run']['y']
CUR = [
    (2.55, 820, 860), (3.3, lx + 6, ly + 4),
    (3.6, lx + 6, ly + 4), (4.5, rx + 10, ry + 2),
    (5.0, rx + 10, ry + 2), (6.0, rx + 60, ry - 140),
]
CLICKS = [3.3, 4.5]

def cursor(v):
    if v < CUR[0][0] or v > CUR[-1][0] + 0.3:
        return None
    for a, b in zip(CUR, CUR[1:]):
        if a[0] <= v <= b[0]:
            p = ease((v - a[0]) / (b[0] - a[0] or 1))
            return (a[1] + (b[1] - a[1]) * p, a[2] + (b[2] - a[2]) * p)
    return CUR[-1][1:]

def cursor_alpha(v):
    return min(1, max(0, (v - CUR[0][0]) / 0.25), max(0, (CUR[-1][0] + 0.3 - v) / 0.3))

TIMES = [x[1] for x in LOG]
import bisect
def frame_for(t):
    i = bisect.bisect_left(TIMES, t)
    i = min(max(i, 0), len(TIMES) - 1)
    if i > 0 and abs(TIMES[i - 1] - t) < abs(TIMES[i] - t):
        i -= 1
    return LOG[i][0]

ARROW = [(0, 0), (0, 21), (5, 16.5), (8.6, 24.5), (12, 23), (8.6, 15.4), (15.2, 15.4)]

def render(v):
    t = demo_t(v)
    img = Image.open(f'rec/f{frame_for(t):04d}.jpg').convert('RGB')
    cx, cy, side = cam(v)
    side = min(side, 900)
    x0 = min(max(cx - side / 2, 0), 1440 - side)
    y0 = min(max(cy - side / 2, 0), 900 - side)
    box = tuple(int(round(z * SRC)) for z in (x0, y0, x0 + side, y0 + side))
    out = img.crop(box).resize((OUT, OUT), Image.LANCZOS)
    k = OUT / side
    c = cursor(v)
    if c:
        a = cursor_alpha(v)
        layer = Image.new('RGBA', (OUT, OUT), (0, 0, 0, 0))
        d = ImageDraw.Draw(layer)
        px, py = (c[0] - x0) * k, (c[1] - y0) * k
        for ct in CLICKS:
            rp = (v - ct) / 0.5
            if 0 <= rp < 1:
                r = (14 + 46 * rp) * k / 1.6
                d.ellipse([px - r, py - r, px + r, py + r], fill=(26, 115, 232, int(90 * (1 - rp) * a)))
        press = 0.85 if any(0 <= v - ct < 0.15 for ct in CLICKS) else 1.0
        s = 1.55 * press * k / 1.6
        pts = [(px + x * s, py + y * s) for x, y in ARROW]
        d.polygon(pts, fill=(32, 33, 36, int(255 * a)), outline=(255, 255, 255, int(255 * a)), width=max(2, int(2 * s)))
        out = Image.alpha_composite(out.convert('RGBA'), layer).convert('RGB')
    return out

if __name__ == '__main__':
    od = sys.argv[1]; os.makedirs(od, exist_ok=True)
    if len(sys.argv) > 2:
        for v in map(float, sys.argv[2].split(',')):
            render(v).save(f'{od}/s{v}.png')
    else:
        n = int(DUR * FPS)
        for i in range(n):
            render(i / FPS).save(f'{od}/f{i:04d}.png')
        print('frames', n)
