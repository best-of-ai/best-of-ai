---
title: 'GLM-5.2 Turbo'
name: 'GLM-5.2 Turbo'
slug: 'glm-5-2-turbo'
subtitle: "La variante plus rapide de GLM-5.2 chez Zhipu, ajustée pour les longs flux de travail d'agents"
description: "La variante plus rapide de GLM-5.2 chez Zhipu, ajustée pour les longs flux de travail d'agents"
company: 'zhipu-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Paid'
rank: 6
release_date: '2026-08-17'
param_count: 'Undisclosed'
context_window_tokens: 202752
input_price_usd_per_m: 1.2
output_price_usd_per_m: 4
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['API']
date: '2026-08-31'
tags: [llm, agentic, api, tool-use]
extra_model_types: ['Reasoning']
i18n_source: '412352bbf7e4'
---

Zhipu AI a sorti GLM-5.2 Turbo le 17 août 2026 comme version plus rapide de GLM-5.2, conçue pour les charges pilotées par des agents, et non pour le chat général ou les requêtes ponctuelles. Sa fenêtre de contexte est plus petite que celle du modèle de base, environ 200 000 tokens contre la capacité complète de 1 million de tokens de GLM-5.2, en échange d'une latence plus basse sur les longues chaînes d'exécution typiques des agents de code et des outils d'automatisation. Zhipu indique avoir amélioré la décomposition d'instructions complexes et l'usage d'outils, ainsi que la stabilité sur les tâches planifiées et persistantes qui tournent longtemps sans supervision humaine.

Le tarif est au-dessus de celui de GLM-5.2 de base, à 1,20 $ par million de tokens d'entrée et 4 $ par million de tokens de sortie, ce qui reflète le compromis vers la vitesse plutôt que vers la longueur de contexte brute. Il vise le même public des frameworks d'agents déjà sur GLM-5.2 et GLM-5.3, et donne aux développeurs une option au contexte moins coûteux et à la réponse plus rapide quand une tâche n'a pas besoin de la fenêtre d'un million de tokens.
