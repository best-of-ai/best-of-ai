---
title: Cloudflare AI Gateway
name: Cloudflare AI Gateway
subtitle: Observabilidade, controles e roteamento entre provedores para aplicações
  de IA
slug: cloudflare-ai-gateway
description: O Cloudflare AI Gateway fica entre um aplicativo e os provedores de modelos
  de IA. Oferece análises, registro de atividades, cache, limitação de taxa, novas
  tentativas e modelos alternativos para que desenvolvedores monitorem o uso e controlem
  custos.
website: https://developers.cloudflare.com/ai-gateway/
company: cloudflare
logo_url: ''
category: devtools
category_name: Ferramentas para desenvolvedores
price: Freemium
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
- cloud_based
- analytics
- model_based
i18n_source: '76831d31774b'
---

O AI Gateway é um proxy para chamadas a modelos de linguagem. O desenvolvedor direciona as solicitações do aplicativo a um endereço da Cloudflare, em vez de enviá-las diretamente ao provedor, e o gateway as encaminha enquanto registra o que acontece. Assim, um painel mostra solicitações, tokens, custos e erros em provedores como OpenAI, Anthropic e Google.

O serviço acrescenta recursos de controle. O cache devolve respostas armazenadas para solicitações repetidas, economizando dinheiro e tempo; limites de taxa protegem o orçamento; e novas tentativas e alternativas encaminham as chamadas a outro modelo quando um falha. Os registros ajudam a depurar prompts, e recursos de proteção e gestão de chaves dão suporte à segurança.

Os principais recursos estão disponíveis nos planos da Cloudflare, muitos deles gratuitos, com alguns limites de armazenamento de registros. O serviço é útil para aplicativos em produção que chamam vários modelos. Entre as alternativas estão Portkey, LiteLLM, Helicone, OpenRouter e Kong AI Gateway. O Cloudflare AI Gateway é indicado para desenvolvedores que querem visibilidade e controle sobre o tráfego de modelos.
