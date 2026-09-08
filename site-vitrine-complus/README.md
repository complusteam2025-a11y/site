# COM+ — Hub interconnecté d'entreprises

Site vitrine statique (HTML/CSS/JS vanilla, sans dépendance ni build) pour **COM+**,
agence de communication digitale 360° basée au Cameroun, présentée comme un **Hub
interconnecté** reliant les entreprises clientes (Grand Sud : Douala, Yaoundé, Kribi,
Ebolowa, Bertoua) à l'expertise COM+.

Conforme à la charte graphique officielle COM+ :
- **Couleurs** : `#F28C28` (orange), `#E05206` (orange foncé), `#2E1A3A` (violet), `#111111` (noir), `#F5F5F5` (gris clair)
- **Typographies** : Montserrat (titres) / Roboto (texte courant)
- **Logo** : recréé en SVG (C + emblème rond + M+), avec effet de relief/3D et halo lumineux
- **Icônes** : micro, signal, chat, partage, cloud, note de musique (jeu d'icônes de la charte)
- **Motifs graphiques** : grille de points, rayures diagonales, éléments 3D

## Contenu du dossier

- `index.html` — structure de la page (une seule page, sections ancrées)
- `style.css` — styles (palette officielle, typographie, 3D, responsive, animations)
- `script.js` — menu mobile, header au scroll, tilt 3D au survol, animations au scroll, formulaire de contact

## Sections de la page

1. Header / Navigation (logo COM+ visible en permanence)
2. Hero — grand logo COM+ + visuel 3D du Hub (nœuds d'entreprises connectés au centre COM+, animation de rotation)
3. Le Hub — concept en 3 étapes (connexion, stratégie & production, rayonnement)
4. Entreprises connectées — grille de cartes (exemples illustratifs, personnalisables avec vos vrais clients)
5. Services (conseil & stratégie, production audiovisuelle, communication digitale, événementiel)
6. À propos (mission, valeurs, équipe fondatrice)
7. Zone d'intervention (carte stylisée du Grand Sud)
8. Contact (formulaire + coordonnées + réseaux sociaux)
9. Footer (logo, liens, hashtags de la charte)

> Les entreprises affichées dans « Entreprises connectées au Hub » sont des exemples
> illustratifs. Remplacez noms, secteurs, descriptions et initiales par vos véritables
> clients dans `index.html` (section `#entreprises`).

## Ouvrir en local

Aucun serveur n'est nécessaire : double-cliquez sur `index.html` pour l'ouvrir
directement dans votre navigateur. Pour un rendu 100% fidèle (polices, animations),
vous pouvez aussi servir le dossier avec un petit serveur local, par exemple :

```
python3 -m http.server 8080
```

puis ouvrez `http://localhost:8080`.

## Héberger le site

Ce dossier peut être déployé tel quel sur n'importe quel hébergement statique :

- **Hébergement mutualisé / cPanel** : uploadez le contenu du dossier dans `public_html/`.
- **Netlify / Vercel** : glissez-déposez le dossier `site-vitrine-complus/` (aucune
  configuration de build requise, dossier de publication = racine du dossier).
- **GitHub Pages** : poussez ce dossier sur une branche/repo et activez GitHub Pages
  sur le dossier correspondant.

Aucune variable d'environnement, base de données ou backend n'est requis : le formulaire
de contact est une interface de démonstration (affiche une confirmation côté client).
Pour le rendre fonctionnel, reliez-le à un service comme Formspree, Netlify Forms,
ou un endpoint backend de votre choix.

## Personnaliser le logo

Le logo est recréé en SVG dans `index.html` (symbole `#emblem-o` + lettres en CSS avec
dégradé/relief). Si vous disposez du fichier logo officiel COM+ (PNG/SVG haute
définition), vous pouvez le substituer facilement : remplacez le bloc `<a class="logo">`
par une simple balise `<img src="logo.png" alt="COM+">` et ajoutez le fichier image au
dossier.
