---
title: 'DeepSeek R1'
name: 'DeepSeek R1'
slug: 'deepseek-r1'
subtitle: 'Reasoning-Modell von DeepSeek, das bei Mathematik und Programmierung mit geschlossenen Frontier-Modellen mithielt'
description: 'Reasoning-Modell von DeepSeek, das bei Mathematik und Programmierung mit geschlossenen Frontier-Modellen mithielt'
company: 'deepseek'
model_type: 'Reasoning'
logo_url: ''
product_url: 'https://www.deepseek.com/'
price: 'Free'
rank: 8
release_date: '2025-01-20'
param_count: '671B (37B active)'
context_window_tokens: 128000
modality: [text]
open_weight: true
license: 'MIT'
input_price_usd_per_m: 0.55
output_price_usd_per_m: 2.19
api_available: true
mmlu_score: 90.8
humaneval_score: 92.0
lmarena_score: 1360
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, reasoning, chain-of-thought]
i18n_source: 'fa3b02ee20e3'
---

DeepSeek R1 ist ein Schlussfolgerungsmodell des chinesischen Labors DeepSeek, veröffentlicht am 20. Januar 2025. Es nutzt eine Mixture-of-Experts-Architektur mit 671 Milliarden Parametern insgesamt und 37 Milliarden aktiven pro Token. Beim Training kam umfangreiches Reinforcement Learning zum Einsatz, nicht nur überwachtes Fine-Tuning. Dadurch arbeitet es Probleme Schritt für Schritt durch, bevor es antwortet. Bei der Veröffentlichung erreichte es in Mathematik, Programmierung und Wissenschaft Werte auf dem Niveau von OpenAI o1: 90,8 Punkte bei MMLU und Spitzenleistungen seinerzeit bei AIME- und Codeforces-ähnlichen Aufgaben. Zugleich wurden offene Gewichte unter MIT-Lizenz veröffentlicht und die API war deutlich günstiger als o1.

Die Veröffentlichung sorgte auch außerhalb der KI-Forschung für Aufsehen: DeepSeeks App stand kurzzeitig an der Spitze des US-App-Store-Rankings. Die Nachricht, dass ein vergleichsweise kleines chinesisches Labor ein Spitzenmodell zu einem Bruchteil der üblichen Kosten trainiert hatte, erschütterte KI-Aktien. R1 ist über DeepSeeks API und Chatoberfläche verfügbar. Die offenen Gewichte können selbst gehostet werden, sind auf Hugging Face weit verbreitet und werden von Drittanbietern bereitgestellt.
