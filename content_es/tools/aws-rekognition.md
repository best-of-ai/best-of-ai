---
title: 'AWS Rekognition'
name: 'AWS Rekognition'
subtitle: 'Servicio de visión artificial en la nube de Amazon para analizar imágenes y vídeo, con detección de objetos...'
slug: 'aws-rekognition'
description: 'Amazon Rekognition es el servicio de visión artificial de AWS. Sus APIs detectan objetos, texto, rostros y contenido inapropiado en imágenes y vídeo, y los desarrolladores pueden entrenar modelos propios para encontrar sus propias etiquetas.'
website: 'https://aws.amazon.com/rekognition/'
company: 'amazon'
logo_url: ''
category: 'computer-vision'
category_name: 'Visión artificial'
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

Rekognition permite a los desarrolladores añadir análisis de imagen y vídeo a una aplicación sin entrenar un modelo desde cero. Envías una imagen o un vídeo y recibes los objetos y escenas detectados, el texto que aparece en la imagen, rostros con atributos como gafas o sonrisa, y avisos de contenido inapropiado. Funciona con fotos, archivos de vídeo almacenados y transmisiones de vídeo en directo, y se integra con S3, Lambda y otros servicios de AWS.

Las funciones de rostros están entre las más usadas. Puede comparar dos caras, buscar en una colección de rostros almacenados y hacer comprobaciones de vida que distinguen a una persona real de una foto o una reproducción durante la verificación de identidad. Custom Labels entrena un clasificador con un conjunto pequeño de imágenes etiquetadas para reconocer cosas propias de tu negocio, como defectos de producto o el logotipo de una marca. La moderación de contenido la usan mucho las plataformas que alojan archivos subidos por usuarios.

Se cobra por imagen o por minuto de vídeo analizado, con un nivel gratuito al principio. El reconocimiento facial ha sido un terreno polémico y AWS ha restringido algunos usos, sobre todo por parte de las fuerzas del orden, así que quien construya sobre él debería revisar la política y las normas de privacidad de su región. La precisión depende de la calidad de la imagen, del tipo de rostro y de la iluminación. Google Cloud Vision y Azure AI Vision son las alternativas más cercanas.
