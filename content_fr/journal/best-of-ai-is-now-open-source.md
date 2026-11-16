---
title: 'Best of AI est maintenant open source !'
slug: 'best-of-ai-is-now-open-source'
subtitle: "Un an à choisir des outils d'IA à la main. Le dépôt, le classement et le pipeline de déploiement sont maintenant sur GitHub, pour qui veut s'en servir."
date: '2026-06-25'
related_categories:
  - ai-directories
related_tools:
  - best-of-ai
i18n_source: 'd8ce6e206afa'
---

On a lancé Best of AI il y a environ un an, comme une liste sélectionnée d'outils d'IA qui valent le coup. Aujourd'hui, tout est [open source sur GitHub](https://github.com/best-of-ai/best-of-ai) : données, site, scripts, CI. À partir de là, c'est la communauté qui le fait vivre.

## Des fichiers plats, pas de base de données

Chaque outil est un fichier Markdown dans `content/tools/`. Les catégories vivent dans `data/categories.yaml`. Le [classement](/leaderboard/) ordonne les outils à partir de `data/leaderboard.yaml`. Pas de Postgres, pas de CMS headless, pas de dépendance à un fournisseur. Tu clones le dépôt, tu fais `git grep` pour ce qu'il te faut, tu envoies un PR quand quelque chose cloche. C'est tout le modèle.

Le site est une build statique [Hugo](https://gohugo.io/). HTML, CSS, un peu de JS vanilla. Tu pousses sur `main`, une GitHub Action lance `hugo --minify`, et le résultat arrive sur GitHub Pages. Pas de serveur à surveiller.

## GitHub Actions fait le travail ennuyeux

Trois workflows utiles à connaître :

- **Deploy** : construit et publie à chaque push sur `main`
- **Issue → PR** : tu ouvres un issue d'envoi d'outil avec le bon template, et `issue-review.py` le valide, ouvre une branche et dépose un PR
- **Update README** : régénère `README.md` à partir des fichiers d'outils quand les données changent

Tu proposes un outil par issue ou par PR. Tu corriges une description en éditant un seul fichier Markdown. Tu débats des places du classement dans `data/leaderboard.yaml`. Tout est relisible, tout reste dans l'historique git.

## Classement, métiers, et le reste

Le [classement](/leaderboard/) est une liste courte et ordonnée : des outils qu'on trouve vraiment bons, pas seulement populaires. Les places sont des données, pas une impression. Tu modifies le YAML, tu ouvres un PR, tu défends ton choix.

Les [pages de métiers](/professionals/) regroupent les outils par rôle : développeurs, designers, marketeurs, rédacteurs, et plus de 200 autres. Chaque fichier de métier liste des slugs de catégorie ; Hugo va chercher les outils qui correspondent, tout seul. Tu ajoutes un métier comme un outil : fichier Markdown, PR, c'est fait.

La recherche se fait côté client. La modale de l'en-tête va chercher [`/index.json`](/index.json), un index JSON construit à la compilation. Forke les données, construis ta propre interface, branche-la où tu veux. Pas de clé d'API.

## Viens bricoler

Si tu aimes les annuaires qui vivent dans git, les sites statiques qui se déploient seuls, et les annuaires auxquels tu peux vraiment envoyer un patch, c'est pour toi.

- [Contribuer](/contribute/) : comment proposer des outils, corriger des fiches, améliorer le classement
- [Dépôt GitHub](https://github.com/best-of-ai/best-of-ai) : clone-le, casse-le, répare-le, envoie un PR

L'annuaire est libre à parcourir. Le code et les données sont à toi, à forker. On préfère cent personnes qui améliorent la liste à une seule qui en garde l'entrée.
