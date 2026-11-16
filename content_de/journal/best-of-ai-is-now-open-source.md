---
title: 'Best of AI ist jetzt Open Source!'
slug: 'best-of-ai-is-now-open-source'
subtitle: 'Ein Jahr lang haben wir KI-Tools handverlesen. Jetzt stehen Repository, Rangliste und Deployment-Pipeline allen auf GitHub offen.'
date: '2026-06-25'
related_categories:
  - ai-directories
related_tools:
  - best-of-ai
i18n_source: 'd8ce6e206afa'
---

Vor etwa einem Jahr haben wir Best of AI als kuratierte Liste empfehlenswerter KI-Tools gestartet. Jetzt ist das ganze Projekt [auf GitHub Open Source](https://github.com/best-of-ai/best-of-ai): Daten, Website, Skripte und CI. Von nun an kann die Community mitgestalten.

## Einfache Dateien statt Datenbank

Jedes Tool ist eine Markdown-Datei in `content/tools/`. Kategorien stehen in `data/categories.yaml`. Die [Rangliste](/leaderboard/) liest ihre Daten aus `data/leaderboard.yaml`. Kein Postgres, kein Headless-CMS, keine Abhängigkeit von einem Anbieter. Klone das Repository, suche mit `git grep`, was du brauchst, und öffne bei Fehlern einen PR. So einfach ist das Modell.

Die Website wird mit [Hugo](https://gohugo.io/) statisch erstellt: HTML, CSS und etwas Vanilla JavaScript. Ein Push auf `main` startet eine GitHub Action, die `hugo --minify` ausführt und das Ergebnis auf GitHub Pages veröffentlicht. Ein Server muss nicht betreut werden.

## GitHub Actions erledigen die Routinearbeit

Drei Workflows sind besonders nützlich:

- **Deploy** erstellt und veröffentlicht die Website bei jedem Push auf `main`.
- **Issue → PR** prüft ein Tool-Vorschlags-Issue mit der passenden Vorlage. `issue-review.py` validiert es, erstellt einen Branch und öffnet einen PR.
- **Update README** erstellt die `README.md` aus den Tool-Dateien neu, sobald sich Daten ändern.

Reiche ein Tool per Issue oder PR ein. Korrigiere eine Beschreibung in einer Markdown-Datei. Diskutiere Ranglistenplätze in `data/leaderboard.yaml`. Alles lässt sich prüfen und bleibt im Git-Verlauf nachvollziehbar.

## Rangliste, Berufe und mehr

Die [Rangliste](/leaderboard/) ist eine Auswahl bewerteter Tools, die wir wirklich gut finden – nicht einfach der beliebtesten. Die Ranglistenplätze beruhen auf Daten, nicht auf Bauchgefühl: Bearbeite die YAML-Datei, öffne einen PR und begründe deinen Vorschlag.

Auf den [Berufsseiten](/professionals/) sind Tools nach Tätigkeitsfeldern sortiert: etwa für Entwickler, Designer, Marketingfachleute, Schreibende und mehr als 200 weitere Berufe. In jeder Berufsdatei stehen Kategorie-Slugs; Hugo fügt passende Tools automatisch hinzu. Einen Beruf ergänzt du wie ein Tool: Markdown-Datei erstellen, PR öffnen, fertig.

Die Suche läuft im Browser. Das Suchfenster im Kopfbereich ruft [`/index.json`](/index.json) ab – einen beim Build erstellten JSON-Index. Du kannst die Daten forken, eine eigene Oberfläche bauen und sie beliebig einbinden. Ein API-Schlüssel ist nicht nötig.

## Mach mit

Wenn du Verzeichnisse magst, die in Git leben, statische Websites, die sich selbst veröffentlichen, und Listen, zu denen man direkt Änderungen beitragen kann, bist du hier richtig.

- [Mitwirken](/contribute/) – Tools einreichen, Einträge korrigieren und Ranglisten verbessern
- [GitHub-Repository](https://github.com/best-of-ai/best-of-ai) – klonen, ausprobieren, korrigieren und einen PR senden

Das Verzeichnis ist kostenlos nutzbar. Code und Daten kannst du forken. Wir freuen uns über hundert Menschen, die die Liste verbessern, statt über eine einzelne Person, die den Zugang kontrolliert.
