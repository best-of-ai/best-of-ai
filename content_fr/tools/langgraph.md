---
title: 'LangGraph'
name: 'LangGraph'
subtitle: "Framework en graphe pour des agents à état, qui tournent longtemps"
slug: 'langgraph'
description: "LangGraph est un framework open source de l'équipe LangChain pour construire des agents à état sous forme de graphes d'étapes. Il prend en charge les bifurcations, les boucles, la mémoire persistante, les étapes de validation humaine et le streaming, et s'associe à LangSmith pour le déploiement et le suivi."
website: 'https://www.langchain.com/langgraph'
logo_url: ''
category: 'ai-agents'
category_name: "Agents d'IA"
price: 'Free'
featured: false
rank: 8
alternatives:
  - langchain
  - crewai
  - autogen-ai
  - llamaindex
  - smolagents
  - mastra
date: '2026-11-05'
tags: [ai_agent, automation, autonomous, ai_assistants, agents, multi_agent, task_automation, orchestration, agentic, collaboration, model_based]
i18n_source: '50181c5f4cd8'
---
LangGraph modélise un agent comme un graphe. Chaque nœud est une étape, comme appeler un modèle, lancer un outil ou vérifier une condition, et les arêtes définissent le flux entre les étapes, y compris les boucles et les bifurcations. Un objet d'état partagé fait passer l'information. Cette structure explicite donne aux développeurs le contrôle de ce que l'agent fait et quand, ce qui rend les agents complexes plus lisibles qu'une boucle libre.

Des fonctions pensées pour la production le distinguent. Le checkpointing enregistre l'état pour qu'une exécution puisse se mettre en pause et reprendre, ou se remettre d'un échec. Des étapes avec un humain dans la boucle permettent à un agent d'attendre une validation avant d'agir, et le débogage par voyage dans le temps permet de rejouer et de modifier des étapes précédentes. Il prend en charge le streaming des résultats intermédiaires, la mémoire à long terme et des conceptions multi-agents, en Python et en JavaScript.

La bibliothèque est gratuite et open source. L'hébergement et le suivi passent par LangSmith, qui a une offre gratuite et des offres payantes. LangGraph a une courbe d'apprentissage plus raide que les bibliothèques d'agents de haut niveau, et sa force sert surtout aux flux de travail complexes. CrewAI et AutoGen proposent des abstractions multi-agents plus hautes, l'OpenAI Agents SDK est plus simple pour un travail centré sur OpenAI, et des constructeurs visuels comme n8n et Dify conviennent à ceux qui ne codent pas. Beaucoup d'agents en production sont construits avec LangGraph.
