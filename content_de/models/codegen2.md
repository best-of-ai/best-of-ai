---
title: 'CodeGen2'
name: 'CodeGen2'
slug: 'codegen2'
subtitle: 'Das offene Programmiermodell von Salesforce für Infill-Aufgaben und mehrstufige Programmsynthese'
description: 'Das offene Programmiermodell von Salesforce für Infill-Aufgaben und mehrstufige Programmsynthese'
company: 'salesforce'
model_type: 'Code'
logo_url: ''
product_url: 'https://github.com/salesforce/CodeGen2'
price: 'Free'
rank: 5
release_date: '2023-05-03'
param_count: '16B'
context_window_tokens: 2048
modality: [text, code]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [code, open-weight]
i18n_source: '19442e527069'
---
CodeGen2 ist die zweite Generation offener Programmiermodelle von Salesforce Research und erschien im Mai 2023 als Nachfolger des ursprünglichen CodeGen. Es ist in vier Größen mit 1B, 3,7B, 7B und 16B Parametern verfügbar. Die wichtigste Neuerung gegenüber der ersten CodeGen-Version ist die Unterstützung für Infill: Das Modell kann fehlenden Code anhand des umgebenden Codes auf beiden Seiten ergänzen, statt Text nur von links nach rechts zu erzeugen. Dadurch eignet es sich besser für typische Abläufe in Code-Editoren wie Autovervollständigung und Fehlerbehebung, bei denen Code mitten in einer bestehenden Datei ergänzt werden muss.

Die Modelle wurden mit einer Mischung aus natürlicher Sprache und Quellcode aus vielen Programmiersprachen trainiert und unter der freizügigen Apache-2.0-Lizenz über Hugging Face und GitHub veröffentlicht. CodeGen2 wurde mit einem nutzbaren Kontext von etwa 2000 Tokens getestet – nach heutigen Maßstäben wenig, für Programmiermodelle dieser Zeit jedoch üblich. Salesforce positionierte es als forschungsfreundliche Alternative zu geschlossenen Programmiermodellen wie Codex. Später folgte CodeGen2.5, ein kleineres Modell, das auf die Leistung seiner größeren Vorgänger abgestimmt wurde.
