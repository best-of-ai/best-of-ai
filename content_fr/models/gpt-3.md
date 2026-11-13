---
title: 'GPT-3'
name: 'GPT-3'
slug: 'gpt-3'
subtitle: "Le modèle de 2020 qui a montré pour la première fois que l'apprentissage few-shot à grande échelle était possible"
description: "Le modèle de 2020 qui a montré pour la première fois que l'apprentissage few-shot à grande échelle était possible"
company: 'openai'
model_type: 'Language'
logo_url: ''
product_url: 'https://openai.com/index/gpt-3-apps/'
price: 'Paid'
rank: 6
release_date: '2020-06-11'
param_count: '175B'
context_window_tokens: 2048
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [API]
runs_at_home: false
platforms: ['API']
date: '2026-07-16'
tags: [llm, foundation-model, legacy]
i18n_source: '15468c089d4b'
---

GPT-3 est le modèle de langage qu'OpenAI a décrit dans son article de mai 2020, « Language Models are Few-Shot Learners », et ouvert via une API en bêta le 11 juin 2020. Avec 175 milliards de paramètres, il était d'un ordre de grandeur au-dessus de GPT-2, et le résultat principal était qu'un seul modèle, avec seulement quelques exemples dans le prompt, pouvait faire de la traduction, de l'arithmétique et de la réponse à des questions, sans fine-tuning propre à la tâche. La fenêtre de contexte était petite pour les standards d'après, autour de 2 048 tokens.

Les résultats d'apprentissage few-shot de l'article sont ce qui a fait de GPT-3 un tournant, et pas seulement un GPT-2 plus gros. Il a montré que l'échelle seule, sans changement d'architecture, produisait des capacités qualitativement nouvelles, et il a lancé la course entre labos pour entraîner des modèles toujours plus grands. GPT-3 lui-même n'était accessible que par API et ses poids n'ont jamais été publiés, et OpenAI a fini par retirer le modèle d'origine au profit de ses successeurs ajustés par instructions.
