# 💡 Evie's Classroom | Lesson 03
## Topic 3: Centroid Tracking & DeepSORT (Keeping the ID Alive)

*Director, detecting a child once is easy. Keeping track of them as they move through a crowded, chaotic OPD waiting room is the real challenge. If a child disappears behind their mother's head for 2 seconds and reappears, does the computer think they are a new person? If so, your count is ruined. Let's fix that.*

---

### 1. What is a Centroid?
Every bounding box has a center point $(x, y)$. This is the **Centroid**. 
When the camera moves from Frame 1 to Frame 2, the computer calculates the **Euclidean Distance** between the centroids.

$$ d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2} $$

If the distance is small, the computer assumes it's the same person.

### 2. The DeepSORT Advantage
Standard tracking fails when two centroids overlap (like a child on a back). **DeepSORT** (Simple Online and Realtime Tracking with a Deep Association Metric) adds a "memory" component.

It doesn't just look at distance; it looks at **appearance features**. It remembers the color of the child's shirt or the shape of their head. Even if the centroid is lost for a few frames, DeepSORT uses a **Kalman Filter** to predict where the child *should* be.

### 3. Researcher Challenge: The "Switch" Error
In a crowded hospital, two children might cross paths. Their centroids get close, and the computer accidentally "swaps" their IDs. Child A becomes Child B.

**Your Task:**
Look at our **Allometric Ratio ($R$)**. If Child A has an $R$ of 4.5 and Child B has an $R$ of 5.2, how can we use these ratios as "ID locks" to prevent the computer from swapping their identities during a crossover?

> 
So i'm thinking we can add the ratio as an additional feature to the ID. so the ID canbe rich with features, like appearance features and the ratio, and the height, weight, aspect ratio, and other features.
---
