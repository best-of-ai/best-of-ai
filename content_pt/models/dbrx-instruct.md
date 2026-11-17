---
title: 'DBRX Instruct'
name: 'DBRX Instruct'
slug: 'dbrx-instruct'
subtitle: 'Versão ajustada para instruções do modelo DBRX de pesos abertos da Databricks'
description: 'Versão ajustada para instruções do modelo DBRX de pesos abertos da Databricks'
company: 'databricks'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm'
price: 'Free'
rank: 4
release_date: '2024-03-27'
param_count: '132B (36B active)'
context_window_tokens: 32000
modality: [text]
open_weight: true
license: 'Databricks Open Model License'
api_available: true
mmlu_score: 73.7
humaneval_score: 70.1
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Databricks']
date: '2026-07-16'
tags: [llm, open-weight, instruction-tuned, self-hosted]
extra_model_types: ['Code']
i18n_source: '2f1996df20fb'
---

O DBRX Instruct é a versão ajustada e pronta para chat do modelo DBRX da Databricks, lançada em março de 2024 junto com o modelo base. Usa uma arquitetura de mistura de especialistas granular com 132 bilhões de parâmetros totais, dos quais apenas 36 bilhões são ativados para cada token, e foi treinado com 12 trilhões de tokens de texto e código. A Databricks o ajustou especificamente para seguir instruções e conversar em várias etapas. No lançamento, a empresa afirmou que ele superava o GPT-3.5 no MMLU (73,7% contra 70,0%) e no HumanEval (70,1% contra 48,1%). Oferece janela de contexto de 32 mil tokens e é distribuído sob a Databricks Open Model License, que permite uso comercial com algumas restrições para implantações muito grandes. Organizações podem executá-lo na plataforma da Databricks ou hospedar os pesos do Hugging Face.