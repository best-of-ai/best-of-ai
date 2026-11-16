---
title: 'Gradio'
name: 'Gradio'
subtitle: 'Bibliothèque Python pour construire des interfaces de démo de machine learning'
slug: 'gradio'
description: 'Gradio est une bibliothèque Python open source pour construire des interfaces web autour de modèles de machine learning et de fonctions en quelques lignes de code. Elle porte beaucoup de démos sur Hugging Face Spaces, et Hugging Face en est propriétaire.'
website: 'https://www.gradio.app'
logo_url: ''
category: 'devtools'
category_name: 'Outils de développement'
price: 'Free'
featured: false
rank: 8
alternatives:
  - streamlit
  - mercury
  - hugging-face
date: '2026-11-05'
tags: [developer_tools, code_generation, infrastructure, deployment, development, devops, ci_cd, cloud, api, model_based]
i18n_source: '561349bd6740'
---
Gradio rend simple de montrer un modèle à d'autres gens. En quelques lignes de Python, tu enveloppes une fonction, par exemple une qui prend une image et renvoie une légende, et Gradio produit une interface web avec les bons composants d'entrée et de sortie : zones de texte, envois d'image, enregistreurs audio, curseurs, et plus. Lancer le script donne une web app locale, et une option de partage crée un lien public temporaire, pratique pour les démos et les retours.

Ça a dépassé les démos simples. L'API Blocks de Gradio permet de construire des interfaces plus complexes, en plusieurs étapes, avec des mises en page personnalisées, et une classe d'interface de chat crée des chatbots avec peu de code. Chaque app Gradio expose aussi une API, et les apps peuvent s'utiliser par programmation via des bibliothèques clientes. Elle prend en charge le Model Context Protocol, donc une fonction Gradio peut être proposée comme outil à des agents d'IA. Beaucoup d'articles de machine learning et de modèles ouverts renvoient vers une démo Gradio.

Gradio est gratuit et open source sous licence Apache 2.0, et l'hébergement sur Hugging Face Spaces est gratuit pour un usage de base, avec du matériel payant pour les démos plus lourdes. Il est pensé pour les démos, les outils internes et les prototypes, donc les grandes applications de production ont en général besoin d'un vrai framework web. Streamlit est l'alternative la plus proche et est courant pour les apps de données, Panel et Dash servent les dashboards, et Chainlit se concentre sur les applications de chat. Gradio est le défaut pour les démos de modèles.
