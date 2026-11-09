---
title: 'NVIDIA CUDA'
name: 'NVIDIA CUDA'
subtitle: 'Plataforma y kit de herramientas de computación en GPU de NVIDIA'
slug: 'nvidia-cuda'
description: 'CUDA es la plataforma de NVIDIA para ejecutar código de propósito general en sus GPU. Incluye un compilador, un runtime y bibliotecas como cuDNN y cuBLAS, y casi todos los grandes frameworks de aprendizaje profundo dependen de ella.'
website: 'https://developer.nvidia.com/cuda-toolkit'
company: 'nvidia'
logo_url: ''
category: 'devtools'
category_name: 'Herramientas para desarrolladores'
price: 'Free'
featured: false
rank: 10
alternatives:
  - amd-rocm
  - openvino
  - qualcomm-ai-hub
  - nvidia-nim
date: '2026-11-05'
tags: [developer_tools, code_generation, infrastructure, deployment, development, devops, ci_cd, cloud, api, machine_learning, training]
i18n_source: '06f483092a94'
---

CUDA es la capa de software que permite a los programadores usar una GPU de NVIDIA para algo más que gráficos. Escribes funciones llamadas kernels, normalmente en C++ o Python, que se ejecutan a la vez en miles de hilos de la GPU, algo que encaja con cargas de trabajo hechas de grandes cantidades de cálculo en paralelo. La simulación científica, el procesamiento de vídeo y, sobre todo, las redes neuronales responden a esa descripción, por lo que CUDA se convirtió en la base del entrenamiento y la inferencia de la IA moderna.

La mayoría de quienes usan CUDA nunca lo escriben directamente. PyTorch, TensorFlow y JAX llaman a las bibliotecas de NVIDIA, entre ellas cuDNN para operaciones de redes neuronales, cuBLAS para álgebra lineal y NCCL para la comunicación entre GPU. TensorRT y herramientas relacionadas optimizan los modelos para su despliegue. Como estas bibliotecas llevan años afinándose, un modelo que corre en CUDA suele ser más rápido de entrada que el mismo código en hardware de otro fabricante. Esa ventaja de software explica en buena parte por qué las GPU de NVIDIA dominan los centros de datos de IA.

CUDA se descarga gratis, pero solo funciona en hardware de NVIDIA, y esa es la crítica principal. El código escrito en CUDA no puede ejecutarse en GPU de AMD o Intel sin portarlo, y muchas empresas intentan evitar esa dependencia. ROCm de AMD, Triton de OpenAI, SYCL y Metal de Apple son las alternativas habituales, y cada una cubre solo una parte de lo que hace CUDA. Para la mayoría de los desarrolladores, el consejo práctico es sencillo: usa un framework que se encargue de CUDA por ti, y baja a escribir kernels solo cuando el perfilado demuestre que necesitas la velocidad extra.
