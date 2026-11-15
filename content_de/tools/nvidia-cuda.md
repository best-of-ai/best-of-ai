---
title: NVIDIA CUDA
name: NVIDIA CUDA
subtitle: NVIDIAs GPU-Computing-Plattform und Toolkit
slug: nvidia-cuda
description: CUDA ist NVIDIAs Plattform zum Ausführen allgemeiner Berechnungen auf den eigenen GPUs. Sie umfasst Compiler,
  Laufzeitumgebung und Bibliotheken wie cuDNN und cuBLAS. Fast alle großen Deep-Learning-Frameworks nutzen sie.
website: https://developer.nvidia.com/cuda-toolkit
company: nvidia
logo_url: ''
category: devtools
category_name: Entwicklertools
price: Free
featured: false
rank: 10
alternatives:
- amd-rocm
- openvino
- qualcomm-ai-hub
- nvidia-nim
date: '2026-11-05'
tags:
- developer_tools
- code_generation
- infrastructure
- deployment
- development
- devops
- ci_cd
- cloud
- api
- machine_learning
- training
i18n_source: '06f483092a94'
---

CUDA ist die Softwareschicht, mit der Programmierer:innen NVIDIA-Grafikprozessoren auch für andere Aufgaben als Grafikberechnungen verwenden können. Du schreibst Funktionen, sogenannte Kernels, meist in C++ oder Python. Sie laufen gleichzeitig auf Tausenden GPU-Threads und eignen sich daher für Aufgaben mit vielen parallelen Berechnungen. Wissenschaftliche Simulationen, Videoverarbeitung und vor allem neuronale Netze folgen diesem Muster. Deshalb wurde CUDA zur Grundlage für modernes KI-Training und die Inferenz.

Die meisten Menschen, die CUDA nutzen, schreiben selbst keinen CUDA-Code. PyTorch, TensorFlow und JAX greifen auf NVIDIAs Bibliotheken zurück: cuDNN für neuronale Netze, cuBLAS für lineare Algebra und NCCL für die Kommunikation zwischen GPUs. TensorRT und verwandte Werkzeuge optimieren Modelle für die Bereitstellung. Da diese Bibliotheken seit Jahren abgestimmt werden, läuft ein CUDA-Modell oft sofort schneller als derselbe Code auf Hardware anderer Anbieter. Dieser Softwarevorsprung ist ein wichtiger Grund dafür, dass NVIDIA-GPUs KI-Rechenzentren dominieren.

CUDA kann kostenlos heruntergeladen werden, funktioniert aber nur auf NVIDIA-Hardware. Das ist der Hauptkritikpunkt. CUDA-Code läuft ohne Portierung nicht auf AMD- oder Intel-GPUs, und viele Unternehmen wollen eine solche Bindung an einen Anbieter vermeiden. Übliche Alternativen sind AMD ROCm, OpenAI Triton, SYCL und Apples Metal. Jede deckt nur einen Teil der CUDA-Funktionen ab. Für die meisten Entwickler:innen ist der praktische Rat einfach: Nutze ein Framework, das CUDA für dich verwaltet, und schreibe erst dann eigene Kernels, wenn Profiling zeigt, dass du die zusätzliche Geschwindigkeit brauchst.
