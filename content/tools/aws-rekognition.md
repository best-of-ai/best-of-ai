---
title: 'AWS Rekognition'
name: 'AWS Rekognition'
subtitle: 'Amazon''s cloud-based computer vision service for image and video analysis including object detect...'
slug: 'aws-rekognition'
description: 'Amazon Rekognition is AWS''s computer vision service. Its APIs detect objects, text, faces, and unsafe content in images and video, and developers can train custom models to find their own labels.'
website: 'https://aws.amazon.com/rekognition/'
company: 'amazon'
logo_url: ''
category: 'computer-vision'
category_name: 'Computer Vision'
price: 'Paid'
featured: false
rank: 9
alternatives:
  - google-cloud-vision
  - azure-ai-vision
  - clarifai
  - roboflow
  - landing-ai
date: '2025-10-01'
tags: [api_available, cloud_based, image_based, training, model_based, easy_to_use, ai_powered, intelligent]
---

Rekognition lets developers add image and video analysis to an application without training a model from scratch. You send an image or a video and get back detected objects and scenes, text found in the picture, faces with attributes such as glasses or smiling, and flags for unsafe or inappropriate content. It works on photos, stored video files, and live video streams, and it integrates with S3, Lambda, and other AWS services.

Face-related features are among its most used. It can compare two faces, search a collection of stored faces, and run liveness checks that tell a real person from a photo or a replay during identity verification. Custom Labels trains a classifier on a small set of labeled images to recognize things specific to your business, such as product defects or a brand logo. Content moderation is widely used by platforms that host user uploads.

Charges are per image or per minute of video analyzed, with a free tier at the start. Facial recognition has been a controversial area, and AWS has restricted some uses, most notably by law enforcement, so anyone building on it should review the policy and the privacy rules in their region. Accuracy depends on image quality and on the type of face and lighting. Google Cloud Vision and Azure AI Vision are the closest alternatives.
