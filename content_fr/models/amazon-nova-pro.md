---
title: 'Amazon Nova Pro'
name: 'Amazon Nova Pro'
slug: 'amazon-nova-pro'
subtitle: "Le modèle de fondation multimodal phare d'Amazon sur Bedrock"
description: "Le modèle de fondation multimodal phare d'Amazon sur Bedrock"
company: 'amazon'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://aws.amazon.com/ai/generative-ai/nova/'
price: 'Paid'
rank: 5
release_date: '2024-12-03'
param_count: 'Undisclosed'
context_window_tokens: 300000
modality: [text, image, video]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.8
output_price_usd_per_m: 3.2
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['AWS Bedrock']
date: '2026-07-16'
tags: [llm, multimodal, enterprise, api]
extra_model_types: ['Reasoning']
i18n_source: 'fc6b13057355'
---

Amazon Nova Pro est le modèle généraliste phare de la famille Nova d'Amazon, annoncé en décembre 2024 et servi via Amazon Bedrock. Il prend du texte, de l'image et de la vidéo en entrée, renvoie du texte, et prend en charge une fenêtre de contexte de 300 000 tokens. Le tarif est de 0,80 $ par million de tokens en entrée et de 3,20 $ par million de tokens en sortie. Amazon le présentait comme le modèle des tâches complexes, comme le raisonnement en plusieurs étapes, l'analyse de documents et les flux de travail agentiques, là où la capacité plus légère de Nova Lite ne suffit pas.

Amazon a insisté sur le couple précision et coût de Nova Pro face à des modèles de palier frontière comparables. Il sert de modèle enseignant pour la distillation de Bedrock : on peut entraîner des Nova Micro ou Lite moins chers sur les sorties de Nova Pro. C'est la principale réponse d'Amazon à des modèles comme GPT-4o et Gemini sur le marché des entreprises de Bedrock, pour des clients déjà investis dans l'infrastructure AWS.
