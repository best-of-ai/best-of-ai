---
title: 'NVIDIA CUDA'
name: 'NVIDIA CUDA'
subtitle: 'NVIDIA''s GPU computing platform and toolkit'
slug: 'nvidia-cuda'
description: 'CUDA is NVIDIA''s platform for running general-purpose code on its GPUs. It includes a compiler, runtime, and libraries such as cuDNN and cuBLAS, and nearly every major deep learning framework relies on it.'
website: 'https://developer.nvidia.com/cuda-toolkit'
company: 'nvidia'
logo_url: ''
category: 'devtools'
category_name: 'DevTools'
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
---

CUDA is the software layer that lets programmers use an NVIDIA graphics processor for things other than graphics. You write functions called kernels, usually in C++ or Python, that run across thousands of GPU threads at once, which suits workloads built from large amounts of parallel math. Scientific simulation, video processing, and above all neural networks fit that description, so CUDA became the foundation for modern AI training and inference.

Most people who use CUDA never write it directly. PyTorch, TensorFlow, and JAX call into NVIDIA's libraries, including cuDNN for neural network operations, cuBLAS for linear algebra, and NCCL for communication between GPUs. TensorRT and related tools optimize models for deployment. Because these libraries have been tuned for years, a model that runs on CUDA is often faster out of the box than the same code on another vendor's hardware. That software lead is a large part of why NVIDIA GPUs dominate AI data centers.

CUDA is free to download, but it only works on NVIDIA hardware, which is the main criticism. Code written in CUDA cannot run on AMD or Intel GPUs without porting, and many companies try to avoid that lock-in. AMD's ROCm, OpenAI's Triton, SYCL, and Apple's Metal are the usual alternatives, and each covers only part of what CUDA does. For most developers the practical advice is simple: use a framework that handles CUDA for you, and only drop down to writing kernels when profiling shows you need the extra speed.
