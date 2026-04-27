# Chapter 5: Results & Discussion

## 5.1 Performance Metrics: Mean Absolute Percentage Error (MAPE)
To evaluate the precision of the automated pediatric census, we calibrate the system against physical manual counts. The error is quantified using the Mean Absolute Percentage Error (MAPE):
$$ MAPE = \frac{1}{n} \sum_{i=1}^{n} \left| \frac{Actual_i - Predicted_i}{Actual_i} \right| \times 100 $$

## 5.2 Discussion: Low-Resolution Robustness
A critical finding of this research is the system's ability to maintain a high accuracy (projected >90%) in $640 \times 480$ resolution environments. By utilizing the Ada-Haar Booster to validate heads, we can "up-sample" our confidence even when the deep learning model (YOLO) struggles with low-light clinical scenes.

## 5.3 Operational Outcomes
- **Occupancy Triggers:** If pediatric density $> 30\%$, the system generates an automated operational alert.
- **Privacy Assurance:** By processing exclusively in volatile memory (RAM), the framework satisfies the highest standards of clinical confidentiality.
