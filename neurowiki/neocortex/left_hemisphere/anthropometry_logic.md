---
neuron_id: anthropometry_logic
title: Mathematical Anthropometry (Head-to-Body Ratio)
synaptic_weight: 10
corpus_callosum: null
blindspot: false
summary: Using biological invariants (Allometric Scaling) to classify pediatric patients.
---

# Mathematical Anthropometry

We utilize the biological invariant of Allometric Scaling.
Head-to-Body Ratio ($R$):
$R = \frac{H_{total}}{H_{head}}$

## Classification Logic ($C$):
- **Adults**: $R \approx 7.5 - 8.0$
- **Infants (0-2 yrs)**: $R \approx 4.0$
- **Children (2-6 yrs)**: $R \approx 5.5 - 6.0$

### Significance
This ratio overrides simple height metrics, preventing short adults from being miscounted as children. 

**Note on Codebase Gap**: The current YOLO prototype only relies on supervised class labels (`Kid` vs `Adult`). To achieve actual mathematical anthropometry, we will need to extract pose/keypoints or bounding box proportions and apply this $R$ formula post-inference.
