---
title: 'IDEFICS2'
name: 'IDEFICS2'
slug: 'idefics2'
subtitle: "Modèle vision-langage ouvert de Hugging Face, conçu pour les questions sur documents et graphiques"
description: "Modèle vision-langage ouvert de Hugging Face, conçu pour les questions sur documents et graphiques"
company: 'hugging-face'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://huggingface.co/blog/idefics2'
price: 'Free'
rank: 5
release_date: '2024-04-15'
param_count: '8B'
context_window_tokens: 32768
modality: [text, image]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, vision]
i18n_source: 'd3fac35a3fdd'
---

IDEFICS2 est le modèle vision-langage ouvert de Hugging Face, sorti en avril 2024 comme suite à son modèle IDEFICS précédent. Il compte 8 milliards de paramètres. Il combine Mistral-7B comme base de langage et un encodeur de vision SigLIP, et il traite les images à leur résolution et leur rapport d'aspect d'origine, au lieu de tout forcer dans un recadrage carré fixe. Ce choix, plus un entraînement sur un mélange plus efficace de tokens d'image, lui donne un avantage net sur la compréhension de documents, la lecture de graphiques et les tâches chargées en OCR, par rapport à des modèles plusieurs fois plus grands, dont LLaVA-NeXT-34B. Hugging Face a publié les poids sous Apache 2.0, ce qui le rend ouvert à l'usage commercial et au fine-tuning, sans restriction de licence. Il est prévu pour tourner en auto-hébergé, pas via une API hébergée, dans la logique de Hugging Face de garder des bases vision-langage ouvertes solides à disposition des chercheurs et des développeurs.
