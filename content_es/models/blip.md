---
title: 'BLIP'
name: 'BLIP'
slug: 'blip'
subtitle: 'Modelo de preentrenamiento de visión y lenguaje de Salesforce, para descripción y recuperación'
description: 'Modelo de preentrenamiento de visión y lenguaje de Salesforce, para descripción y recuperación'
company: 'salesforce'
model_type: 'Multimodal'
logo_url: ''
product_url: 'https://github.com/salesforce/BLIP'
price: 'Free'
rank: 6
release_date: '2022-01-28'
param_count: '223M'
modality: [text, image]
open_weight: true
license: 'BSD-3-Clause'
api_available: false
access_methods: [Self-hosted]
runs_at_home: true
platforms: ['Hugging Face']
date: '2026-07-16'
tags: [multimodal, open-weight, vision, legacy]
i18n_source: '0a995979513f'
---

BLIP (Bootstrapping Language-Image Pre-training) es un modelo de visión y lenguaje que Salesforce Research presentó a principios de 2022. Cubre tanto tareas de comprensión, como la descripción de imágenes y la respuesta a preguntas visuales, como tareas de recuperación, como emparejar imágenes con texto. El modelo se entrenó con un método de arranque que limpia los pies de foto ruidosos extraídos de la web: genera otros sintéticos y descarta los emparejamientos malos, lo que le permitió llegar a buenos resultados sin depender solo de conjuntos enormes y sin curar. Con unos 223 millones de parámetros, BLIP es pequeño al lado de los sistemas multimodales posteriores, pero influyó al mostrar que la calidad de los pies de foto importa tanto como su cantidad en el preentrenamiento.

Salesforce publicó los pesos y el código de BLIP en abierto bajo una licencia BSD, y se convirtió en una referencia habitual en la investigación de visión y lenguaje y en una pieza de otros proyectos, incluidas versiones tempranas de funciones de interrogación de herramientas como Stable Diffusion. Su sucesor, BLIP-2, mejoró la eficiencia al emparejar encoders de imagen congelados con modelos de lenguaje congelados a través de un módulo de puente ligero, pero el BLIP original se sigue usando en trabajo académico y en procesos autoalojados donde basta un modelo de descripción compacto y bien documentado.
