---
title: 'ChatGLM3'
name: 'ChatGLM3'
slug: 'chatglm3'
subtitle: 'Le modèle de dialogue bilingue à poids ouverts de troisième génération, chez Zhipu'
description: 'Le modèle de dialogue bilingue à poids ouverts de troisième génération, chez Zhipu'
company: 'zhipu-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.zhipuai.cn/'
price: 'Free'
rank: 4
release_date: '2023-10-27'
param_count: '6B'
context_window_tokens: 8192
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, self-hosted, legacy]
i18n_source: '9a38147f22d8'
---

ChatGLM3 est la troisième génération de la ligne de modèles de dialogue ChatGLM, construit ensemble par Zhipu AI et le laboratoire KEG de l'université Tsinghua, et publié fin octobre 2023. Le modèle de base ChatGLM3-6B suit une conception bilingue chinois-anglais. Il apporte un meilleur soutien à l'appel de fonctions, à l'exécution de code et à l'usage d'outils façon agent par rapport à ses prédécesseurs, avec un mélange de préentraînement plus varié, davantage de tokens d'entraînement et un meilleur entraînement d'alignement. À la sortie, Zhipu indiquait que le modèle de base en 6B devançait les autres modèles préentraînés de moins de 10 milliards de paramètres, sur des dizaines de benchmarks qui couvrent le raisonnement, les maths, le code et les connaissances générales.

Zhipu a publié ChatGLM3 en plusieurs variantes de longueur de contexte : le ChatGLM3-6B standard, à côté de versions 32K et 128K à contexte plus long, pour de plus gros documents et de plus longues conversations. Le modèle est à poids ouverts sous Apache 2.0 et largement disponible via Hugging Face, ce qui en fait un choix courant pour des applications de chat en chinois auto-hébergées. Zhipu est depuis passé à des modèles plus récents de la série GLM-4, à plus grande échelle et avec de meilleurs résultats aux benchmarks, et opère maintenant sous la marque Z.ai. ChatGLM3 reste une option d'ancienne génération, surtout là où sa taille plus petite et son faible coût d'hébergement comptent plus que le plus haut niveau de capacité.
