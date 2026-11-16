---
title: 'AMD ROCm'
name: 'AMD ROCm'
subtitle: 'Plataforma de software abierta para desarrollo de IA y computación en GPU'
slug: 'amd-rocm'
description: 'AMD ROCm es una plataforma de software abierta para IA y computación de alto rendimiento en GPU de AMD. Ofrece controladores, compiladores, bibliotecas y compatibilidad con frameworks para que los desarrolladores entrenen y ejecuten modelos de aprendizaje automático.'
website: 'https://rocm.docs.amd.com/'
company: 'amd'
logo_url: ''
category: 'devtools'
category_name: 'Herramientas para desarrolladores'
price: 'Free'
featured: false
rank: 5
alternatives:
  - nvidia-cuda
  - openvino
  - qualcomm-ai-hub
date: '2026-07-17'
tags: [developer_tools, code_generation, infrastructure, deployment, development, devops, ci_cd, cloud, api, machine_learning, training, model_based]
i18n_source: 'b6be5b2911d8'
---

ROCm es la respuesta de AMD a CUDA de NVIDIA. Es un conjunto de software que permite a los programas usar los procesadores gráficos de AMD para computación general: incluye controladores, una cadena de compilación, bibliotecas de matemáticas y comunicación, y herramientas de depuración y perfilado. Gran parte es de código abierto.

Para trabajo con IA, la pieza clave es la compatibilidad con frameworks. PyTorch, TensorFlow, JAX y otros funcionan sobre ROCm, y herramientas de inferencia como vLLM y muchas bibliotecas de modelos tienen versiones para AMD. Se puede portar código CUDA con HIP, una capa de programación parecida a CUDA, y grandes despliegues en la nube y en supercomputadores usan aceleradores AMD Instinct con ROCm.

ROCm es gratuito. Históricamente ha ido por detrás de CUDA en madurez y soporte del ecosistema, así que la compatibilidad con GPU y bibliotecas concretas varía y hay que comprobarla, aunque la distancia se ha ido acortando. Entre las alternativas están NVIDIA CUDA, Intel oneAPI, Apple Metal para Mac y la computación basada en Vulkan. ROCm es adecuado para desarrolladores y organizaciones que usan hardware AMD para IA.
