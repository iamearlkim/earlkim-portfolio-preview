const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1280,height:900}});
await p.goto('file://'+process.argv[2]);await p.screenshot({path:process.argv[3],fullPage:false});
const p2=await b.newPage({viewport:{width:390,height:844}});await p2.goto('file://'+process.argv[2]);
const w=await p2.evaluate(()=>document.documentElement.scrollWidth);console.log('phone scrollWidth',w);await b.close();})();
