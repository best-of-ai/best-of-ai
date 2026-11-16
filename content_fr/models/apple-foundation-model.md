---
title: 'Apple Foundation Model'
name: 'Apple Foundation Model'
slug: 'apple-foundation-model'
subtitle: "Les modèles de fondation d'Apple, sur l'appareil et sur serveur, derrière Apple Intelligence"
description: "Les modèles de fondation d'Apple, sur l'appareil et sur serveur, derrière Apple Intelligence"
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

Les Foundation Models d'Apple sont la paire de modèles de langage derrière Apple Intelligence, présentés en juin 2024 à la WWDC : un modèle d'environ 3 milliards de paramètres qui tourne directement sur iPhone, iPad et Mac, et un modèle plus gros qui tourne sur les serveurs Private Cloud Compute d'Apple pour les tâches que le modèle sur l'appareil ne traite pas seul. Le modèle sur l'appareil s'appuie sur des techniques comme le partage du cache KV et un entraînement qui tient compte de la quantification à 2 bits, pour tenir dans la mémoire et le budget d'énergie d'un téléphone. Le modèle serveur utilise un transformer à mélange d'experts. La fenêtre de contexte utilisable sur l'appareil est limitée à 4 096 tokens, alors que le modèle serveur va jusqu'à 32 000 tokens.

Apple ne vend pas d'accès API à ces modèles comme le font OpenAI ou Anthropic. Ils font tourner des fonctions système intégrées, comme les outils d'écriture, les résumés de notifications et les capacités revues de Siri. Depuis la WWDC 2025, des développeurs tiers y accèdent via le framework Foundation Models : une app peut appeler le modèle sur l'appareil directement, gratuitement et sans connexion réseau. Apple a depuis mis la gamme à jour à la WWDC 2025 et présenté une troisième génération à la WWDC 2026, en général autour de gains de qualité et d'efficacité plutôt que d'une forte hausse de taille. Ça suit la préférence d'Apple pour la confidentialité et l'inférence sur l'appareil, plutôt que d'envoyer les données des utilisateurs vers des modèles frontière hébergés dans le cloud.
