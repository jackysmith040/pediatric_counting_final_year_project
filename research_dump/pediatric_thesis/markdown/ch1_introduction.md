# Chapter 1: Introduction

## 1.1 Overview
In the evolving landscape of digital healthcare, the precision of patient data is the bedrock of operational efficiency. This is particularly true in the Department of Pediatrics, where patient populations are transient, diverse in scale, and often physically occluded in high-density waiting environments. This research explores the synthesis of biological scaling laws, the Ada-Haar feature extraction pipeline, and computer vision to automate the pediatric census.

## 1.2 Problem Statement: The Failure of Standard Geometry
In major Ghanaian hospitals, such as Komfo Anokye Teaching Hospital (KATH), optimizing medical staff allocation through the Local Health Information Management System (LHIMS) requires precise demographic data. Currently, hospitals rely heavily on manual tallying, which is highly susceptible to human error. Introducing standard surveillance algorithms to a Ghanaian OPD creates a severe geometric flaw (Ouyang & Wang, 2015). Because infants are often carried on the mother's back, their spatial coordinates heavily intersect. Standard Non-Maximum Suppression (NMS) actively merges these overlapping shapes, discarding the carried child as visual noise (Addotey-Delove et al., 2023). This "invisible child" phenomenon causes a Mean Absolute Percentage Error (MAPE) of over 40% in current automated attempts.

## 1.3 Research Gap and Motivation
While specialized models like **YOLOCDD** have been developed for monitoring children in controlled medical scenes using the **Child Detection Dataset (CDD)** (Diop et al., 2025), these models are often infant-centric and lack the spatial inference required for high-density occlusion in African clinical norms. Furthermore, there is a need to extend these high-precision tracking techniques—previously used for neonatal intensive care (Keles & Bagci, 2023) and infantile spasm detection (Diop et al., 2024)—to the broader challenge of general pediatric counting in resource-limited settings.

## 1.4 Research Objectives
The primary objective of this study is to develop a privacy-preserving, automated mathematical framework capable of accurately counting pediatric visitors. Specifically, the project aims to:
- **Automated Child Detection:** Formulate a spatial detection model to mathematically separate carried children from adult caregivers (Osei et al., 2024).
- **Mathematical Anthropometry:** Apply physical constraints via Head-to-Body Ratios to prevent misclassification (Mlinarić et al., 2024).
- **Data Tracking:** Implement geometric centroid tracking utilizing Euclidean distance to ensure unique, non-repeating patient counts.
- **Privacy-Preserving Architecture:** Design a localized Edge computing architecture that outputs strictly numerical matrices.

## 1.5 Significance of the Study
For the administrator, this research provides a **Force Multiplier** for resource allocation. For the clinician, it provides an automated triage priority alert. For the researcher, it bridges the gap between abstract geometry and biological reality.
