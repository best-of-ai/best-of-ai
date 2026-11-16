---
title: 'CLIP (LAION variant)'
name: 'CLIP (LAION variant)'
slug: 'clip-laion-variant'
subtitle: 'Offenes CLIP-Vision-Language-Embedding-Modell von LAION mit neu trainierten Gewichten'
description: 'Offenes CLIP-Vision-Language-Embedding-Modell von LAION mit neu trainierten Gewichten'
company: 'laion'
model_type: 'Embedding'
logo_url: ''
product_url: 'https://laion.ai/'
price: 'Free'
rank: 4
release_date: '2022-09-15'
param_count: '428M'
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [embedding, open-weight, vision, self-hosted]
i18n_source: '40efbd85bd2a'
---
Diese CLIP-Variante ist ein erneutes Training der ursprünglichen CLIP-Architektur von OpenAI mit offenen Gewichten. Sie wurde von LAION erstellt und über das Projekt open_clip statt von OpenAI selbst verbreitet. Das Modell verwendet den Vision-Transformer ViT-L/14, hat etwa 428 Millionen Parameter und wurde mit LAION-2B trainiert – einer englischsprachigen Teilmenge von zwei Milliarden Bild-Text-Paaren aus dem größeren LAION-5B-Datensatz. Das Training lief auf 384 A100-GPUs des Supercomputers JUWELS. Wie das ursprüngliche CLIP ordnet es Bilder und Texte einem gemeinsamen Embedding-Raum zu. Dadurch sind Zero-Shot-Bildklassifizierung, Bild-Text-Retrieval und Ähnlichkeitssuche ohne aufgabenspezifisches Fine-Tuning möglich. Auf ImageNet-1k erreicht es eine Zero-Shot-Genauigkeit von etwa 75,3 Prozent. Da die Gewichte unter einer offenen Lizenz stehen und auf Hugging Face verfügbar sind, hat es sich als gängiger Ersatz für die geschlossenen CLIP-Checkpoints von OpenAI in offenen Bildsuch-, Bildbeschreibungs- und generativen Kunst-Pipelines etabliert. Es dient auch in mehreren Stable-Diffusion-Varianten als Text-Encoder.
