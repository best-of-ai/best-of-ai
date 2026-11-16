---
title: 'ESM-2'
name: 'ESM-2'
slug: 'esm-2'
subtitle: 'Sprachmodell von Meta für Proteine, das aus Sequenzen deren Struktur vorhersagt'
description: 'Sprachmodell von Meta für Proteine, das aus Sequenzen deren Struktur vorhersagt'
company: 'meta-ai'
model_type: 'Language'
logo_url: ''
product_url: 'https://ai.meta.com/blog/protein-folding-esmfold-metagenomics/'
price: 'Free'
rank: 6
release_date: '2022-10-31'
param_count: '15B'
modality: [text]
open_weight: true
license: 'MIT'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [science, biology, open-weight]
i18n_source: '603d0e8b688e'
---

ESM-2 ist ein Sprachmodell für Proteine von Meta AI. Es erschien im Oktober 2022 und wurde mit rund 250 Millionen Proteinsequenzen trainiert, ohne Multiple-Sequence-Alignment. Es gibt mehrere Größen bis zu 15 Milliarden Parametern – bei der Veröffentlichung das größte Protein-Sprachmodell. Meta stellte fest, dass die internen Repräsentationen bei wachsendem Modellumfang beginnen, Informationen über die 3D-Struktur von Proteinen zu kodieren, obwohl das Modell nicht ausdrücklich darauf trainiert wurde. Diese Eigenschaft ermöglicht ESMFold, Metas System zur Strukturvorhersage: Es verarbeitet eine Proteinsequenz mit ESM-2 und wandelt die resultierende Repräsentation direkt in Atomkoordinaten um. So entfällt die Suche in Alignment-Datenbanken, auf die sich Werkzeuge wie AlphaFold stützen, und Strukturvorhersagen werden erheblich schneller. Meta veröffentlichte die Gewichte offen und nutzte ESM-2 zum Aufbau des ESM Metagenomic Atlas, einer öffentlichen Datenbank vorhergesagter Strukturen für Hunderte Millionen zuvor nicht charakterisierter Proteine.
