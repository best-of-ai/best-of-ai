---
title: 'DeepSeek-R1-Distill-Qwen-32B'
name: 'DeepSeek-R1-Distill-Qwen-32B'
slug: 'deepseek-r1-distill-qwen-32b'
subtitle: 'Qwen-basierte Destillation der Reasoning-Abläufe von DeepSeek-R1 in ein kleineres offenes Modell'
description: 'Qwen-basierte Destillation der Reasoning-Abläufe von DeepSeek-R1 in ein kleineres offenes Modell'
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://github.com/deepseek-ai/DeepSeek-R1'
price: 'Free'
rank: 6
release_date: '2025-01-20'
param_count: '32B'
context_window_tokens: 131072
modality: [text]
open_weight: true
license: 'MIT'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Together AI']
date: '2026-07-16'
tags: [llm, reasoning, open-weight, api]
i18n_source: '3cf96c55115c'
---

DeepSeek-R1-Distill-Qwen-32B ist ein dichtes Modell mit 32 Milliarden Parametern, das DeepSeek durch Feinabstimmung von Qwen2.5-32B auf Schlussfolgerungsspuren des vollständigen DeepSeek-R1 entwickelte. Statt ein kleineres Modell neu zu trainieren, destillierte DeepSeek R1s schrittweise Schlussfolgerungen in mehrere Basismodelle. Die 32B-Qwen-Variante erwies sich als stärkste der Gruppe. Bei Mathematik-, Programmier- und Wissenschafts-Benchmarks übertraf sie OpenAI o1-mini trotz ihrer moderaten Größe. Damit gehörte sie zu den ersten offenen Modellen, die auf einer einzelnen High-End-GPU laufen und dennoch echtes Schlussfolgerungsvermögen zeigen. Die Gewichte stehen unter MIT-Lizenz auf Hugging Face bereit und sind über Anbieter wie Together AI und Groq verfügbar.

Das Modell passt zu Teams, die schrittweises Schlussfolgern im Stil von R1 möchten, ohne das vollständige 671B-Modell zu bezahlen oder zu hosten. Als dichter Transformer statt Mixture-of-Experts-Modell ist es außerdem einfacher feinabzustimmen und bereitzustellen als DeepSeeks Spitzenmodelle.
