---
title: 'MiniMax-01'
name: 'MiniMax-01'
slug: 'minimax-01'
subtitle: 'Offenes Modell von MiniMax aus dem Jahr 2025 mit einem Kontextfenster von 4 Millionen Tokens'
description: 'Offenes Modell von MiniMax aus dem Jahr 2025 mit einem Kontextfenster von 4 Millionen Tokens'
company: 'minimax-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://www.minimaxi.com/'
price: 'Free'
rank: 6
release_date: '2025-01-15'
param_count: '456B (45.9B active)'
context_window_tokens: 4000000
modality: [text]
open_weight: true
license: 'Apache 2.0'
input_price_usd_per_m: 0.2
output_price_usd_per_m: 1.1
api_available: true
access_methods: [API, Self-hosted]
runs_at_home: true
platforms: ['Hugging Face', 'API']
date: '2026-07-16'
tags: [llm, open-weight, long-context, mixture-of-experts]
extra_model_types: ['Multimodal']
i18n_source: '7af458104dd5'
---

MiniMax-01 ist eine Familie von Modellen mit offenen Gewichten, die das chinesische KI-Labor MiniMax im Januar 2025 veröffentlichte. Sie umfasst ein Textmodell (MiniMax-Text-01) und ein Vision-Language-Modell (MiniMax-VL-01), die auf derselben hybriden Architektur basieren. Das Mixture-of-Experts-Modell hat insgesamt 456 Milliarden Parameter, von denen pro Token etwa 45,9 Milliarden aktiv sind. Es kombiniert Lightning Attention mit regulärer Softmax-Attention, damit sich sehr lange Sequenzen mit vertretbarem Rechenaufwand verarbeiten lassen. Das herausragende Merkmal ist die Kontextlänge: Das Modell kann Eingaben mit bis zu vier Millionen Tokens verarbeiten – deutlich mehr als die meisten Konkurrenzmodelle zu dieser Zeit. Über die API gehostete Versionen bieten in der Regel ein Kontextfenster von einer Million Tokens.

MiniMax veröffentlichte die Gewichte unter der Apache-2.0-Lizenz auf Hugging Face und bietet das Modell auch über die eigene API an. Der Preis beträgt 0,20 US-Dollar pro Million Eingabetokens und 1,10 US-Dollar pro Million Ausgabetokens und liegt damit unter dem der meisten westlichen Spitzenmodelle. Das Modell richtet sich an Anwendungsfälle wie die Analyse umfangreicher Dokumente, lang laufende Agenten-Workflows und Schlussfolgerungen über ganze Codebasen hinweg, bei denen die Kontextlänge und nicht die reine Parameterzahl den Engpass bildet.
