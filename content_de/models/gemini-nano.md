---
title: 'Gemini Nano'
name: 'Gemini Nano'
slug: 'gemini-nano'
subtitle: 'Die für den Einsatz auf Geräten entwickelte Gemini-Stufe von Google, integriert in Pixel und Android'
description: 'Die für den Einsatz auf Geräten entwickelte Gemini-Stufe von Google, integriert in Pixel und Android'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://deepmind.google/technologies/gemini/'
price: 'Paid'
rank: 4
release_date: '2023-12-06'
param_count: '3.25B'
context_window_tokens: 8192
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Self-hosted]
runs_at_home: false
platforms: ['Android', 'Chrome']
date: '2026-07-16'
tags: [llm, on-device, small-model]
i18n_source: '6991c4c972f9'
---
Gemini Nano ist die kleinste Stufe der Gemini-Familie von Google und dafür ausgelegt, vollständig auf einem Smartphone zu laufen, statt einen Server aufzurufen. Google kündigte es am 6. Dezember 2023 zusammen mit Gemini Pro und Ultra an und brachte es zuerst auf dem Pixel 8 Pro heraus. Dort unterstützt es Gerätefunktionen wie intelligente Antwortvorschläge in Messaging-Apps, Anrufzusammenfassungen und Zusammenfassungen in der Recorder-App. Es gibt mehrere Größen mit ungefähr 1,8 und 3,25 Milliarden Parametern. Sie sind für die Speicher- und NPU-Grenzen eines Smartphones quantisiert und arbeiten vollständig offline, ohne dass Daten das Gerät verlassen.

Da es lokal läuft, bietet Nano weniger Leistung als größere Modelle, dafür aber Geschwindigkeit, Datenschutz und keine zusätzlichen Kosten pro Anfrage. Sein nutzbares Kontextfenster ist erheblich kleiner als bei Googles serverseitigen Modellen. Google hat die Geräteunterstützung seit der Einführung auf weitere Pixel- und über Partnerschaften auch auf Samsung-Galaxy-Geräte ausgeweitet. Android-Entwickler können Nano über das AICore-System und die ML-Kit-GenAI-APIs verwenden, nicht über eine öffentliche Cloud-API.
