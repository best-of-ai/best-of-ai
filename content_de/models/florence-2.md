---
title: 'Florence-2'
name: 'Florence-2'
slug: 'florence-2'
subtitle: 'Kompaktes Grundlagenmodell für Bildverarbeitung von Microsoft, das Beschriftung, Erkennung und Segmentierung in einem Modell vereint'
description: 'Kompaktes Grundlagenmodell für Bildverarbeitung von Microsoft, das Beschriftung, Erkennung und Segmentierung in einem Modell vereint'
company: 'microsoft'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://www.microsoft.com/en-us/research/publication/florence-2-advancing-a-unified-representation-for-a-variety-of-vision-tasks/'
price: 'Free'
rank: 6
release_date: '2024-06-15'
param_count: '0.77B'
modality: [text, image]
open_weight: true
license: 'MIT'
api_available: true
access_methods: [Self-hosted, API]
runs_at_home: true
platforms: ['Hugging Face', 'Azure AI Foundry']
date: '2026-07-16'
tags: [computer-vision, open-weight, multimodal]
i18n_source: '9791d240cd8e'
---

Florence-2 ist ein Vision-Grundmodell von Microsoft Research, veröffentlicht im Juni 2024. Es bewältigt Bildbeschriftung, Objekterkennung, Segmentierung und visuelle Verankerung in einem Modell, statt für jede Aufgabe ein eigenes Modell zu erfordern. Es arbeitet promptbasiert: Dasselbe Netzwerk kann je nach Textanweisung eine Bildbeschreibung, Begrenzungsrahmen oder Segmentierungsmaske erzeugen. Dafür nutzt es eine einheitliche Sequence-to-Sequence-Architektur. Microsoft veröffentlichte zwei Größen: eine Basisversion mit 230 Millionen und eine große mit 770 Millionen Parametern. Beide sind im Vergleich zu typischen Vision-Language-Modellen klein. Trainiert wurde Florence-2 auf FLD-5B, einem internen Microsoft-Datensatz mit rund 126 Millionen Bildern und 5,4 Milliarden Annotationen. Dadurch kann das kleine Modell größere spezialisierte Modelle etwa bei COCO-Bildbeschriftung und dem Verständnis verweisender Ausdrücke erreichen oder übertreffen. Microsoft veröffentlichte die Gewichte unter MIT-Lizenz auf Hugging Face und bietet das Modell außerdem über Azure AI Foundry an. Es ist eine beliebte Wahl für Teams, die Bildverarbeitung ohne ein großes multimodales LLM benötigen.
