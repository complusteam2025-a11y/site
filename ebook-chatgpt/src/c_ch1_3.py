from lib import *

def ch1():
    o = chapter(1, "COMPRENDRE CHATGPT AVANT DE VOULOIR GAGNER DE L'ARGENT", "Dix minutes pour comprendre l'outil évitent dix heures de mauvais résultats.")
    o += ('<section>' + h2("Comment ça marche, simplement") +
      table(["Notion","Ce que ça veut dire"],[
        ["<strong>Conversation</strong>","Tu écris, il répond, tu corriges, il améliore. Tu peux continuer dans la même discussion."],
        ["<strong>Contexte</strong>","Tout ce que tu as dit plus haut dans la discussion. Plus il est riche, plus les réponses sont adaptées."],
        ["<strong>Prompt</strong>","Ta demande, ton instruction. C'est le texte que tu envoies."],
        ["<strong>Limites</strong>","Il ne connaît pas ta situation exacte, et ses connaissances peuvent être dépassées ou incomplètes."],
        ["<strong>Hallucination</strong>","Quand l'IA invente une information (un chiffre, une loi, une source) avec un ton très sûr."]]) +
      h3("Les erreurs possibles") +
      ul(["Chiffres, dates, lois ou prix inventés ou périmés.","Textes trop « génériques », qui pourraient s'appliquer à n'importe quelle entreprise.","Expressions qui sonnent peu naturelles pour ton public local.","Réponses qui ignorent ta consigne si elle est floue."], "dots") +
      callout("Règle d'or : vérifie avant de livrer", "<p>Tout ce qui est chiffré, juridique, médical, financier ou lié à un nom propre doit être <strong>vérifié par toi</strong> sur une source fiable. Demande aussi à ChatGPT : « Qu'est-ce que tu n'es pas sûr de ce que tu viens d'écrire ? »</p>", "stop", "🛑") +
      '</section>')
    o += ('<section>' + h2("5 erreurs des débutants") +
      table(["Erreur","Pourquoi c'est un problème","Que faire à la place"],[
        ["<strong>1. Prompt trop court</strong>","Réponse vague et générique","Donne contexte, cible, objectif et format"],
        ["<strong>2. Copier-coller sans relire</strong>","Erreurs, ton impersonnel, risque de faux","Relis, corrige, ajoute tes détails réels"],
        ["<strong>3. Tout croire</strong>","Les hallucinations existent","Vérifie chiffres, lois et noms propres"],
        ["<strong>4. S'arrêter à la 1re réponse</strong>","Le premier jet est rarement le meilleur","Demande : plus court, plus direct, 3 variantes"],
        ["<strong>5. Chercher un « truc magique »</strong>","On ne vend pas un outil, on vend un résultat","Choisis un service et un client précis"]]) +
      h2("Le principe du bon prompt") +
      p("Un bon prompt répond à cinq questions. Retiens cette formule :") +
      '<div class="formula">CONTEXTE <span>+</span> OBJECTIF <span>+</span> RÔLE <span>+</span> CONTRAINTES <span>+</span> FORMAT ATTENDU</div>' +
      '<div class="grid2"><div class="card"><b>Contexte</b>Qui tu es, pour qui, dans quelle situation.</div><div class="card"><b>Objectif</b>Ce que tu veux obtenir exactement.</div>' +
      '<div class="card"><b>Rôle</b>« Agis comme un community manager expérimenté… »</div><div class="card"><b>Contraintes</b>Ton, longueur, mots à éviter, langue.</div></div>' +
      '<div class="card"><b>Format attendu</b>Liste, tableau, message WhatsApp de 5 lignes, script de 30 secondes…</div>' +
      '</section>')
    o += ('<section>' + h2("5 exemples avant / après") +
      table(["Avant (faible)","Après (efficace)"],[
        ["« Fais un post pour ma boutique »","« Je tiens une boutique de vêtements à Douala. Écris un post Facebook pour annoncer l'arrivée de robes en wax, cible : femmes de 20–35 ans. Ton chaleureux, 80 mots max, avec appel à écrire sur WhatsApp. »"],
        ["« Aide-moi à vendre »","« Agis comme un conseiller commercial. Je vends des téléphones d'occasion reconditionnés à Yaoundé. Propose 5 arguments honnêtes face à un client qui hésite à cause de la garantie. Format : liste courte. »"],
        ["« Écris une vidéo TikTok »","« Écris un script TikTok de 30 secondes pour une coiffeuse de Bafoussam qui propose des tresses à domicile. Accroche forte dans les 3 premières secondes, langage simple, fin avec appel à réserver. »"],
        ["« Corrige mon texte »","« Corrige l'orthographe et rends ce message plus clair et poli pour un client professionnel. Garde le sens et mon ton direct. Ne rajoute aucune information. Texte : [colle ton texte] »"],
        ["« Je veux apprendre le marketing »","« Je suis étudiant, 1 h par jour. Crée un plan de 14 jours pour apprendre les bases du marketing sur les réseaux sociaux, avec un mini-exercice par jour à faire sur mon téléphone. »"]]) +
      callout("Astuce", "<p>Termine souvent par : « <strong>Pose-moi d'abord 3 questions si tu manques d'informations.</strong> » Tu obtiendras des réponses plus justes.</p>", "ok", "✨") +
      play(["Écris un prompt « avant » pour une tâche réelle de ta semaine, puis réécris-le avec la formule des 5 éléments.",
            "Teste les deux versions et compare les réponses : note 3 différences.",
            "Demande à ChatGPT de te poser 3 questions pour améliorer ton prompt.",
            "Repère une information dans une réponse et vérifie-la sur une autre source."]) +
      '</section>')
    return o

def ch2():
    o = chapter(2, "10 FAÇONS DE MONÉTISER UNE COMPÉTENCE AVEC L'AIDE DE CHATGPT", "Dix pistes réalistes. Pas des promesses : des points de départ à tester.")
    o += ('<section>' + callout("À lire avant", "<p>Les prix ci-dessous sont des <strong>exemples indicatifs en FCFA</strong>. Ils ne sont ni garantis ni universels : ils dépendent de ta ville, de ton niveau, de ta cible et de la qualité de ton travail. Commence par tester, puis ajuste.</p>", "warn", "⚠️"))
    def fiche(n, titre, vend, a_qui, gpt, humain, offre, prix):
        return ('<div class="pblock" style="break-inside:avoid"><div class="ptitle"><span class="pnum">'+str(n)+'</span>'+titre+'</div>'
          '<table style="margin:0"><tbody>'
          f'<tr><td style="width:27%"><strong>Ce qu\'on vend</strong></td><td>{vend}</td></tr>'
          f'<tr><td><strong>À qui</strong></td><td>{a_qui}</td></tr>'
          f'<tr><td><strong>ChatGPT aide à</strong></td><td>{gpt}</td></tr>'
          f'<tr><td><strong>L\'humain contrôle</strong></td><td>{humain}</td></tr>'
          f'<tr><td><strong>Exemple d\'offre</strong></td><td>{offre}</td></tr>'
          f'<tr><td><strong>Prix indicatif</strong></td><td><strong>{prix}</strong></td></tr></tbody></table></div>')
    o += fiche(1,"Rédaction web","Articles de blog, pages de site, textes de présentation","PME, écoles, cabinets, boutiques en ligne","Plan, premier jet, reformulation, titres","Exactitude, ton, SEO de base, relecture complète","Pack 3 articles de 500 mots, livrés en 5 jours","3 000 à 10 000 FCFA par article")
    o += fiche(2,"Copywriting","Textes qui donnent envie d'acheter : pubs, pages de vente, emails","Vendeurs en ligne, formateurs, restaurants","Variantes d'accroches, structures de vente","Promesses honnêtes, adaptation locale, preuve réelle","Texte de vente pour une formation + 2 variantes d'accroche","10 000 à 40 000 FCFA selon la longueur")
    o += fiche(3,"Création de contenu","Idées, scripts et textes pour réseaux sociaux","Coachs, marques locales, églises, artistes","Idées de sujets, scripts, légendes","Authenticité, cohérence de marque, images réelles","Pack 12 posts + 4 scripts TikTok / mois","15 000 à 50 000 FCFA / mois")
    o += fiche(4,"Community management","Gestion régulière d'une page Facebook, Instagram ou TikTok","Boutiques, salons, restaurants, PME","Calendrier éditorial, posts, réponses types","Calendrier, validation client, modération, créativité","Gestion de 1 page : 12 publications + réponses messages","20 000 à 60 000 FCFA / mois")
    o += '</section><section>'
    o += fiche(5,"Création de fiches produits","Descriptions claires et vendeuses pour catalogues et boutiques en ligne","Vendeurs WhatsApp, boutiques Facebook, e-commerçants","Rédaction en série, variantes, mise en forme","Caractéristiques exactes (taille, prix, matière), orthographe","Pack 20 fiches produits, livrées en 48 h","500 à 1 500 FCFA par fiche")
    o += fiche(6,"Assistance virtuelle","Aide administrative à distance : emails, tableaux, organisation","Entrepreneurs, consultants, cabinets","Modèles d'emails, résumés, plannings","Confidentialité, exactitude, respect des délais","Gestion d'agenda et emails, 5 h par semaine","15 000 à 50 000 FCFA / mois")
    o += fiche(7,"Service client","Réponses types, scripts, FAQ pour répondre vite et bien","Boutiques, écoles, agences de voyage","Rédaction de réponses, FAQ, ton poli","Informations réelles, politique de l'entreprise, cas sensibles","Pack « 30 réponses types WhatsApp » + FAQ","10 000 à 30 000 FCFA")
    o += fiche(8,"Traduction et adaptation","Traduction FR ⇄ EN et adaptation de ton selon le public","Entrepreneurs, ONG, artisans qui visent l'export","Traduction brute, variantes de ton","Sens exact, termes techniques, relecture par une personne qui maîtrise la langue","Traduction de 5 pages + version adaptée réseaux sociaux","2 000 à 6 000 FCFA par page")
    o += '</section><section>'
    o += fiche(9,"CV et lettres de motivation","Documents clairs, adaptés au poste visé","Étudiants, jeunes diplômés, personnes en reconversion","Structure, reformulation, mots-clés du poste","Vérité absolue des informations, mise en page","CV 1 page + lettre de motivation adaptée à une offre","2 000 à 7 000 FCFA le pack")
    o += fiche(10,"Supports marketing","Flyers (textes), brochures, présentations, catalogues","Commerces, écoles, événements, associations","Textes, structure, slogans, idées de sections","Cohérence visuelle, infos de contact, validation","Brochure de 4 pages (textes) + 3 slogans","10 000 à 35 000 FCFA")
    o += callout("Comment choisir ?", "<p>Prends la piste qui combine : <strong>(1)</strong> ce que tu sais déjà faire un peu, <strong>(2)</strong> ce que des gens autour de toi cherchent, <strong>(3)</strong> ce que tu as envie d'améliorer. Commence par <strong>une seule</strong> piste.</p>", "info", "🧭")
    o += play(["Note les 10 pistes de 1 à 5 selon ton intérêt et ta facilité actuelle.",
               "Garde les 2 meilleures et liste 5 personnes autour de toi qui pourraient en avoir besoin.",
               "Demande à ChatGPT de te proposer 3 variantes de mini-offre pour chacune.",
               "Choisis UNE piste pour les 30 prochains jours."])
    o += '</section>'
    return o

def ch3():
    o = chapter(3, "CRÉER SA PREMIÈRE OFFRE", "Une compétence ne se vend pas. Une solution claire à un problème précis, si.")
    o += ('<section>' + h2("Les 7 étapes pour transformer une compétence en offre") +
      table(["Étape","Question à te poser","Exemple"],[
        ["<strong>1. Compétence</strong>","Qu'est-ce que je sais faire, même un peu ?","Écrire des textes clairs"],
        ["<strong>2. Problème</strong>","Quel problème concret cela résout-il ?","Les vendeurs WhatsApp écrivent des descriptions peu attractives"],
        ["<strong>3. Cible</strong>","Qui précisément a ce problème ?","Vendeuses de vêtements à Douala sur WhatsApp / Facebook"],
        ["<strong>4. Solution</strong>","Comment je le résous, étape par étape ?","Je rédige des fiches produits prêtes à publier"],
        ["<strong>5. Livrables</strong>","Qu'est-ce que le client reçoit, exactement ?","20 fiches en document Word + 5 légendes"],
        ["<strong>6. Prix</strong>","Combien ça vaut pour lui ? Combien de temps pour moi ?","Prix de lancement, puis ajustement"],
        ["<strong>7. Présentation</strong>","Comment l'expliquer en 5 lignes ?","Message WhatsApp + une page PDF"]]) +
      callout("Comment fixer un premier prix", "<p>Estime ton temps de travail (avec ChatGPT) et la valeur pour le client. Pour tes premiers clients, un <strong>prix de lancement</strong> honnête est possible, mais ne travaille pas gratuitement sans limites : définis toujours un cadre (livrables, délai, nombre de modifications).</p>", "warn", "💰") +
      h2("Exercice : construis ton offre en 15 minutes") +
      p("Remplis ce modèle. Écris court, concret, sans jargon.") +
      '<div class="form"><div>Je cible : <span>__________________________</span></div><div>Mon client a ce problème : <span>__________________</span></div><div>Je lui propose : <span>__________________________</span></div><div>Je vais lui livrer : <span>__________________________</span></div><div>Délai : <span>__________</span></div><div>Prix : <span>__________ FCFA</span></div><div>Résultat attendu : <span>_____________________</span></div></div>' +
      '</section>')
    o += ('<section>' + h2("Exemple rempli") +
      '<div class="form"><div>Je cible : <span style="color:#1b2236">les petites boutiques de vêtements sur WhatsApp à Douala</span></div>'
      '<div>Mon client a ce problème : <span style="color:#1b2236">ses descriptions de produits sont courtes et il perd des clients</span></div>'
      '<div>Je lui propose : <span style="color:#1b2236">des fiches produits claires, prêtes à copier-coller</span></div>'
      '<div>Je vais lui livrer : <span style="color:#1b2236">20 fiches + 5 phrases d\'accroche</span></div>'
      '<div>Délai : <span style="color:#1b2236">48 heures</span></div>'
      '<div>Prix : <span style="color:#1b2236">à fixer selon ton marché (ex. 10 000 FCFA de lancement)</span></div>'
      '<div>Résultat attendu : <span style="color:#1b2236">des annonces plus claires, plus de messages de clients intéressés (sans garantie de ventes)</span></div></div>' +
      mini_prompt("P","Prompt pour affiner ton offre",
        "Agis comme un consultant en freelancing pour débutants en Afrique francophone.\nVoici mon offre : [colle ton modèle rempli].\nTâche : 1) dis-moi ce qui est flou, 2) propose 3 façons de la rendre plus claire, 3) suggère un nom simple pour cette offre, 4) rédige une présentation de 5 lignes pour WhatsApp.\nContraintes : langage simple, pas de promesses de résultats garantis.") +
      mini_prompt("P","Prompt pour tester ton prix",
        "Je propose [service] à [cible] à [prix] FCFA. Liste les arguments qu'un client pourrait avoir pour dire que c'est trop cher ou trop bon marché, puis propose 3 façons de structurer l'offre (basique, standard, complète) avec livrables et délais.") +
      h2("Le pack à 3 niveaux") +
      table(["Niveau","Contenu","Pour qui"],[["Essentiel","1 livrable simple, 1 correction","Client qui teste"],["Standard","Livrables complets + 2 corrections","Cas le plus courant"],["Premium","Livrables + suivi + bonus","Client régulier"]]) +
      play(["Remplis le modèle avec une vraie compétence.","Utilise les prompts pour obtenir une version plus claire.","Montre ton offre à une personne de confiance : comprend-elle en 20 secondes ?","Crée trois niveaux de prix pour ton offre."]) +
      '</section>')
    return o
