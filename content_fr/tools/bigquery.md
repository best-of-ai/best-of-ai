---
title: 'BigQuery'
name: 'BigQuery'
subtitle: "Entrepôt de données serverless de Google Cloud"
slug: 'bigquery'
description: "BigQuery est l'entrepôt de données serverless de Google Cloud. On interroge de très grands jeux de données en SQL, on construit des modèles de machine learning en SQL avec BigQuery ML, et Gemini aide à écrire les requêtes."
website: 'https://cloud.google.com/bigquery'
company: 'google'
logo_url: ''
category: 'data'
category_name: 'Données'
price: 'Paid'
featured: false
rank: 8
alternatives:
  - snowflake
  - databricks
  - motherduck
  - dbt-cloud
date: '2026-11-05'
tags: [data_analysis, analytics, business, insights, visualization, data_science, reporting, dashboards, sql, cloud_based, machine_learning, training]
i18n_source: '902eae4f55c8'
---

BigQuery permet aux équipes d'analyser d'énormes volumes de données sans gérer de serveurs. On charge des données depuis des fichiers, des bases, des flux ou d'autres services Google, on écrit du SQL, et BigQuery répartit le travail sur de nombreuses machines et renvoie les résultats vite, que la table compte des millions ou des billions de lignes. Comme le stockage et le calcul sont séparés et managés, il n'y a pas de cluster à dimensionner ou à régler, ce qui est une grande raison pour laquelle les équipes d'analytique l'apprécient.

Il a ajouté beaucoup de fonctions pour le travail moderne sur les données et l'IA. BigQuery ML permet aux analystes d'entraîner et de faire tourner des modèles, dont la prévision et la classification, avec des instructions SQL, et de se connecter à Gemini et à d'autres modèles pour générer du texte ou des embeddings depuis les requêtes. La recherche vectorielle prend en charge les charges de similarité et de retrieval. Gemini dans BigQuery aide à écrire et expliquer le SQL, à générer du code et à suggérer des transformations de données. Il se connecte aussi à Looker, Connected Sheets et des outils de BI tiers.

Les tarifs ont deux modèles : des frais à la demande selon le volume de données qu'une requête scanne, et un tarif de capacité pour du calcul réservé, plus des frais de stockage. Il y a un quota gratuit mensuel. Il est facile de lancer une requête chère par accident si les tables sont grandes et non partitionnées, donc les contrôles de coût comptent. Snowflake et Databricks sont les principaux concurrents, Amazon Redshift est l'équivalent chez AWS, et DuckDB couvre l'analyse locale plus petite. BigQuery convient aux équipes qui utilisent déjà Google Cloud.
