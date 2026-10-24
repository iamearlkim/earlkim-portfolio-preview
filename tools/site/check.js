const { chromium } = require('playwright'); const fs=require('fs');
(async()=>{const b=await chromium.launch(); const R='/home/claude/earlkim-portfolio-preview/';
const files=fs.readdirSync(R).filter(f=>f.endsWith('.html'));
for(const f of files){const p=await b.newPage({viewport:{width:1280,height:900}});await p.goto('file://'+R+f);await p.waitForLoadState('load');
 const r=await p.evaluate(()=>({broken:[...document.images].filter(i=>!i.naturalWidth).map(i=>i.getAttribute('src')),links:[...document.querySelectorAll('a[href]')].map(a=>a.getAttribute('href')).filter(h=>!h.startsWith('#')&&!h.startsWith('mailto'))}));
 const bad=r.links.filter(h=>!fs.existsSync(R+h.split('#')[0]));
 const p2=await b.newPage({viewport:{width:390,height:844}});await p2.goto('file://'+R+f);const sw=await p2.evaluate(()=>document.documentElement.scrollWidth);
 console.log(f,'broken',r.broken.length,'badlinks',bad,'phoneW',sw); if(f==='index.html'||f==='samsung.html'||f==='hanon.html') await p.screenshot({path:'shot-'+f+'.png',fullPage:true});}
await b.close();})();
