---
title: 'Redis'
name: 'Redis'
subtitle: 'In-Memory-Datenbank für Caching und Vektorsuche'
slug: 'redis'
description: 'Redis ist ein In-Memory-Datenspeicher für Caching, Warteschlangen, Sitzungen und Echtzeitfunktionen. Er unterstützt außerdem Vektorsuche, JSON und semantisches Caching und wird deshalb in KI-Anwendungen für schnelle Abfragen eingesetzt.'
website: 'https://redis.io'
logo_url: ''
category: 'devtools'
category_name: 'Entwicklerwerkzeuge'
price: 'Freemium'
featured: false
rank: 8
alternatives:
  - pinecone
  - qdrant
  - weaviate
  - mongodb-atlas
  - elasticsearch
date: '2026-11-05'
tags: [developer_tools, code_generation, infrastructure, deployment, development, devops, ci_cd, cloud, api, collaboration, fast]
i18n_source: '294da6bd62ae'
---
Redis speichert Daten im Arbeitsspeicher und ermöglicht dadurch sehr schnelle Lese- und Schreibzugriffe. Entwickler nutzen es als Cache vor einer langsameren Datenbank, als Sitzungsspeicher für angemeldete Nutzer, als Nachrichtenwarteschlange sowie für Ranglisten, Ratenbegrenzungen und Zähler. Datentypen wie Listen, Mengen, sortierte Mengen, Hashes und Streams erleichtern die Umsetzung dieser Muster mit einfachen Befehlen. Redis ist eine der am häufigsten eingesetzten Infrastrukturkomponenten im Web.

Für KI wurde Vektorsuche ergänzt. Anwendungen können Embeddings speichern und ähnliche Elemente für Retrieval-Augmented Generation, Empfehlungen und semantische Suche finden. Semantisches Caching speichert Antworten auf frühere Fragen und gibt sie bei ähnlichen neuen Fragen zurück. So sinken Kosten und Latenz beim Aufruf von Sprachmodellen. Redis speichert außerdem den Gesprächskontext von Agenten. Es ist als Open-Source-Software, Redis Cloud und für Unternehmensinstallationen verfügbar.

Die Lizenzierung war umstritten: Redis änderte seine Lizenz. Daraufhin entstand die von Cloudanbietern unterstützte Community-Abspaltung Valkey; später bot Redis erneut eine Open-Source-Lizenzoption an. Arbeitsspeicher ist teurer als Festplattenspeicher, daher können große Datensätze kostspielig sein. Auch die dauerhafte Speicherung muss konfiguriert werden. Alternativen sind Valkey, Memcached für einfaches Caching, DragonflyDB und Cloudangebote wie Amazon ElastiCache. Redis eignet sich für Anwendungen, bei denen Geschwindigkeit entscheidend ist.
