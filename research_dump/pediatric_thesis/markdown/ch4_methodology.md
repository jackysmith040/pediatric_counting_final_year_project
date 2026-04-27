# Chapter 4: Methodology

## 4.1 System Architecture
The proposed system follows a modular "Pipeline" architecture:
1.  **Ingestion:** Real-time stream from a $640 \times 480$ (Low-Res) clinical camera.
2.  **Detection & Segmentation:** YOLOv8-seg identifies "Person" masks.
3.  **Refinement (The Booster):** AdaBoost-Haar scans person masks to confirm the presence of one or more "Pediatric Head" signatures.
4.  **Math Layer:** Calculation of the $R$ ratio for each confirmed head.
5.  **Tracking:** DeepSORT assigns and maintains IDs ($ID_1, ID_2, \dots$).

## 4.2 Handling the "Invisible Child" (Algorithm 1)
When two heads are detected within a single body mask:
- **Step A:** Extract vertical centroids $C_{head1}$ and $C_{head2}$.
- **Step B:** Calculate Euclidean distance $d(C_1, C_2)$.
- **Step C:** If $d < \tau$ and $R_{child} < 6.0$, increment the **Pediatric Census Counter**.

## 4.3 Data Augmentation for Ghana Context
To ensure robustness in local environments, we apply **Domain Randomization**:
- **Brightness Shifting:** Simulating variable lighting in rural clinics.
- **Occlusion Simulation:** Artificially overlaying "cloth" textures to mimic children being wrapped in *ntoma*.
- **Angle Variance:** Simulating non-ideal camera mounting positions.

## 4.4 Hardware Constraints
The system is designed to run on low-power edge devices (e.g., NVIDIA Jetson Nano) to ensure it can be deployed in resource-limited Ghanaian hospitals without the need for expensive server infrastructure.
