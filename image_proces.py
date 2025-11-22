import cv2
import numpy as np


# 0) Contrast Stretching

def contrast_stretch(img, r1, s1, r2, s2):
    img = img.astype('float')
    r1 = r1 + 1e-6
    r2 = r2 + 1e-6

    stretched = np.piecewise(
        img,
        [img < r1, (img >= r1) & (img <= r2), img > r2],
        [
            lambda r: (s1 / r1) * r,
            lambda r: ((s2 - s1) / (r2 - r1)) * (r - r1) + s1,
            lambda r: ((255 - s2) / (255 - r2)) * (r - r2) + s2
        ]
    )

    return np.uint8(np.clip(stretched, 0, 255))



# 1) Gamma Correction

def gamma_correct(img, gamma=1 / 1.5):
    normalized = img / 255.0
    corrected = np.power(normalized, gamma)
    return np.uint8(corrected * 255)



# 2) Load grayscale

def read_image(path="cells.png"):
    gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    #histogram equalization
    gray = cv2.equalizeHist(gray)
    #---Gaussian blur---
    #affected the output to have a little more clear borders which affected the count by 1 cell more
    # --- Contrast Stretching ---
    rmin = np.min(gray)
    rmax = np.max(gray)
    gray = contrast_stretch(gray, rmin, 0, rmax, 255)

    # --- Gamma Correction ---
    gray = gamma_correct(gray, gamma=1 / 1.5)
    #gamma parameter also taken 0.4,2.2 0.7 the chosen parameter has value is one of the best output

    return gray


# 3) Threshold + Logical NOT

def apply_threshold(gray):

    _, bw = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    bw = cv2.bitwise_not(bw)
    return bw



# 4) Opening (7×7)

def remove_noise(binary):
    kernel7 = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel7)
    return opened



# 5) Hole Filling (FloodFill)

def flood_fill_holes(binary):
    flood = binary.copy()
    h, w = binary.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)
    cv2.floodFill(flood, mask, (0, 0), 255)

    flood_inv = cv2.bitwise_not(flood)
    filled = cv2.bitwise_or(binary, flood_inv)
    return filled



# 6) Opening (20×20)

def large_opening(filled):
    kernel25 = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 20))
    opened2 = cv2.morphologyEx(filled, cv2.MORPH_OPEN, kernel25)
    return opened2