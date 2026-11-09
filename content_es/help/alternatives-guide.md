---
title: 'Alternativas: sugerencias y calidad'
slug: 'alternatives-guide'
subtitle: 'Cómo se construyen las páginas de comparación y cómo proponer una.'
order: 3
i18n_source: 'dc055f116fcc'
---

## Qué significa «alternativas» aquí

Cada ficha de herramienta puede listar unas pocas alternativas: otras herramientas que resuelven el mismo problema de una forma parecida. Best of AI convierte esa lista en una página propia en `/alternatives/<tool>/`, así que si estás mirando un creador de sitios web ves al lado opciones similares.

## Cómo pasa una herramienta a ser alternativa

Las alternativas se eligen por categoría y por uso, no por el tamaño de la marca. Una herramienta solo se lista como alternativa de otra si de verdad compite por el mismo trabajo. Una app de notas no va junto a un editor de vídeo solo porque las dos usen IA.

## Cómo proponer una

La lista de alternativas vive en el archivo de la propia herramienta, en un campo `alternatives:` que apunta a otros slugs. Para proponer un alta o una corrección, abre un pull request en [GitHub](https://github.com/best-of-ai/best-of-ai) que edite ese campo, o abre un issue describiendo la herramienta y la alternativa que tienes en mente.

## El listón de calidad

Una alternativa solo entra si pasa el mismo listón que cualquier otra herramienta del sitio: tiene que funcionar, hacer lo que dice y merecer el tiempo de alguien. Los sitios muertos, las herramientas fuera de categoría y los envoltorios de poco esfuerzo no entran, ni siquiera como «alternativa».

## Cómo funciona la página

Nada se monta a mano página por página. `/alternatives/<slug>/` se genera sola a partir del campo `alternatives:` del archivo de cada herramienta. Añades el campo y, en la siguiente build, aparecen la página y una sección de «alternativas a X» en la ficha de la herramienta.
