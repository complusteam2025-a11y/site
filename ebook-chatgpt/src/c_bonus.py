from lib import *

B = [
("BUSINESS", [
("Valider une idée de service","Agis comme un consultant business. Mon idée de service : <b>[idée]</b>. Cible : <b>[cible]</b>. Liste 5 hypothèses à vérifier, 5 questions à poser à de vrais clients et un test simple à faire en 7 jours avec un budget minimal."),
("Analyser ma niche","Je veux me lancer dans la niche <b>[niche]</b> à <b>[ville/pays]</b>. Décris les problèmes fréquents des clients, ce qui existe déjà, ce qui pourrait me différencier. Indique clairement ce que tu ne peux pas savoir et que je dois vérifier sur le terrain."),
("Définir ma cible idéale","Aide-moi à décrire mon client idéal pour <b>[service]</b> : âge, activité, problèmes, objections, où il passe du temps en ligne. Termine par 5 questions pour valider ces hypothèses auprès de vraies personnes."),
("Construire des niveaux de prix","Mon service : <b>[service]</b>. Propose 3 niveaux (Essentiel, Standard, Premium) avec contenu, délais, nombre de corrections et une fourchette de prix en FCFA à tester. Explique comment ajuster selon les retours."),
("Nommer mon activité","Propose 15 noms simples et faciles à retenir pour une activité de <b>[service]</b> à <b>[ville]</b>. Évite les noms trop compliqués. Pour les 5 meilleurs, ajoute un slogan de 6 mots."),
("Contrat simple de prestation (modèle à faire relire)","Rédige un modèle simple d'accord de prestation en français : parties, description du service, livrables, délai, prix en FCFA, révisions, paiement, confidentialité. Précise que ce modèle doit être relu par un professionnel du droit local."),
("Plan d'affaires en une page","Crée un plan en une page pour mon activité <b>[activité]</b> : problème, solution, cible, offre, prix, canaux d'acquisition, dépenses principales, objectifs de 90 jours. Format tableau court."),
]),
("MARKETING", [
("Message de positionnement","Résume en 2 phrases ce que je fais, pour qui et avec quel bénéfice : <b>[détails]</b>. Donne 3 versions (simple, professionnelle, chaleureuse)."),
("Bio Facebook / Instagram / TikTok","Écris 3 bios de 150 caractères pour <b>[activité]</b>, qui indiquent clairement l'offre et comment me contacter. Ton : <b>[ton]</b>."),
("Slogans","Propose 12 slogans pour <b>[activité]</b>. Ils doivent être courts, vrais, sans promesse irréaliste. Indique les 3 plus mémorables."),
("Idée de campagne locale","Imagine une campagne de 2 semaines pour <b>[activité]</b> dans <b>[ville]</b> avec peu de budget : message, canaux, contenus, actions simples en quartier. Précise ce qui est gratuit et ce qui coûte."),
("Étude de la concurrence","Voici 3 pages concurrentes que je viens d'observer : <b>[mes observations]</b>. Compare leurs messages, leurs offres, leurs points forts et leurs faiblesses visibles, puis propose 3 façons de me différencier. Ne devine pas d'informations privées."),
("Newsletter / message de diffusion","Écris un message de diffusion WhatsApp de 8 lignes pour annoncer <b>[nouveauté]</b> aux clients qui ont accepté de recevoir mes messages. Ton amical. Ajoute une phrase pour se désabonner."),
("Test de messages (A/B)","Écris 2 versions du message <b>[message]</b> à tester. Indique ce qui diffère, quelle métrique observer et comment lire les résultats sans conclure trop vite."),
]),
("CONTENU", [
("Réécrire un texte plus clair","Réécris ce texte en français simple, sans changer le sens, en phrases courtes : <b>[texte]</b>. Propose une version courte et une version détaillée."),
("Résumé en post","Transforme cet article en un post de 120 mots avec 3 idées clés : <b>[texte]</b>."),
("Série de 5 publications","Crée une série de 5 publications connectées sur <b>[thème]</b> pour <b>[cible]</b>, avec un fil conducteur, une accroche différente chaque jour et un appel à l'action unique."),
("Script de vidéo explicative","Écris un script de 60 secondes qui explique <b>[concept]</b> à un débutant, avec une analogie du quotidien africain francophone (marché, transport, cuisine…)."),
("Idées de photos pour un petit budget","Propose 15 idées de photos ou vidéos réalisables avec un smartphone pour <b>[activité]</b> : lumière naturelle, fond simple, mise en scène du produit."),
("Contenu spécial fêtes / événements","Propose 8 idées de contenu pour <b>[événement local]</b> adaptées à <b>[activité]</b>, respectueuses de la culture locale et sans fausse promesse."),
]),
("VENTE", [
("Message d'ouverture à froid (respectueux)","Écris 3 messages d'ouverture polis pour contacter <b>[type d'entreprise]</b> à propos de <b>[service]</b>. Chacun fait 4 lignes max, personnalisable, avec une porte de sortie élégante."),
("Questions de découverte","Liste 10 questions à poser à un prospect avant de proposer un prix pour <b>[service]</b>, classées par thèmes : besoin, budget, délai, décision."),
("Argumentaire en 3 minutes","Prépare un argumentaire oral de 3 minutes pour <b>[service]</b> : accroche, problème, solution, preuve, offre, question de clôture."),
("Négocier sans brader","Un client demande une réduction sur <b>[offre/prix]</b>. Propose 4 réponses qui protègent ma valeur : contreparties, version allégée, paiement en deux fois, et refus poli."),
("Message de clôture","Écris un message pour conclure une vente : récapitulatif, prix, mode de paiement, délai, prochaine étape, remerciement. Max 8 lignes."),
("Offre de réactivation","Rédige un message pour proposer une nouvelle offre à d'anciens clients satisfaits : rappel du travail passé, nouveauté, avantage réel, invitation sans pression."),
]),
("PRODUCTIVITÉ", [
("Plan de semaine","Voici mes objectifs : <b>[objectifs]</b> et mes contraintes : <b>[contraintes]</b>. Crée un plan de semaine réaliste, avec 3 priorités par jour et du temps tampon."),
("Méthode des blocs de 45 minutes","Organise ma journée de travail de <b>[heure]</b> à <b>[heure]</b> en blocs de 45 min avec pauses, en tenant compte de ces tâches : <b>[tâches]</b>."),
("Débloquer une tâche","Je procrastine sur <b>[tâche]</b>. Découpe-la en micro-étapes de 10 minutes maximum et propose la toute première action à faire maintenant."),
("Modèles de réponses emails","Crée 5 modèles d'emails professionnels : demande de rendez-vous, confirmation, relance, remerciement, report. Ton poli et direct."),
("Tableau de suivi clients","Propose la structure d'un tableau de suivi (Google Sheets) pour mes prospects et clients : colonnes, statuts, formules simples, rappels."),
("Bilan de fin de mois","Voici mes chiffres et actions du mois : <b>[données]</b>. Prépare un bilan : réussites, échecs, leçons, 3 objectifs pour le mois suivant."),
]),
("APPRENTISSAGE", [
("Expliquer simplement","Explique-moi <b>[notion]</b> comme si j'avais 15 ans, avec un exemple concret du quotidien africain francophone, puis pose-moi 3 questions pour vérifier ma compréhension."),
("Plan d'étude de 30 jours","Je veux apprendre <b>[compétence]</b> en 30 jours, 30 min par jour. Crée un plan hebdomadaire avec objectifs, exercices pratiques et critères de réussite."),
("Quiz pour réviser","Crée un quiz de 10 questions sur <b>[sujet]</b> avec les réponses à la fin, niveau débutant. Après mes réponses, corrige-moi et explique mes erreurs."),
("Apprendre l'anglais professionnel","Aide-moi à pratiquer l'anglais pour échanger avec des clients : propose 10 phrases utiles, puis fais un jeu de rôle d'une conversation de vente où tu corriges mes fautes."),
("Fiche de révision","Transforme ce cours en fiche de révision d'une page : définitions, points clés, erreurs fréquentes, exemples : <b>[texte]</b>."),
("Trouver un mentor virtuel","Joue le rôle d'un mentor bienveillant mais exigeant en <b>[domaine]</b>. Je te présente mon travail : <b>[travail]</b>. Donne-moi 3 points forts, 3 points à améliorer, et 1 exercice pour progresser."),
]),
("SERVICE CLIENT", [
("Réponses types WhatsApp","Crée 10 réponses types pour <b>[activité]</b> : salutation, horaires, prix, livraison, paiement, retard, remerciement, indisponibilité, absence, fin de conversation. Ton chaleureux, précis."),
("Gérer un retard","Rédige un message pour informer un client d'un retard de livraison : excuses sincères, nouvelle date, proposition de geste commercial raisonnable, remerciement pour sa patience."),
("Message d'absence","Écris 3 messages d'absence automatiques pour WhatsApp Business (soir, week-end, congés), courts et aimables."),
("Collecter un avis","Écris un message simple pour demander un avis à un client satisfait, en proposant de répondre à 2 questions rapides."),
("Refuser poliment une demande","Un client demande <b>[demande hors de mon offre]</b>. Écris un refus poli qui explique mes limites et propose une alternative ou une redirection."),
("Résoudre un malentendu","Voici l'échange tendu avec un client : <b>[échange]</b>. Propose un message d'apaisement qui clarifie les faits, assume ce qui doit l'être et propose une solution réaliste."),
]),
("RECHERCHE D'IDÉES", [
("Brainstorming de services","Propose 20 idées de services numériques adaptés à <b>[compétence]</b> et au contexte de <b>[ville/pays]</b>, avec le problème résolu pour chacun. Classe-les de la plus facile à la plus complexe."),
("Idées de produits digitaux","Propose 10 idées de petits produits numériques (guide PDF, modèle, checklist) que je pourrais créer à partir de mon expérience : <b>[expérience]</b>."),
("Trouver des problèmes à résoudre","Liste 20 problèmes quotidiens des petites entreprises de <b>[secteur]</b> en Afrique francophone qui pourraient être aidés par la rédaction, l'organisation ou la communication."),
("Idées de partenariats","Propose 10 types de partenaires locaux (commerces, associations, écoles) avec lesquels collaborer pour <b>[activité]</b>, et un message pour leur proposer un échange."),
("Idées de contenus gratuits utiles","Quels contenus gratuits (mini-guides, checklists, modèles) pourraient aider <b>[cible]</b> et me faire connaître ? Donne 10 idées avec le titre."),
("Pivoter intelligemment","Mon offre actuelle <b>[offre]</b> ne rencontre pas d'intérêt. Voici ce que j'ai observé : <b>[observations]</b>. Propose 5 ajustements possibles (cible, message, prix, format) et le test le plus simple pour chacun."),
]),
]

SERV = [
("Pack fiches produits WhatsApp","Vendeurs sur WhatsApp / Facebook","Annonces peu claires","20 fiches + 5 accroches","500–1 500 FCFA / fiche","Groupes de commerçants autorisés, boutiques de ton quartier, pages Facebook locales"),
("Calendrier de contenu mensuel","Salons, restaurants, boutiques","Manque d'idées, publications irrégulières","Tableau de 30 jours + 12 textes","15 000–40 000 FCFA","Commerces proches, pages locales, recommandations"),
("CV + lettre de motivation","Étudiants, jeunes diplômés","CV peu structuré","CV 1 page + lettre adaptée","2 000–7 000 FCFA","Universités, groupes d'étudiants, réseau personnel"),
("Traduction FR ⇄ EN de supports","Artisans, ONG, PME","Communication limitée aux anglophones","Documents traduits et adaptés","2 000–6 000 FCFA / page","LinkedIn, ONG, associations"),
("Réponses types WhatsApp Business","Boutiques, écoles","Réponses lentes ou incohérentes","30 réponses + FAQ","10 000–30 000 FCFA","Boutiques actives sur WhatsApp"),
("Scripts de vidéos courtes","Coachs, marques, artistes","Peu d'idées de vidéos","10 scripts avec accroches","10 000–30 000 FCFA","TikTok, Instagram, groupes de créateurs"),
("Rédaction d'articles de blog","PME, cabinets, écoles","Site peu alimenté","3 articles de 500 mots","3 000–10 000 FCFA / article","Entreprises avec site ou page active"),
("Page de présentation d'activité","Indépendants, petites entreprises","Pas de présentation claire","Texte « À propos » + services","5 000–20 000 FCFA","Recommandations, Facebook, LinkedIn"),
("Dossier de présentation (PDF)","Entrepreneurs","Pas de document à envoyer","Brochure de 4 pages (texte)","10 000–35 000 FCFA","Associations d'entrepreneurs, incubateurs"),
("Descriptions de produits par lot","E-commerçants","Catalogue incomplet","50 descriptions harmonisées","300–1 000 FCFA / description","Boutiques en ligne, marchés digitaux"),
("Préparation de pitch","Étudiants, porteurs de projets","Difficulté à présenter son projet","Pitch de 3 min + support texte","5 000–15 000 FCFA","Clubs, concours, écoles"),
("Résumés de documents","Étudiants, cadres","Manque de temps","Résumés d'une page","1 000–3 000 FCFA / document","Universités, entreprises"),
("Gestion de messages et emails","Entrepreneurs occupés","Messages sans réponse","Réponses préparées + suivi","15 000–50 000 FCFA / mois","Indépendants, petites structures"),
("Cartes / textes d'événements","Églises, associations, familles","Besoin de textes soignés","Invitations, discours, programmes","3 000–15 000 FCFA","Associations, événements locaux"),
("Fiches de formation","Formateurs, coachs","Supports peu structurés","Plan + fiches pédagogiques","10 000–40 000 FCFA","Centres de formation, coachs"),
("Réponses aux avis clients","Hôtels, restaurants","Avis sans réponse","Modèles de réponses personnalisés","10 000–25 000 FCFA","Établissements locaux"),
("Études de cas rédigées","Prestataires et petites agences","Preuve de travail difficile à présenter","1 étude de cas de 1 page","5 000–15 000 FCFA","Freelances, agences"),
("Newsletters / messages de diffusion","Boutiques, associations","Contact irrégulier avec les clients","4 messages / mois","10 000–30 000 FCFA / mois","Commerces avec liste de contacts consentants"),
("Offres commerciales prêtes à envoyer","Freelances, PME","Propositions improvisées","Modèle d'offre + devis simple","5 000–20 000 FCFA","Réseaux de freelances"),
("Atelier d'initiation à ChatGPT","Étudiants, commerçants","Ne savent pas utiliser l'outil","Atelier 2 h + fiche prompts","À fixer selon le groupe et le lieu","Écoles, associations, quartiers"),
]

def bonus1():
    o = chapter("BONUS 1", "50 PROMPTS ULTRA-PRATIQUES", "8 catégories. Copie, remplace les crochets, adapte à ta réalité.")
    n = 0
    o += '<section>' + callout("Mode d'emploi", "<p>Chaque prompt est volontairement polyvalent. Les mots entre <b style='color:#b57e00'>[crochets]</b> sont à remplacer. Ajoute toujours <strong>ta ville, ta cible et ton ton</strong> pour de meilleurs résultats.</p>", "info", "📋")
    for cat, items in B:
        o += h2(cat)
        for t, pr in items:
            n += 1
            o += mini_prompt(n, t, pr)
    o += '</section>'
    assert n == 50, n
    return o

def bonus2():
    o = chapter("BONUS 2", "20 IDÉES DE SERVICES À VENDRE AVEC L'AIDE DE CHATGPT", "Des idées à tester, pas des promesses. Choisis-en une et adapte-la.")
    o += '<section>' + callout("Rappel", "<p>Les prix sont <strong>indicatifs</strong>, non garantis, et à ajuster selon ton marché, ton niveau et la qualité de ton travail.</p>", "warn", "⚠️")
    for i, (nm, cl, pb, lv, px, ou) in enumerate(SERV, 1):
        o += ('<div class="pblock" style="break-inside:avoid"><div class="ptitle"><span class="pnum">'+str(i)+'</span>'+nm+'</div>'
              '<table style="margin:0;font-size:8.2pt"><tbody>'
              f'<tr><td style="width:24%"><strong>Client cible</strong></td><td>{cl}</td></tr>'
              f'<tr><td><strong>Problème résolu</strong></td><td>{pb}</td></tr>'
              f'<tr><td><strong>Livrable</strong></td><td>{lv}</td></tr>'
              f'<tr><td><strong>Prix indicatif</strong></td><td><strong>{px}</strong></td></tr>'
              f'<tr><td><strong>Où trouver les clients</strong></td><td>{ou}</td></tr></tbody></table></div>')
        if i % 4 == 0 and i < len(SERV): o += '</section><section>'
    o += '</section>'
    return o

def bonus3():
    o = chapter("BONUS 3", "CHECKLIST DU PREMIER CLIENT", "De la première idée à la première livraison : tout sur une page.")
    o += ('<section>' + checklist(["Choisir une compétence","Choisir une niche","Créer une offre","Créer 3 exemples","Créer un portfolio","Optimiser WhatsApp (photo, description, catalogue)","Préparer son message de prospection","Contacter 5 prospects par jour","Relancer (poliment, 3 fois maximum)","Livrer correctement","Demander un témoignage lorsque pertinent","Améliorer son offre"]) +
      callout("Pour optimiser WhatsApp Business", "<ul><li>Photo de profil nette et professionnelle.</li><li>Description claire : ce que tu fais, pour qui, comment te contacter.</li><li>Catalogue ou liste de services avec prix de départ.</li><li>Messages d'accueil et d'absence.</li></ul>", "ok", "📱") +
      '</section>')
    return o

def conclusion():
    o = ('<section><div class="page-title"><small>CONCLUSION</small>Maintenant, c\'est à toi</div>' +
      quote("ChatGPT ne fera pas le travail à ta place. Mais si tu apprends à bien l'utiliser, il peut devenir l'un de tes meilleurs assistants.") +
      p("Tu as maintenant des méthodes, des prompts, des scripts et un plan. Ce qui manque, c'est toi, en action.") +
      p("Ne cherche pas à tout faire. Choisis :") +
      '<div class="formula"><span>UNE</span> COMPÉTENCE · <span>UNE</span> CIBLE · <span>UNE</span> OFFRE</div>' +
      p("Puis commence <strong>aujourd'hui</strong> : écris ton offre, envoie tes premiers messages, publie ton premier contenu. Les premiers résultats seront imparfaits : c'est normal. Chaque essai t'apprend quelque chose.") +
      p("Reste honnête, respecte tes clients, vérifie ton travail et améliore-toi chaque semaine. C'est ainsi qu'une compétence devient, avec du temps et de la régularité, une activité.") +
      callout("Ton premier pas, dans les 10 prochaines minutes", "<p>Ouvre ChatGPT et utilise le prompt du chapitre 3 pour clarifier ton offre. Puis envoie un message à une personne qui pourrait en avoir besoin.</p>", "ok", "🚀") +
      '</section>')
    o += ('<section class="end"><h1>Bonne route,<br>et bon travail.</h1><p>Retrouve ci-dessous les 3 règles à garder en tête :</p>'
          '<p>1. L\'outil accélère, ta valeur décide.<br>2. Vérifie toujours avant de livrer.<br>3. La régularité bat l\'inspiration.</p></section>')
    return o
