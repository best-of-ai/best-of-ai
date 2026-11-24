---
title: 'Kalanos Grader'
name: 'Kalanos Grader'
subtitle: 'Open-source quality audit for robot training recordings'
slug: 'kalanos-grader'
description: 'Kalanos Grader is a free, Apache-2.0 command-line tool that audits robot and physical AI training recordings locally. It scores timing, motion, integrity, vision and annotation issues and writes an HTML or JSON report.'
website: 'https://kalanos.ai/grader'
logo_url: ''
category: 'robotics'
category_name: 'Robotics'
price: 'Free'
featured: false
rank: 5
alternatives:
  - foxglove
  - cleanlab
  - formant
date: '2026-11-24'
tags: [robotics, data_quality, dataset_audit, imitation_learning, physical_ai, open_source, cli, python, lerobot, free_tier]
---

Kalanos Grader checks recorded robot episodes before you train on them. You install it with pip and run `kalanos grade ./my_recordings --report audit.html`. It looks for timing, signal and motion problems, shows which episodes need review and why, and writes the result as an HTML report or as JSON. Nothing needs an account, and local audits run on your own machine.

Each recording gets a score from 0 to 100 across five families: integrity, timing, motion, vision and annotation. Integrity is weighted 3, timing, motion and vision 2 each, and annotation 1 by default. The score measures quality within what was assessed. Kalanos says it is not a pass rate and not a prediction of how a trained model will behave. The page shows a sample audit of 50 ALOHA episodes where 39 passed and 11 needed review.

It needs Python 3.10 or newer. LeRobot v2.0, v2.1 and v3.0 datasets, CSV and JSON or JSONL files work in the base package. HDF5 and MCAP or ROS 2 recordings need extras, camera checks need the video extra, and arbitrary HDF5 layouts may not map. A full report on 1,000 episodes took about 52 minutes in Kalanos's own run, which it says is not a benchmark. It suits teams doing imitation learning who want a quick look at dataset quality.
