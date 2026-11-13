---
title: 'Granite Code'
name: 'Granite Code'
slug: 'granite-code'
subtitle: "La famille de modèles de génération de code à poids ouverts d'IBM"
description: "La famille de modèles de génération de code à poids ouverts d'IBM"
company: 'ibm'
model_type: 'Code'
logo_url: ''
product_url: 'https://www.ibm.com/granite'
price: 'Free'
rank: 4
release_date: '2024-05-06'
param_count: '3B, 8B, 20B, 34B'
context_window_tokens: 8192
modality: [text, code]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'IBM watsonx']
date: '2026-07-16'
tags: [llm, open-weight, code, self-hosted]
i18n_source: '10f0aa565ad0'
---

Granite Code est la famille de modèles de code ouverts d'IBM, sortie en mai 2024 en quatre tailles : 3B, 8B, 20B et 34B de paramètres, chacune en version de base et en version ajustée pour les instructions. IBM Research a entraîné les modèles sur environ 3 à 4 billions de tokens, couvrant 116 langages de programmation, en mêlant du code brut et du texte en langue naturelle sur le code. Le même système gère donc la génération de code, la correction de bugs et l'explication de code. Les modèles sortent sous Apache 2.0, ce qui permet de faire du fine-tuning et de les redéployer sans friction de licence. IBM visait les entreprises méfiantes des assistants de code fermés. Au lancement, les benchmarks montraient que Granite Code égalait ou dépassait d'autres modèles de code ouverts de taille proche sur HumanEval et les suites associées. La ligne est disponible sur Hugging Face, via Ollama, et sur AWS via Bedrock et SageMaker. Des travaux d'échelle plus tardifs ont poussé certaines variantes jusqu'à une fenêtre de contexte de 128 000 tokens.
