---
title: 'DVC'
name: 'DVC'
subtitle: 'Contrôle de version open source pour les jeux de données et les expériences de ML'
slug: 'dvc'
description: 'DVC, pour Data Version Control, est un outil open source pour versionner des jeux de données, des modèles et des expériences à côté du code dans Git. Il suit les gros fichiers stockés dans le cloud avec une interface proche de Git.'
website: 'https://dvc.org'
logo_url: ''
category: 'devtools'
category_name: 'Outils de développement'
price: 'Free'
featured: false
rank: 5
alternatives:
  - mlflow
  - zenml
  - metaflow
  - clearml
  - comet-ml
  - weights-biases
  - prefect
date: '2025-06-15'
tags: [developer_tools, code_generation, infrastructure, deployment, development, devops, ci_cd, cloud, api, open_source, cloud_based, machine_learning]
i18n_source: '18847a8c544f'
---

DVC résout un problème pour lequel Git n'a pas été conçu : les gros fichiers de données. Les data scientists suivent jeux de données et fichiers de modèles avec DVC, qui stocke de petits fichiers pointeurs dans Git et garde les données réelles dans un stockage cloud ou local comme S3 ou Google Cloud Storage. Récupérer un ancien commit ramène les données correspondantes.

Il prend aussi en charge des pipelines reproductibles. On définit des étapes qui prennent des données et du code en entrée et produisent des sorties, et DVC ne relance que ce qui a changé. Les expériences peuvent être suivies et comparées, et les métriques et graphiques sont stockés avec le dépôt. Le projet est désormais maintenu sous lakeFS.

DVC est gratuit et open source. Il demande d'être à l'aise avec Git et la ligne de commande. Les alternatives incluent lakeFS, Git LFS pour les cas plus simples, MLflow, Weights & Biases Artifacts et Pachyderm. DVC convient aux data scientists qui veulent un contrôle de version pour les données.
