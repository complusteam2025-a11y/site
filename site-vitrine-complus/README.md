# Site vitrine COM+

Site vitrine statique (HTML/CSS/JS vanilla, sans dépendance ni build) pour **COM+**,
agence de communication digitale 360° basée au Cameroun (Grand Sud : Douala, Yaoundé,
Kribi, Ebolowa, Bertoua).

## Contenu du dossier

- `index.html` — structure de la page (une seule page, sections ancrées)
- `style.css` — styles (palette, typographie, responsive, animations)
- `script.js` — menu mobile, animations au scroll, formulaire de contact (interface uniquement)

## Ouvrir en local

Aucun serveur n'est nécessaire : double-cliquez sur `index.html` pour l'ouvrir
directement dans votre navigateur.

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

## Sections de la page

1. Header / Navigation
2. Hero (Accueil)
3. Services
4. À propos (équipe fondatrice)
5. Portfolio / Réalisations
6. Zone d'intervention
7. Contact
8. Footer
