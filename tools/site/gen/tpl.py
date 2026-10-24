import json, html as H, os
BLOBS = json.load(open(os.path.join(os.path.dirname(__file__), '..', 'blobs.json')))
HOME = 'Artboard-mosb.dc.html'
INK, MUTED, SEC, BORDER, DIV, TAGB, BG = '#121316', '#4A4C53', '#3B3D44', '#E2E2DC', '#ECECE6', '#DADAD3', '#F6F6F3'
H2 = "font-size: clamp(2rem, 3.6vw, 2.75rem); letter-spacing: -0.025em; font-weight: 600; line-height: 1.1"
LBL = f"font-size: 13px; letter-spacing: 0.04em; text-transform: uppercase; color: {MUTED}"
W = "max-width: 1200px; margin: 0 auto"

def e(s): return H.escape(s, quote=True)
def img(name): return '/_blob/' + BLOBS[name]

def head_block(label, heading, maxch=24):
    return (f'<div style="display: flex; flex-direction: column; gap: 12px">'
            f'<span style="{LBL}">{e(label)}</span>'
            f'<h2 style="margin: 0; {H2}; max-width: {maxch}ch">{e(heading)}</h2></div>')

def page(title, sections, back_href=HOME, back_label='All work'):
    body = '\n'.join(sections)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{e(title)}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600&amp;display=swap">
<style>
body{{margin:0;background:#F6F6F3}}
a{{color:#1F3FD1}}a:hover{{color:#142C99}}
</style>
</helmet>
<div style="font-family: 'Instrument Sans', system-ui, sans-serif; color: {INK}; background: {BG}; min-height: 100vh; -webkit-font-smoothing: antialiased">
<header style="border-bottom: 1px solid {BORDER}; background: {BG}">
<nav aria-label="Primary" style="{W}; padding: 20px 24px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 16px">
<a href="{HOME}" style="display: flex; align-items: center; gap: 12px; text-decoration: none; color: {INK}">
<span style="width: 36px; height: 36px; border-radius: 8px; background: {INK}; color: {BG}; display: flex; align-items: center; justify-content: center; font-weight: 600; font-size: 13px; letter-spacing: 0.02em">EK</span>
<span style="font-weight: 600; font-size: 16px">Earl Kim</span>
</a>
<a href="{back_href}" style="color: {SEC}; text-decoration: none; font-size: 16px; padding: 12px 0">← {e(back_label)}</a>
</nav>
</header>
{body}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"accent":{{"editor":"color","default":"#1F3FD1","options":["#1F3FD1","#0F766E","#B4441C","#121316"]}},"$preview":{{"width":1440,"height":8000}}}}'>
class Component extends DCLogic {{
  renderVals() {{
    return {{ accent: this.props.accent ?? '#1F3FD1' }};
  }}
}}
</script>
</body>
</html>
'''

def hero(tags, title, lead, meta, kicker=None):
    t = ''.join(f'<span style="border: 1px solid {TAGB}; border-radius: 999px; padding: 4px 10px">{e(x)}</span>' for x in tags)
    m = ''.join(f'<div style="display: flex; flex-direction: column; gap: 4px"><dt style="{LBL}">{e(k)}</dt><dd style="margin: 0; font-size: 16px; line-height: 1.5">{e(v)}</dd></div>' for k, v in meta)
    k = f'<span style="{LBL}">{e(kicker)}</span>' if kicker else ''
    return f'''<section style="{W}; padding: 96px 24px 56px; display: flex; flex-direction: column; gap: 28px">
{k}<div style="display: flex; flex-wrap: wrap; gap: 8px; font-size: 13px; color: {MUTED}">{t}</div>
<h1 style="margin: 0; font-size: clamp(2.6rem, 5.6vw, 4.6rem); line-height: 1.04; letter-spacing: -0.03em; font-weight: 600; max-width: 18ch">{e(title)}</h1>
<p style="margin: 0; font-size: 22px; line-height: 1.5; color: {SEC}; max-width: 46rem">{e(lead)}</p>
<dl style="margin: 16px 0 0; padding-top: 28px; border-top: 1px solid {BORDER}; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 200px), 1fr)); gap: 24px">{m}</dl>
</section>'''

def cover(name, alt, pad_bottom=96):
    return f'''<section style="{W}; padding: 0 24px {pad_bottom}px">
<img src="{img(name)}" alt="{e(alt)}" style="display: block; width: 100%; height: auto; border-radius: 16px">
</section>'''

def stats(items):
    cells = []
    for i, (num, cap) in enumerate(items):
        col = '; color: {{accent}}' if i == len(items) - 1 else ''
        cells.append(f'<div style="display: flex; flex-direction: column; gap: 8px"><span style="font-size: clamp(2rem, 3.6vw, 2.75rem); font-weight: 600; letter-spacing: -0.03em; line-height: 1{col}">{e(num)}</span><span style="font-size: 16px; line-height: 1.5; color: {MUTED}">{e(cap)}</span></div>')
    return f'''<section aria-label="At a glance" style="border-top: 1px solid {BORDER}; border-bottom: 1px solid {BORDER}; background: #FFFFFF">
<div style="{W}; padding: 56px 24px; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 220px), 1fr)); gap: 40px">
{''.join(cells)}
</div>
</section>'''

def _body(paras=(), bullets=()):
    out = ''.join(f'<p style="margin: 0">{p}</p>' for p in paras)
    if bullets:
        out += '<ul style="margin: 0; padding: 0 0 0 20px; display: flex; flex-direction: column; gap: 12px">' + ''.join(f'<li>{b}</li>' for b in bullets) + '</ul>'
    return out

def split(label, heading, paras=(), bullets=(), white=False, top=64, bottom=64):
    inner = f'''<div style="{W}; padding: {top}px 24px {bottom}px; display: flex; flex-wrap: wrap; gap: 48px">
<div style="flex: 1 1 280px; min-width: 0">{head_block(label, heading, 18)}</div>
<div style="flex: 999 1 560px; min-width: 0; display: flex; flex-direction: column; gap: 20px; font-size: 16px; line-height: 1.65; color: {SEC}">{_body(paras, bullets)}</div>
</div>'''
    if white:
        return f'<section style="background: #FFFFFF; border-top: 1px solid {BORDER}; border-bottom: 1px solid {BORDER}; margin: 48px 0">{inner}</section>'
    return f'<section>{inner}</section>'

def cards(label, heading, items, numbered=False, minw=240, dark_last=False):
    out = []
    for i, it in enumerate(items):
        title, desc = it
        dark = dark_last and i == len(items) - 1
        bg = f'background: {INK}; color: {BG}' if dark else f'background: #FFFFFF; border: 1px solid {BORDER}'
        dc = '#B4B6BD' if dark else MUTED
        num = f'<span style="font-size: 13px; font-weight: 600; color: {"#B4B6BD" if dark else "{{accent}}"}">{i+1:02d}</span>' if numbered else ''
        d = f'<span style="font-size: 16px; line-height: 1.6; color: {dc}">{e(desc)}</span>' if desc else ''
        out.append(f'<li style="{bg}; border-radius: 16px; padding: 24px; display: flex; flex-direction: column; gap: 10px">{num}<span style="font-size: {"16px" if not desc else "22px"}; font-weight: 600; letter-spacing: -0.01em; line-height: 1.3">{e(title)}</span>{d}</li>')
    hb = head_block(label, heading) if heading else ''
    return f'''<section style="{W}; padding: 64px 24px; display: flex; flex-direction: column; gap: 32px">
{hb}
<ol style="list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, {minw}px), 1fr)); gap: 16px">{''.join(out)}</ol>
</section>'''

def section_title(label, heading):
    return f'<section style="{W}; padding: 64px 24px 16px">{head_block(label, heading)}</section>'

def figure(title, desc, imgs, maxw=1000, caption=None):
    t = f'<span style="font-size: 22px; font-weight: 600; letter-spacing: -0.015em">{e(title)}</span>' if title else ''
    d = f'<p style="margin: 0; font-size: 16px; line-height: 1.6; color: {MUTED}">{desc}</p>' if desc else ''
    head = f'<div style="display: flex; flex-direction: column; gap: 8px; max-width: 48rem">{t}{d}</div>' if (t or d) else ''
    ims = ''.join(f'<img src="{img(n)}" alt="{e(a)}" style="display: block; width: 100%; max-width: {maxw}px; height: auto; align-self: center; border-radius: 12px">' for n, a in imgs)
    cap = f'<p style="margin: 0; font-size: 13px; color: {MUTED}; text-align: center">{e(caption)}</p>' if caption else ''
    return f'<section style="{W}; padding: 32px 24px; display: flex; flex-direction: column; gap: 24px">{head}{ims}{cap}</section>'

def gallery(imgs, minw=280, caption=None, title=None, desc=None, colmax=None):
    t = f'<span style="font-size: 22px; font-weight: 600; letter-spacing: -0.015em">{e(title)}</span>' if title else ''
    d = f'<p style="margin: 0; font-size: 16px; line-height: 1.6; color: {MUTED}">{desc}</p>' if desc else ''
    head = f'<div style="display: flex; flex-direction: column; gap: 8px; max-width: 48rem">{t}{d}</div>' if (t or d) else ''
    figs = ''.join(f'<figure style="margin: 0; display: flex; flex-direction: column; gap: 10px"><img src="{img(n)}" alt="{e(a)}" style="display: block; width: 100%; height: auto; border-radius: 12px">{f"<figcaption style=\"font-size: 13px; color: {MUTED}\">{e(c)}</figcaption>" if c else ""}</figure>' for n, a, c in imgs)
    cap = f'<p style="margin: 0; font-size: 13px; color: {MUTED}">{e(caption)}</p>' if caption else ''
    cols = f'repeat(auto-fill, minmax(min(100%, {minw}px), {colmax}px))' if colmax else f'repeat(auto-fit, minmax(min(100%, {minw}px), 1fr))'
    return f'<section style="{W}; padding: 32px 24px; display: flex; flex-direction: column; gap: 24px">{head}<div style="display: grid; grid-template-columns: {cols}; gap: 20px; align-items: start; justify-content: start">{figs}</div>{cap}</section>'

def idea(n, title, desc, image, alt):
    return f'''<section style="{W}; padding: 24px 24px; display: flex; flex-wrap: wrap; gap: 32px; align-items: center">
<img src="{img(image)}" alt="{e(alt)}" style="flex: 1 1 320px; min-width: 0; max-width: 420px; height: auto; border-radius: 12px">
<div style="flex: 2 1 420px; min-width: 0; display: flex; flex-direction: column; gap: 10px">
<span style="font-size: 13px; font-weight: 600; color: {{{{accent}}}}">IDEA {n}</span>
<span style="font-size: 22px; font-weight: 600; letter-spacing: -0.015em; line-height: 1.3">{e(title)}</span>
<p style="margin: 0; font-size: 16px; line-height: 1.6; color: {MUTED}">{e(desc)}</p>
</div>
</section>'''

def quote(text, who):
    return f'''<section style="{W}; padding: 64px 24px">
<figure style="margin: 0; border-top: 2px solid {INK}; padding-top: 32px; display: flex; flex-direction: column; gap: 16px; max-width: 52rem">
<blockquote style="margin: 0; font-size: 22px; line-height: 1.5; letter-spacing: -0.01em">“{e(text)}”</blockquote>
<figcaption style="font-size: 16px; color: {MUTED}">{e(who)}</figcaption>
</figure>
</section>'''

def project_link(title, desc, image, alt, href, meta):
    return f'''<a href="{href}" style="text-decoration: none; color: {INK}; background: #FFFFFF; border: 1px solid {BORDER}; border-radius: 16px; overflow: hidden; display: flex; flex-direction: column">
<img src="{img(image)}" alt="{e(alt)}" style="display: block; width: 100%; height: 280px; object-fit: cover">
<div style="padding: 28px; display: flex; flex-direction: column; gap: 12px">
<span style="font-size: 13px; color: {MUTED}">{e(meta)}</span>
<span style="font-size: 22px; font-weight: 600; letter-spacing: -0.015em; line-height: 1.25">{e(title)}</span>
<span style="font-size: 16px; line-height: 1.55; color: {MUTED}">{e(desc)}</span>
<span style="font-size: 16px; font-weight: 500; color: {{{{accent}}}}; padding-top: 4px">Read project →</span>
</div>
</a>'''

def nxt(title, href, back_href=HOME, back_label='All work', kicker='Next case study'):
    return f'''<section style="background: {INK}; color: {BG}; margin-top: 64px">
<div style="{W}; padding: 80px 24px; display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 32px">
<div style="display: flex; flex-direction: column; gap: 12px">
<span style="font-size: 13px; letter-spacing: 0.04em; text-transform: uppercase; color: #B4B6BD">{e(kicker)}</span>
<span style="{H2}; max-width: 20ch">{e(title)}</span>
</div>
<div style="display: flex; flex-wrap: wrap; gap: 12px">
<a href="{back_href}" style="text-decoration: none; color: {BG}; font-weight: 500; font-size: 16px; padding: 14px 23px; border-radius: 999px; border: 1px solid #5A5C63">← {e(back_label)}</a>
<a href="{href}" style="text-decoration: none; background: {BG}; color: {INK}; font-weight: 500; font-size: 16px; padding: 15px 24px; border-radius: 999px">Next →</a>
</div>
</div>
</section>'''


def video(name, label, maxw=1100, pad='32px 24px'):
    return (f'<section style="{W}; padding: {pad}; display: flex; justify-content: center">'
            f'<video src="{img(name)}" autoplay="" muted="" loop="" playsinline="" controls="" aria-label="{e(label)}" '
            f'style="display: block; width: 100%; max-width: {maxw}px; height: auto; aspect-ratio: 16 / 10; border-radius: 16px; background: #E9EAF0"></video></section>')

def before_after(before, after, metrics=None):
    bs = ''.join(f'<img src="{img(n)}" alt="{e(a)}" style="display: block; width: 100%; height: auto; border-radius: 12px; border: 1px solid {BORDER}">' for n, a in before)
    af = ''.join(f'<img src="{img(n)}" alt="{e(a)}" style="display: block; width: 100%; height: auto; border-radius: 12px; border: 1px solid {BORDER}">' for n, a in after)
    col = lambda lab, inner: f'<div style="display: flex; flex-direction: column; gap: 12px"><span style="{LBL}">{lab}</span>{inner}</div>'
    m = ''
    if metrics:
        m = '<dl style="margin: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 200px), 1fr)); gap: 16px 24px; padding-top: 8px">' + ''.join(f'<div><dt style="{LBL}">{e(k)}</dt><dd style="margin: 4px 0 0; font-size: 16px; line-height: 1.5">{e(v)}</dd></div>' for k, v in metrics) + '</dl>'
    return (f'<section style="{W}; padding: 16px 24px 48px; display: flex; flex-direction: column; gap: 24px">'
            f'<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 420px), 1fr)); gap: 24px; align-items: start">{col("Before", bs)}{col("After", af)}</div>{m}</section>')


def project_link_ph(title, desc, href, meta):
    return f'''<a href="{href}" style="text-decoration: none; color: {INK}; background: #FFFFFF; border: 1px solid {BORDER}; border-radius: 16px; overflow: hidden; display: flex; flex-direction: column">
<div role="img" aria-label="Cover image placeholder" style="height: 280px; background: #E6ECEE; display: flex; align-items: center; justify-content: center; color: {MUTED}; font-size: 13px">[Project cover image]</div>
<div style="padding: 28px; display: flex; flex-direction: column; gap: 12px">
<span style="font-size: 13px; color: {MUTED}">{e(meta)}</span>
<span style="font-size: 22px; font-weight: 600; letter-spacing: -0.015em; line-height: 1.25">{e(title)}</span>
<span style="font-size: 16px; line-height: 1.55; color: {MUTED}">{e(desc)}</span>
<span style="font-size: 16px; font-weight: 500; color: {{{{accent}}}}; padding-top: 4px">Read project →</span>
</div>
</a>'''
