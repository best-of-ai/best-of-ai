---
title: 'Amazon Bedrock'
name: 'Amazon Bedrock'
subtitle: 'Servicio gestionado de AWS para acceder a modelos fundacionales mediante API'
slug: 'amazon-bedrock'
description: 'Amazon Bedrock es el servicio gestionado de AWS para crear aplicaciones de IA generativa. Da acceso a modelos fundacionales de muchos proveedores a través de una sola API, con herramientas de recuperación, agentes, guardarraíles y evaluación.'
website: 'https://aws.amazon.com/bedrock'
company: 'amazon'
logo_url: ''
category: 'devtools'
category_name: 'Herramientas para desarrolladores'
price: 'Freemium'
featured: false
rank: 9
alternatives:
  - azure-openai
  - vertex-ai
  - together-ai
  - fireworks-ai
  - openrouter
  - groq
date: '2025-09-21'
tags: [developer_tools, code_generation, infrastructure, deployment, development, devops, ci_cd, cloud, api, api_available, enterprise, secure]
i18n_source: '03ddec47ee00'
---

Bedrock es la forma en que muchas empresas de AWS usan grandes modelos de lenguaje sin gestionar ninguna infraestructura de modelos. En lugar de firmar contratos distintos con cada laboratorio de IA, eliges de un catálogo de modelos de proveedores como Anthropic, Meta, Mistral y la propia Amazon, y los llamas a través de una sola API. Los datos permanecen dentro de tu cuenta de AWS, algo importante para equipos con requisitos de seguridad, privacidad y cumplimiento, y funciona con las herramientas de IAM, red y registro que ya usan.

Alrededor de los modelos están las piezas necesarias para crear una aplicación real. Knowledge Bases conecta un modelo con tus propios documentos para dar respuestas con recuperación aumentada. Agents permite que un modelo planifique y llame a APIs para completar tareas, y AgentCore ofrece infraestructura para ejecutar agentes creados con cualquier framework. Guardrails bloquea temas no deseados y datos sensibles, y puede comprobar que las respuestas estén fundamentadas en hechos. También hay herramientas para evaluar modelos entre sí, ajustarlos con fine-tuning y guardar prompts en caché para reducir costes.

Bedrock cobra por uso, normalmente por token en el uso bajo demanda, con procesamiento por lotes y capacidad reservada como opciones cuando las cargas son estables. La variedad de modelos y la rapidez con que llegan los nuevos difieren de las APIs de los propios proveedores, así que un modelo puede llegar a Bedrock más tarde que a la web del laboratorio. Sus competidores son Azure AI Foundry y Vertex AI de Google Cloud. Los equipos que ya están comprometidos con AWS suelen elegir Bedrock por comodidad y por la facturación unificada.
