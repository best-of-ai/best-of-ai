---
title: 'BLIP'
name: 'BLIP'
slug: 'blip'
subtitle: "Modelo de pré-treinamento visão-linguagem da Salesforce para legendagem e recuperação"
description: "Modelo de pré-treinamento visão-linguagem da Salesforce para legendagem e recuperação"
company: 'salesforce'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/salesforce/BLIP'
price: 'Free'
rank: 6
release_date: '2022-01-28'
param_count: '223M'
modality: [text, image]
open_weight: true
license: 'BSD-3-Clause'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, vision, legacy]
i18n_source: '0a995979513f'
---

BLIP (Pré-treinamento de Linguagem e Imagem por Inicialização) é um modelo de visão e linguagem apresentado pelo Salesforce Research no início de 2022. Ele atende tanto a tarefas de compreensão, como legendagem de imagens e respostas visuais a perguntas, quanto a tarefas de recuperação, como associar imagens a textos. O modelo foi treinado com um método de inicialização que limpa legendas ruidosas extraídas da web: ele gera legendas sintéticas e filtra associações incorretas, alcançando bons resultados sem depender exclusivamente de conjuntos de dados enormes e sem curadoria. Com cerca de 223 milhões de parâmetros, o BLIP é pequeno em comparação com sistemas multimodais posteriores, mas foi importante por mostrar que a qualidade das legendas importa tanto quanto sua quantidade no pré-treinamento.

O Salesforce publicou abertamente os pesos e o código do BLIP sob uma licença BSD, e ele se tornou uma referência comum em pesquisa de visão e linguagem e um componente de outros projetos, incluindo versões iniciais de recursos de interrogação de ferramentas como Stable Diffusion. Seu sucessor, BLIP-2, aumentou a eficiência ao combinar codificadores de imagens congelados com modelos de linguagem congelados por meio de um módulo leve de conexão, mas o BLIP original ainda é usado em pesquisas acadêmicas e fluxos auto-hospedados que precisam de um modelo de legendagem compacto e bem documentado.
