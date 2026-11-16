---
title: 'Cloudflare AI Gateway'
name: 'Cloudflare AI Gateway'
subtitle: 'AI application observability, controls, and multi-provider routing'
slug: 'cloudflare-ai-gateway'
description: 'Cloudflare AI Gateway sits between an application and AI model providers. It provides analytics, logging, caching, rate limiting, retries, and model fallback so developers can observe usage and control costs.'
website: 'https://developers.cloudflare.com/ai-gateway/'
company: 'cloudflare'
logo_url: ''
category: 'devtools'
category_name: 'DevTools'
price: 'Freemium'
featured: false
rank: 5
alternatives:
  - portkey
  - litellm
  - helicone
  - langfuse
  - openrouter
  - vercel-ai-platform
  - eden-ai
date: '2026-07-17'
tags: [developer_tools, code_generation, infrastructure, deployment, development, devops, ci_cd, cloud, api, cloud_based, analytics, model_based]
---

AI Gateway is a proxy for calls to language models. A developer points their app's requests at a Cloudflare URL instead of the provider's, and the gateway forwards them while recording what happens. This gives a dashboard of requests, tokens, costs, and errors across providers like OpenAI, Anthropic, and Google.

It adds control features. Caching returns stored answers for repeated requests to save money and time, rate limits protect budgets, and retries and fallbacks switch to another model when one fails. Logging helps debug prompts, and guardrails and key management features support security.

The core features are available on Cloudflare's plans, many of them free, with some limits on log storage. It is useful for production applications that call several models. Alternatives include Portkey, LiteLLM, Helicone, OpenRouter, and Kong AI Gateway. Cloudflare AI Gateway suits developers who want visibility and control over model traffic.
