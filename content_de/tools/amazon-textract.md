---
title: 'Amazon Textract'
name: 'Amazon Textract'
subtitle: 'AWS-Dienst zum Erkennen von Text, Tabellen und Formularen in gescannten Dokumenten'
slug: 'amazon-textract'
description: 'Amazon Textract extrahiert Text und Dokumentstrukturen aus Scans und PDFs, darunter Tabellen, Formularfelder, Ausweise und Rechnungen.'
website: 'https://aws.amazon.com/textract/'
company: 'amazon'
logo_url: ''
category: 'document-ai'
category_name: 'Dokumenten-KI'
price: 'Paid'
featured: false
rank: 7
alternatives:
  - google-document-ai
  - azure-ai-document-intelligence
  - abbyy
  - nanonets
  - docsumo
  - reducto
date: '2026-11-05'
tags: [document_ai, pdf, productivity, extraction, documents, ocr, summarization, document_processing, parsing, voice_enabled]
i18n_source: '41f5cac62ceb'
---
Textract wandelt Dokumentbilder in strukturierte Daten um. Ein Entwickler sendet eine gescannte Datei oder PDF, und der Dienst gibt den erkannten Text samt Layout zurück: Er identifiziert Tabellen und erhält deren Zeilen und Spalten, erkennt Schlüssel-Wert-Paare in Formularen und liest auch Handschrift. Das ist nützlicher als reine Texterkennung, die lediglich einen ungeordneten Zeichenblock liefern würde.

Spezialisierte Funktionen sind auf häufige Dokumenttypen zugeschnitten. Analyze ID liest Pässe und Führerscheine, Analyze Expense extrahiert Positionen und Summen aus Rechnungen und Belegen, und Funktionen für die Kreditvergabe verarbeiten Hypothekendokumente. Mit Queries lassen sich Fragen stellen, etwa nach dem Rechnungsbetrag, und die Antwort aus dem Dokument abrufen. Ergebnisse können für weitere Analysen mit AWS-Diensten wie Comprehend, Bedrock und Step Functions verbunden werden.

Textract wird pro Seite abgerechnet; die Preise unterscheiden sich je nach Funktion. Für die ersten Monate gibt es ein kostenloses Kontingent. Die Erkennung ist bei sauberen Dokumenten gut, kann bei schlechten Scans, ungewöhnlichen Layouts oder Handschrift jedoch nachlassen. Bei sensiblen Dokumenten ist eine sorgfältige Sicherheitskonfiguration wichtig. Alternativen sind Google Document AI, Azure Document Intelligence, ABBYY und Open-Source-Werkzeuge wie Tesseract, das kostenlos ist, aber Strukturen weniger zuverlässig erkennt. Textract eignet sich für AWS-Teams, die Formulare und Rechnungen verarbeiten.
