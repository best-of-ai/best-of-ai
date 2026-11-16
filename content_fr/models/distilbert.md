---
title: 'DistilBERT'
name: 'DistilBERT'
slug: 'distilbert'
subtitle: "La version distillée de BERT par Hugging Face, 40 % plus petite, qui garde l'essentiel de ses performances"
description: "La version distillée de BERT par Hugging Face, 40 % plus petite, qui garde l'essentiel de ses performances"
company: 'hugging-face'
model_type: 'Language'
logo_url: ''
product_url: 'https://arxiv.org/abs/1910.01108'
price: 'Free'
rank: 7
release_date: '2019-10-02'
param_count: '66M'
context_window_tokens: 512
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, legacy, small-model]
i18n_source: '4bb37eb28b4c'
---

DistilBERT est une version compressée du BERT de Google que Hugging Face a publiée en octobre 2019. La distillation de connaissances sert à entraîner un modèle élève plus petit à imiter les sorties du BERT enseignant, plus grand, pendant le préentraînement. Avec 66 millions de paramètres, il est 40 % plus petit que le BERT-base d'origine et environ 60 % plus rapide, tout en conservant autour de 97 % des performances de BERT sur la suite de benchmarks GLUE. Sur des tâches comme la question-réponse SQuAD et la classification de sentiment IMDb, il reste à quelques points du BERT complet malgré la réduction de taille.

L'article, « DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter », est devenu l'un des plus cités en NLP, et le modèle lui-même un choix par défaut pour les équipes qui voulaient une compréhension du langage de niveau BERT sur du hardware contraint, y compris les appareils mobiles. Il est publié sous licence Apache 2.0 et reste l'un des modèles les plus téléchargés sur Hugging Face, des années après sa sortie.
