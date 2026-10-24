const { chromium } = require('playwright');
const B='https://jimnidev.github.io/google-cloud-docs-capstone/pages/';
const fs=require('fs');
(async()=>{const b=await chromium.launch();
const p=await b.newPage({viewport:{width:1440,height:900},deviceScaleFactor:2});
const hide=async()=>{await p.addStyleTag({content:'::-webkit-scrollbar{display:none} html{scrollbar-width:none}'});await p.evaluate(()=>{const r=document.getElementById('detailRuns');if(r)r.style.visibility='hidden';});};
const full=async(name)=>{const d=await p.evaluate(()=>({w:document.documentElement.clientWidth,h:document.documentElement.scrollHeight}));await p.screenshot({path:name,fullPage:true,clip:{x:0,y:0,width:d.w,height:d.h}});return d;};
const R={};
// home
await p.goto(B+'home.html',{waitUntil:'networkidle'});await p.waitForTimeout(1200);await hide();
await p.screenshot({path:'home0.png'});
const ta=await p.$('textarea, [contenteditable="true"], input[type=text]');await ta.click();await p.keyboard.type('/');await p.waitForTimeout(900);
await p.screenshot({path:'home1.png'});
R.browse=await p.evaluate(()=>{const a=[...document.querySelectorAll('a,button')].find(e=>/Browse all skills/.test(e.innerText));const r=a.getBoundingClientRect();return [r.left+r.width/2,r.top+r.height/2]});
R.input=await p.evaluate(el=>{const r=el.getBoundingClientRect();return [r.left,r.top+r.height/2]},ta);
// skills intro
await p.goto(B+'skills.html',{waitUntil:'networkidle'});await p.waitForTimeout(1200);await hide();R.skillsDoc=await full('skills.png');
// library
await p.goto(B+'skill-library.html',{waitUntil:'networkidle'});await p.waitForTimeout(1200);await hide();R.libDoc=await full('lib0.png');
const lab=await p.evaluateHandle(()=>[...document.querySelectorAll('label')].find(l=>/Troubleshooting/.test(l.innerText)));
R.filter=await p.evaluate(l=>{const r=l.getBoundingClientRect();return [r.left+12,r.top+r.height/2+scrollY]},lab);
await lab.asElement().click();await p.waitForTimeout(900);await p.evaluate(()=>scrollTo(0,0));R.libDoc1=await full('lib1.png');
R.fixCard=await p.evaluate(()=>{const e=[...document.querySelectorAll('*')].filter(x=>x.children.length<3&&/Fix 403 Forbidden Access/.test(x.innerText||''))[0];const r=e.getBoundingClientRect();return [r.left+r.width/2,r.top+r.height/2+scrollY]});
R.count=await p.evaluate(()=>{const e=[...document.querySelectorAll('*')].find(x=>/skills? found/.test(x.innerText||'')&&x.children.length===0);return e?e.innerText:''});
// doc page
await p.goto(B+'skill-on-doc.html',{waitUntil:'networkidle'});await p.waitForTimeout(1200);await hide();R.docDoc=await full('ondoc.png');
// detail + modal
await p.goto(B+'skill-detail-screen.html',{waitUntil:'networkidle'});await p.waitForTimeout(1200);await hide();
await p.screenshot({path:'detail0.png'});
R.exec=await p.evaluate(()=>{const b=[...document.querySelectorAll('button')].find(b=>b.innerText.trim()==='Execute');const r=b.getBoundingClientRect();return [r.left+r.width/2,r.top+r.height/2]});
await p.click('button.btn-primary-action');await p.waitForTimeout(900);
await p.screenshot({path:'detail1.png'});
R.modal=await p.evaluate(()=>{const m=document.querySelector('#executionModal .exec-modal, #executionModal > div, #executionModal');const all=[...document.querySelectorAll('#executionModal *')].map(e=>e.getBoundingClientRect()).filter(r=>r.width>300&&r.width<900);const r=all[0];return [r.left,r.top,r.width,r.height]});
fs.writeFileSync('rects.json',JSON.stringify(R,null,1));console.log(JSON.stringify(R));
await b.close();})();
