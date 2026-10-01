# Petits helpers HTML pour composer l'e-book
import html as _h

def esc(t):
    return _h.escape(t, quote=False)

def p(t): return f"<p>{t}</p>"
def h2(t): return f"<h2>{t}</h2>"
def h3(t): return f"<h3>{t}</h3>"

def ul(items, cls=""):
    return f'<ul class="{cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def ol(items):
    return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"

def quote(t, who=""):
    w = f"<cite>{who}</cite>" if who else ""
    return f'<blockquote>{t}{w}</blockquote>'

def callout(title, body, kind="info", icon="💡"):
    return (f'<div class="callout {kind}"><div class="ct"><span class="ic">{icon}</span>{title}</div>'
            f'<div class="cb">{body}</div></div>')

def table(headers, rows, cls=""):
    th = "".join(f"<th>{x}</th>" for x in headers)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'

def prompt_box(num, title, prompt, objectif=None, adapter=None, exemple=None):
    """Bloc prompt copiable. Les champs None sont omis."""
    out = f'<div class="pblock"><div class="ptitle"><span class="pnum">{num}</span>{title}</div>'
    if objectif:
        out += f'<div class="plabel">Objectif</div><p class="pt">{objectif}</p>'
    out += '<div class="plabel">Prompt à copier</div>'
    out += f'<div class="prompt">{prompt}</div>'
    if adapter:
        out += f'<div class="plabel">Comment l\'adapter</div><p class="pt">{adapter}</p>'
    if exemple:
        out += f'<div class="plabel">Exemple de résultat</div><div class="example">{exemple}</div>'
    return out + "</div>"

def mini_prompt(num, title, prompt):
    return (f'<div class="pmini"><div class="ptitle"><span class="pnum">{num}</span>{title}</div>'
            f'<div class="prompt">{prompt}</div></div>')

def checklist(items):
    return '<ul class="check">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def play(exos):
    return ('<div class="play"><div class="pt2">À toi de jouer</div><ol>'
            + "".join(f"<li>{e}</li>" for e in exos) + "</ol></div>")

def pagebreak(): return '<div class="pb"></div>'

def chapter(num, title, tagline, marker=None):
    label = f"CHAPITRE {num}" if isinstance(num, int) else num
    return (f'<section class="open"><div class="o-glow"></div>'
            f'<div class="o-num">{num if isinstance(num,int) else "★"}</div>'
            f'<div class="o-label">{label}</div><h1>{title}</h1>'
            f'<div class="o-rule"></div><p class="o-tag">{tagline}</p></section>')

def divider(label, title, tagline):
    return chapter(label, title, tagline)
