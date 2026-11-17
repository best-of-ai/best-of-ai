---
title: 'AWS Rekognition'
name: 'AWS Rekognition'
subtitle: "Serviço de visão computacional da Amazon para analisar imagens e vídeos"
slug: 'aws-rekognition'
description: "Amazon Rekognition é o serviço de visão computacional da AWS. Suas APIs detectam objetos, texto, rostos e conteúdo inseguro em imagens e vídeos, e desenvolvedores podem treinar modelos personalizados para reconhecer seus próprios rótulos."
website: 'https://aws.amazon.com/rekognition/'
company: 'amazon'
logo_url: ''
category: 'computer-vision'
category_name: "Visão computacional"
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

Rekognition permite que desenvolvedores adicionem análise de imagens e vídeos a um aplicativo sem treinar um modelo do zero. Você envia uma imagem ou um vídeo e recebe objetos e cenas detectados, texto encontrado na imagem, rostos com atributos como uso de óculos ou sorriso e sinalizações de conteúdo inseguro ou impróprio. O serviço funciona com fotos, arquivos de vídeo armazenados e transmissões ao vivo, e integra-se ao S3, Lambda e outros serviços da AWS.

Os recursos relacionados a rostos estão entre os mais usados. O serviço pode comparar dois rostos, pesquisar uma coleção de rostos armazenados e executar verificações de vivacidade para distinguir uma pessoa real de uma foto ou reprodução durante a verificação de identidade. O Custom Labels treina um classificador com um pequeno conjunto de imagens rotuladas para reconhecer itens específicos da empresa, como defeitos de produtos ou um logotipo. A moderação de conteúdo é amplamente usada por plataformas que hospedam arquivos enviados por usuários.

A cobrança é feita por imagem ou por minuto de vídeo analisado, com uma modalidade gratuita inicial. O reconhecimento facial é uma área controversa, e a AWS restringiu alguns usos, sobretudo por forças policiais; por isso, quem desenvolve soluções com o serviço deve consultar a política e as regras de privacidade da região. A precisão depende da qualidade da imagem, do tipo de rosto e da iluminação. Google Cloud Vision e Azure AI Vision são as alternativas mais próximas.
