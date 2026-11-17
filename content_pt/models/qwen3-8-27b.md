---
title: 'Qwen3.8-27B'
name: 'Qwen3.8-27B'
slug: 'qwen3-8-27b'
subtitle: "Modelo multimodal de pesos abertos da Alibaba dimensionado para funcionar em uma única GPU local"
description: "Modelo multimodal de pesos abertos da Alibaba dimensionado para funcionar em uma única GPU local"
company: 'alibaba'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://qwen.ai/'
price: 'Free'
rank: 7
release_date: '2026-08-14'
param_count: '27B'
context_window_tokens: 262144
modality: [text, image, video]
open_weight: true
license: 'Apache 2.0'
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'Alibaba Cloud', 'API']
date: '2026-08-17'
tags: [llm, open-weight, multimodal, single-gpu, apache-2.0, local]
i18n_source: '1e091b27bdc3'
---

A equipe Qwen da Alibaba lançou o Qwen3.8-27B em 14 de agosto de 2026, com pesos abertos imediatamente disponíveis sob a licença Apache 2.0. É um modelo denso de 27 bilhões de parâmetros, e não de mistura de especialistas, que processa texto, imagens e vídeo, incluindo diagramas, documentos e gravações de várias horas. O contexto nativo chega a 262.000 tokens e pode se estender a um milhão usando o método de escalonamento YaRN. A Alibaba afirma que ele supera o Qwen3.7-Plus, maior, em tarefas de programação e escritório, e aprimorou seu planejamento com agentes, permitindo concluir tarefas em várias etapas com menos supervisão.

O lançamento foi direcionado a desenvolvedores que querem um modelo capaz que caiba em uma única GPU de consumo ou de estação de trabalho, em vez de um cluster de centro de dados, posicionando-o contra lançamentos com prioridade local semelhantes da Meta e do Google. A Alibaba combinou o lançamento com pesos abertos para o Qwen3.8-2.4T-A95B, o modelo da classe Max da mesma geração, oferecendo aos desenvolvedores a escolha entre esta versão leve e um modelo de escala de fronteira criado para cargas de trabalho mais pesadas com agentes.
