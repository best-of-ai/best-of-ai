---
title: 'GLM-5.3'
name: 'GLM-5.3'
slug: 'glm-5-3'
subtitle: "La mise à jour de Zhipu orientée code de GLM-5.2, fortement ajustée sur la recherche de vulnérabilités"
description: "La mise à jour de Zhipu orientée code de GLM-5.2, fortement ajustée sur la recherche de vulnérabilités"
company: 'zhipu-ai'
model_type: 'Code'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Paid'
rank: 7
release_date: '2026-08-14'
param_count: '~744B (MoE, ~40B active)'
context_window_tokens: 1000000
modality: [text, code]
open_weight: false
license: 'Proprietary'
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['GLM Coding Plan', 'API']
date: '2026-08-17'
tags: [llm, coding, cybersecurity, agentic, mixture-of-experts]
extra_model_types: ['Reasoning']
i18n_source: '87f3720943f0'
---

Zhipu AI a publié GLM-5.3 le 14 août 2026 en le présentant comme le modèle de code à poids ouverts le plus fort du moment, même si les poids eux-mêmes n'arrivent que deux semaines après l'annonce. Il partage son architecture de base avec GLM-5.2, donc le gain d'environ 50 % en capacité de programmation que Zhipu annonce vient entièrement d'un post-entraînement prolongé, pas d'un modèle plus gros. L'entreprise insiste en particulier sur l'angle sécurité : GLM-5.3 a obtenu 84,5 % sur CyberGym, un benchmark pour trouver et valider des vulnérabilités à partir du code source, juste devant Claude Mythos d'Anthropic à 83,8 % et GPT-5.6 Sol d'OpenAI à 83,6 %. Zhipu indique que des équipes de sécurité internes ont utilisé le modèle pour faire remonter 2 436 vulnérabilités sur 269 projets.

Pour l'instant, l'accès passe par le GLM Coding Plan de Zhipu, et le modèle fonctionne avec des agents de code, dont Claude Code, OpenCode et ZCode, celui de Zhipu. Le déploiement échelonné, d'abord l'API puis les poids ouverts, est un schéma que Zhipu a déjà utilisé avec la gamme GLM.
