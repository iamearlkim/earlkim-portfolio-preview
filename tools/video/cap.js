const { chromium } = require('playwright');
const [,, html, outDir, mode] = process.argv;
(async()=>{const b=await chromium.launch();
const p=await b.newPage({viewport:{width:Number(process.env.VWW||1600),height:Number(process.env.VHH||1000)},deviceScaleFactor: Number(process.env.DSF|| (mode==='frames'?1.2:0.6))});
if(process.env.ALPHA){await p.addInitScript(()=>{document.addEventListener('DOMContentLoaded',()=>{const st=document.createElement('style');st.textContent='html,body{background:transparent!important}.blob{display:none!important}';document.head.appendChild(st);});});}
await p.goto('file://'+html+'?capture',{waitUntil:'networkidle'});
await p.waitForFunction(()=>window.__ready);await p.waitForTimeout(500);
await p.evaluate(()=>window.setupKeys());
const fs=require('fs');fs.mkdirSync(outDir,{recursive:true});
if(mode==='frames'){const fps=30;for(let i=Number(process.env.S||0);i<Number(process.env.N||300);i++){await p.evaluate(t=>window.render(t),i/fps);await p.screenshot({path:`${outDir}/f${String(i).padStart(4,'0')}.png`,omitBackground:!!process.env.ALPHA});}}
else{for(const t of (process.env.TS||"0.2,1.2,2.4,3.0,4.0,5.0,6.8,7.05,8.2,9.8").split(",").map(Number)){await p.evaluate(t=>window.render(t),t);await p.screenshot({path:`${outDir}/t${t}.png`});}}
await b.close();})();
