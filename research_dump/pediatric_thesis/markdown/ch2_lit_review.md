# Chapter 2: Literature Review

## 2.1 The Evolution of Object Detection
From the early days of **Haar Cascades** (Viola & Jones, 2001) to the modern **YOLO** (You Only Look Once) paradigm, object detection has prioritized speed and bounding box accuracy. However, as Ouyang & Wang (2015) noted, partial occlusion remains the "Achilles' heel" of deep learning models.

## 2.2 Pediatric Anthropometry & Allometry
Allometric scaling, the study of the relationship of body size to shape, anatomy, and physiology, provides a reliable mathematical constant (Mlinarić et al., 2024). In pediatrics, the **Head-to-Body ratio** changes predictably with age:
-   **Infancy:** Head accounts for $\approx 1/4$ of total height.
-   **Adulthood:** Head accounts for $\approx 1/7.5$ of total height.
This biological law offers a deterministic way to classify entities that a purely pixel-based model might miss.

## 2.3 Computer Vision in Emerging Economies
Research by Addotey-Delove et al. (2023) highlights the barriers to adopting health information systems in emerging economies like Ghana. One major barrier is the lack of robust, automated data entry. Automated counting systems adapted to local norms (e.g., infants on backs) are a critical step toward solving the "data gap" in Ghanaian hospitals.

## 2.4 Gap in Current Literature
While literature exists for crowd counting and pedestrian detection, there is a notable absence of frameworks that combine **biological allometry** with **instance segmentation** to solve the specific problem of pediatric patient identification in high-density clinical scenes.
