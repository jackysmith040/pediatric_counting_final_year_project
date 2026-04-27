# Chapter 3: Mathematical Preliminaries

## 3.1 Object Detection & Instance Segmentation
We utilize YOLOv8-seg, where the detection process is modeled as an optimization problem. Given an image $I$, the model predicts a set of masks $M = \{m_1, m_2, \dots, m_k\}$ and class probabilities $P$. To ensure feasibility on edge hardware, we consider lightweight architectures such as **ShuffleNetV2** (Liu et al., 2020), which utilize channel splitting to reduce computational FLOPs without sacrificing feature depth.

## 3.2 Allometric Scaling: The Biological Constant
The Allometric Ratio $R$ is defined as:
$$ R = \frac{H_{total}}{H_{head}} $$
Where:
- $H_{total} = y_{max} - y_{min}$ of the entire person segment.
- $H_{head} = y_{max\_head} - y_{min\_head}$ of the head segment.

As a 4th-year Mathematician, we define a decision boundary $\Gamma$ such that:
$$ \text{Entity} = \begin{cases} \text{Child} & \text{if } R < 6.0 \\ \text{Adult} & \text{if } R \ge 7.0 \end{cases} $$

## 3.3 Temporal Tracking: The Kalman Filter
To handle "jitter" and temporary occlusion, we employ a linear Kalman Filter to predict the state $x$ of a centroid at time $t$:
$$ x_{t|t-1} = F_t x_{t-1|t-1} + B_t u_t $$
This ensures that the "Invisible Child" maintains their identity even if their pixels are momentarily merged with the mother's pixels.

## 3.4 Boosting via AdaBoost
The AdaBoost classifier "boosts" head detection confidence in low-resolution environments by combining weak learners $h_j(x)$ into a strong classifier $H(x)$:
$$ H(x) = \text{sign}\left( \sum_{t=1}^T \alpha_t h_t(x) \right) $$
This allows the system to remain robust even when the deep learning model has low confidence.
