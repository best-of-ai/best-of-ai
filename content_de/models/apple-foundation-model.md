---
title: 'Apple Foundation Model'
name: 'Apple Foundation Model'
slug: 'apple-foundation-model'
subtitle: 'On-Device- und Server-Grundlagenmodelle von Apple hinter Apple Intelligence'
description: 'On-Device- und Server-Grundlagenmodelle von Apple hinter Apple Intelligence'
company: 'apple'
model_type: 'Language'
logo_url: ''
product_url: 'https://machinelearning.apple.com/research/introducing-apple-foundation-models'
price: 'Paid'
rank: 6
release_date: '2024-06-10'
param_count: '3B (on-device)'
context_window_tokens: 32000
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Self-hosted]
runs_at_home: false
platforms: ['iOS', 'macOS']
date: '2026-07-16'
tags: [llm, on-device, foundation-model]
i18n_source: '7fbb8197cfde'
---

Apples Foundation Models sind zwei Sprachmodelle, die Apple Intelligence zugrunde liegen und im Juni 2024 auf der WWDC vorgestellt wurden: Ein Modell mit rund drei Milliarden Parametern läuft direkt auf iPhone, iPad und Mac; ein größeres Modell wird auf Apples Private-Cloud-Compute-Servern für Aufgaben ausgeführt, die das Gerät allein nicht bewältigt. Das Gerätemodell nutzt Techniken wie KV-Cache-Sharing und quantisierungsbewusstes 2-Bit-Training, um in den Speicher- und Energiebedarf eines Smartphones zu passen. Das Servermodell verwendet eine Mixture-of-Experts-Transformer-Architektur. Das nutzbare Kontextfenster des Gerätemodells ist auf 4.096 Tokens begrenzt, das Servermodell verarbeitet bis zu 32.000 Tokens.

Apple verkauft keinen API-Zugang wie OpenAI oder Anthropic. Stattdessen treiben die Modelle integrierte Funktionen wie Schreibwerkzeuge, Mitteilungszusammenfassungen und neue Siri-Funktionen an. Seit der WWDC 2025 können Drittanbieter über das Foundation-Models-Framework direkt und kostenlos auf das Gerätemodell zugreifen – auch ohne Netzwerkverbindung. Apple aktualisierte die Modellreihe auf der WWDC 2025 und stellte auf der WWDC 2026 eine dritte Generation vor. Im Mittelpunkt standen vor allem Qualität und Effizienz statt großer Zuwächse bei der Modellgröße. Das entspricht Apples Schwerpunkt auf Datenschutz und lokaler Inferenz statt der Übertragung von Nutzerdaten an Cloud-Modelle.
