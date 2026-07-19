---
title: 'ESM-2'
name: 'ESM-2'
slug: 'esm-2'
subtitle: 'Meta''s protein language model used to predict structure from sequence'
description: 'Meta''s protein language model used to predict structure from sequence'
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
---

ESM-2 is a protein language model from Meta AI, released in October 2022, trained on around 250 million protein sequences with no multiple-sequence alignment step. It comes in a range of sizes up to 15 billion parameters, the largest protein language model at the time of release, and Meta found that as the model scales up, its internal representations start to encode 3D structural information about proteins without being explicitly trained to do so. That property is what powers ESMFold, Meta's structure-prediction system, which reads a protein sequence through ESM-2 and turns the resulting representation directly into atomic coordinates, skipping the alignment databases that tools like AlphaFold rely on and making structure prediction dramatically faster. Meta released the weights openly and used ESM-2 to build the ESM Metagenomic Atlas, a public database of predicted structures for hundreds of millions of previously uncharacterized proteins.
