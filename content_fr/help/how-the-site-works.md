---
title: 'Comment le site fonctionne'
slug: 'how-the-site-works'
subtitle: 'Hugo, des fichiers plats, et un pipeline GitHub Actions. Pas de base de données.'
order: 8
i18n_source: '2f8d3f5e4878'
---

## Pas de base de données, juste des fichiers

Chaque outil est un fichier Markdown dans `content/tools/`. Chaque catégorie vit dans `data/categories.yaml`. Pas de panneau d'admin, pas de backend à tenir : tout le site, ce sont des fichiers plats dans un dépôt Git. L'ensemble se construit avec [Hugo](https://gohugo.io/), un générateur de sites statiques, et sort en HTML simple.

## Ce que fait GitHub Actions

Trois workflows s'occupent de la partie ennuyeuse :

- **Deploy** construit et publie le site à chaque push sur `main`.
- **Issue to PR** relit automatiquement les issues d'envoi d'outils et ouvre un pull request pour tout ce qui tient dans le format.
- **Update README** régénère `README.md` dès que les données des outils changent.

## Pourquoi c'est fait comme ça

Les fichiers plats, ça veut dire que n'importe qui peut cloner le dépôt et voir exactement ce qu'il y a sur le site, et pourquoi. Pas de base de données cachée à laquelle il faudrait faire confiance : les données sont le fichier que tu modifierais pour les corriger.

## Regarde le code

Le code complet, les templates du site, les scripts et les données sont publics sur [github.com/best-of-ai/best-of-ai](https://github.com/best-of-ai/best-of-ai).
