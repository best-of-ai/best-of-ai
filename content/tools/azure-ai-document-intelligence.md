---
title: 'Azure AI Document Intelligence'
name: 'Azure AI Document Intelligence'
subtitle: 'Microsoft''s service for pulling structured data out of documents'
slug: 'azure-ai-document-intelligence'
description: 'Azure AI Document Intelligence, formerly Form Recognizer, extracts text, key-value pairs, tables, and structure from documents. It includes prebuilt models for invoices, receipts, IDs, and tax forms, and custom models for your own layouts.'
website: 'https://azure.microsoft.com/products/ai-services/ai-document-intelligence'
company: 'microsoft'
logo_url: ''
category: 'document-ai'
category_name: 'Document AI'
price: 'Paid'
featured: false
rank: 7
alternatives:
  - amazon-textract
  - google-document-ai
  - abbyy
  - nanonets
  - instabase
  - reducto
date: '2026-11-05'
tags: [document_ai, pdf, productivity, extraction, documents, ocr, summarization, document_processing, parsing, customizable, templates, voice_enabled]
---

Azure AI Document Intelligence reads documents so applications can use the data. Its layout model finds text, tables, headings, and selection marks, and prebuilt models recognize common document types such as invoices, receipts, business cards, identity documents, and many tax and mortgage forms, returning fields like totals, dates, and names with confidence scores. You can train custom models with a small number of examples to extract the fields in your own forms.

It plays a role in AI pipelines as well. Output can be formatted as Markdown to prepare documents for retrieval-augmented generation, preserving structure that helps language models answer questions, and it integrates with Azure AI Search, Logic Apps, and Power Automate. Accuracy is generally high on clean documents, and a studio tool allows testing without code.

Pricing is per page, depending on the model, with a free tier for experimentation. Handwriting, poor scans, and unusual layouts can reduce accuracy, and sensitive documents need careful security handling. Competitors include Amazon Textract, Google Document AI, ABBYY, and open-source tools such as Tesseract and newer vision-language models. Document Intelligence suits teams on Azure that need dependable form and invoice extraction.
