---
title: 'NVIDIA Open Agent Safety Platform'
name: 'NVIDIA Open Agent Safety Platform'
subtitle: 'Capa de seguridad de código abierto que puede aislar en milisegundos a un agente de IA que se comporte mal'
slug: 'nvidia-open-agent-safety-platform'
description: 'Open Agent Safety Platform de NVIDIA combina OpenShell, un entorno abierto que aísla agentes, con Sentry, una capa de supervisión en DPU BlueField que funciona separada del equipo del agente y puede ponerlo en cuarentena.'
website: 'https://developer.nvidia.com/'
company: 'nvidia'
logo_url: ''
category: 'cybersecurity'
category_name: 'Ciberseguridad'
price: 'Free'
featured: false
rank: 5
alternatives:
  - lakera
  - patronus-ai
  - giskard
  - nightfall
date: '2026-09-28'
tags: [ai_powered, intelligent, platform, tool, service, solution, saas, online]
i18n_source: '9264e993765c'
---

La plataforma aborda una preocupación de seguridad: los agentes autónomos que pueden ejecutar comandos y acceder a datos necesitan límites que un agente comprometido no pueda desactivar. OpenShell es un entorno de ejecución de código abierto que coloca cada agente en un espacio aislado con permisos basados en políticas. Un verificador comprueba que los permisos concedidos no puedan combinarse para hacer algo que el operador no pretendía.

Sentry añade un mecanismo de control fuera de la máquina del agente. Funciona en unidades de procesamiento de datos BlueField, separadas del equipo anfitrión, y por eso puede vigilar el comportamiento y aislar rápidamente a un agente incluso si ese equipo está comprometido. NVIDIA la ha descrito como un diseño de referencia en el que muchos socios están integrando sus componentes.

El software es de código abierto y el componente de hardware requiere infraestructura NVIDIA. Los analistas señalan que demostrar la coherencia de los permisos no prueba que un agente sea seguro en todos los sentidos; revisar sus acciones sigue siendo importante. Entre las alternativas están herramientas de aislamiento como E2B y Daytona, los entornos aislados de Anthropic y OpenAI, y startups de seguridad centradas en agentes. La plataforma de NVIDIA sirve a organizaciones que despliegan agentes con fuertes necesidades de aislamiento.
