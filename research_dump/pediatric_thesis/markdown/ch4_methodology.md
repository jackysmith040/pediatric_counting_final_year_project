# Chapter 4: Methodology

## 4.1 System Architecture
The proposed system follows a modular "Pipeline" architecture:
1.  **Ingestion:** Real-time stream from a $640 \times 480$ (Low-Res) clinical camera.
2.  **Detection & Segmentation:** YOLOv8-seg identifies "Person" masks with pixel-level precision.
3.  **Refinement (The Booster):** AdaBoost-Haar Cascade classifier validates pediatric head signatures (Viola & Jones, 2001).
4.  **Math Layer:** Calculation of the scale-invariant $R$ ratio for each confirmed head.
5.  **Tracking:** DeepSORT assigns and maintains IDs ($ID_1, ID_2, \dots$) using appearance features and allometric signatures.

## 4.2 Handling the "Invisible Child" (Spatial Inference)
To solve the occlusion problem, the proposed algorithm independently isolates all human Heads ($H$) and Bodies ($B$). When a single body geometry bounds two distinct heads ($h_1, h_2 \in H$), the system evaluates two spatial parameters:
1. **Vertical Displacement:** $y_{h2} < y_{h1}$ (The secondary head is physically lower).
2. **Area Proportion:** $A_{h2} < A_{h1}$ (The secondary head's geometric area is strictly smaller).

If both conditions hold true, the algorithm overrides standard suppression limits, correctly infers a carried child, and updates the pediatric matrix by $+1$.

## 4.3 Geometric Tracking
In every video frame $t$, the system extracts the bounding box centroid $C_t = (x_t, y_t)$. The algorithm links the child across frames by minimizing the Euclidean distance $d$:
$$ d = \sqrt{(x_{t+1} - x_t)^2 + (y_{t+1} - y_t)^2} $$
Through memory reassignment, if a child leaves the frame, the system temporarily caches their exact boundary coordinates to restore their ID (Ralhan et al., 2023).
