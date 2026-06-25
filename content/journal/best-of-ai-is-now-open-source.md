---
title: 'Best of AI is now open source!'
slug: 'best-of-ai-is-now-open-source'
subtitle: 'A year of handpicking AI tools — now the repo, leaderboard, and deploy pipeline are on GitHub for anyone to use.'
date: '2026-06-25'
related_categories:
  - ai-directories
related_tools:
  - best-of-ai
---

We started Best of AI about a year ago as a curated list of AI tools worth using. Today the whole thing is [open source on GitHub](https://github.com/best-of-ai/best-of-ai) — data, site, scripts, CI. Community-driven from here on out.

## Flat files, no database

Every tool is a Markdown file in `content/tools/`. Categories live in `data/categories.yaml`. The [leaderboard](/leaderboard/) ranks tools from `data/leaderboard.yaml`. No Postgres, no headless CMS, no vendor lock-in. Clone the repo, `git grep` for what you need, send a PR when something's wrong. That's the whole model.

The site is a [Hugo](https://gohugo.io/) static build. HTML, CSS, a bit of vanilla JS. Push to `main`, a GitHub Action runs `hugo --minify`, and the result lands on GitHub Pages. No server to babysit.

## GitHub Actions do the boring stuff

Three workflows worth knowing about:

- **Deploy** — builds and publishes on every push to `main`
- **Issue → PR** — open a tool submission issue with the right template and `issue-review.py` validates it, opens a branch, and files a PR
- **Update README** — regenerates `README.md` from the tool files whenever the data changes

Submit a tool via issue or PR. Fix a description by editing one Markdown file. Argue about leaderboard rankings in `data/leaderboard.yaml`. All reviewable, all in git history.

## Leaderboard, professions, and the rest

The [leaderboard](/leaderboard/) is a ranked shortlist — tools we think are genuinely good, not just popular. Rankings are data, not vibes: edit the YAML, open a PR, make your case.

[Profession pages](/professionals/) group tools by role — developers, designers, marketers, writers, and 200+ more. Each profession file lists category slugs; Hugo pulls matching tools automatically. Add a profession the same way you'd add a tool: Markdown file, PR, done.

Search is client-side. The header modal fetches [`/index.json`](/index.json) — a JSON index built at compile time. Fork the data, build your own UI, plug it into whatever you want. No API key.

## Come hack on it

If you like directories that live in git, static sites that deploy themselves, and directories you can actually send a patch to — this is for you.

- [Contribute](/contribute/) — how to submit tools, fix listings, improve rankings
- [GitHub repo](https://github.com/best-of-ai/best-of-ai) — clone it, break it, fix it, PR it

The directory is free to browse. The code and data are yours to fork. We'd rather have a hundred people improving the list than one person gatekeeping it.