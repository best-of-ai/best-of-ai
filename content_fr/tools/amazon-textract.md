---
title: 'Amazon Textract'
name: 'Amazon Textract'
subtitle: 'Service AWS qui extrait texte, tableaux et formulaires de documents scannés'
slug: 'amazon-textract'
description: 'Amazon Textract est un service AWS qui extrait le texte, les tableaux et les champs de formulaire de documents scannés et de PDF. Il va au-delà de l''OCR de base en comprenant la structure, et inclut des fonctions pour les pièces d''identité, les factures et les requêtes.'
website: 'https://aws.amazon.com/textract/'
company: 'amazon'
logo_url: ''
category: 'document-ai'
category_name: 'IA pour documents'
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

Textract transforme des images de documents en données structurées. Un développeur envoie un fichier scanné ou un PDF, et le service renvoie le texte trouvé avec sa mise en page : il identifie les tableaux et conserve lignes et colonnes, détecte les paires clé-valeur dans les formulaires, comme un champ nom et sa valeur, et reconnaît l'écriture manuscrite. C'est bien plus utile qu'une reconnaissance de texte brut, qui renverrait un bloc de caractères sans ordre.

Des fonctions spécialisées visent des documents courants. Analyze ID lit passeports et permis de conduire, Analyze Expense extrait les lignes et les totaux de factures et de reçus, et des fonctions propres au crédit traitent des documents hypothécaires. La fonction Queries permet de poser une question comme quel est le total de la facture, et d'obtenir la réponse depuis le document. Les résultats s'intègrent à d'autres services AWS, comme Comprehend, Bedrock et Step Functions, pour une analyse plus loin.

Textract est facturé à la page, avec des tarifs différents selon les fonctions, et une offre gratuite les premiers mois. La justesse est bonne sur des documents propres, mais peut baisser avec de mauvais scans, des mises en page inhabituelles ou de l'écriture. Les documents sensibles demandent une attention à la configuration de sécurité. Les alternatives incluent Google Document AI, Azure Document Intelligence, ABBYY, et des outils open source comme Tesseract, gratuit mais moins capable sur la structure. Textract convient aux équipes sur AWS qui traitent formulaires et factures.
