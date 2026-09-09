---
title: 'text-to-cad'
name: 'text-to-cad'
slug: 'earthtojake-text-to-cad'
subtitle: 'A library of Agent Skills for generating, inspecting, and fabricating CAD/robot files.'
description: 'text-to-cad produces and handles CAD and robot-description artifacts from local project files. Individual skills cover model generation and export, off-the-shelf part sourcing, 2D drawing, robot description formats, slicing, and manufacturing checks, shipping as provider-native plugins.'
author: 'earthtojake'
skill_type: 'Development & Engineering'
source_url: 'https://github.com/earthtojake/text-to-cad'
compatible_with: ['Claude Code', 'Codex']
install: 'Install via the Skills CLI (npx skills add earthtojake/text-to-cad) or a provider-native plugin command.'
price: 'Free'
open_source: true
license: 'MIT'
stars: 14538
stars_this_week: 75
stars_updated: '2026-09-07'
rank: 7
date: '2026-09-07'
tags: [cad, robotics, engineering]
---
This repository bundles the following skills:

- **CAD**: Creates and edits CAD models with STEP output plus STL, 3MF, and GLB export.
- **CAD Viewer**: Provides local browser previews of CAD and robot files.
- **step.parts**: Sources off-the-shelf STEP components such as screws, bearings, and motors.
- **DXF**: Generates 2D drawings from Python or CAD geometry.
- **URDF/SRDF**: Writes robot structure and MoveIt planning files.
- **G-code**: Slices meshes into G-code using real slicer command-line tools.
