---
title: 'Elasticsearch'
name: 'Elasticsearch'
subtitle: 'Moteur de recherche distribué et base vectorielle'
slug: 'elasticsearch'
description: 'Elasticsearch est un moteur de recherche et d''analytique open source. Il gère la recherche plein texte, vectorielle et hybride sur de grandes quantités de données, et il est largement utilisé pour la recherche de site, l''analyse de logs et la récupération dans les applications d''IA.'
website: 'https://www.elastic.co/elasticsearch'
company: 'elastic-nv'
logo_url: ''
category: 'search-engines'
category_name: 'Moteurs de recherche'
price: 'Freemium'
featured: false
rank: 9
alternatives:
  - algolia-ai-search
  - typesense
  - meilisearch
  - vectara
  - weaviate
date: '2026-11-05'
tags: [search, ai_assistant, discovery, information, query, web_search, answers, knowledge, retrieval, analytics]
i18n_source: '9de9525c0d39'
---

Elasticsearch stocke les documents en JSON et les indexe pour que les recherches reviennent en millisecondes, même sur des milliards d'enregistrements. Il a commencé comme un moteur de recherche plein texte pour des choses comme les catalogues produits et la recherche de site, et il est aussi beaucoup utilisé pour les logs, les métriques et les données de sécurité. C'est le cœur de l'Elastic Stack, qui ajoute Kibana pour les dashboards, et des outils d'ingestion pour faire entrer les données. Les entreprises s'en servent partout où elles ont besoin de chercher ou d'agréger vite un grand volume de données riches en texte.

Pour l'IA, Elasticsearch sert de base vectorielle et de couche de récupération. Il peut stocker des embeddings, lancer des recherches sémantiques et hybrides qui mêlent correspondance de mots-clés et similarité vectorielle, et reranker les résultats avant qu'ils aillent vers un modèle de langage. Ça en fait un composant courant des systèmes de génération augmentée par la recherche. Des langages de requête comme ES|QL prennent en charge l'analytique, et la plateforme inclut des outils pour se connecter à des LLM et construire des agents au-dessus des données de l'entreprise.

On peut gérer Elasticsearch soi-même sur ses serveurs ou utiliser Elastic Cloud, en forme hébergée ou serverless. Le logiciel est disponible sous des options de licence open source, avec certaines fonctions réservées aux abonnements payants. Bien le faire tourner demande du savoir-faire sur le dimensionnement de cluster, l'indexation et les mises à jour, donc beaucoup d'équipes préfèrent le service managé. OpenSearch, un fork surtout maintenu par Amazon, Algolia et Meilisearch sont des alternatives, et des bases vectorielles dédiées comme Pinecone concurrencent l'usage IA.
