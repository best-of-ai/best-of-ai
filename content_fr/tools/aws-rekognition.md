---
title: 'AWS Rekognition'
name: 'AWS Rekognition'
subtitle: "Le service de vision par ordinateur d'Amazon dans le cloud, pour l'analyse d'images et de vidéo, dont la détection d'objets..."
slug: 'aws-rekognition'
description: "Amazon Rekognition est le service de vision par ordinateur d'AWS. Ses API détectent des objets, du texte, des visages et du contenu dangereux dans des images et de la vidéo, et les développeurs peuvent entraîner des modèles sur mesure pour trouver leurs propres étiquettes."
website: 'https://aws.amazon.com/rekognition/'
company: 'amazon'
logo_url: ''
category: 'computer-vision'
category_name: "Vision par ordinateur"
price: 'Paid'
featured: false
rank: 9
alternatives:
  - google-cloud-vision
  - azure-ai-vision
  - clarifai
  - roboflow
  - landing-ai
date: '2025-10-01'
tags: [api_available, cloud_based, image_based, training, model_based, easy_to_use, ai_powered, intelligent]
i18n_source: '20aefe9aa5b9'
---

Rekognition permet aux développeurs d'ajouter l'analyse d'images et de vidéo à une application sans entraîner un modèle de zéro. Tu envoies une image ou une vidéo et tu récupères les objets et les scènes détectés, le texte trouvé dans l'image, les visages avec des attributs comme les lunettes ou le sourire, et des drapeaux pour le contenu dangereux ou inapproprié. Ça marche sur des photos, des fichiers vidéo stockés et des flux vidéo en direct, et ça s'intègre à S3, Lambda et d'autres services AWS.

Les fonctions liées au visage sont parmi les plus utilisées. Il peut comparer deux visages, chercher dans une collection de visages stockés, et lancer des contrôles de vivacité qui distinguent une vraie personne d'une photo ou d'une rediffusion pendant une vérification d'identité. Custom Labels entraîne un classifieur sur un petit jeu d'images étiquetées pour reconnaître des choses propres à ton activité, comme des défauts produit ou un logo de marque. La modération de contenu est très utilisée par les plateformes qui hébergent des envois d'utilisateurs.

La facturation est par image ou par minute de vidéo analysée, avec une offre gratuite au départ. La reconnaissance faciale a été un sujet controversé, et AWS a restreint certains usages, surtout par les forces de l'ordre, donc quiconque construit dessus doit relire la politique et les règles de confidentialité de sa région. La justesse dépend de la qualité de l'image et du type de visage et de lumière. Google Cloud Vision et Azure AI Vision sont les alternatives les plus proches.
