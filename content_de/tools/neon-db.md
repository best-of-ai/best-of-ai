---
title: Neon
name: Neon
slug: neon-db
description: Neon ist ein serverloser PostgreSQL-Datenbankdienst mit automatischer Skalierung, Scale-to-Zero und sofortigen
  Datenbank-Branches. Der Dienst gehört inzwischen zu Databricks und ist beliebt für Apps, Vorschauumgebungen und KI-Agenten,
  die viele Datenbanken benötigen.
website: https://neon.tech
company: neon
logo_url: ''
category: database-tools
category_name: Datenbanken
price: Freemium
featured: false
rank: 8
alternatives:
- supabase-ai
- planetscale
- turso
- mongodb-atlas
date: '2026-06-15'
tags:
- collaboration
- model_based
- fast
- ai_powered
- intelligent
- platform
- tool
- service
i18n_source: 'c4e0f3856856'
---

Neon hat Postgres für die Cloud neu aufgestellt, indem Speicher und Rechenleistung voneinander getrennt wurden. So kann eine Datenbank bei hoher Last wachsen und im Leerlauf auf null skalieren. Du zahlst nach Nutzung, statt einen Server dauerhaft laufen zu lassen. Entwickler:innen erhalten Standard-Postgres; vorhandene Tools, Treiber und Erweiterungen funktionieren weiter, darunter pgvector zum Speichern von Embeddings in KI-Anwendungen.

Die besondere Funktion sind Branches. Da Speicher per Copy-on-Write arbeitet, lässt sich eine vollständige Datenbankkopie in Sekunden erstellen – ähnlich einem Git-Branch. Das hilft beim Testen von Migrationen, beim Erstellen einer Vorschauumgebung für jeden Pull Request oder beim Bereitstellen isolierter Kopien für Entwickler:innen. Dieselbe Funktion macht Neon für KI-Programmieragenten und Plattformen attraktiv, die viele kurzlebige Datenbanken starten. Verbindungspooling, Lesereplikate und Integrationen mit Vercel und anderen Plattformen sind ebenfalls verfügbar.

Neon bietet einen kostenlosen Tarif für kleinere Projekte und nutzungsbasierte Bezahlpläne. Databricks übernahm Neon, um Datenbanken für KI-Agenten bereitzustellen, und erklärte, der Dienst werde fortgeführt. Nach Scale-to-Zero kann der Kaltstart eine kurze Verzögerung verursachen; die Kosten hängen von Rechenzeit und Speicher ab. Supabase bietet Postgres mit einem breiteren Backend-Werkzeugkasten; PlanetScale und AWS Aurora Serverless sind Konkurrenten. CockroachDB bedient verteilte Anwendungen. Neon ist eine beliebte Wahl für moderne Web-Apps.
