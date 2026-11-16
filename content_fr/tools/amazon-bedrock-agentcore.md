---
title: 'Amazon Bedrock AgentCore'
name: 'Amazon Bedrock AgentCore'
subtitle: 'Plateforme AWS pour construire, déployer et faire tourner des agents d''IA en production'
slug: 'amazon-bedrock-agentcore'
description: 'Amazon Bedrock AgentCore est la plateforme d''AWS pour construire et faire tourner des agents d''IA en production. Elle fournit un runtime managé, l''identité, la mémoire, des outils de passerelle et des contrôles de politique, et marche avec des agents bâtis sur n''importe quel framework ou modèle.'
website: 'https://aws.amazon.com/bedrock/agentcore/'
company: 'amazon'
logo_url: ''
category: 'ai-agents'
category_name: 'Agents d''IA'
price: 'Paid'
featured: false
rank: 7
alternatives:
  - azure-ai-foundry
  - vertex-ai
  - databricks-agent-bricks
  - salesforce-agentforce
date: '2026-11-05'
tags: [ai, assistant, automation, productivity, enterprise, agent]
i18n_source: '27c7992a821e'
---

AgentCore traite le travail d'infrastructure pour passer un agent du prototype à la production. Un runtime héberge les agents avec une isolation de session, pour que le travail de chaque utilisateur reste séparé, et gère la montée en charge. Des fonctions d'identité permettent aux agents de s'authentifier auprès d'autres services au nom d'un utilisateur, une passerelle transforme des API et des services existants en outils que les agents peuvent appeler, et l'observabilité trace ce que les agents font. Les développeurs peuvent l'utiliser avec des frameworks comme LangGraph, CrewAI et le SDK Strands Agents, et avec des modèles sur Bedrock ou d'autres fournisseurs.

La mémoire est un composant majeur. AgentCore stocke le contexte à court terme dans une session et des mémoires à long terme entre les sessions, y compris une mémoire épisodique qui permet à un agent de se rappeler d'interactions antérieures. Une capacité de politique, actuellement en preview, permet de fixer des limites à ce que les agents peuvent faire. Des outils d'interpréteur de code et de navigateur donnent aux agents des moyens d'exécuter du code et d'utiliser le web dans des sandboxes sûrs.

AgentCore est facturé à l'usage de ses composants, sans engagement initial. Il vise les équipes qui construisent déjà sur AWS et veulent une infrastructure managée pour les agents. Les alternatives incluent le service d'agents d'Azure AI Foundry, Vertex AI Agent Engine de Google, et des piles open source ou auto-gérées sur Kubernetes. Le bon choix dépend souvent du cloud qu'une entreprise utilise déjà. Voir la fiche Amazon Bedrock pour le service de modèles qui est en dessous.
