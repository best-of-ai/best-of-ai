---
title: 'Aider'
name: 'Aider'
slug: 'aider'
subtitle: 'Terminal-based AI pair programmer for your git repo'
description: 'Aider is an open-source AI coding assistant that runs in your terminal and edits files in your local git repository. You ask for a change in plain language, and it makes the edits, can run tests, and commits the result.'
website: 'https://aider.chat'
company: 'aider'
logo_url: ''
category: 'code-assistant'
category_name: 'Code Assistant'
price: 'Free'
featured: false
rank: 9
alternatives:
  - cline
  - claude-code
  - codex
  - opencode
  - continue-dev
  - plandex
date: '2025-01-01'
tags: [code_generation, developer_tools, productivity, coding, programming, autocomplete, debugging, refactoring, ide, open_source, cloud_based, nlp]
---

Aider is a command-line tool for pair programming with a language model. You start it inside a git repository, add the files you want to work on, and describe what you want in plain English. It edits the files directly, shows the diff, and commits each change with a sensible message, so you can review or undo anything the model did with ordinary git commands. That tight git integration is what makes it feel safe to use on a real project.

To handle larger codebases it builds a map of the repository, which helps the model understand how files relate without loading everything into one prompt. It can lint and run tests after each change and try to fix the problems it finds. Aider works with a wide range of models, from hosted ones such as Claude, GPT, and DeepSeek to local models, and it supports voice input and image or web page context when you need them.

The tool itself is free and open source, and you pay only for the API usage of whichever model you connect. That makes costs transparent but also means heavy sessions can add up. Aider has no graphical interface, so it suits developers who are comfortable in a terminal and prefer to stay in their own editor. Cursor and Windsurf offer editor-based alternatives, and Claude Code and Codex CLI are the closest terminal competitors.
