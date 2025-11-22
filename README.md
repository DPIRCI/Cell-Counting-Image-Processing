**🔬 Cell Counting Pipeline – Image Processing Report**

This repository contains the implementation and analysis of a multi-step image processing pipeline developed for COMP 4360 – Image Processing, Assignment 1: Object Counting.
The goal of the project was to detect and count circular cells in the cells.png microscopy image using classical image processing techniques.

**🎯 Objectives**

The main objective was to design a clear, reproducible workflow to:

Enhance image contrast

Remove noise

Segment circular cell-like structures

Refine masks using morphological operations

Accurately count cells with connected components analysis

The pipeline was tuned to maximize segmentation accuracy while reducing noise and artifacts.

**🛠️ Methodology: Step-by-Step Pipeline**

The cell-counting pipeline consists of the following sequential operations (implemented in image_process.py and executed via main.py):

Step	Technique	Purpose	Key Parameters	Cell Count
1. Preprocessing	Gaussian Blur	Reduces high-frequency noise and smooths edges	Kernel: 7×7	1 (expected)
2. Contrast Enhancement	Histogram Equalization, Contrast Stretching, Gamma Correction	Improves global and local contrast	γ = 1/1.5	1 (expected)
3. Segmentation	Otsu Thresholding + NOT	Converts to binary image; cells become white	—	237
4. Noise Reduction	Morphological Opening	Removes small particles while preserving cell structure	Kernel: 7×7 rectangle	246
5. Hole Filling	Flood Fill	Fills internal gaps in detected cells	—	246
6. Artifact Removal	Large Morphological Opening	Eliminates larger non-cell regions	Kernel: 20×20	224 (final)
**📊 Results**

Connected Components Analysis was used to count cells after each major step.
The final count was 224 cells.

**📈 Cell Count Trends**
Step	Cell Count	Notes
Gaussian Blur	1	Preprocessing only
Contrast Enhancement	1	Preprocessing only
Thresholding (Otsu + NOT)	237	Initial segmentation; noise present
Opening (7×7)	246	Small noise removed; some touching cells separated
Flood Fill	246	Filled internal holes; no change in object count
Large Opening (20×20)	224	Removed large artifacts, reducing false positives
🔑 Key Findings
✔️ Strengths

Noise Reduction: Combination of Gaussian blur, small opening, and large opening effectively removed most noise.

Contrast Enhancement: Histogram equalization + contrast stretch + gamma correction prepared the image well for thresholding.

Stable Pipeline: Once tuned, the steps produced a clean and interpretable mask.

⚠️ Challenges

Parameter Sensitivity:
Especially gamma correction — values between 1.2–1.5 worked best.
Very low values (e.g., 0.4) caused severe under-segmentation.

Overlapping Cells:
Touching or overlapping cells were often counted as a single region.

Large Artifact Removal:
Required careful balancing: the 20×20 kernel removed artifacts but risked removing real cells if larger.

💡 Recommendations for Future Work

To improve performance and robustness:

🔹 Advanced Segmentation

Implement Watershed segmentation or distance transform-based splitting to separate touching cells.

🔹 Adaptive Morphology

Use adaptive kernel sizes depending on local cell density or estimated cell radius.

🔹 Systematic Parameter Tuning

Perform automated tuning for:

Gamma values

Thresholding techniques

Morphological kernel sizes

against a ground-truth dataset.

📁 Project Structure
.
├── main.py                # Controls pipeline execution
├── image_process.py       # All preprocessing and morphological functions
├── visualize.py           # Connected components + visualization utilities
├── cells.png              # Input microscopy image
└── README.md              # Project documentation

File Responsibilities

image_process.py
Contains core operations such as:

contrast_stretch

gamma_correct

apply_threshold

flood_fill_holes

morphological operations

visualize.py

Connected components analysis

Drawing bounding boxes

Displaying step-by-step results

main.py

Calls each step

Logs cell counts

Runs the full workflow end-to-end

🎓 Acknowledgments

This work was completed as Assignment 1 for COMP 4360 – Image Processing at Yaşar University.
