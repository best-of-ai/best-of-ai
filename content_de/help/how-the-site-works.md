---
title: 'So funktioniert die Website'
slug: 'how-the-site-works'
subtitle: 'Hugo, einfache Dateien und eine GitHub-Actions-Pipeline. Ohne Datenbank.'
order: 8
i18n_source: '2f8d3f5e4878'
---

## Keine Datenbank, nur Dateien

Jedes Tool ist eine Markdown-Datei in `content/tools/`. Jede Kategorie steht in `data/categories.yaml`. Es gibt weder ein Admin-Panel noch ein Backend, das verwaltet werden muss: Die ganze Website besteht aus Dateien in einem Git-Repository. [Hugo](https://gohugo.io/) erstellt daraus als statischer Website-Generator einfaches HTML.

## Was GitHub Actions übernimmt

Drei Workflows erledigen die Routinearbeit:

- **Deploy** erstellt und veröffentlicht die Website bei jedem Push auf `main`.
- **Issue to PR** prüft Einreichungen für neue Tools automatisch und öffnet für passende Vorschläge einen Pull Request.
- **Update README** erstellt die `README.md` neu, wenn sich Tool-Daten ändern.

## Warum die Website so aufgebaut ist

Mit einfachen Dateien kann jede Person das Repository klonen und genau sehen, was auf der Website steht und warum. Es gibt keine verborgene Datenbank, der man vertrauen muss. Die Daten stehen in derselben Datei, die man zur Korrektur bearbeiten würde.

## Sieh dir den Code an

Der vollständige Quellcode mit Website-Vorlagen, Skripten und Daten ist öffentlich unter [github.com/best-of-ai/best-of-ai](https://github.com/best-of-ai/best-of-ai) verfügbar.
