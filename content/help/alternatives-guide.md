---
title: 'Alternatives: Suggestions & Quality'
slug: 'alternatives-guide'
subtitle: 'How the alternative comparison pages get built, and how to suggest one.'
order: 3
---

## What "alternatives" means here

Every tool page can list a handful of alternatives: other tools that solve the same problem in a similar way. Best of AI turns that list into a dedicated page at `/alternatives/<tool>/`, so if you're looking at a website builder, you can immediately see similar options next to it.

## How a tool becomes a listed alternative

Alternatives are picked by category and use case, not by brand size. A tool only gets listed as an alternative to another if it genuinely competes for the same job. A note-taking app doesn't belong next to a video editor just because both happen to use AI.

## How to suggest one

The alternatives list lives inside the tool's own file, as an `alternatives:` field pointing to other tool slugs. To suggest an addition or a correction, open a pull request on [GitHub](https://github.com/best-of-ai/best-of-ai) that edits that field, or open an issue describing the tool and the alternative you have in mind.

## The quality bar

An alternative only gets added if it clears the same bar as every other tool on the site: it has to work, do what it claims, and be worth someone's time. Dead sites, off-category tools, and low-effort wrappers don't make the cut, even as an "alternative."

## How the page works

Nothing is hand-built per page. `/alternatives/<slug>/` is generated automatically from the `alternatives:` field on each tool's file. Add the field, and the page, along with a matching "alternatives to X" section on the tool's own page, appears the next time the site builds.
