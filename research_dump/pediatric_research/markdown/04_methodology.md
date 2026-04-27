# 4. Methodology

## Proposed Pipeline
The proposed system follows a 4-stage pipeline: **Detection -> Segmentation -> Tracking -> Classification.**

### 1. Object Detection & Segmentation
- **Model:** YOLOv8-seg (You Only Look Once with Instance Segmentation).
- **Refinement (The Booster):** AdaBoost-Haar Cascade classifier.
- **Function:** YOLOv8-seg detects "Human" entities, while the **Ada-Haar Booster** specifically validates the pediatric head signatures within overlapping masks to ensure 99% detection confidence.

### 2. Centroid Tracking (Euclidean Distance)
- **Algorithm:** DeepSORT (Simple Online and Realtime Tracking).
- **Mechanism:** Calculates the Euclidean distance between centroids across frames and applies a Kalman Filter to maintain identity (ID) during temporary occlusions.

### 3. Allometric Classification (The R Ratio)
For every detected entity, the system calculates the ratio:
$$ R = \frac{H_{total}}{H_{head}} $$
Where $H_{total}$ is the combined height of the adult-child cluster and $H_{head}$ is the height of the individual head mask.
- **Thresholds:** $R \in [4.0, 6.0]$ triggers an "Infant" count, while $R \in [7.0, 8.0]$ indicates an "Adult".

### 4. Training & Data
- **Dataset:** COCO + Custom Synthetic Data (African clinical scenes).
- **Implementation:** Python (PyTorch/OpenCV).
