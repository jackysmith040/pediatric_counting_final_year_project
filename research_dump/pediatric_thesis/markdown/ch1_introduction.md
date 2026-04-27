# Chapter 1: Introduction

## 1.1 Overview
In the evolving landscape of digital healthcare, the precision of patient data is the bedrock of operational efficiency. This is particularly true in the Department of Pediatrics, where patient populations are transient, diverse in scale, and often physically occluded in high-density waiting environments. This research explores the synthesis of biological scaling laws and computer vision to automate the pediatric census.

## 1.2 Problem Statement: The Blindness of Standard Geometry
Current state-of-the-art object detection models (e.g., YOLOv11, SSD) are primarily optimized for adult anthropometric signatures in commercial or surveillance contexts. In a Ghanaian clinical setting (e.g., KNUST OPD), these models face three critical failures:
1.  **Scale Invariance Failure:** The vast difference in height and volume between a newborn and an adolescent leads to significant undercounting of infants.
2.  **The "Invisible Child" (Occlusion):** The cultural practice of infants being carried on mothers' backs causes two independent biological entities to be merged into a single "Adult" bounding box.
3.  **Resource Inefficiency:** Reliance on manual "clickers" or logbooks introduces human error and wastes critical staff bandwidth.

## 1.3 Research Objectives
The primary aim is to develop an **Occlusion-Resistant Pediatric Counting Framework**. Specific objectives include:
-   Integrating **Allometric Scaling** (Head-to-Body ratios) as a secondary classification layer.
-   Implementing **DeepSORT** for multi-target tracking and ID persistence.
-   Utilizing **YOLOv8-seg** for pixel-level precision.
-   Refining head detection with an **AdaBoost-Haar Booster**.

## 1.4 Significance of the Study
For the administrator, this research provides a **Force Multiplier** for resource allocation. For the clinician, it provides an automated triage priority alert. For the researcher, it bridges the gap between abstract geometry and biological reality.
