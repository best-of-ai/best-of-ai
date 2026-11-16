---
title: 'Cloudflare Kitesurf'
name: 'Cloudflare Kitesurf'
subtitle: 'Un navegador en la nube pensado para agentes de IA, no para personas'
slug: 'cloudflare-kitesurf'
description: 'Kitesurf es un navegador que Cloudflare creó para que lo manejen agentes de IA, no para que lo mire una persona. Funciona en Cloudflare Workers y elimina partes de un navegador normal que los agentes no necesitan, como las pestañas y las extensiones.'
website: 'https://kitesurf.cloudflare.app/'
company: 'cloudflare'
logo_url: ''
category: 'devtools'
category_name: 'Herramientas para desarrolladores'
price: 'Free'
featured: false
rank: 5
alternatives:
  - browserbase
  - multion
  - e2b-ai
  - firecrawl
  - openai-operator
date: '2026-08-07'
tags: [developer_tools, code_generation, infrastructure, deployment, development, devops, ci_cd, cloud, api, free_tier, cloud_based, machine_learning]
i18n_source: '8918f291d1e6'
---

Kitesurf repiensa el navegador para el software. La mayoría de las herramientas de automatización controlan un navegador de escritorio completo, que es pesado y está construido en torno al uso humano. Kitesurf es un navegador ligero escrito para ejecutarse dentro de la plataforma Workers de Cloudflare, de modo que un agente pueda abrir páginas, leerlas y hacer clic o escribir sin la carga de una instancia completa de Chrome.

Funciona con las herramientas existentes. Los clientes que usan Puppeteer, Playwright o el Model Context Protocol pueden conectarse a través del servicio de navegador de Cloudflare con pocos cambios. El diseño trata cada página como no confiable y empieza cada sesión desde cero, lo que favorece la seguridad de los agentes. Cloudflare asegura que usa menos memoria que Chromium en sus pruebas.

Kitesurf está en beta y tiene límites. No sirve para reproducción de vídeo, WebGL, sesiones largas con inicio de sesión ni sitios que comprueban huellas de navegador reales, así que para eso sigue siendo la opción el servicio de navegador estándar de Cloudflare. Entre las alternativas están Browserbase, Browserless, Steel y Playwright alojado por cuenta propia. Kitesurf encaja con desarrolladores que crean agentes que leen e interactúan con la web a gran escala.
