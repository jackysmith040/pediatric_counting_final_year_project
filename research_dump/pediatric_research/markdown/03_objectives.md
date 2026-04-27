# 3. Research Objectives

## Primary Objective
To develop an occlusion-resistant computer vision framework for accurate pediatric patient counting in high-density medical waiting rooms, specifically addressing the "Invisible Child" scenario (infants carried on backs).

## Specific Objectives
1.  **Develop an Allometric Scaling Model:** Establish a robust Head-to-Body ratio ($R$) classifier to distinguish between adults and infants in overlapping pixel matrices.
2.  **Implement Euclidean Centroid Tracking:** Utilize DeepSORT algorithms to maintain patient identity (ID persistence) during temporary occlusions or crossovers.
3.  **Optimize with Instance Segmentation:** Integrate YOLOv8-seg to achieve pixel-level mask precision for more accurate $R$ ratio calculations compared to standard bounding boxes.
4.  **Validate in Local Context:** Fine-tune the model using synthetic and locally-captured data reflecting Ghanaian clinical settings.
