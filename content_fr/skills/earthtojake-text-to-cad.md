---
title: 'text-to-cad'
name: 'text-to-cad'
slug: 'earthtojake-text-to-cad'
subtitle: "Une bibliothèque d'Agent Skills pour générer, inspecter et fabriquer des fichiers CAD et de robots."
description: "text-to-cad produit et gère des artefacts CAD et de description de robots à partir des fichiers locaux du projet. Les skills séparés couvrent la génération et l'export de modèles, la recherche de pièces du commerce, le dessin 2D, les formats de description de robots, le slicing et les contrôles de fabrication, et ils sortent comme plugins natifs de chaque fournisseur."
author: 'earthtojake'
skill_type: 'Development & Engineering'
source_url: 'https://github.com/earthtojake/text-to-cad'
compatible_with: ['Claude Code', 'Codex']
install: 'Install via the Skills CLI (npx skills add earthtojake/text-to-cad) or a provider-native plugin command.'
price: 'Free'
open_source: true
license: 'MIT'
stars: 25311
stars_this_week: 1170
stars_updated: '2026-11-04'
rank: 8
date: '2026-11-04'
tags: [cad, robotics, engineering]
i18n_source: '97819cd5ef73'
---
Ce dépôt regroupe les skills suivants :

- **CAD** : Crée et édite des modèles CAD, avec une sortie STEP et l'export en STL, 3MF et GLB.
- **CAD Viewer** : Propose des aperçus locaux dans le navigateur pour les fichiers CAD et de robots.
- **step.parts** : Trouve des composants STEP du commerce, comme des vis, des roulements et des moteurs.
- **DXF** : Génère des dessins 2D à partir de géométrie Python ou CAD.
- **URDF/SRDF** : Écrit la structure du robot et les fichiers de planification MoveIt.
- **G-code** : Découpe des maillages en G-code avec de vrais outils de slicer en ligne de commande.
