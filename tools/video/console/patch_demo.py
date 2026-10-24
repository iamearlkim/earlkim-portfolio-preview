"""Download the console prototype and make the local copy used for recording.
usage: curl -s https://jimnidev.github.io/skill-terminal-demo/ -o demo.html && python3 patch_demo.py"""
s = open('demo.html').read()
s = s.replace('jimin31', 'alex').replace('light-haven-484520-f8', 'orbit-ml-417203')
s = s.replace('Troubleshooting · ★ 12,400 runs in the last 30 days', 'Troubleshooting')
s = s.replace('<div class="avatar">J</div>', '<div class="avatar">A</div>')
s = s.replace('function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }',
              'function sleep(ms) { return new Promise(r => setTimeout(r, ms * (window.__F || 1))); }')
s = s.replace('</head>', '<style>#demoControls{display:none!important}</style></head>', 1)
old = "  document.getElementById('skillVerify').classList.add('show');"
s = s.replace(old, old + "\n  (function(){const b=document.querySelector('.skill-overlay-body');const st=b.scrollTop,en=b.scrollHeight-b.clientHeight,D=500*(window.__F||1),t0=performance.now();(function f(){const p=Math.min(1,(performance.now()-t0)/D);const e=p<.5?2*p*p:1-Math.pow(-2*p+2,2)/2;b.scrollTop=st+(en-st)*e;if(p<1)requestAnimationFrame(f);})();})();", 1)
open('demo-local.html', 'w').write(s)
print('wrote demo-local.html')
