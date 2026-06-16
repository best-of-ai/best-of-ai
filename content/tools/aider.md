---
title: 'Aider'
name: 'Aider'
slug: 'aider'
subtitle: 'Terminal-based AI pair programmer for your git repo'
description: 'Aider is an open-source AI coding assistant that runs in your terminal and edits code directly in your local git repository. You describe what you want in natural language and Aider makes the changes, runs tests, and commits the result — working across multiple files simultaneously. Developers who prefer a keyboard-driven, local workflow over a cloud IDE use Aider as a powerful alternative to Cursor or Copilot.'
website: 'https://aider.chat'
logo_url: ''
category: 'code-assistant'
category_name: 'Code Assistant'
price: 'Free'
featured: false
rank: 9
date: '2025-01-01'
tags: [code_generation, developer_tools, productivity, coding, programming, autocomplete, debugging, refactoring, ide, open_source, cloud_based, nlp]
---

Aider connects to your local git repository and lets you make changes through natural language commands in your terminal. You describe what you want — "add input validation to the signup form," "refactor the database connection to use a connection pool," "write unit tests for the auth module" — and Aider reads the relevant files, plans the changes, and applies them. When it's done, it shows you a diff and asks if you want to commit. It handles multi-file changes that would take significant manual effort.

What differentiates Aider from browser-based AI coding tools is that it works entirely locally on your own codebase. There's no sync to a cloud editor, no project setup process, and no leaving your terminal environment. It uses whichever LLM you configure — Claude, GPT-4o, Gemini, or local models via Ollama — through their APIs. This means your model choice, your API key, and your code all stay within your control. The tool is open-source, so you can inspect the code and run it on air-gapped machines if needed.

Aider itself is free to install and run via `pip install aider-install`. You pay only for the API tokens consumed by whichever model you connect it to. The most capable coding performance comes from Claude Sonnet and Opus models. Aider's benchmark performance on SWE-bench (a measure of coding agent effectiveness on real GitHub issues) has consistently ranked it among the top-performing open-source AI coding tools. Developers who live in the terminal and want AI that meets them there rather than pulling them into a browser-based editor find Aider the most natural fit.