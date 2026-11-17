---
title: 'Fuyu-8B'
name: 'Fuyu-8B'
slug: 'fuyu-8b'
subtitle: "Modelo multimodal de pesos abertos da Adept para percepção por agentes digitais"
description: "Modelo multimodal de pesos abertos da Adept para percepção por agentes digitais"
company: 'adept-ai'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.adept.ai/blog/fuyu-8b'
price: 'Free'
rank: 3
release_date: '2023-10-17'
param_count: '8B'
context_window_tokens: 16000
modality: [text, image]
open_weight: true
license: 'CC-BY-NC 4.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, multimodal, open-weight, agentic]
i18n_source: 'f65d9839efe1'
---

O Fuyu-8B é um modelo multimodal lançado pela Adept AI em outubro de 2023, criado especificamente para agentes digitais que precisam ver e agir em telas, e não para funcionar como chatbot de uso geral. A Adept o projetou com uma arquitetura simplificada: insere recortes de imagem diretamente em um transformer padrão apenas decodificador, sem encoder de imagem separado. Assim, pode receber imagens em qualquer resolução, sem redimensionar tudo para um tamanho fixo. Isso importa para o caso de uso da Adept, pois o modelo precisa ler elementos de interface, botões e texto na resolução nativa para responder a perguntas sobre capturas de tela, gráficos e diagramas e localizar elementos específicos na tela. A Adept publicou o modelo de 8 bilhões de parâmetros no Hugging Face sob a licença CC-BY-NC, que permite uso e modificação gratuitos, mas não uso comercial. Ele foi apresentado como prévia pública menor do modelo que alimenta o produto da Adept, não como oferta independente completa. O modelo aceita contexto de 16 mil tokens. Desde então, a Adept foi adquirida e grande parte de sua equipe foi para a Amazon em 2024, deixando o Fuyu-8B como registro de sua linha de pesquisa voltada a agentes.
