from lib import *

def cover():
    # Illustration conceptuelle : réseau de neurones + puce, sobre
    nodes = [(95,52),(118,70),(76,76),(104,98),(126,112),(84,118),(112,134),(70,140),(98,152),(122,166)]
    nodes = [(x, int(y*.75+36)) for x,y in nodes]
    edges = [(0,1),(0,2),(1,3),(2,3),(3,4),(2,5),(3,5),(4,6),(5,6),(5,7),(6,8),(7,8),(8,9),(6,9)]
    s = '<svg viewBox="0 0 148 210" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg"><defs><radialGradient id="g" cx="75%" cy="45%" r="50%"><stop offset="0" stop-color="#4670ff" stop-opacity=".55"/><stop offset="1" stop-color="#4670ff" stop-opacity="0"/></radialGradient></defs>'
    s += '<rect width="148" height="210" fill="url(#g)"/>'
    for gx in range(0,148,12): s += f'<line x1="{gx}" y1="0" x2="{gx}" y2="210" stroke="#fff" stroke-opacity=".035"/>'
    for gy in range(0,210,12): s += f'<line x1="0" y1="{gy}" x2="148" y2="{gy}" stroke="#fff" stroke-opacity=".035"/>'
    for a,b in edges:
        s += f'<line x1="{nodes[a][0]}" y1="{nodes[a][1]+14}" x2="{nodes[b][0]}" y2="{nodes[b][1]+14}" stroke="#7d9bff" stroke-opacity=".55" stroke-width=".4"/>'
    for i,(x,y) in enumerate(nodes):
        c = "#f5b81c" if i in (0,4,8) else "#9fb4ff"
        r = 3 if i in (0,4,8) else 2
        s += f'<circle cx="{x}" cy="{y+14}" r="{r+3}" fill="{c}" fill-opacity=".15"/><circle cx="{x}" cy="{y+14}" r="{r}" fill="{c}"/>'
    # puce IA
    s += '<g transform="translate(88 108)" opacity=".9"><rect x="0" y="0" width="30" height="30" rx="4" fill="#0c1840" stroke="#f5b81c" stroke-width=".7"/>'
    for k in range(5):
        s += f'<line x1="{5+k*5}" y1="-4" x2="{5+k*5}" y2="0" stroke="#f5b81c" stroke-width=".6"/><line x1="{5+k*5}" y1="30" x2="{5+k*5}" y2="34" stroke="#f5b81c" stroke-width=".6"/>'
    s += '<text x="15" y="19" text-anchor="middle" font-size="10" font-weight="800" fill="#f5b81c" font-family="Liberation Sans,Arial">IA</text></g>'
    s += '</svg>'
    return (f'<section class="cover">{s}<div class="ct1"><div class="kick">GUIDE PRATIQUE · ÉDITION AFRIQUE FRANCOPHONE</div>'
            '<h1>CHATGPT<br>POUR GAGNER<br><em>DE L\'ARGENT</em></h1>'
            '<div class="sub">50+ prompts et méthodes pour transformer ChatGPT en assistant de travail</div></div>'
            '<div class="hook">Apprends à utiliser l\'IA pour créer plus vite, vendre tes compétences et développer ton activité.'
            '<small>PROMPTS PRÊTS À COPIER · SCRIPTS WHATSAPP · PLAN D\'ACTION 30 JOURS</small></div></section>')

def titlepage():
    return ('<section class="titlepage"><div class="k">LE GUIDE PRATIQUE</div>'
            '<h1>CHATGPT<br>POUR GAGNER<br><em>DE L\'ARGENT</em></h1>'
            '<div class="s">Le guide pratique pour utiliser l\'intelligence artificielle afin de développer ses compétences, créer des services et trouver ses premiers clients</div>'
            '<div class="auth">Édition numérique · Version 1.0</div></section>')

def legal():
    return ('<section class="legal"><div class="pb">' + h2("Avant de commencer : à lire absolument") +
      p("Ce guide est <strong>éducatif</strong>. Il t'explique comment utiliser ChatGPT comme un assistant de travail. Il ne garantit <strong>aucun revenu</strong>, aucun résultat et aucun délai pour trouver des clients.") +
      p("Les prix en FCFA donnés dans le livre sont des <strong>ordres de grandeur indicatifs</strong>. Ils varient selon ta ville, ta niche, ton niveau, la qualité de ton travail et le budget de tes clients. À toi de les adapter.") +
      p("ChatGPT peut se tromper. Tu restes <strong>responsable</strong> de tout ce que tu livres : relis, vérifie, corrige. N'écris jamais de fausses informations sur ton expérience et ne partage pas de données privées de tes clients dans un outil d'IA sans leur accord.") +
      p("Les interfaces et fonctionnalités de ChatGPT évoluent régulièrement. Les prompts de ce livre fonctionnent avec la logique de conversation : si un bouton change de place, la méthode reste la même.") +
      p("ChatGPT est une marque d'OpenAI. Cet ouvrage est indépendant et n'est pas affilié à OpenAI.") +
      callout("Comment utiliser les prompts", "<p>Les blocs sombres sont à <strong>copier-coller</strong>. Remplace tout ce qui est entre [crochets] par tes propres informations. Plus tu donnes de détails, meilleure sera la réponse.</p>", "info", "📋") +
      '</div></section>')

def toc(rows):
    out = '<section class="toc"><h1>Sommaire</h1>'
    for r in rows:
        if r[0] == "sec":
            out += f'<div class="sec">{r[1]}</div>'
        else:
            out += f'<div class="row"><span class="n">{r[0]}</span><span class="t">{r[1]}</span><span class="pg">{r[2]}</span></div>'
    return out + '</section>'

def avant_propos():
    return ('<section><div class="page-title"><small>AVANT-PROPOS</small>L\'IA change la façon de travailler</div>' +
      p("Il y a encore peu de temps, rédiger un texte de vente, préparer un calendrier de publications ou répondre proprement à vingt clients prenait des heures. Aujourd'hui, un outil comme <strong>ChatGPT</strong> peut produire un premier jet en quelques secondes.") +
      p("Cela ne veut pas dire que le travail se fait tout seul. Cela veut dire que <strong>celui qui sait bien utiliser l'outil avance plus vite</strong> que celui qui travaille entièrement à la main.") +
      h3("ChatGPT, un assistant pour de nombreuses tâches") +
      '<div class="grid2">' +
      '<div class="card"><b>✍️ Rédaction</b>Posts, articles, emails, descriptions, scripts.</div>' +
      '<div class="card"><b>💡 Idées</b>Noms, angles, thèmes, offres, slogans.</div>' +
      '<div class="card"><b>🗂️ Organisation</b>Plannings, checklists, priorités, comptes rendus.</div>' +
      '<div class="card"><b>📣 Marketing</b>Publicités, calendriers, messages de vente.</div>' +
      '<div class="card"><b>🎧 Service client</b>Réponses types, gestion des objections.</div>' +
      '<div class="card"><b>🎬 Contenu</b>Scripts TikTok, carrousels, légendes.</div>' +
      '<div class="card"><b>🤝 Préparation commerciale</b>Offres, propositions, relances.</div>' +
      '<div class="card"><b>🎓 Apprentissage</b>Explications simples, quiz, plans d\'étude.</div></div>' +
      quote("Le but n'est pas de remplacer tes compétences par l'IA, mais d'utiliser l'IA pour augmenter tes capacités.") +
      callout("Ce que ce livre ne promet pas", "<p>Pas de « devenir riche en 7 jours ». Pas de revenus garantis. ChatGPT est un outil : l'argent vient de la <strong>valeur que tu crées</strong>, de tes compétences, de la qualité de ton travail et de ta capacité à trouver des clients.</p>", "warn", "⚠️") +
      '</section>')

def intro():
    return ('<section><div class="page-title"><small>INTRODUCTION</small>Tu n\'as pas besoin d\'être expert en IA pour commencer</div>' +
      h2("C'est quoi, ChatGPT ?") +
      p("ChatGPT est un assistant conversationnel : tu lui écris une demande en français (ou dans une autre langue), il te répond par écrit. Tu peux l'utiliser sur smartphone ou sur ordinateur, avec une connexion internet.") +
      p("Il a été entraîné sur une énorme quantité de textes. Il ne « réfléchit » pas comme un humain : il produit des réponses probables à partir de ce que tu lui demandes. D'où l'importance de <strong>bien demander</strong>.") +
      '<div class="grid2"><div class="card"><b>✅ Ce qu\'il peut faire</b>Rédiger, reformuler, résumer, traduire, proposer des idées, structurer un plan, expliquer simplement, simuler un client, corriger un texte.</div>' +
      '<div class="card"><b>🚫 Ce qu\'il ne peut pas faire</b>Connaître ton marché local mieux que toi, garantir des résultats, remplacer ton jugement, toujours dire la vérité, encaisser un client à ta place.</div></div>' +
      h2("Pourquoi savoir demander change tout") +
      p("Deux personnes ouvrent ChatGPT. La première écrit : « Fais-moi un post ». La seconde explique son activité, sa cible, le ton voulu et le format. La seconde obtient un texte utilisable ; la première, un texte générique que personne n'a envie de lire.") +
      p("Une personne qui a <strong>une compétence + ChatGPT</strong> produit plus vite, propose plus d'options et peut consacrer son temps à ce qui compte : comprendre le client et soigner le résultat.") +
      '<div class="formula">COMPÉTENCE <span>+</span> CHATGPT <span>+</span> PROBLÈME À RÉSOUDRE<br><span>=</span> SERVICE POTENTIELLEMENT VENDABLE</div>' +
      h2("5 exemples concrets") +
      table(["Combinaison","Problème résolu","Service possible"],[
        ["<strong>1. Rédaction + ChatGPT</strong>","Un commerçant n'a pas le temps d'écrire ses textes","Fiches produits et textes de vente"],
        ["<strong>2. Community management + ChatGPT</strong>","Une boutique publie de façon irrégulière","Calendrier et posts Facebook / TikTok"],
        ["<strong>3. Traduction + ChatGPT</strong>","Un entrepreneur veut parler à des clients anglophones","Traduction et adaptation de supports"],
        ["<strong>4. Service client + ChatGPT</strong>","Les messages WhatsApp restent sans réponse claire","Réponses types et scripts de vente"],
        ["<strong>5. Création de contenu + ChatGPT</strong>","Un coach manque d'idées de vidéos","Scripts courts et idées de contenu"]]) +
      callout("Retiens bien", "<p>ChatGPT accélère. Mais c'est toi qui apportes le <strong>contexte local</strong>, le <strong>goût</strong> et la <strong>relation avec le client</strong>. C'est là que se trouve ta valeur.</p>", "info", "🎯") +
      '</section>')
