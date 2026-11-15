---
title: 'AlphaCode 2'
name: 'AlphaCode 2'
slug: 'alphacode-2'
subtitle: 'Modell von DeepMind für Wettbewerbsprogrammierung auf Gemini-Basis, unter den besten menschlichen Teilnehmenden eingestuft'
description: 'Modell von DeepMind für Wettbewerbsprogrammierung auf Gemini-Basis, unter den besten menschlichen Teilnehmenden eingestuft'
company: 'google-deepmind'
model_type: 'Code'
logo_url: ''
product_url: 'https://deepmind.google/discover/blog/alphacode-2-technical-report/'
price: 'Paid'
rank: 6
release_date: '2023-12-06'
param_count: 'Undisclosed'
modality: [text, code]
open_weight: false
license: 'Proprietary'
api_available: false
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [code, research]
i18n_source: 'd985a201f8f1'
---

AlphaCode 2 ist das System von Google DeepMind für kompetitives Programmieren. Es wurde im Dezember 2023 als technischer Bericht veröffentlicht und folgte auf das ursprüngliche AlphaCode. Statt eines einzelnen Modells nutzt es eine Pipeline aus feinabgestimmten Gemini-Modellen: Für jede Aufgabe werden bis zu einer Million C++-Lösungen erzeugt und anschließend anhand von Tests, Verhaltensclustern und einem trainierten Bewertungsmodell gefiltert. Etwa zehn endgültige Einsendungen bleiben übrig. Bei aktuellen Codeforces-Wettbewerben löste es mit höchstens zehn Versuchen 43 Prozent der Aufgaben – fast doppelt so viele wie AlphaCode mit 25 Prozent.

DeepMind schätzte die Leistung von AlphaCode 2 auf das 85. Perzentil menschlicher Codeforces-Teilnehmender, zwischen den Rängen „Expert“ und „Candidate Master“. Das Projekt blieb Forschung und wurde weder als Produkt noch als API veröffentlicht. Es sollte vor allem zeigen, wie ein leistungsfähiges Basismodell durch umfangreiches Sampling und Filtern schwierige, überprüfbare Programmieraufgaben besser bewältigen kann. Es ist ein direkter Vorläufer später in Gemini und AlphaProof eingeflossener Methoden für Schlussfolgern und Codegenerierung.
