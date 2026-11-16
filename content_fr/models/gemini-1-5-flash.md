---
title: 'Gemini 1.5 Flash'
name: 'Gemini 1.5 Flash'
slug: 'gemini-1-5-flash'
subtitle: 'Le palier Gemini 1.5 rapide et peu coûteux de Google, distillé à partir de Gemini 1.5 Pro'
description: 'Le palier Gemini 1.5 rapide et peu coûteux de Google, distillé à partir de Gemini 1.5 Pro'
company: 'google-deepmind'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://deepmind.google/technologies/gemini/flash/'
price: 'Paid'
rank: 7
release_date: '2024-05-14'
param_count: 'Undisclosed'
context_window_tokens: 1000000
modality: [text, image, audio, video]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.075
output_price_usd_per_m: 0.3
api_available: true
mmlu_score: 78.9
access_methods: [API, Chat UI]
runs_at_home: false
platforms: ['Google AI Studio', 'Vertex AI', 'Gemini app']
date: '2026-07-16'
tags: [llm, multimodal, api, low-cost]
i18n_source: '33dfe5878945'
---

Gemini 1.5 Flash est le palier rapide et peu coûteux de la génération Gemini 1.5 chez Google, sorti en mai 2024 comme version distillée de Gemini 1.5 Pro. Google l'a construit en apprenant à un modèle plus petit à imiter les sorties de Pro, ce qui a gardé une bonne part du raisonnement de Pro tout en coupant nettement la latence et le coût. Il a la même fenêtre de contexte d'un million de tokens que Pro et traite le texte, les images, l'audio et la vidéo, ce qui en fait un choix pratique pour les tâches à fort volume, comme résumer de longs documents ou légender de la vidéo, là où le prix de Pro monterait vite.

Au lancement, Google le tarifait à 0,075 $ par million de tokens en entrée et 0,30 $ par million de tokens en sortie, pour les prompts sous 128 000 tokens, parmi les tarifs d'API de classe frontière les moins chers à l'époque. Il est disponible via Google AI Studio, Vertex AI et l'app Gemini, et il est devenu l'offre gratuite par défaut pour beaucoup d'utilisateurs de l'app. Google a depuis déplacé l'essentiel du nouveau développement vers les générations Flash 2.0 et 2.5, donc 1.5 Flash est surtout gardé pour la compatibilité des anciennes intégrations API.
