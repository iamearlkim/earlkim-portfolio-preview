import re, sys, json, os
pages = {'Artboard-mosb.dc.html': ('index.html', 'Earl Kim — Senior UX Designer'),
         'CaseStudy-Samsung.dc.html': ('samsung.html', 'Samsung enterprise platforms — Earl Kim'),
         'CaseStudy-SamsungESG.dc.html': ('samsung-esg.html', 'Samsung ESG — Earl Kim'),
         'CaseStudy-SamsungEcom.dc.html': ('samsung-ecommerce.html', 'Samsung e-commerce — Earl Kim'),
         'CaseStudy-Doosan.dc.html': ('doosan.html', 'Doosan AI recruitment — Earl Kim'),
         'CaseStudy-Hanon.dc.html': ('hanon.html', 'Hanon Systems — Earl Kim'),
         'CaseStudy-BHP.dc.html': ('bhp.html', 'BHP financial planning — Earl Kim'),
         'CaseStudy-JGSummit.dc.html': ('jg-summit.html', 'JG Summit — Earl Kim'),
         'CaseStudy-FoodDelivery.dc.html': ('food-delivery.html', 'Eco-friendly food delivery — Earl Kim'),
         'CaseStudy-Gogoro.dc.html': ('gogoro.html', 'Gogoro — Earl Kim'),
         'CaseStudy-Clerro.dc.html': ('clerro.html', 'Clerro — Earl Kim'),
         'CaseStudy-GoogleCloud.dc.html': ('google-cloud.html', 'Google Cloud documentation — Earl Kim'),
         'CaseStudy-SamsungProcurement.dc.html': ('samsung-procurement.html', 'Samsung procurement — Earl Kim'),
         'CaseStudy-FPA.dc.html': ('financial-planning.html', 'Financial planning and analysis — Earl Kim'),
         'CaseStudy-SamsungDSCloud.dc.html': ('samsung-ds-cloud.html', 'Samsung DS cloud platform — Earl Kim'),
         'CaseStudy-SamsungDXRisk.dc.html': ('samsung-dx-risk.html', 'Samsung DX risk management — Earl Kim'),
         'CaseStudy-SamsungShipment.dc.html': ('samsung-shipment.html', 'Samsung shipment — Earl Kim')}
out_dir = sys.argv[1]
blobs = {v: k for k, v in json.load(open('blobs.json')).items()}
os.makedirs(f'{out_dir}/images', exist_ok=True)
used = set()
for src_name, (dst, title) in pages.items():
    src = open(f'canvas/project/{src_name}', encoding='utf-8').read()
    helmet = re.search(r'<helmet>(.*?)</helmet>', src, re.S).group(1).strip()
    body = re.search(r'</helmet>(.*?)</x-dc>', src, re.S).group(1).strip()
    body = body.replace('{{accent}}', '#1F3FD1')
    def sub(m):
        f = blobs[m.group(1)]; used.add(f); return f'images/{f}'
    body = re.sub(r'/_blob/([0-9a-f]{32})', sub, body)
    for s, (d, _) in pages.items():
        body = body.replace(f'href="{s}', f'href="{d}')
    helmet = helmet.replace('body{margin:0;background:#F6F6F3}', 'body{margin:0;background:#F6F6F3}\nhtml{scroll-behavior:smooth}')
    html = f'<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n<title>{title}</title>\n{helmet}\n</head>\n<body>\n{body}\n</body>\n</html>\n'
    assert '{{' not in html and 'support.js' not in html and '/_blob/' not in html and '.dc.html' not in html, dst
    open(f'{out_dir}/{dst}', 'w', encoding='utf-8').write(html)
import shutil
for f in used: shutil.copy(f'img/{f}', f'{out_dir}/images/{f}')
print(len(pages), 'pages,', len(used), 'images')
