---
title: 'Grok-1'
name: 'Grok-1'
slug: 'grok-1'
subtitle: 'Das erste Modell von xAI, später unter Apache 2.0 mit offenen Gewichten veröffentlicht'
description: 'Das erste Modell von xAI, später unter Apache 2.0 mit offenen Gewichten veröffentlicht'
company: 'xai'
model_type: 'Language'
logo_url: ''
product_url: 'https://x.ai/blog/grok-os'
price: 'Free'
rank: 5
release_date: '2023-11-04'
param_count: '314B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: false
platforms: ['Hugging Face', 'GitHub']
date: '2026-07-16'
tags: [llm, open-weight, legacy]
i18n_source: '1027c6ce5f38'
---
Grok-1 ist das erste große Sprachmodell von xAI, dem KI-Labor von Elon Musk. Ab November 2023 wurde es zunächst X-Premium+-Abonnenten angeboten. Es ist ein Mixture-of-Experts-Modell mit 314 Milliarden Parametern, acht Experten und Top-2-Routing. Für jedes Token wird dadurch nur etwa ein Viertel der Gewichte aktiviert. Das Kontextfenster umfasst 8192 Tokens. Am 17. März 2024 veröffentlichte xAI die Basisgewichte und Architektur unter Apache 2.0 als Open Source. Damit war Grok-1 damals das größte öffentlich verfügbare MoE-Modell mit offenen Gewichten. Die Veröffentlichung enthielt nur die rohen vortrainierten Gewichte, keine instruction-tuned oder chatfertige Version. Daher nutzten es hauptsächlich Forschende und Infrastrukturteams statt Endnutzer. xAI trainierte Grok-1 mit einem eigenen JAX- und Rust-Stack statt PyTorch. Das Pretraining war im Oktober 2023 abgeschlossen, bevor Grok-2 es später 2024 ablöste.
