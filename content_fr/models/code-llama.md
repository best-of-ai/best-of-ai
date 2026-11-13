---
title: 'Code Llama'
name: 'Code Llama'
slug: 'code-llama'
subtitle: "Variante Llama de Meta à poids ouverts, spécialisée dans le code"
description: "Variante Llama de Meta à poids ouverts, spécialisée dans le code"
company: 'meta-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://ai.meta.com/blog/code-llama-large-language-model-coding/'
price: 'Free'
rank: 6
release_date: '2023-08-24'
param_count: '34B'
context_window_tokens: 100000
modality: [text, code]
open_weight: true
license: 'Llama 2 Community License'
api_available: true
humaneval_score: 53.7
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, code, self-hosted]
i18n_source: 'f77a90c92a53'
---

Code Llama est la version de Llama 2 centrée sur le code chez Meta, sortie en août 2023. Il a poursuivi l'entraînement sur des données riches en code, à partir des poids Llama 2 de base, et il est sorti en trois tailles de fondation (7B, 13B et 34B de paramètres), chacune avec une version de base, une version spécialisée en Python et une version ajustée pour les instructions, pour une aide au code en forme de chat. Meta a ensuite ajouté une variante 70B. Par rapport au Llama 2 de base, le changement important a été d'étendre la fenêtre de contexte de 4 096 à 100 000 tokens, en ajustant les embeddings positionnels RoPE. Le modèle est ainsi devenu bien plus utile pour lire et modifier de longs fichiers, ou des bases de code entières, en une seule passe.

Sur le benchmark HumanEval, le modèle 34B a obtenu 53,7 % en pass@1, à peu près au niveau de GPT-3.5 au moment de la sortie, tout en restant loin derrière GPT-4. Code Llama est publié sous la même Llama 2 Community License que le modèle parent, ce qui autorise un usage commercial pour la plupart des entreprises, et ses poids se téléchargent librement sur Hugging Face. C'est l'un des premiers modèles de code à poids ouverts à avoir été largement adoptés, et il a servi de référence face à laquelle les modèles de code ouverts suivants, dont Codestral et DeepSeek Coder, se sont ensuite mesurés.
