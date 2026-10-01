import sys, os, re, subprocess
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
import c_front as F, c_ch1_3 as A, c_ch4 as B4, c_ch5_6 as C, c_ch7_10 as D, c_bonus as E

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
css = open(os.path.join(root, "src", "style.css"), encoding="utf-8").read()

TOC_ITEMS = [("sec","DÉBUT"),("","Avant-propos","AVANT-PROPOS"),("","Introduction","INTRODUCTION"),("sec","LES 10 CHAPITRES"),
 (1,"Comprendre ChatGPT","CHAPITRE 1"),(2,"10 façons de monétiser une compétence","CHAPITRE 2"),(3,"Créer sa première offre","CHAPITRE 3"),
 (4,"25 prompts pour créer du contenu","CHAPITRE 4"),(5,"20 prompts pour vendre","CHAPITRE 5"),(6,"Trouver ses premiers clients","CHAPITRE 6"),
 (7,"Utiliser ChatGPT pour gagner du temps","CHAPITRE 7"),(8,"Créer son portfolio même sans expérience","CHAPITRE 8"),
 (9,"Devenir plus productif avec ChatGPT","CHAPITRE 9"),(10,"Ton plan pour passer à l'action","CHAPITRE 10"),
 ("sec","BONUS"),("★","50 prompts ultra-pratiques","BONUS 1"),("★","20 idées de services à vendre","BONUS 2"),("★","Checklist du premier client","BONUS 3"),("sec","FIN"),("","Conclusion","CONCLUSION")]

def assemble(pages):
    rows = []
    for it in TOC_ITEMS:
        if it[0] == "sec": rows.append(it)
        else: rows.append((it[0] if it[0] != "" else "·", it[1], pages.get(it[2], "")))
    body = (F.cover() + F.titlepage() + F.legal() + F.toc(rows) + F.avant_propos() + F.intro()
            + A.ch1() + A.ch2() + A.ch3() + B4.ch4() + C.ch5() + C.ch6() + D.ch7() + D.ch8() + D.ch9() + D.ch10()
            + E.bonus1() + E.bonus2() + E.bonus3() + E.conclusion())
    return f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>CHATGPT POUR GAGNER DE L\'ARGENT</title><style>{css}</style></head><body>{body}</body></html>'

def render(html_path, pdf_path):
    subprocess.run(["/opt/pw-browsers/chromium",
        "--headless=new","--no-sandbox","--disable-gpu","--no-pdf-header-footer","--print-to-pdf="+pdf_path,"file://"+html_path],
        check=True, capture_output=True)

def find_pages(pdf):
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout).group(1))
    pages, markers = {}, ["AVANT-PROPOS","INTRODUCTION","CONCLUSION"] + [f"CHAPITRE {i}" for i in range(1,11)] + ["BONUS 1","BONUS 2","BONUS 3"]
    for pg in range(5, n+1):
        t = subprocess.run(["pdftotext","-f",str(pg),"-l",str(pg),pdf,"-"], capture_output=True, text=True).stdout
        tt = re.sub(r"\s","",t)[:40]
        for m in markers:
            if m not in pages and tt.startswith(m.replace(" ","")): pages[m] = pg
    return n, pages

if __name__ == "__main__":
    out = os.path.join(root, "CHATGPT-POUR-GAGNER-DE-L-ARGENT.pdf"); hp = os.path.join(root, "ebook.html")
    open(hp,"w",encoding="utf-8").write(assemble({})); render(hp,out)
    n, pages = find_pages(out)
    open(hp,"w",encoding="utf-8").write(assemble(pages)); render(hp,out)
    n2, pages2 = find_pages(out)
    print("pages:", n2, pages2)
