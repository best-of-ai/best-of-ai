---
title: 'SmolAgents'
name: 'SmolAgents'
subtitle: "Bibliothèque légère d'agents d'IA par Hugging Face"
slug: 'smolagents'
description: "SmolAgents est une petite bibliothèque Python open source de Hugging Face pour construire des agents d'IA. Elle se concentre sur des agents qui écrivent et exécutent du code pour résoudre des tâches, prend en charge de nombreux modèles et outils, et garde le cœur simple."
website: 'https://huggingface.co/docs/smolagents'
company: 'hugging-face'
logo_url: ''
category: 'ai-agents'
category_name: "Agents d'IA"
price: 'Free'
featured: false
rank: 8
alternatives:
  - langgraph
  - crewai
  - agno-ai
  - mastra
  - autogen-ai
  - langchain
  - llamaindex
date: '2025-09-21'
tags: [ai_agent, automation, autonomous, ai_assistants, agents, multi_agent, task_automation, orchestration, agentic, integrations, model_based]
i18n_source: '2acb38d44046'
---
SmolAgents est conçu pour être facile à lire et à utiliser. La logique centrale tient dans peu de code, et construire un agent prend quelques lignes : tu choisis un modèle, tu lui donnes des outils, et tu lances une tâche. Son idée signature est le code agent, où le modèle écrit ses actions en code Python au lieu d'appels d'outils structurés. Ça lui permet de combiner des étapes, d'utiliser des boucles et des variables, et de traiter des problèmes en plusieurs étapes efficacement, et l'approche a souvent besoin de moins d'étapes que les méthodes traditionnelles.

Il fonctionne avec un large éventail de modèles, des API hébergées aux modèles locaux, et prend en charge des outils du Hugging Face Hub, de LangChain et du Model Context Protocol. Des configurations multi-agents, des agents de vision et de navigation web, et des options d'exécution en bac à sable sont disponibles, parce qu'exécuter du code écrit par un modèle demande des garde-fous. La bibliothèque s'intègre au Hub de Hugging Face pour partager des agents et des outils.

SmolAgents est gratuit et open source sous la licence Apache 2.0. Exécuter du code généré comporte des risques de sécurité, donc un environnement sûr est indispensable. C'est plus léger que des frameworks comme LangGraph ou CrewAI, qui offrent plus de structure pour des flux complexes, et l'OpenAI Agents SDK est une autre option simple. SmolAgents convient aux développeurs qui veulent une façon minimale et transparente d'expérimenter avec des agents.
