---
title: 'Temporal'
name: 'Temporal'
subtitle: "Plateforme d'exécution durable pour les flux de travail longs"
slug: 'temporal'
description: "Temporal est une plateforme open source pour exécuter des flux de travail en code, avec une exécution durable. Elle conserve l'état si un serveur tombe, pour que les tâches longues reprennent là où elles se sont arrêtées. On s'en sert pour les paiements, l'intégration, les pipelines de données et les agents d'IA."
website: 'https://temporal.io'
logo_url: ''
category: 'devtools'
category_name: "Outils de développement"
price: 'Freemium'
featured: false
rank: 7
alternatives:
  - inngest
  - trigger-dev
  - prefect
date: '2026-11-05'
tags: [developer_tools, code_generation, infrastructure, deployment, development, devops, ci_cd, cloud, api, collaboration]
i18n_source: 'db4f201d9543'
---

Temporal traite une partie difficile du logiciel fiable : faire survivre aux pannes des processus longs, en plusieurs étapes. Les développeurs écrivent les flux dans un langage ordinaire, comme Go, Java, Python ou TypeScript, et Temporal enregistre chaque étape et son état. Si un serveur tombe ou qu'un appel réseau échoue, le flux reprend là où il s'est arrêté, sans perdre l'avancement. Relances, délais et minuteurs sont intégrés.

Ça convient aux processus qui durent de quelques minutes à plusieurs mois, comme les flux de paiement, l'exécution des commandes, l'intégration client, le provisionnement d'infrastructure et le traitement de données. De plus en plus, les équipes s'en servent pour orchestrer des agents d'IA, quand les tâches appellent des modèles et des outils sur de longues durées et ont besoin de fiabilité et d'observabilité. Temporal Cloud fournit un service géré, et le serveur open source peut être auto-hébergé.

Temporal est gratuit et open source sous licence MIT, et Temporal Cloud est facturé à l'usage. Le modèle a une courbe d'apprentissage, et les équipes doivent faire tourner le service ou le payer. Les alternatives incluent AWS Step Functions, Apache Airflow pour les flux de données, Inngest, Restate, Camunda et des files comme Celery. Temporal convient aux équipes d'ingénierie qui construisent des processus critiques et longs.
