---
title: 'Gemini 1.5 Pro'
name: 'Gemini 1.5 Pro'
slug: 'gemini-1-5-pro'
subtitle: "Le modèle de Google de 2024 qui a introduit la fenêtre de contexte d'un million de tokens"
description: "Le modèle de Google de 2024 qui a introduit la fenêtre de contexte d'un million de tokens"
company: 'google-deepmind'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://deepmind.google/technologies/gemini/'
price: 'Paid'
rank: 6
release_date: '2024-02-15'
param_count: 'Undisclosed'
context_window_tokens: 1000000
modality: [text, image, audio, video]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 1.25
output_price_usd_per_m: 5
api_available: true
mmlu_score: 85.9
humaneval_score: 71.9
lmarena_score: 1260
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Gemini app', 'Google Vertex AI', 'API']
date: '2026-07-16'
tags: [llm, multimodal, long-context, api, legacy]
extra_model_types: ['Code']
i18n_source: 'eceffcd944e2'
---

Gemini 1.5 Pro est le modèle qui a introduit les fenêtres de contexte d'un million de tokens dans une API grand public, publié par Google en février 2024 et passé en disponibilité générale en mai de la même année. Il lit texte, images, audio et vidéo dans un seul prompt, et Google a montré qu'il tenait une heure entière de vidéo, ou des centaines de pages de documents, en contexte d'un coup, bien au-delà de ce que GPT-4 ou Claude proposaient alors. Il utilise une architecture en mélange d'experts, dont Google disait qu'elle lui permettait d'égaler ou de dépasser le plus grand Gemini 1.0 Ultra sur la plupart des benchmarks, tout en coûtant moins cher à faire tourner.

Google a baissé le prix de 1.5 Pro deux fois en 2024, pour finir autour de 1,25 $ par million de tokens en entrée et 5 $ par million de tokens en sortie, pour les prompts sous 128 000 tokens. Il a obtenu environ 85,9 au MMLU et 71,9 au HumanEval, et il est devenu le modèle de production par défaut de Google pendant la plus grande partie de 2024, via l'app Gemini, Vertex AI et l'API Gemini. Google l'a remplacé comme phare par Gemini 2.5 Pro en 2025, même si 1.5 Pro reste disponible via l'API pour les intégrations existantes.
