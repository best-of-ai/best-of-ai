---
title: 'CLIP'
name: 'CLIP'
slug: 'clip'
subtitle: 'Grundlegendes Bild-Text-Kontrastmodell von OpenAI, das vielen modernen multimodalen KI-Systemen zugrunde liegt'
description: 'Grundlegendes Bild-Text-Kontrastmodell von OpenAI, das vielen modernen multimodalen KI-Systemen zugrunde liegt'
company: 'openai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://openai.com/index/clip/'
price: 'Free'
rank: 8
release_date: '2021-01-05'
param_count: '428M'
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'GitHub']
date: '2026-07-16'
tags: [multimodal, open-weight, vision, legacy, foundation-model]
i18n_source: 'bc970f441b1f'
---

CLIP (Contrastive Language-Image Pre-training) ist ein Modell von OpenAI aus dem Januar 2021, das Bilder passenden Textbeschreibungen zuordnet. Es wurde mit 400 Millionen Bild-Text-Paaren aus dem Internet trainiert. Ein kontrastives Lernziel zieht Embeddings passender Bilder und Texte zusammen und rückt unpassende Paare auseinander. Die größte veröffentlichte Variante basiert auf dem Vision-Transformer ViT-L/14 und einem Text-Transformer mit 63 Millionen Parametern; insgesamt umfasst sie etwa 428 Millionen Parameter. Statt nur für eine einzelne Aufgabe trainiert zu werden, lernt CLIP einen allgemeinen gemeinsamen Embedding-Raum für Bilder und Text. So kann es Bilder ohne aufgabenspezifisches Fine-Tuning klassifizieren, indem es ein Bild mit einer Auswahl von Textetiketten vergleicht.

Die große Wirkung von CLIP zeigte sich erst nach der Veröffentlichung und ging über Benchmarkwerte hinaus. Bild- und Text-Encoder wurden zur Grundlage zahlreicher späterer Systeme, darunter die Bildgenerierungspipeline von DALL-E 2, die Textsteuerung von Stable Diffusion sowie viele Werkzeuge für Bildsuche und Retrieval. Meta, Salesforce und andere Labore veröffentlichten eigene CLIP-Varianten und Fine-Tunes. Die ursprünglichen, unter MIT-Lizenz auf GitHub und Hugging Face veröffentlichten Gewichte bleiben jedoch auch Jahre später ein häufiger Ausgangspunkt für multimodale Projekte.
