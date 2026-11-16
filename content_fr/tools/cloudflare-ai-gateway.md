---
title: 'Cloudflare AI Gateway'
name: 'Cloudflare AI Gateway'
subtitle: "Observabilité, contrôles et routage multi-fournisseurs pour les applications d'IA"
slug: 'cloudflare-ai-gateway'
description: "Cloudflare AI Gateway se place entre une application et les fournisseurs de modèles d'IA. Il fournit de l'analytique, des logs, du cache, de la limitation de débit, des tentatives et un repli de modèle pour que les développeurs observent l'usage et maîtrisent les coûts."
website: 'https://developers.cloudflare.com/ai-gateway/'
company: 'cloudflare'
logo_url: ''
category: 'devtools'
category_name: 'Outils de développement'
price: 'Freemium'
featured: false
rank: 5
alternatives:
  - portkey
  - litellm
  - helicone
  - langfuse
  - openrouter
  - vercel-ai-platform
  - eden-ai
date: '2026-07-17'
tags: [developer_tools, code_generation, infrastructure, deployment, development, devops, ci_cd, cloud, api, cloud_based, analytics, model_based]
i18n_source: '76831d31774b'
---

AI Gateway est un proxy pour les appels aux modèles de langage. Un développeur pointe les requêtes de son app vers une URL Cloudflare au lieu de celle du fournisseur, et la passerelle les transmet tout en enregistrant ce qui se passe. Ça donne un tableau de bord des requêtes, des tokens, des coûts et des erreurs à travers des fournisseurs comme OpenAI, Anthropic et Google.

Il ajoute des fonctions de contrôle. Le cache renvoie des réponses stockées pour les requêtes répétées, pour économiser de l'argent et du temps, les limites de débit protègent les budgets, et les tentatives et les replis basculent vers un autre modèle quand l'un échoue. Les logs aident à déboguer les prompts, et des fonctions de garde-fous et de gestion de clés appuient la sécurité.

Les fonctions de base sont disponibles sur les offres Cloudflare, beaucoup d'entre elles gratuites, avec quelques limites sur le stockage des logs. C'est utile pour les applications en production qui appellent plusieurs modèles. Parmi les alternatives : Portkey, LiteLLM, Helicone, OpenRouter et Kong AI Gateway. Cloudflare AI Gateway convient aux développeurs qui veulent de la visibilité et du contrôle sur le trafic des modèles.
