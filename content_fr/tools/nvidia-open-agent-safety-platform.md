---
title: 'NVIDIA Open Agent Safety Platform'
name: 'NVIDIA Open Agent Safety Platform'
subtitle: "Couche de sécurité open source qui peut mettre en quarantaine un agent d'IA déviant en quelques millisecondes"
slug: 'nvidia-open-agent-safety-platform'
description: "L'Open Agent Safety Platform de NVIDIA associe OpenShell, un runtime ouvert qui isole les agents, à Sentry, une couche de surveillance sur des DPU BlueField qui tourne à part de l'ordinateur de l'agent et peut le mettre en quarantaine."
website: 'https://developer.nvidia.com/'
company: 'nvidia'
logo_url: ''
category: 'cybersecurity'
category_name: 'Cybersécurité'
price: 'Free'
featured: false
rank: 5
alternatives:
  - lakera
  - patronus-ai
  - giskard
  - nightfall
date: '2026-09-28'
tags: [ai_powered, intelligent, platform, tool, service, solution, saas, online]
i18n_source: '9264e993765c'
---

La plateforme répond à une inquiétude de sécurité : les agents autonomes qui peuvent lancer des commandes et accéder à des données ont besoin de limites qu'un agent compromis ne peut pas désactiver. OpenShell est un runtime open source qui place chaque agent dans son propre bac à sable, avec des permissions fondées sur des politiques, et un vérificateur contrôle que les permissions accordées ne peuvent pas se combiner en quelque chose que l'opérateur n'avait pas prévu.

Sentry ajoute une application en dehors de la machine de l'agent. Il tourne sur des unités de traitement de données BlueField, à l'écart de l'hôte, donc il peut surveiller le comportement et isoler un agent rapidement même si l'hôte est compromis. NVIDIA l'a décrit comme un design de référence, avec de nombreux partenaires qui intègrent les pièces.

Le logiciel est open source et le composant hardware exige une infrastructure NVIDIA. Des analystes notent que prouver que les permissions sont cohérentes ne prouve pas qu'un agent est sûr dans tous les sens, et la relecture des actions d'un agent reste importante. Parmi les alternatives : des outils de bac à sable comme E2B et Daytona, le sandboxing d'Anthropic et d'OpenAI, et des startups de sécurité centrées sur les agents. La plateforme de NVIDIA convient aux organisations qui déploient des agents avec de forts besoins d'isolation.
