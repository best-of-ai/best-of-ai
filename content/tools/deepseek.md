---
title: 'DeepSeek'
name: 'DeepSeek'
slug: 'deepseek'
subtitle: 'Chinese open-source AI models rivalling frontier performance'
description: 'DeepSeek is a Chinese AI lab that released DeepSeek-R1 and DeepSeek-V3 — models that match or surpass GPT-4-class performance at a fraction of the training cost, sending shockwaves through the AI industry in early 2025. Both models are open-weight and free to use, making them the most capable freely available models at their release. Developers and researchers worldwide use DeepSeek models as cost-efficient alternatives to proprietary frontier models.'
website: 'https://deepseek.com'
logo_url: ''
category: 'models'
category_name: 'Models'
price: 'Free'
featured: false
rank: 10
date: '2025-01-01'
tags: [llm, foundation_model, ai_model, machine_learning, neural, inference, fine_tuning, api, open_source, free_tier, training, model_based]
---

DeepSeek became a major story in early 2025 when V3 and then R1 appeared on standard benchmarks — MMLU, HumanEval, AIME, SWE-bench — with scores comparable to GPT-4o and Claude Sonnet, at a reported training cost fraction of what US labs spend. The models are open-weight, meaning anyone can download and run them without paying licensing fees, which made them immediately significant for the self-hosting community.

DeepSeek-R1 in particular attracted attention for its reasoning capabilities. Like OpenAI's o1, R1 uses extended chain-of-thought reasoning before responding to hard problems — mathematics, logic puzzles, and complex coding tasks — and its benchmark scores on those tasks are genuinely competitive. The model's reasoning traces are transparent (you can read the model's working-out), which some users find useful for debugging its logic on tricky problems.

The web chat interface at chat.deepseek.com is free to use, with no account required for basic queries. The API is priced very aggressively compared to US providers, making it attractive for high-volume applications where inference cost is a constraint. Data privacy considerations have led some organisations to self-host the open weights rather than use the API — the model is large (running the full V3 requires significant GPU memory) but community-built quantised versions run on more modest hardware.