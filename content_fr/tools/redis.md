---
title: 'Redis'
name: 'Redis'
subtitle: 'Base en mémoire utilisée pour le cache et la recherche vectorielle'
slug: 'redis'
description: 'Redis est un magasin de données en mémoire utilisé pour le cache, les files, les sessions et les fonctions temps réel. Il prend aussi en charge la recherche vectorielle, le JSON et le cache sémantique, donc les équipes s''en servent pour des applications d''IA qui ont besoin de lectures rapides.'
website: 'https://redis.io'
logo_url: ''
category: 'devtools'
category_name: 'Outils de développement'
price: 'Freemium'
featured: false
rank: 8
alternatives:
  - pinecone
  - qdrant
  - weaviate
  - mongodb-atlas
  - elasticsearch
date: '2026-11-05'
tags: [developer_tools, code_generation, infrastructure, deployment, development, devops, ci_cd, cloud, api, collaboration, fast]
i18n_source: '294da6bd62ae'
---

Redis stocke les données en mémoire, ce qui rend la lecture et l'écriture extrêmement rapides. Les développeurs s'en servent comme cache devant une base plus lente, comme magasin de sessions pour les utilisateurs connectés, comme file de messages, et pour des classements, de la limitation de débit et des compteurs. Ses types de données, comme les listes, les ensembles, les ensembles triés, les hashes et les streams, rendent ces motifs faciles à construire avec des commandes simples. C'est l'une des briques d'infrastructure les plus déployées du web.

Pour l'IA, Redis a ajouté la recherche vectorielle, pour que les applications stockent des embeddings et trouvent des éléments proches, pour la génération augmentée par récupération, les recommandations et la recherche sémantique. Le cache sémantique garde les réponses à d'anciennes questions et les renvoie pour des questions nouvelles proches, ce qui réduit le coût et la latence des appels aux modèles de langage. Redis garde aussi la mémoire de conversation des agents. Il tourne en logiciel open source, en Redis Cloud et en déploiements entreprise.

La licence a fait débat : Redis a changé sa licence d'une façon qui a mené à un fork communautaire appelé Valkey, soutenu par des fournisseurs cloud, puis a de nouveau proposé une option de licence open source. La mémoire coûte plus cher que le disque, donc les grands jeux de données peuvent coûter cher, et la durabilité demande de la configuration. Parmi les alternatives : Valkey, Memcached pour un cache simple, DragonflyDB, et des services cloud comme Amazon ElastiCache. Redis convient aux applications où la vitesse est critique.
