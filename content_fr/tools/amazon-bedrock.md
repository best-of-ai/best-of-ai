---
title: 'Amazon Bedrock'
name: 'Amazon Bedrock'
subtitle: 'Le service managé d''AWS pour accéder à des modèles de fondation via une API'
slug: 'amazon-bedrock'
description: 'Amazon Bedrock est le service managé d''AWS pour construire des applications d''IA générative. Il donne accès à des modèles de fondation de nombreux fournisseurs via une seule API, avec des outils de récupération, d''agents, de garde-fous et d''évaluation.'
website: 'https://aws.amazon.com/bedrock'
company: 'amazon'
logo_url: ''
category: 'devtools'
category_name: 'Outils de développement'
price: 'Freemium'
featured: false
rank: 9
alternatives:
  - azure-openai
  - vertex-ai
  - together-ai
  - fireworks-ai
  - openrouter
  - groq
date: '2025-09-21'
tags: [developer_tools, code_generation, infrastructure, deployment, development, devops, ci_cd, cloud, api, api_available, enterprise, secure]
i18n_source: '03ddec47ee00'
---

Bedrock est la façon dont beaucoup d'entreprises sur AWS utilisent des grands modèles de langage sans faire tourner d'infrastructure de modèle. Au lieu de signer des contrats séparés avec chaque labo d'IA, tu choisis dans un catalogue de modèles de fournisseurs comme Anthropic, Meta, Mistral et Amazon lui-même, et tu les appelles via une seule API. Les données restent dans ton compte AWS, ce qui compte pour les équipes aux exigences de sécurité, de confidentialité et de conformité, et ça marche avec les outils IAM, réseau et logs qu'elles utilisent déjà.

Autour des modèles, les pièces pour construire une vraie application. Knowledge Bases relient un modèle à tes propres documents pour des réponses augmentées par récupération. Les agents permettent à un modèle de planifier et d'appeler des API pour mener des tâches, et AgentCore fournit l'infrastructure pour faire tourner des agents bâtis avec n'importe quel framework. Les garde-fous bloquent des sujets non voulus et des données sensibles, et peuvent vérifier l'ancrage factuel des réponses. Il y a aussi des outils pour évaluer des modèles les uns contre les autres, les ajuster (fine-tuning), et mettre des prompts en cache pour couper le coût.

Bedrock facture à l'usage, en général au token pour l'usage à la demande, avec le traitement par lots et de la capacité réservée quand les charges sont stables. L'éventail de modèles et la vitesse d'arrivée des nouveaux diffèrent des API propres des fournisseurs, donc un modèle peut arriver sur Bedrock plus tard que sur le site du labo. Les concurrents sont Azure AI Foundry et Vertex AI de Google Cloud. Les équipes déjà engagées sur AWS choisissent en général Bedrock pour le confort et la facturation consolidée.
