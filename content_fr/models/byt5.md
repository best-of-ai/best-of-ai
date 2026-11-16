---
title: 'ByT5'
name: 'ByT5'
slug: 'byt5'
subtitle: 'La variante de T5 de Google, sans tokens, qui travaille directement sur les octets bruts'
description: 'La variante de T5 de Google, sans tokens, qui travaille directement sur les octets bruts'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://arxiv.org/abs/2105.13626'
price: 'Free'
rank: 4
release_date: '2021-05-28'
param_count: '13B'
modality: [text]
open_weight: true
license: 'Apache 2.0'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [llm, open-weight, legacy, research]
i18n_source: 'e8007dd611dd'
---

ByT5 est une variante du modèle texte-vers-texte T5 de Google, publiée par Google Research à la mi-2021. Elle se distingue en abandonnant toute tokenisation pour travailler directement sur les octets UTF-8 bruts. Les modèles de langage habituels découpent le texte en tokens de sous-mots, avec un vocabulaire fixe construit par un tokenizer. Ça marche bien pour les langues et les écritures autour desquelles ce vocabulaire a été construit, mais ça gère mal les mots rares, les fautes d'orthographe et les langues moins courantes. ByT5 contourne ça en traitant chaque entrée comme une suite d'octets, avec un vocabulaire de quelques centaines de valeurs possibles seulement, au lieu de dizaines de milliers de tokens de sous-mots.

Le compromis, c'est que les suites d'octets sont bien plus longues que les suites de tokens pour le même texte. ByT5 a donc besoin d'encodeurs plus profonds et de plus de calcul par entrée pour égaler les modèles à base de tokens sur les benchmarks standards. Google a publié une famille de tailles ByT5, jusqu'à ByT5-XXL autour de 13 milliards de paramètres, tous les checkpoints étant ouverts sur Hugging Face sous Apache 2.0. Il s'en sortait particulièrement bien sur le texte bruité, la translittération et les tâches multilingues avec des écritures peu dotées. Ça en a fait un point de référence utile pour la recherche sur la modélisation sans tokens et au niveau du caractère, même si la plupart des modèles de langage en production sont restés sur des approches à base de tokens, pour leur efficacité.
