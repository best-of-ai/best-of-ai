---
title: 'Amazon Nova Lite'
name: 'Amazon Nova Lite'
slug: 'amazon-nova-lite'
subtitle: "Le palier multimodal Bedrock d'Amazon, à bas coût"
description: "Le palier multimodal Bedrock d'Amazon, à bas coût"
company: 'amazon'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://aws.amazon.com/ai/generative-ai/nova/'
price: 'Paid'
rank: 4
release_date: '2024-12-03'
param_count: 'Undisclosed'
context_window_tokens: 300000
modality: [text, image, video]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.06
output_price_usd_per_m: 0.24
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['AWS Bedrock']
date: '2026-07-16'
tags: [llm, multimodal, low-latency, api]
i18n_source: 'e235a3a5281e'
---

Amazon Nova Lite est un modèle multimodal de la famille Nova d'Amazon, annoncé en décembre 2024 à l'AWS re:Invent et disponible via Amazon Bedrock. Il accepte du texte, des images et de la vidéo en entrée et renvoie du texte, avec une fenêtre de contexte de 300 000 tokens. Le tarif est de 0,06 $ par million de tokens en entrée et de 0,24 $ par million de tokens en sortie. Amazon l'a placé comme l'option du milieu, entre Nova Micro, limité au texte, et le plus capable Nova Pro, pour des applications qui doivent traiter des images ou de la vidéo tout en gardant des réponses rapides et un coût bas.

Nova Lite concurrence des modèles multimodaux de taille comparable chez OpenAI et Google, et Amazon a surtout vendu la gamme Nova sur le rapport prix-performance plutôt que sur la tête des classements de benchmarks. Le fine-tuning et la distillation sont pris en charge sur Bedrock, donc on peut l'adapter à une tâche précise, comme la compréhension de documents ou les questions visuelles, sans payer un modèle plus gros au moment de l'inférence.
