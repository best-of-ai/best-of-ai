---
title: 'Azure Content Moderator'
name: 'Azure Content Moderator'
subtitle: "Le service d'IA d'Azure de Microsoft pour détecter du contenu potentiellement offensant, indésirable ou risqué dans le t..."
slug: 'azure-content-moderator'
description: "Azure Content Moderator est l'ancien service de Microsoft pour détecter du texte, des images et de la vidéo offensants ou risqués. Il est déprécié et prévu pour l'arrêt, et Azure AI Content Safety est le remplaçant."
website: 'https://azure.microsoft.com/en-us/products/ai-services/ai-content-moderator'
company: 'microsoft'
logo_url: ''
category: 'content-moderation'
category_name: "Modération de contenu"
price: 'Paid'
featured: false
rank: 7
alternatives:
  - hive-moderation
  - perspective-api
  - aws-rekognition
  - clarifai
date: '2025-10-01'
tags: [collaboration, image_based, model_based, ai_powered, intelligent, platform, tool, service]
i18n_source: '937cdb14870b'
---

Content Moderator était l'outil de Microsoft pour contrôler le contenu généré par les utilisateurs. Il scannait le texte pour les insultes et les données personnelles, analysait les images pour le contenu adulte ou suggestif, et filtrait la vidéo, en renvoyant des scores et des drapeaux que les plateformes pouvaient utiliser pour filtrer ou envoyer des éléments à une revue humaine. Des communautés en ligne, des places de marché et des apps avec des envois d'utilisateurs s'en servaient comme première ligne de défense automatisée.

Microsoft a déprécié le service et n'autorise plus de nouveaux projets, en orientant les clients vers Azure AI Content Safety. Le service plus récent utilise des modèles plus avancés, gère plusieurs niveaux de gravité sur des catégories comme la haine, le contenu sexuel, la violence et l'automutilation, prend en charge beaucoup plus de langues, et ajoute des fonctions tournées vers l'IA générative, dont des prompt shields et la détection d'ancrage. Les projets Content Moderator existants continuent de marcher jusqu'à la date d'arrêt.

Quiconque utilise encore Content Moderator doit prévoir une migration vers Azure AI Content Safety ou un autre fournisseur avant la fin du service. Parmi les alternatives : le point de terminaison de modération d'OpenAI, les fonctions de modération de contenu de Google Cloud, la modération d'Amazon Rekognition, Hive, et Perspective API pour la toxicité du texte. Les nouveaux projets doivent commencer avec Content Safety. Cette fiche reste pour référence, parce que d'anciens tutoriels et de la documentation parlent encore de Content Moderator.
