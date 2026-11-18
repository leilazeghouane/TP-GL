# -*- coding: utf-8 -*-
import subprocess

terminal_html = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        body {
            margin: 0;
            padding: 10px;
            background: #000000;
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 11px;
            line-height: 1.35;
            color: #cccccc;
        }
        .prompt { color: #55ff55; font-weight: bold; }
        .path { color: #55ffff; }
        .branch { color: #ffff55; }
        .cmd { color: #ffffff; font-weight: bold; }
        .green { color: #55ff55; }
        .cyan { color: #55ffff; }
        .yellow { color: #ffff55; }
        .red { color: #ff5555; }
        .white { color: #ffffff; }
    </style>
</head>
<body>
<div><span class="prompt">Adel_Kouidi@DESKTOP-UNIV</span> <span class="path">~/UniAccounts_work1</span> <span class="branch">(main)</span></div>
<div>$ <span class="cmd">javac -d bin $(find src -name "*.java")</span></div>
<div><span class="prompt">Adel_Kouidi@DESKTOP-UNIV</span> <span class="path">~/UniAccounts_work1</span> <span class="branch">(main)</span></div>
<div>$ <span class="cmd">java -cp bin dz.univ.accounts.MainWork1</span></div>
<br>
<div><span class="cyan">--- 1) BUILDER ---</span></div>
<div>StudentAccount[id=20240001, name=Med Adel Kouidi, email=medadel.kouidi@univ-eloued.dz, phone=0550112233, level=L3, major=Informatique (Genie Logiciel), scholarship=true, courses=[POO, Reseaux, BD]]</div>
<br>
<div><span class="yellow">--- Validation (cas invalides) ---</span></div>
<div><span class="red">Refuse:</span> id obligatoire et non vide</div>
<div><span class="red">Refuse:</span> email invalide (doit contenir @)</div>
<div><span class="red">Refuse:</span> level invalide : Doctorate</div>
<br>
<div><span class="cyan">--- 2) SINGLETON ---</span></div>
<div>Meme depot ? <span class="green">true</span></div>
<div>Meme journal ? <span class="green">true</span></div>
<div><span class="red">Doublon refuse:</span> id deja existant : 20240001</div>
<br>
<div><span class="cyan">--- 3) PROTOTYPE ---</span></div>
<div>StudentAccount[id=20241001, name=Oualid Laroum, phone=0661223344, level=M1, major=Informatique, scholarship=true, courses=[POO, Reseaux, BD, Cloud Computing]]</div>
<div>StudentAccount[id=20241002, name=Farah Kouidi, phone=0770556677, level=M1, major=Informatique, scholarship=false, courses=[POO, Reseaux, BD]]</div>
<br>
<div><span class="cyan">--- Depot: 3 comptes | Journal d'audit ---</span></div>
<div>2026-11-17T20:52:51 | <span class="green">REPO_INIT</span> | Central AccountRepository initialized.</div>
<div>2026-11-17T20:52:51 | <span class="green">CREATE (builder)</span> 20240001 : Med Adel Kouidi</div>
<div>2026-11-17T20:52:51 | <span class="green">CREATE (template)</span> 20241001 : Oualid Laroum</div>
<div>2026-11-17T20:52:51 | <span class="green">CREATE (template)</span> 20241002 : Farah Kouidi</div>
<br>
<div><span class="prompt">Adel_Kouidi@DESKTOP-UNIV</span> <span class="path">~/UniAccounts_work1</span> <span class="branch">(main)</span></div>
<div>$</div>
</body>
</html>
"""

html_p = r"c:\Users\PC\Desktop\Tp GL\docs\terminal_shot.html"
with open(html_p, "w", encoding="utf-8") as f:
    f.write(terminal_html)

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out_img = r"c:\Users\PC\Desktop\Tp GL\docs\images\sample_terminal.png"
subprocess.run([
    chrome, '--headless=new', '--disable-gpu',
    '--window-size=950,420',
    f'--screenshot={out_img}',
    html_p
])
print("Terminal screenshot rendered successfully!")
