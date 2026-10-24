// usage: node render.js <screen.html> <theme> <out.png> [height]
const { chromium } = require('playwright'); const http = require('http'); const fs = require('fs'); const path = require('path');
const [,, file, theme, out, h] = process.argv;
const root = path.join(__dirname, 'screens');
const srv = http.createServer((req, res) => { const p = path.join(root, decodeURIComponent(req.url.split('?')[0])); if (!fs.existsSync(p)) { res.statusCode = 404; return res.end(); }
  const ext = path.extname(p); res.setHeader('Content-Type', ext === '.js' ? 'text/javascript' : ext === '.css' ? 'text/css' : ext === '.json' ? 'application/json' : 'text/html'); fs.createReadStream(p).pipe(res); }).listen(0, async () => {
  const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1440, height: +(h || 900) }, deviceScaleFactor: 2 });
  const errs = []; pg.on('pageerror', e => errs.push(e.message));
  await pg.goto(`http://localhost:${srv.address().port}/${file}?theme=${theme}`); await pg.waitForFunction(() => window.__ui5ready); await pg.waitForTimeout(2500);
  await pg.screenshot({ path: out }); if (errs.length) console.log('ERR', errs.slice(0,3)); await b.close(); srv.close(); });
