from lib import *

def flow(*steps):
    return '<div class="flow">' + "<i>→</i>".join(f"<span>{s}</span>" for s in steps) + '</div>'

def ch7():
    o = chapter(7, "UTILISER CHATGPT POUR GAGNER DU TEMPS", "Un workflow, c'est une suite d'étapes que tu répètes. Écris-la une fois, utilise-la cent fois.")
    o += ('<section>' + p("Gagner du temps ne veut pas dire bâcler. Cela veut dire <strong>automatiser les premiers jets</strong> pour consacrer plus d'énergie à la vérification et à la relation client.") +
      h2("Workflow 1 : de l'idée à la publication") + flow("Idée","ChatGPT","Contenu","Correction","Publication") +
      ul(["<strong>Idée</strong> : choisis un sujet utile à ta cible.","<strong>ChatGPT</strong> : génère 2 versions avec le prompt adapté.","<strong>Contenu</strong> : garde la meilleure, ajoute un détail réel.","<strong>Correction</strong> : relis à voix haute, corrige faits et orthographe.","<strong>Publication</strong> : publie, puis note les réactions."], "dots") +
      h2("Workflow 2 : du prospect à la relance") + flow("Prospect","Analyse","Proposition","Relance") +
      ul(["<strong>Analyse</strong> : note ce que tu sais du prospect (activité, besoins visibles).","<strong>Proposition</strong> : génère une proposition courte et personnalisée.","<strong>Relance</strong> : programme tes relances (24 h, 3 jours, 7 jours)."], "dots") +
      h2("Workflow 3 : du produit à la vente") + flow("Produit","Description","Publication","WhatsApp","Vente") +
      ul(["Prends 3 photos claires et note les caractéristiques exactes.","Génère description et version courte WhatsApp.","Publie sur Facebook et en statut, réponds aux questions.","Prépare tes réponses types (prix, livraison, paiement)."], "dots") +
      h2("Workflow 4 : du brief à la livraison") + flow("Client","Brief","Production","Vérification","Livraison") +
      ul(["<strong>Brief</strong> : pose 5 questions au client avant de commencer.","<strong>Production</strong> : génère un premier jet avec le prompt adapté.","<strong>Vérification</strong> : checklist qualité (faits, ton, fautes, cohérence).","<strong>Livraison</strong> : envoie propre, avec un message clair."], "dots") +
      '</section>')
    o += ('<section>' + h2("Tableau : combien de temps peut-on gagner ?") +
      table(["Tâche","Sans IA","Avec IA","Gain potentiel de temps"],[
        ["Écrire 10 fiches produits","2 h 30","1 h","≈ 60 %"],
        ["Plan de 4 semaines de contenu","2 h","30–40 min","≈ 70 %"],
        ["Rédiger un article de 500 mots","1 h 30","45 min","≈ 50 %"],
        ["Répondre à 10 questions fréquentes","1 h","20 min","≈ 65 %"],
        ["Préparer une proposition commerciale","1 h","25 min","≈ 60 %"],
        ["Traduire et adapter 2 pages","1 h 30","50 min","≈ 45 %"],
        ["Résumer un document de 10 pages","40 min","10 min","≈ 75 %"]]) +
      callout("Attention", "<p>Ces chiffres sont des <strong>estimations indicatives</strong>. Ton gain réel dépendra de ton niveau, de ta connexion et de la qualité de tes prompts. Les étapes de vérification restent obligatoires et prennent du temps.</p>", "warn", "⏱️") +
      mini_prompt("P","Prompt pour créer ton propre workflow",
        "Je fais le service suivant : <b>[service]</b>. Décris mon processus actuel en étapes : <b>[étapes]</b>. Propose un workflow optimisé avec ChatGPT : pour chaque étape, dis ce que ChatGPT peut faire, ce que je dois vérifier, le prompt à utiliser, et le temps estimé. Format : tableau.") +
      mini_prompt("P","Prompt « brief client »",
        "Je dois réaliser <b>[service]</b> pour un client. Rédige 8 questions de brief (objectif, cible, ton, contenu à inclure, délai, budget, exemples aimés, contraintes). Formule-les de façon simple pour un entrepreneur débutant, en message WhatsApp.") +
      callout("Checklist qualité avant livraison", checklist(["Faits et chiffres vérifiés","Orthographe relue","Ton cohérent avec le client","Informations de contact correctes","Format demandé respecté"]), "ok", "✅") +
      play(["Écris le workflow de ton service en 5 étapes maximum.","Chronomètre une tâche faite à la main puis avec ChatGPT : note la différence.","Crée ta checklist qualité personnelle.","Garde tes meilleurs prompts dans un document ou dans les notes de ton téléphone."]) +
      '</section>')
    return o

def ch8():
    o = chapter(8, "CRÉER SON PORTFOLIO MÊME SANS EXPÉRIENCE", "Un portfolio honnête montre ce que tu sais faire, pas ce que tu prétends avoir fait.")
    o += ('<section>' + callout("Règle d'honnêteté", "<p>Tu peux créer des <strong>exemples personnels ou fictifs</strong>, à condition de les <strong>indiquer clairement</strong> : « Exemple fictif créé pour démontrer ma méthode ». Ne prétends jamais avoir travaillé pour une marque ou une personne qui n'a pas été ton client.</p>", "stop", "🛑") +
      h2("Les 5 éléments d'un portfolio simple") +
      table(["Élément","Contenu","Format"],[
        ["<strong>Présentation personnelle</strong>","Qui tu es, ce que tu fais, pour qui","5 lignes + photo"],
        ["<strong>Exemples de travaux</strong>","3 à 5 réalisations (personnelles ou fictives, indiquées)","Images / texte"],
        ["<strong>Étude de cas fictive</strong>","Situation → méthode → résultat visé, marquée « fictive »","1 page"],
        ["<strong>Offre commerciale</strong>","Ce que tu proposes, livrables, délai, prix","1 page PDF"],
        ["<strong>Contact</strong>","WhatsApp, email, réseau social","Lien clair"]]) +
      h3("Où le publier ?") +
      p("Un document PDF partageable sur WhatsApp, une page Facebook, un profil LinkedIn, ou un dossier Google Drive / Canva. Choisis le plus simple à partager.") +
      h2("Idées d'exemples sans client") +
      ul(["Rédige les textes d'une boutique fictive (clairement indiquée).","Améliore l'annonce d'une entreprise connue <strong>en tant qu'exercice personnel</strong> (sans prétendre être son prestataire).","Crée un calendrier éditorial pour un type de commerce (ex. salon de coiffure).","Aide gratuitement une personne proche, avec son accord, et documente le résultat."], "dots") +
      '</section>')
    o += ('<section>' + h2("Modèle d'étude de cas fictive") +
      '<div class="form"><div>⚠️ Étude de cas fictive <span>(créée pour démontrer ma méthode)</span></div><div>Contexte : <span>Boutique de vêtements imaginaire à Douala</span></div><div>Problème : <span>Descriptions courtes, peu de réponses</span></div><div>Ce que j\'ai fait : <span>Fiches claires, calendrier de 4 semaines</span></div><div>Résultat visé : <span>Messages plus précis des clients, annonces plus claires</span></div></div>' +
      h2("4 prompts pour ton portfolio") +
      prompt_box(1,"Créer ton profil",
        "Aide-moi à rédiger ma bio professionnelle (5 lignes) pour WhatsApp et Facebook.\nMon activité : <b>[activité]</b>. Ma cible : <b>[cible]</b>. Mes compétences réelles : <b>[liste]</b>. Mon expérience : <b>[expérience vraie, même petite]</b>.\nStyle : simple, honnête, sans exagération. N'invente aucune expérience.") +
      prompt_box(2,"Présenter tes compétences",
        "Voici mes compétences : <b>[liste]</b>. Pour chacune, écris une phrase qui explique le bénéfice pour un client (ex. « Je rédige des textes clairs pour que vos clients comprennent vite »). Ajoute 3 exemples de livrables que je peux proposer.") +
      prompt_box(3,"Structurer ton portfolio",
        "Propose la structure d'un portfolio d'une page pour <b>[activité]</b> : titres, ordre des sections, texte d'introduction. J'ai : <b>[ce que tu as déjà]</b>. Indique ce qu'il me manque et comment le créer honnêtement (exemples fictifs clairement indiqués).") +
      prompt_box(4,"Rédiger ta proposition commerciale",
        "Rédige une page de proposition commerciale pour mon offre <b>[offre]</b> : à qui elle s'adresse, ce que je livre, délai, prix <b>[prix]</b> FCFA, déroulement en 3 étapes, modalités. Ton professionnel et simple. N'ajoute aucune référence client inventée.") +
      play(["Écris ta bio avec le prompt 1 puis adapte-la avec tes mots.","Crée 3 exemples de travaux (personnels ou fictifs, avec mention claire).","Rédige une étude de cas fictive d'une page.","Assemble le tout dans un PDF simple et envoie-le à une personne de confiance pour avis."]) +
      '</section>')
    return o

def ch9():
    o = chapter(9, "DEVENIR PLUS PRODUCTIF AVEC CHATGPT", "La productivité n'est pas faire plus de choses : c'est faire les bonnes, dans le bon ordre.")
    o += ('<section>' + h2("Ton système personnel : matin, journée, soir") +
      '<div class="grid2"><div class="card"><b>🌅 MATIN : planification (10 min)</b>Objectif du jour, 3 priorités, créneaux de travail.</div><div class="card"><b>⚡ JOURNÉE : production</b>Travail en blocs de 45 min, prompts préparés, pauses courtes.</div></div><div class="card"><b>🌙 SOIR : analyse (10 min)</b>Ce qui a marché, ce qui bloque, ce que je prépare pour demain.</div>' +
      h2("8 prompts de productivité") +
      mini_prompt(1,"Organiser sa journée","Je dispose de <b>[X heures]</b> aujourd'hui. Mes tâches : <b>[liste]</b>. Contraintes : <b>[coupures de courant, connexion, trajets…]</b>. Crée un planning réaliste avec des blocs de 45 minutes et des pauses. Signale ce qui devrait être reporté.") +
      mini_prompt(2,"Établir ses priorités","Voici mes tâches : <b>[liste]</b>. Classe-les avec la méthode importance/urgence. Dis-moi les 3 à faire en premier, celles à déléguer ou reporter, et pourquoi.") +
      mini_prompt(3,"Créer une checklist","Crée une checklist détaillée pour <b>[tâche ou projet]</b>. Découpe en étapes, du début à la fin, avec une estimation de temps pour chacune. Format : cases à cocher.") +
      '</section><section>' +
      mini_prompt(4,"Analyser son travail","Voici ce que j'ai fait cette semaine : <b>[liste]</b>, et voici mes résultats : <b>[résultats]</b>. Analyse honnêtement : 3 points forts, 3 points à améliorer, 1 changement à tester la semaine prochaine. Ne me flatte pas.") +
      mini_prompt(5,"Préparer une réunion","Je prépare une réunion avec <b>[personne/client]</b> pour <b>[objet]</b>. Propose : un ordre du jour de 20 minutes, 8 questions à poser, les objections probables, et un message de compte rendu à envoyer après.") +
      mini_prompt(6,"Prendre des notes","Voici mes notes brutes de réunion : <b>[notes]</b>. Organise-les en : décisions, actions à faire (qui, quoi, quand), questions en suspens. Format court.") +
      mini_prompt(7,"Résumer un document","Résume le texte suivant en 10 lignes, puis en 3 idées clés, puis liste 3 questions que je devrais me poser. Si tu n'es pas sûr d'une information, signale-le. Texte : <b>[colle ton texte]</b>") +
      mini_prompt(8,"Apprendre une nouvelle compétence","Je veux apprendre <b>[compétence]</b>. Mon niveau : <b>[débutant]</b>, temps disponible : <b>[30 min/jour]</b>, matériel : smartphone. Crée un plan de 14 jours avec un mini-exercice par jour, un quiz à la fin de chaque semaine et des ressources à vérifier par moi-même.") +
      callout("Garde un carnet de prompts", "<p>Crée un document « Mes meilleurs prompts » : date, usage, prompt, résultat. En 30 jours, tu auras ta bibliothèque personnelle, bien plus utile que n'importe quelle liste générique.</p>", "info", "📓") +
      play(["Fais ta planification du matin avec le prompt 1 pendant 3 jours.","Termine chaque journée par une analyse de 5 lignes.","Résume un document ou une leçon avec le prompt 7.","Démarre ton carnet de prompts."]) +
      '</section>')
    return o

def ch10():
    o = chapter(10, "TON PLAN POUR PASSER À L'ACTION", "Un plan simple, sur 30 jours. Pas parfait : réalisable.")
    o += ('<section>' + callout("Avant de commencer", "<p>Ce plan est une <strong>trame</strong>. Il ne garantit pas de clients en 30 jours. Il t'assure en revanche d'avoir, à la fin : une offre claire, un portfolio, une habitude de prospection et des retours réels pour t'améliorer.</p>", "warn", "📅") +
      table(["Jours","Objectif","Actions concrètes","Livrable"],[
        ["<strong>1–3</strong>","Identifier sa compétence","Liste de 10 choses que tu sais faire ; choisis-en 1 ; demande l'avis de 3 proches","Une compétence choisie"],
        ["<strong>4–7</strong>","Choisir sa cible","Définis qui a le problème ; observe 10 pages ou boutiques ; liste 20 prospects","Fiche cible + 20 contacts"],
        ["<strong>8–10</strong>","Créer son offre","Remplis le modèle du chapitre 3 ; fixe 3 niveaux de prix","Offre d'une page"],
        ["<strong>11–15</strong>","Créer son portfolio","3 exemples (mention claire si fictifs) ; bio ; PDF","Portfolio PDF"],
        ["<strong>16–20</strong>","Commencer la prospection","5 messages personnalisés par jour ; suivi dans un tableau","25 à 100 contacts, notés"],
        ["<strong>21–25</strong>","Publier du contenu","1 publication utile par jour (Facebook / TikTok / statut)","5 contenus publiés"],
        ["<strong>26–30</strong>","Analyser, améliorer, relancer","Analyse des réponses ; amélioration de l'offre ; relances polies","Bilan + plan du mois 2"]]) +
      '</section>')
    o += ('<section>' + h2("Checklist quotidienne") +
      checklist(["Planifier ma journée (10 min)","Faire mon action n°1 (la plus importante)","Contacter ou relancer mes prospects du jour","Publier ou préparer un contenu","Utiliser ChatGPT pour 1 tâche précise, puis vérifier","Noter mes résultats dans mon tableau","Écrire 3 lignes de bilan (ce qui a marché, ce qui bloque)"]) +
      h2("Prompt de bilan hebdomadaire") +
      mini_prompt("P","Faire le point chaque dimanche","Voici mon bilan de la semaine : actions faites <b>[actions]</b>, messages envoyés <b>[nombre]</b>, réponses reçues <b>[nombre]</b>, difficultés <b>[difficultés]</b>. Analyse honnêtement ce qui fonctionne et ce qui doit changer. Propose 3 actions précises pour la semaine prochaine et un message type à améliorer.") +
      callout("Quand tu te sens bloqué(e)", "<ul><li>Réduis l'objectif : 2 messages au lieu de 5, mais fais-les.</li><li>Demande l'avis d'une personne de confiance sur ton offre.</li><li>Rappelle-toi : les premiers résultats viennent de la <strong>régularité</strong>, pas de l'inspiration.</li></ul>", "info", "🧭") +
      play(["Imprime ou recopie le plan sur une feuille et affiche-le.","Fixe l'heure précise de ton travail quotidien.","Écris ton objectif du mois (activité, pas revenu garanti).","Commence aujourd'hui avec le jour 1."]) +
      '</section>')
    return o
