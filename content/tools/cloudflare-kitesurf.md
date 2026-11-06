---
title: 'Cloudflare Kitesurf'
name: 'Cloudflare Kitesurf'
subtitle: 'A cloud browser built for AI agents, not humans'
slug: 'cloudflare-kitesurf'
description: 'Kitesurf is a browser Cloudflare built for AI agents to drive, not for people to look at. It runs on Cloudflare Workers and removes parts of a normal browser that agents do not need, such as tabs and extensions.'
website: 'https://kitesurf.cloudflare.app/'
company: 'cloudflare'
logo_url: ''
category: 'devtools'
category_name: 'DevTools'
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
---

Kitesurf rethinks the browser for software. Most automation tools control a full desktop browser, which is heavy and built around human use. Kitesurf is a lean browser written to run inside Cloudflare's Workers platform, so an agent can open pages, read them, and click or type without the overhead of a complete Chrome instance.

It works with existing tools. Clients that use Puppeteer, Playwright, or the Model Context Protocol can connect to it through Cloudflare's browser service with small changes. The design treats every page as untrusted and starts each session fresh, which suits agent security. Cloudflare says it uses less memory than Chromium in its tests.

Kitesurf is in beta and has limits. It is not suited to video playback, WebGL, long logged-in sessions, or sites that check for real browser fingerprints, so Cloudflare's standard browser service remains the option for those. Alternatives include Browserbase, Browserless, Steel, and self-hosted Playwright. Kitesurf suits developers building agents that read and interact with the web at scale.
