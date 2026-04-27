---
neuron_id: centroid_tracking
title: Centroid Tracking & Re-Identification
synaptic_weight: 10
corpus_callosum: null
blindspot: false
summary: Geometric centroid tracking using Euclidean distance to maintain unique counts.
---

# Tracking & Re-Identification

Maintaining Unique Counts is critical to prevent double-counting if a child wanders off and returns. We utilize geometric centroid tracking.

## Centroid Extraction
We calculate the bounding box centroid $(x_c, y_c)$ for each detection.

## Distance Metric
We apply Euclidean distance to link identities across consecutive frames $t$ and $t+1$:

$d = \sqrt{(x_{t+1} - x_t)^2 + (y_{t+1} - y_t)^2}$

## Re-entry Logic
IDs are cached for a set time window. If a new detection appears at the boundary with matching geometric dimensions, the original ID is reassigned.
