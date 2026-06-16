---
title: 'Llama 3'
name: 'Llama 4'
subtitle: 'Meta''s latest open-weight language model family'
slug: 'llama-3'
description: 'Llama 4 is Meta''s latest generation of open-weight large language models, featuring a Mixture-of-Experts architecture that achieves frontier-level capability while remaining freely downloadable under Meta''s community licence. The family spans Scout (17B active parameters, 10M-token context), Maverick (17B active, multimodal), and Behemoth (288B active, teacher model) variants. Its open nature makes it the most widely self-hosted and fine-tuned LLM family, deployed in production across research labs, enterprises, and consumer applications worldwide.'
website: 'https://llama.meta.com'
logo_url: ''
category: 'models'
category_name: 'Models'
price: 'Free'
featured: false
rank: 10
date: '2025-09-21'
tags: [llm, foundation_model, ai_model, machine_learning, neural, inference, fine_tuning, api, open_source, multimodal, enterprise, free_tier]
---

Llama's importance to the AI ecosystem comes from what its open weights enable that closed models don't: full control. You can download the model, run it locally, fine-tune it on proprietary data that never leaves your infrastructure, modify the system prompt without restrictions, and build products without API dependency or per-token costs at scale. For enterprises with sensitive data, healthcare applications, or legal requirements around data jurisdiction, self-hosted Llama is often the only feasible path.

The Llama 4 architecture uses Mixture-of-Experts (MoE), activating only a subset of its total parameters for each forward pass. This means that despite having a very large total parameter count, the compute per token is closer to a much smaller model — enabling competitive capability at lower inference cost. The Scout variant has a 10 million-token context window, which is the longest of any publicly released model and opens up use cases like full-codebase analysis and extended document research that would require multiple chunked calls with shorter-context models.

Meta releases Llama models under a community licence that allows commercial use for most organisations, with restrictions for very large companies. The weights are available on Hugging Face and Meta's own Llama repository. Quantised versions (GGUF format) run on consumer hardware with as little as 8GB of RAM for the smaller variants. Developers access Llama through every major cloud provider's model API, through services like Groq and Together AI for fast inference, or run it locally via Ollama. Its community is the largest of any open-source model, meaning fine-tunes, guides, and tooling are widely available.