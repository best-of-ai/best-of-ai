---
title: 'Amazon SageMaker'
name: 'Amazon SageMaker'
subtitle: 'Plateforme AWS pour construire, entraîner et déployer des modèles de ML'
slug: 'amazon-sagemaker'
description: 'Amazon SageMaker est la plateforme d''AWS pour construire, entraîner et déployer des modèles de machine learning et d''IA. Elle inclut désormais SageMaker AI, un studio unifié pour le travail data et IA, et un lakehouse pour gérer les données à travers AWS.'
website: 'https://aws.amazon.com/sagemaker/'
company: 'amazon'
logo_url: ''
category: 'devtools'
category_name: 'Outils de développement'
price: 'Paid'
featured: false
rank: 8
alternatives:
  - vertex-ai
  - azure-ai-foundry
  - databricks
  - dataiku
  - datarobot
date: '2026-11-05'
tags: [developer_tools, code_generation, infrastructure, deployment, development, devops, ci_cd, cloud, api, collaboration, machine_learning, training]
i18n_source: 'a69e213128f4'
---

SageMaker a commencé comme un moyen de faire du machine learning sur AWS sans gérer de serveurs. Les data scientists utilisent des notebooks pour préparer les données et écrire du code, puis entraînent des modèles sur du calcul managé qui monte selon le besoin. Une fois un modèle entraîné, SageMaker peut le déployer derrière un endpoint, surveiller sa performance et gérer les versions, ce qui transforme une expérience de notebook en service de production. Il prend en charge des frameworks courants comme PyTorch et TensorFlow.

Le produit s'est élargi. SageMaker AI couvre l'entraînement et le déploiement de modèles, y compris des modèles de fondation, avec des fonctions d'entraînement distribué sur de grands clusters, de fine-tuning et d'hébergement de modèles ouverts. SageMaker Unified Studio est un seul environnement pour l'ingénierie data, l'analytique et le travail d'IA, et SageMaker Lakehouse rassemble des données de S3, Redshift et d'autres sources sous un même jeu de permissions et de gouvernance. Pipelines, feature stores et suivi d'expériences soutiennent les équipes qui construisent des flux répétables.

SageMaker est facturé à l'usage sur le calcul, le stockage et les fonctions managées, et une offre gratuite couvre de petites quantités les premiers mois. Son ampleur est aussi son défaut : beaucoup de services, de réglages et de dimensions de prix le rendent compliqué, et il est facile de trop dépenser. Les équipes déjà sur AWS tiennent à l'intégration avec IAM, S3 et les contrôles de sécurité. Google Vertex AI et Azure Machine Learning sont des concurrents directs, tandis que Databricks est une alternative courante pour les équipes très data. Pour appeler des modèles hébergés sans gérer l'entraînement, Amazon Bedrock est plus simple.
