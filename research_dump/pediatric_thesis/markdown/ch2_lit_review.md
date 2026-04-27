# Chapter 2: Literature Review

## 2.1 The Evolution of Object Detection in Specialized Contexts
The transition from traditional feature engineering, such as **Haar Cascades** (Viola & Jones, 2001), to deep learning architectures like **YOLO** (You Only Look Once) has revolutionized real-time detection (Jiang et al., 2022). However, general-purpose models often fail in specialized medical environments where subject morphology deviates from standard datasets like COCO (Lin et al., 2014; Diop et al., 2025).

## 2.2 Pediatric Anthropometry & Allometric Scaling
Children exhibit distinct morphological characteristics compared to adults, notably a **head-to-body ratio** of approximately 1/4 in infancy versus 1/7.5 in adulthood (Diop et al., 2025; Mlinarić et al., 2024). This biological law, or allometric scaling, serves as a deterministic anchor for age-group classification (Lin et al., 2022). Historical models by Kwon et al. (1999) utilized these anthropometric invariants for early facial age estimation.

## 2.3 Handling Partial Occlusion in Crowded Scenes
Occlusion remains a fundamental bottleneck in computer vision (Ouyang & Wang, 2015). In Ghanaian OPDs, the "Invisible Child" phenomenon—infants carried on mothers' backs—creates overlapping geometries that standard Non-Maximum Suppression (NMS) algorithms actively erase as visual noise (Addotey-Delove et al., 2023).

## 2.4 Specialized Pediatric Datasets
The development of specialized datasets is a prerequisite for robust detection. The **Child Detection Dataset (CDD)** (Diop et al., 2025) provides 1,928 real-world images that capture the complexity of medical environments.

![Figure 1: Sample results from the Child Detection Dataset (CDD) illustrating diverse pediatric postures and interactions.](/home/peace/Desktop/Uni_Research_Pediatric_Counting/research_dump/research_papers/extracted_images/fig-008.jpg)

## 2.5 Morphological Deviations & Detection Failure
Standard detectors like YOLOv11x often fail to distinguish children as a distinct class, instead absorbing them into the general "person" category. General models struggle with scale and posture compared to domain-specific fine-tuning.

![Figure 2: Comparative detection analysis showing general YOLOv11 limitations (left) versus specialized pediatric fine-tuning (right) in a clinical consultation scene.](/home/peace/Desktop/Uni_Research_Pediatric_Counting/research_dump/research_papers/extracted_images/fig-010.jpg)

## 2.6 The Ghana Context: Triage and Tallying
Research in Kumasi facilities underscores the operational strain of high patient density and manual record-keeping (Osei et al., 2024). The integration of automated census tools within the **Lightwave Health Information Management System (LHIMS)** is a critical step toward data-driven hospital management (Addotey-Delove et al., 2023).
