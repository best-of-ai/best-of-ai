---
title: 'Alternativen: Vorschläge und Qualität'
slug: 'alternatives-guide'
subtitle: 'So entstehen Vergleichsseiten für Alternativen und so kannst du eine vorschlagen.'
order: 3
i18n_source: 'dc055f116fcc'
---

## Was „Alternativen“ hier bedeutet

Auf jeder Tool-Seite können einige Alternativen stehen: andere Tools, die ein ähnliches Problem auf ähnliche Weise lösen. Best of AI macht daraus eine eigene Seite unter `/alternatives/<tool>/`. Wenn du dir also einen Website-Baukasten ansiehst, findest du dort direkt ähnliche Optionen.

## Wann ein Tool als Alternative aufgeführt wird

Alternativen wählen wir nach Kategorie und Einsatzzweck aus, nicht nach der Größe einer Marke. Ein Tool wird nur dann als Alternative zu einem anderen aufgeführt, wenn es tatsächlich um denselben Anwendungsfall konkurriert. Eine Notiz-App gehört nicht neben einen Videoeditor, nur weil beide KI nutzen.

## Eine Alternative vorschlagen

Die Alternativen stehen in der Datei des jeweiligen Tools im Feld `alternatives:`. Dort verweisen sie auf die Slugs anderer Tools. Um einen Eintrag vorzuschlagen oder zu korrigieren, öffne auf [GitHub](https://github.com/best-of-ai/best-of-ai) einen Pull Request, der dieses Feld ändert, oder beschreibe das Tool und die gewünschte Alternative in einem Issue.

## Unser Qualitätsmaßstab

Eine Alternative wird nur aufgenommen, wenn sie denselben Maßstab wie alle anderen Tools auf der Website erfüllt: Sie muss funktionieren, halten, was sie verspricht, und die Zeit wert sein. Inaktive Websites, Tools aus unpassenden Kategorien und lieblos zusammengestellte Wrapper schaffen es auch als „Alternative“ nicht auf die Liste.

## So funktioniert die Seite

Keine Seite wird von Hand erstellt. `/alternatives/<slug>/` entsteht automatisch aus dem Feld `alternatives:` in der jeweiligen Tool-Datei. Füge das Feld hinzu, und beim nächsten Build der Website erscheinen sowohl die Seite als auch ein passender Abschnitt „Alternativen zu X“ auf der Tool-Seite.
