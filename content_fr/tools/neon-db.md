---
title: 'Neon'
name: 'Neon'
slug: 'neon-db'
description: "Neon est un service de base Postgres serverless, avec mise à l'échelle automatique, scale to zero et branchement instantané de bases. Il fait maintenant partie de Databricks et est courant pour les apps, les previews et les agents d'IA qui ont besoin de beaucoup de bases."
website: 'https://neon.tech'
company: 'neon'
logo_url: ''
category: 'database-tools'
category_name: "Outils de bases de données"
price: 'Freemium'
featured: false
rank: 8
alternatives:
  - supabase-ai
  - planetscale
  - turso
  - mongodb-atlas
date: '2026-06-15'
tags: [collaboration, model_based, fast, ai_powered, intelligent, platform, tool, service]
i18n_source: 'c4e0f3856856'
---

Neon a reconstruit Postgres pour le cloud en séparant le stockage du calcul. Cette conception permet à une base de monter en charge sous la charge et de redescendre à zéro au repos, pour que tu paies l'usage au lieu de garder un serveur allumé. Les développeurs ont un Postgres standard, donc les outils, drivers et extensions existants fonctionnent, y compris pgvector pour stocker des embeddings dans des applications d'IA.

La fonction qui se démarque, c'est le branching. Comme le stockage est en copy-on-write, tu peux créer une copie complète d'une base en quelques secondes, comme une branche Git, pour tester une migration, lancer un environnement de preview pour chaque pull request, ou donner à chaque développeur une copie isolée. La même capacité rend Neon attractif pour les agents de code par IA et les plateformes qui démarrent beaucoup de bases de courte durée. Le pooling de connexions, les réplicas de lecture et les intégrations avec Vercel et d'autres plateformes sont disponibles.

Neon a une offre gratuite adaptée aux petits projets, avec des offres payantes à l'usage. Databricks a acquis Neon pour soutenir des bases pour les agents d'IA, et a dit que le service continuerait. Les démarrages à froid après un scale to zero peuvent ajouter un petit délai, et les coûts dépendent du temps de calcul et du stockage. Supabase propose Postgres avec une boîte à outils backend plus large, PlanetScale et AWS Aurora Serverless sont en concurrence, et CockroachDB sert les besoins distribués. Neon est un choix courant pour les apps web modernes.
