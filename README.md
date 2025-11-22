# Cell Counting Pipeline – Classical Image Processing

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)

A complete classical image processing pipeline developed for **COMP 4360 – Image Processing**, Assignment 1: Object Counting.  
The goal is to accurately detect and count circular cells in the provided microscopy image `cells.png` using only traditional (non-deep-learning) techniques.

**Final Result → 224 cells counted**

---

## Objectives
- Enhance image contrast
- Remove noise and artifacts
- Segment circular cell-like structures
- Refine binary masks with morphological operations
- Count cells using connected components analysis

---

## Pipeline Steps

| Step | Technique                              | Purpose                                          | Key Parameters          | Cell Count |
|------|----------------------------------------|--------------------------------------------------|--------------------------|------------|
| 1    | Gaussian Blur                          | Reduce high-frequency noise                      | 7×7 kernel               | –          |
| 2    | Contrast Enhancement                   | Improve global & local contrast                  | γ = 1/1.5                | –          |
| 3    | Otsu Thresholding + Inversion (NOT)    | Binarization (cells → white)                     | Automatic threshold      | 237        |
| 4    | Small Morphological Opening            | Remove small noise & tiny particles              | 7×7 rectangular kernel   | 246        |
| 5    | Hole Filling (Flood Fill)              | Fill internal holes in cells                     | –                        | 246        |
| 6    | Large Morphological Opening            | Eliminate large artifacts & merged clusters      | 20×20 kernel             | **224**    |

**Final cell count: 224**

---

## Cell Count Progression

| Step                          | Cell Count | Notes                                           |
|-------------------------------|------------|-------------------------------------------------|
| Gaussian Blur                 | –          | Preprocessing only                              |
| Contrast Enhancement          | –          | Preprocessing only                              |
| Otsu + NOT                    | 237        | Initial noisy segmentation                      |
| Small Opening (7×7)           | 246        | Small noise removed, some touching cells split  |
| Flood Fill                    | 246        | Holes filled, count unchanged                   |
| Large Opening (20×20)         | **224**    | Large artifacts removed → final clean result   |

---

## Key Findings

**Strengths**
- Effective noise reduction using multi-scale morphological opening
- Strong contrast enhancement chain (Histogram Eq → Stretching → Gamma)
- Highly reproducible and fully explainable pipeline

**Challenges**
- Touching/overlapping cells are counted as one
- Sensitive to gamma and morphological kernel sizes
- Large kernel (20×20) risks removing real cells if set too aggressively

---

## Future Improvements
- Watershed or distance-transform-based separation for touching cells
- Adaptive kernel sizes based on local cell density
- Automated parameter tuning with ground-truth data
- Hough Circle Transform as an alternative/complementary method

---

## 📁 Project Structure

```bash
├── main.py              # Runs the full pipeline & prints cell counts
├── image_process.py     # All core image processing functions (blur, contrast, threshold, morph, etc.)
├── visualize.py         # Connected components analysis, bounding boxes & step-by-step visualization
├── cells.png            # Input microscopy image
├── output/              # Automatically created → contains all intermediate and final results
└── README.md            # You're here :)
```
---

## 🙏 Acknowledgments

This project was completed as **Assignment 1** for the **COMP 4360 – Image Processing** course at Yaşar University.

Special thanks to our instructor **Dr. Suphi Uçar** for his excellent guidance, clear explanations, and valuable feedback throughout the course.

If you found this project useful, feel free to give it a ⭐ **star** — it really means a lot!
