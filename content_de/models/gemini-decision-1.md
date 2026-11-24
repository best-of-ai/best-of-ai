---
title: 'Gemini Decision 1'
name: 'Gemini Decision 1'
slug: 'gemini-decision-1'
subtitle: 'Nicht generatives Modell von Google, das Optionen bewertet und statt Text eine Konfidenz zurückgibt'
description: 'Nicht generatives Modell von Google, das Optionen bewertet und statt Text eine Konfidenz zurückgibt'
company: 'google-deepmind'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/'
price: 'Paid'
rank: 6
release_date: '2026-11-11'
param_count: 'Undisclosed'
context_window_tokens: 256000
modality: [text, image, audio, video]
open_weight: false
license: 'Proprietary'
input_price_usd_per_m: 0.1
output_price_usd_per_m: 0
api_available: true
access_methods: [API]
runs_at_home: false
platforms: ['Gemini API', 'Google AI Studio']
date: '2026-11-24'
tags: [classification, decision-model, multimodal, api]
i18n_source: '1bbd28f7737a'
---
Gemini Decision 1 ist ein Modell hinter der Decisions API von Google, die am 11. November 2026 startete, und schreibt keinen Text. Es bewertet Optionen in einem einzigen Vorwärtsdurchlauf und gibt für jede eine Wahrscheinlichkeit und eine Konfidenz zurück. Es beantwortet Ja/Nein-Fragen, Multiple-Choice-Fragen mit 2 bis 255 Optionen und geordnete Bewertungen nach Rubrik, mit bis zu 1.000 Fragen in einer Anfrage. Eingaben können Text, Bilder, Audio, Video und PDFs sein, bis zu 256.000 Tokens.

Google nennt eine Ende-zu-Ende-Latenz von 150 bis 250 Millisekunden. Der Preis beträgt 0,10 US-Dollar pro Million Eingabe-Tokens und nichts für die Ausgabe, und AI Studio hat einen kostenlosen Tarif zum Prototyping. Laut Google ist es auf derselben Testsuite fast fünfmal günstiger als Gemini 3.5 Flash-Lite. Die Modell-ID lautet gemini-decision-1, und Integrationen werden gerade für OpenRouter, LangChain, Vercel und LiteLLM ausgerollt.
