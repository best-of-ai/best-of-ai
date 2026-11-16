---
title: 'BabyAGI'
name: 'BabyAGI'
subtitle: "Agent autonome minimal, open source et piloté par les tâches"
slug: 'babyagi'
description: "BabyAGI est un petit projet Python open source de Yohei Nakajima, qui a montré comment un LLM peut créer, prioriser et exécuter des tâches vers un objectif. Il a influencé beaucoup de frameworks d'agents autonomes ensuite."
website: 'https://github.com/yoheinakajima/babyagi'
logo_url: ''
category: 'ai-agents'
category_name: "Agents d'IA"
price: 'Free'
featured: false
rank: 6
alternatives:
  - autogpt
  - agentgpt
  - superagi
  - crewai
  - manus
date: '2026-11-05'
tags: [ai_agent, automation, autonomous, ai_assistants, agents, multi_agent, task_automation, orchestration, agentic, model_based]
i18n_source: '0dec64a691c0'
---

BabyAGI est arrivé tôt dans la vague d'expériences d'agents autonomes. Le script d'origine ne faisait que quelques dizaines de lignes : étant donné un objectif, un modèle de langage crée une liste de tâches, exécute la première, stocke le résultat dans une base vectorielle, puis génère et re-priorise de nouvelles tâches selon ce qu'il a appris. Cette boucle simple a été largement copiée et adaptée.

Le projet a compté parce qu'il a rendu l'idée d'un agent d'IA facile à comprendre et à essayer. Il a lancé beaucoup de descendants et une discussion sur ce que les systèmes autonomes pouvaient faire, et les développeurs ont appris de ses limites, comme les boucles, la dérive et le coût. Des versions plus tardives ont été refondues en framework pour construire des agents qui s'améliorent, avec des fonctions stockées dans une base.

BabyAGI est gratuit et open source, destiné aux développeurs et à ceux qui apprennent, pas au grand public. Il se voit mieux comme un design de référence que comme un outil de production. Pour du vrai travail, on tend à utiliser des frameworks comme LangGraph, CrewAI, AutoGen, ou les SDK d'agents d'OpenAI et d'Anthropic. BabyAGI convient à quiconque veut étudier comment marchent de simples boucles d'agents.
