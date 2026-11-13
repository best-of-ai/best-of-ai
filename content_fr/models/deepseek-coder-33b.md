---
title: 'DeepSeek-Coder-33B'
name: 'DeepSeek-Coder-33B'
slug: 'deepseek-coder-33b'
subtitle: "Ancien modèle de code phare de DeepSeek, avant DeepSeek-Coder-V2"
description: "Ancien modèle de code phare de DeepSeek, avant DeepSeek-Coder-V2"
company: 'deepseek'
model_type: 'Code'
logo_url: ''
product_url: 'https://github.com/deepseek-ai/DeepSeek-Coder'
price: 'Free'
rank: 6
release_date: '2023-11-02'
param_count: '33B'
context_window_tokens: 16384
modality: [text, code]
open_weight: true
license: 'DeepSeek License'
api_available: true
humaneval_score: 79.3
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'DeepSeek API']
date: '2026-07-16'
tags: [code, open-weight, api, legacy]
i18n_source: 'e1d443d0e69c'
---

DeepSeek-Coder-33B est un modèle de langage centré sur le code, sorti par DeepSeek en novembre 2023, avant que l'entreprise soit largement connue pour ses modèles de raisonnement plus tardifs. Il a été entraîné depuis zéro sur 2 billions de tokens, surtout répartis entre le code et la langue naturelle, avec une fenêtre de contexte de 16 000 tokens et un entraînement au niveau du projet, qui lui permet de raisonner sur plusieurs fichiers plutôt que sur des extraits isolés. La version ajustée pour les instructions a obtenu 79,3 % en pass@1 sur HumanEval à la sortie, devant la plupart des modèles de code ouverts de l'époque, et pas loin de GPT-3.5 sur les benchmarks de code. Il gère la complétion fill-in-the-middle pour les éditeurs, et couvre un large éventail de langages. DeepSeek l'a depuis remplacé par DeepSeek-Coder-V2, un modèle à mélange d'experts plus gros, avec une fenêtre de contexte plus longue. Le 33B reste toutefois sur Hugging Face pour l'auto-hébergement.
