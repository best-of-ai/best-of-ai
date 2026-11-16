---
title: 'Cloudflare Kitesurf'
name: 'Cloudflare Kitesurf'
subtitle: "Un navigateur cloud construit pour les agents d'IA, pas pour les humains"
slug: 'cloudflare-kitesurf'
description: "Kitesurf est un navigateur que Cloudflare a construit pour que des agents d'IA le pilotent, pas pour que des gens le regardent. Il tourne sur Cloudflare Workers et retire des parties d'un navigateur normal dont les agents n'ont pas besoin, comme les onglets et les extensions."
website: 'https://kitesurf.cloudflare.app/'
company: 'cloudflare'
logo_url: ''
category: 'devtools'
category_name: 'Outils de développement'
price: 'Free'
featured: false
rank: 5
alternatives:
  - browserbase
  - multion
  - e2b-ai
  - firecrawl
  - openai-operator
date: '2026-08-07'
tags: [developer_tools, code_generation, infrastructure, deployment, development, devops, ci_cd, cloud, api, free_tier, cloud_based, machine_learning]
i18n_source: '8918f291d1e6'
---

Kitesurf repense le navigateur pour le logiciel. La plupart des outils d'automatisation pilotent un navigateur de bureau complet, lourd et construit autour de l'usage humain. Kitesurf est un navigateur léger écrit pour tourner dans la plateforme Workers de Cloudflare, pour qu'un agent puisse ouvrir des pages, les lire, et cliquer ou taper sans le poids d'une instance Chrome complète.

Il fonctionne avec des outils existants. Les clients qui utilisent Puppeteer, Playwright ou le Model Context Protocol peuvent s'y connecter via le service de navigateur de Cloudflare avec de petits changements. Le design traite chaque page comme non fiable et démarre chaque session à neuf, ce qui convient à la sécurité des agents. Cloudflare dit qu'il utilise moins de mémoire que Chromium dans ses tests.

Kitesurf est en bêta et a des limites. Il ne convient pas à la lecture vidéo, à WebGL, aux longues sessions connectées, ni aux sites qui vérifient de vraies empreintes de navigateur, donc le service de navigateur standard de Cloudflare reste l'option pour ça. Parmi les alternatives : Browserbase, Browserless, Steel et Playwright auto-hébergé. Kitesurf convient aux développeurs qui construisent des agents qui lisent le web et interagissent avec lui à grande échelle.
