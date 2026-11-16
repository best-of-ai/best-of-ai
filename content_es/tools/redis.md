---
title: 'Redis'
name: 'Redis'
subtitle: 'Base de datos en memoria que se usa para caché y búsqueda vectorial'
slug: 'redis'
description: 'Redis es un almacén de datos en memoria que se usa para caché, colas, sesiones y funciones en tiempo real. También admite búsqueda vectorial, JSON y caché semántica, por lo que los equipos lo usan en aplicaciones de IA que necesitan consultas rápidas.'
website: 'https://redis.io'
logo_url: ''
category: 'devtools'
category_name: 'Herramientas para desarrolladores'
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

Redis guarda los datos en memoria, lo que hace que leerlos y escribirlos sea muy rápido. Los desarrolladores lo usan como caché delante de una base de datos más lenta, como almacén de sesiones de usuarios autenticados, como cola de mensajes, y para rankings, limitación de peticiones y contadores. Sus tipos de datos, como listas, conjuntos, conjuntos ordenados, hashes y streams, facilitan construir estos patrones con comandos sencillos. Es una de las piezas de infraestructura más desplegadas de la web.

Para la IA, Redis ha añadido búsqueda vectorial, de modo que las aplicaciones pueden guardar embeddings y encontrar elementos similares para la generación aumentada por recuperación, las recomendaciones y la búsqueda semántica. La caché semántica guarda las respuestas a preguntas anteriores y las devuelve para preguntas nuevas parecidas, lo que reduce el coste y la latencia al llamar a modelos de lenguaje. Redis también guarda la memoria de conversación de los agentes. Funciona como software de código abierto, como Redis Cloud y en despliegues para empresas.

La licencia ha sido motivo de debate: Redis la cambió de una forma que dio lugar a un fork de la comunidad llamado Valkey, respaldado por proveedores de nube, y más tarde volvió a ofrecer una opción de licencia de código abierto. La memoria es más cara que el disco, así que los conjuntos de datos grandes pueden costar mucho, y la durabilidad requiere configuración. Entre las alternativas están Valkey, Memcached para cachés sencillas, DragonflyDB y servicios en la nube como Amazon ElastiCache. Redis encaja con aplicaciones donde la velocidad es crítica.
