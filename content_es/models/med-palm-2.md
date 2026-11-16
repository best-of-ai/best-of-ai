---
title: 'Med-PaLM 2'
name: 'Med-PaLM 2'
slug: 'med-palm-2'
subtitle: 'El LLM médico de Google que alcanzó puntuaciones de nivel experto en preguntas del examen de licencia médica de EE. UU.'
description: 'El LLM médico de Google que alcanzó puntuaciones de nivel experto en preguntas del examen de licencia médica de EE. UU.'
company: 'google-deepmind'
model_type: 'Language'
logo_url: ''
product_url: 'https://sites.research.google/med-palm/'
price: 'Paid'
rank: 6
release_date: '2023-05-16'
param_count: 'Undisclosed'
modality: [text]
open_weight: false
license: 'Proprietary'
api_available: false
mmlu_score: 86.5
access_methods: [Research]
runs_at_home: false
platforms: ['Research']
date: '2026-07-16'
tags: [llm, healthcare, research]
i18n_source: 'c1f1e4c9a2e1'
---

Med-PaLM 2 es el modelo de preguntas y respuestas médicas de segunda generación de Google, construido sobre la base PaLM 2 y ajustado (fine-tuned) con datos del dominio médico. Fue el primer modelo de lenguaje que alcanzó un rendimiento de nivel experto en el benchmark MedQA, un conjunto de preguntas al estilo del US Medical Licensing Examination, con un 86,5 %: un salto de unos 19 puntos respecto al Med-PaLM original. Google lo evaluó en MultiMedQA, una colección de siete conjuntos de datos que cubre exámenes profesionales, preguntas de investigación médica y consultas de salud del público, e introdujo una técnica llamada ensemble refinement: el modelo genera varios caminos de razonamiento y luego los combina en una respuesta final.

Google compartió Med-PaLM 2 con un grupo pequeño de organizaciones sanitarias para pruebas, en lugar de publicarlo de forma amplia, por la cautela a la hora de desplegar IA médica en entornos clínicos. Más tarde alimentó MedLM, un producto de Google Cloud para clientes del sector sanitario, y se presenta como un paso de investigación hacia sistemas de IA que puedan apoyar a los médicos y responder con seguridad a las preguntas de los pacientes, no como un chatbot de propósito general.
