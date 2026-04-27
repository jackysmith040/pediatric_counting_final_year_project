# 1. Background: The Search for a Reliable Census

## The Mission: Beyond the Clicker
We began this research with a fundamental administrative question: In a high-stakes environment like the KNUST Pediatric OPD, can we replace the manual "clicker" with a precise, automated census? 

## The False Start
Our journey started with standard Computer Vision models (YOLO). We assumed that if an AI can detect a car or a tree, it could count a child. 

## The Discovery of "Invisible" Data
As we stress-tested these models in local clinical settings, we discovered a systemic failure. The AI wasn't just inaccurate; it was **blind**. 
1. **Scale Blindness:** It often ignored infants as "noise."
2. **Geometric Occlusion:** Most critically, the "Invisible Child" phenomenon—where infants carried on backs were mathematically absorbed by the adult's bounding box—revealed that current AI is structurally biased against African clinical norms.

This is where our research truly began: not as a coding exercise, but as a mathematical quest to make the invisible, visible.
