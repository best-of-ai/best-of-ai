---
title: 'Cómo funciona el sitio'
slug: 'how-the-site-works'
subtitle: 'Hugo, archivos planos y un pipeline de GitHub Actions. Sin base de datos.'
order: 8
i18n_source: '2f8d3f5e4878'
---

## Sin base de datos, solo archivos

Cada herramienta es un archivo Markdown en `content/tools/`. Cada categoría vive en `data/categories.yaml`. No hay panel de administración ni backend que mantener; el sitio entero son archivos planos en un repositorio de Git. Todo se construye con [Hugo](https://gohugo.io/), un generador de sitios estáticos, y sale en HTML plano.

## Qué hace GitHub Actions

Tres flujos de trabajo se ocupan de la parte aburrida:

- **Deploy** construye y publica el sitio en cada push a `main`.
- **Issue to PR** revisa solo los issues de envío de herramientas y abre un pull request cuando el formato encaja.
- **Update README** regenera `README.md` cuando cambian los datos de las herramientas.

## Por qué está hecho así

Los archivos planos permiten que cualquiera clone el repositorio y vea exactamente qué hay en el sitio y por qué. No hay una base de datos oculta de la que fiarse; los datos son el mismo archivo que editarías para corregirlos.

## Mira el código

El código, las plantillas, los scripts y los datos son públicos en [github.com/best-of-ai/best-of-ai](https://github.com/best-of-ai/best-of-ai).
