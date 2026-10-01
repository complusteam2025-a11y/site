from lib import *

V = [
("Rédiger une offre commerciale","Présenter ton service en une page claire.","Agis comme un expert en vente de services pour freelances débutants.\nRédige une offre commerciale d'une page pour <b>[service]</b> destinée à <b>[client / type d'entreprise]</b>.\nÉléments : problème du client, solution, livrables, délai, prix <b>[prix] FCFA</b>, modalités de paiement (Mobile Money / espèces), 2 corrections incluses.\nTon : professionnel et simple. Aucune promesse de résultat garanti.","Ajoute un exemple de ton travail à la fin."),
("Page de vente (texte)","Écrire une page ou un long post de vente.","Écris une page de vente pour <b>[offre]</b>.\nCible : <b>[cible]</b>. Problème principal : <b>[problème]</b>.\nStructure : titre, sous-titre, problème, solution, ce que le client reçoit, comment ça se passe en 3 étapes, FAQ (5 questions), appel à l'action.\nLongueur : 350 mots. Style : clair, sans exagération ni fausse promesse.","Remplace le texte générique par des détails vrais sur ton travail."),
("Proposition commerciale","Répondre professionnellement à une demande de devis.","Rédige une proposition commerciale pour <b>[nom du client]</b>.\nBesoin exprimé : <b>[besoin]</b>. Mon offre : <b>[offre]</b>. Prix : <b>[prix]</b>. Délai : <b>[délai]</b>.\nStructure : contexte, objectifs, ce que je propose, livrables, planning, tarif, conditions, prochaines étapes.\nTon : sérieux, humain. Longueur : 1 page.","Envoie en PDF, pas en simple photo."),
("Répondre à un prospect","Répondre vite et clairement à un premier message.","Voici le message d'un prospect : <b>[message]</b>.\nMon service : <b>[service]</b>.\nÉcris une réponse WhatsApp de 5 lignes maximum : remerciement, 1–2 questions pour mieux comprendre son besoin, prochaine étape claire.\nPas de prix tant que je n'ai pas compris son besoin, sauf s'il le demande.","Réponds idéalement dans les premières heures."),
("Traiter une objection","Répondre calmement à un frein.","Un prospect me dit : <b>[objection, ex. « c'est trop cher »]</b>.\nContexte : <b>[service, prix]</b>.\nPropose 3 réponses possibles : une qui clarifie la valeur, une qui propose une option plus simple, une qui respecte sa décision.\nTon : respectueux, sans pression, sans mensonge.","Choisis la réponse qui te ressemble le plus."),
("Relancer un prospect","Faire un suivi poli.","Écris 3 messages de relance pour un prospect qui n'a pas répondu à mon offre <b>[offre]</b> : après 24 h, 3 jours et 7 jours.\nChaque message : 3 lignes max, ton aimable, un seul appel à l'action, une sortie élégante (« pas de souci si ce n'est pas le moment »).","N'envoie jamais plus de 3 relances."),
("Argumentaire de vente","Préparer tes arguments.","Prépare un argumentaire pour <b>[service]</b> face à <b>[type de client]</b>.\nDonne : 5 bénéfices concrets (pas de généralités), 3 preuves à montrer (exemples, témoignages réels), 3 questions à poser au client, et une phrase de conclusion.\nÉvite toute promesse de revenus ou de résultats garantis.","Garde uniquement les arguments que tu peux prouver."),
("Écrire une publicité","Créer une pub courte.","Écris 3 versions de publicité Facebook pour <b>[offre]</b> destinée à <b>[cible]</b>.\nVersion A : problème → solution. Version B : preuve / avant-après. Version C : offre limitée réelle.\nLongueur : 60 mots. Ajoute un titre court et un appel à l'action.\nRespecte l'honnêteté : pas de chiffres inventés.","Teste 2 versions avec un petit budget ou en les publiant à des moments différents."),
("Description produit orientée vente","Mettre en avant les bénéfices.","Transforme les caractéristiques suivantes en description orientée bénéfices pour <b>[client cible]</b> : <b>[caractéristiques]</b>.\nPour chaque caractéristique, explique ce qu'elle change pour le client. Termine par un appel à l'action simple.\nN'ajoute aucun détail technique que je n'ai pas fourni.","Parle de la vie réelle du client, pas seulement du produit."),
("Séquence WhatsApp en 4 messages","Créer un suivi progressif.","Crée une séquence de 4 messages WhatsApp pour un prospect intéressé par <b>[offre]</b> : 1) accueil et question, 2) présentation de l'offre, 3) preuve ou exemple, 4) proposition de prochaine étape.\nMessages courts (4 lignes max), un seul objectif par message. Ton : naturel et respectueux.","Envoie un message à la fois, selon les réponses du prospect."),
("Titre de vente (10 versions)","Trouver un titre qui attire l'attention.","Propose 10 titres de vente pour <b>[offre]</b> destinée à <b>[cible]</b>. Styles : bénéfice, question, avant/après, curiosité honnête. 12 mots maximum, sans fausse promesse.","Teste 2 titres sur 2 publications."),
("Présentation de 30 secondes (pitch)","Te présenter à l'oral ou par écrit.","Écris un pitch de 30 secondes pour me présenter : métier <b>[métier]</b>, cible <b>[cible]</b>, problème résolu <b>[problème]</b>, ce que je livre <b>[livrables]</b>.\nDonne une version orale (3 phrases) et une version écrite pour WhatsApp.","Répète à voix haute pour que ça sonne naturel."),
("Offre de lancement honnête","Attirer les premiers clients.","Aide-moi à créer une offre de lancement pour mes 5 premiers clients : <b>[service]</b>.\nPropose : ce qui est inclus, ce qui est limité (nombre de places réel), le prix de lancement, ce que je demande en échange (retour d'expérience / témoignage si le client est d'accord).\nPas de fausse rareté.","Respecte toujours le nombre de places annoncé."),
("Compte rendu après un rendez-vous","Confirmer par écrit ce qui a été décidé.","Voici mes notes de rendez-vous avec un client : <b>[notes]</b>.\nRédige un message de compte rendu : besoin exprimé, ce qui est convenu, livrables, délai, prix, prochaine étape et date.\nTon professionnel, 8 lignes maximum.","Un écrit protège les deux parties."),
("Devis simple","Présenter un prix clairement.","Prépare un devis simple pour <b>[client]</b> : lignes de prestation <b>[liste]</b>, prix unitaires en FCFA, total, délai, modalités de paiement, validité de 7 jours.\nPrésente sous forme de tableau clair, prêt à copier dans un document.","Vérifie les calculs toi-même."),
("Message de remerciement + demande d'avis","Obtenir un retour honnête après livraison.","Écris un message de remerciement après la livraison de <b>[service]</b>, avec une demande de retour honnête (2 questions simples) et, si le client est d'accord, l'autorisation de citer son avis.\nTon : sincère, court, sans pression.","Ne demande l'avis que quand le client est satisfait ou s'il le propose."),
("Réponse à un client mécontent","Gérer un problème avec calme.","Un client me dit : <b>[message]</b>. Les faits : <b>[faits]</b>.\nÉcris une réponse calme : reconnaître, clarifier, proposer une solution réaliste, fixer la suite. Pas de justifications agressives, pas de promesse impossible.","Prends 10 minutes avant de répondre à chaud."),
("Programme de fidélisation simple","Faire revenir les clients.","Propose 5 idées simples de fidélisation pour <b>[activité]</b> sans gros budget (ex. carte de fidélité, bonus de recommandation, liste de diffusion WhatsApp).\nPour chaque idée : mise en place en 3 étapes et message d'annonce.","Choisis une seule idée et applique-la un mois."),
("Plan de prospection de la semaine","Organiser ton travail commercial.","Crée mon plan de prospection pour 5 jours : objectif <b>[ex. contacter 5 personnes par jour]</b>, cible <b>[cible]</b>, canaux <b>[WhatsApp, Facebook…]</b>.\nFormat : tableau Jour / Action / Message à utiliser / Suivi. Pas de messages en masse, pas de spam.","Note tes résultats chaque soir."),
("Répondre à « J'ai trouvé moins cher »","Rester professionnel face à la comparaison.","Un prospect me dit qu'il a trouvé <b>[service équivalent]</b> moins cher. Mon offre : <b>[offre, prix, livrables, délai]</b>.\nÉcris une réponse WhatsApp sans critiquer le concurrent : demander ce qui est inclus chez l'autre, expliquer clairement ce que je livre, proposer une option adaptée à son budget.\nTon : calme et honnête.","Ne baisse pas ton prix sans réduire le contenu de l'offre."),
]

SCRIPTS = [
("1. Premier message","Bonjour <b>[Prénom]</b>, j'espère que vous allez bien. Je m'appelle <b>[ton nom]</b> et j'aide les <b>[type d'entreprises]</b> à <b>[bénéfice]</b>. J'ai vu votre page et j'ai pensé à une idée simple pour <b>[situation précise]</b>. Puis-je vous la présenter en 2 minutes ?"),
("2. Relance après 24 h","Bonjour <b>[Prénom]</b>, je me permets un petit rappel de mon message d'hier. Si c'est un bon moment, je peux vous envoyer l'idée en 3 lignes. Sinon, pas de souci, bonne journée !"),
("3. Relance après 3 jours","Bonjour <b>[Prénom]</b>, je reviens vers vous une dernière fois pour savoir si cela peut vous intéresser. Si ce n'est pas le moment, dites-le moi simplement, je comprends tout à fait."),
("4. Présentation d'une offre","Merci pour votre réponse ! Voici ce que je propose : <b>[offre]</b>. Vous recevez <b>[livrables]</b> en <b>[délai]</b>, pour <b>[prix] FCFA</b>. Souhaitez-vous que je vous prépare un exemple pour voir si cela vous convient ?"),
("5. Réponse à « C'est combien ? »","Merci pour votre question ! Pour vous donner un prix juste, j'ai besoin de savoir <b>[1–2 informations]</b>. En général, mon offre <b>[nom]</b> se situe à <b>[prix] FCFA</b> pour <b>[ce qui est inclus]</b>. Voulez-vous que je vous envoie le détail ?"),
("6. Réponse à « Je vais réfléchir »","Bien sûr, prenez le temps qu'il faut. Pour vous aider, y a-t-il un point précis qui vous fait hésiter (prix, délai, contenu) ? Je peux vous apporter une précision. Je reste disponible."),
("7. Réponse à « C'est trop cher »","Je comprends. Peut-on regarder ensemble ce qui est le plus important pour vous ? Je peux ajuster le contenu pour rester dans votre budget, par exemple <b>[version simplifiée]</b> à <b>[prix] FCFA</b>. Qu'en pensez-vous ?"),
("8. Message après livraison","Bonjour <b>[Prénom]</b>, votre <b>[livrable]</b> a été envoyé. Dites-moi si tout vous convient ; je reste disponible pour les corrections prévues. Si vous êtes satisfait(e), un petit retour de votre part m'aiderait beaucoup. Merci pour votre confiance !"),
]

def ch5():
    o = chapter(5, "20 PROMPTS POUR VENDRE", "Vendre, c'est d'abord comprendre un besoin. ChatGPT t'aide à le dire clairement.")
    o += '<section>' + callout("Vendre honnêtement", "<p>Ces prompts t'aident à <strong>formuler</strong> ton offre. Ils ne remplacent pas la vérité : ne promets que ce que tu peux livrer, et n'invente jamais de témoignages ou de chiffres.</p>", "warn", "🤝")
    for i, (t, ob, pr, ad) in enumerate(V, 1):
        o += prompt_box(i, t, pr, ob, ad)
        if i % 5 == 0 and i < len(V): o += '</section><section>'
    o += '</section>'
    o += ('<section>' + h2("Comment transformer une conversation WhatsApp en opportunité commerciale") +
      p("Une conversation WhatsApp n'est pas un « spam » : c'est un échange. Voici le chemin simple :") +
      '<div class="flow"><span>Écouter</span><i>→</i><span>Clarifier</span><i>→</i><span>Proposer</span><i>→</i><span>Confirmer</span><i>→</i><span>Livrer</span></div>' +
      h3("Exemple 1 : un client demande « C'est combien ? »") +
      '<div class="chat"><div class="cl"><span class="who">CLIENTE</span>Bonjour, c\'est combien pour les fiches produits ?</div>'
      '<div class="me"><span class="who">TOI</span>Bonjour Mme Nana 😊 Pour bien vous répondre : combien de produits avez-vous et où publiez-vous (WhatsApp, Facebook) ?</div>'
      '<div class="cl"><span class="who">CLIENTE</span>J\'ai 15 produits, surtout sur WhatsApp.</div>'
      '<div class="me"><span class="who">TOI</span>Parfait. Je peux rédiger 15 fiches claires, prêtes à copier, en 48 h. Voulez-vous que je vous prépare d\'abord 1 exemple pour voir le style ?</div></div>' +
      h3("Exemple 2 : réactiver une conversation silencieuse") +
      '<div class="chat"><div class="me"><span class="who">TOI</span>Bonjour Paul, j\'espère que votre semaine se passe bien. Je repensais à votre boutique : j\'ai préparé une petite idée de description pour votre produit phare. Souhaitez-vous la voir ?</div>'
      '<div class="cl"><span class="who">PAUL</span>Oui envoie.</div>'
      '<div class="me"><span class="who">TOI</span>Voilà ! Si cela vous plaît, je peux faire la même chose pour les autres produits. Dites-moi ce que vous en pensez 🙂</div></div>' +
      callout("Les 4 règles d'or", "<ul><li>Réponds poliment et rapidement.</li><li>Pose des questions avant de donner un prix.</li><li>Un message = une idée.</li><li>Respecte un « non » ou un silence prolongé.</li></ul>", "ok", "✅") +
      mini_prompt("P","Prompt pour simuler une conversation (entraînement)",
        "Joue le rôle d'une cliente propriétaire d'une petite boutique à Douala. Elle est intéressée par mon service <b>[service]</b> mais hésite à cause du prix et de la confiance. Réponds comme dans une vraie conversation WhatsApp, un message à la fois. Après 8 échanges, évalue mes réponses et donne-moi 3 points à améliorer.") +
      play(["Choisis 3 prompts et prépare les textes pour ton service.","Écris ta propre réponse à « C'est combien ? ».","Fais un entraînement de 8 messages avec ChatGPT en jeu de rôle.","Prépare un document « devis simple » à envoyer en PDF."]) +
      '</section>')
    return o

def ch6():
    o = chapter(6, "TROUVER SES PREMIERS CLIENTS", "Les premiers clients arrivent par des conversations, pas par des miracles.")
    o += ('<section>' + h2("Où chercher ?") +
      table(["Canal","Comment l'utiliser","Précaution"],[
        ["<strong>WhatsApp</strong>","Statut régulier, WhatsApp Business, contacts qui te connaissent","Pas d'ajout forcé dans des groupes"],
        ["<strong>Facebook</strong>","Page + publications utiles, groupes de commerçants autorisés","Respecte les règles des groupes"],
        ["<strong>TikTok</strong>","Vidéos courtes qui montrent ton savoir-faire","Régularité avant perfection"],
        ["<strong>LinkedIn</strong>","Profil clair, contenus pro, messages personnalisés","Évite les messages copiés-collés"],
        ["<strong>Groupes professionnels</strong>","Aide gratuite sur des questions précises, présence utile","Pas de pub non autorisée"],
        ["<strong>Prospection directe</strong>","Message personnalisé à une entreprise ciblée","Personnalise, reste bref"],
        ["<strong>Recommandations</strong>","Demande à tes clients satisfaits","Remercie sincèrement"],
        ["<strong>Réseau personnel</strong>","Famille, amis, anciens camarades, voisins","Ne mélange pas faveur et business"]]) +
      callout("Prospection respectueuse = pas de spam", "<ul><li>Envoie un message <strong>personnalisé</strong> (pourquoi lui, pourquoi maintenant).</li><li>Demande la permission avant d'envoyer des détails.</li><li>Maximum 3 relances espacées.</li><li>Si la personne dit non ou ne répond plus : tu arrêtes, avec politesse.</li><li>Ne partage jamais les contacts de quelqu'un et n'écris pas en masse à des inconnus.</li></ul>", "stop", "🛑") +
      h2("Ton rythme quotidien") +
      p("Contacter <strong>5 personnes par jour</strong>, de façon sincère et personnalisée, vaut mieux que 100 messages copiés. Note tout dans un petit tableau : nom, date, message envoyé, réponse, prochaine action.") +
      table(["Nom","Date","Canal","Statut","Prochaine action"],[["Mme Nana","J1","WhatsApp","Intéressée","Envoyer exemple"],["Boutique Lumière","J1","Facebook","Pas de réponse","Relance J2"],["…","…","…","…","…"]]) +
      '</section>')
    o += '<section>' + h2("8 scripts prêts à utiliser")
    o += p("Adapte chaque script avec ton style. Les mots entre crochets sont à remplacer.")
    for t, s in SCRIPTS:
        o += f'<div class="pmini"><div class="ptitle">{t}</div><div class="prompt">{s}</div></div>'
    o += '</section><section>'
    o += mini_prompt("P","Prompt pour personnaliser un script",
      "Voici mon script de premier message : <b>[script]</b>. Voici la boutique ciblée : <b>[nom, activité, ce que j'ai observé de vrai sur sa page]</b>. Réécris le message pour qu'il soit personnalisé, poli et court (5 lignes). Ne fais aucune affirmation que je ne t'ai pas donnée.")
    o += mini_prompt("P","Prompt pour préparer 5 prospects",
      "Je veux aider des <b>[type de cible]</b> à <b>[bénéfice]</b>. Donne-moi 10 critères pour reconnaître un bon prospect et 5 questions à lui poser dans une première conversation. Ensuite, propose 3 façons respectueuses de l'approcher.")
    o += callout("Après la livraison", "<p>Un client satisfait est ta meilleure vitrine. Demande poliment un retour et une recommandation <strong>quand c'est pertinent</strong>, et accepte un « non ».</p>", "ok", "🌱")
    o += play(["Fais une liste de 20 contacts ou entreprises potentiels dans ta cible.","Personnalise le script 1 pour 5 d'entre eux et envoie les messages.","Crée ton tableau de suivi et note chaque réponse.","Prépare tes réponses aux scripts 5, 6 et 7 avec tes vrais prix."])
    o += '</section>'
    return o
