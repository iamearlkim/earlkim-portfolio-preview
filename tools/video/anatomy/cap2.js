const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();
const p=await b.newPage({viewport:{width:1440,height:900},deviceScaleFactor:3});
await p.goto('https://jimnidev.github.io/google-cloud-docs-capstone/pages/skill-detail-screen.html',{waitUntil:'networkidle'});
await p.waitForTimeout(1500);
await p.addStyleTag({content:'html{overflow:hidden!important} ::-webkit-scrollbar{display:none}'});
await p.evaluate(()=>{const r=document.getElementById('detailRuns'); if(r) r.style.visibility='hidden';});
await p.waitForTimeout(300);
const R=await p.evaluate(()=>{
 const rect=el=>{const r=el.getBoundingClientRect();return {x:r.left+scrollX,y:r.top+scrollY,w:r.width,h:r.height}};
 const q=s=>document.querySelector(s);
 const exec=[...document.querySelectorAll('button')].find(b=>b.innerText.trim()==='Execute');
 const h=id=>rect(document.getElementById(id));
 return {doc:{w:document.documentElement.scrollWidth,h:document.documentElement.scrollHeight},
  title:rect(q('#detailTitle')), meta:rect(q('#detailMeta')), overview:rect(q('section#overview')),
  prereqH:h('prerequisites'), stepsH:h('steps'), s1:h('1-identify-which-identity-is-calling-the-endpoint'), s4:h('4-re-run-test_endpointpy-to-verify-access'), valid:h('validation-logic'),
  tabs:rect(q('#agentTabs')), cmd:rect(q('#installCommand').closest('div').parentElement), exec:rect(exec), preview:rect(q('#skillMdPreview'))};
});
console.log(JSON.stringify(R));
require('fs').writeFileSync('rects.json',JSON.stringify(R,null,1));
await p.screenshot({path:'detail@3x.png',fullPage:true,clip:{x:0,y:0,width:R.doc.w,height:R.doc.h}});
await b.close();})();
