import cv2
import matplotlib.pyplot as plt
from image_proces import (
    read_image,
    apply_threshold,
    remove_noise,
    flood_fill_holes,
    large_opening
)
from visualize import count_and_show


def show_step(prev_img, curr_img, prev_title, curr_title, step_name, min_area=80):
    # Cell Count (on current image)
    count = count_and_show(curr_img, step_name, min_area=min_area)

    plt.figure(figsize=(15, 7))
    plt.subplot(1, 2, 1)
    if len(prev_img.shape) == 2:
        plt.imshow(prev_img, cmap="gray")
    else:
        plt.imshow(cv2.cvtColor(prev_img, cv2.COLOR_BGR2RGB))
    plt.title(prev_title)
    plt.axis("off")

    plt.subplot(1, 2, 2)
    if len(curr_img.shape) == 2:
        plt.imshow(curr_img, cmap="gray")
    else:
        plt.imshow(cv2.cvtColor(curr_img, cv2.COLOR_BGR2RGB))
    plt.title(f"{curr_title}\nCount: {count}")
    plt.axis("off")

    plt.suptitle(step_name, fontsize=16)
    plt.show()

    return count


def pipeline():
    print("\n--- Cell Count Pipeline Started ---\n")
    print("{:<50} {:>10}".format("Processes implemented", "Cell Count"))
    print("-" * 65)

    # 1) Read image (grayscale + preprocess)
    original = cv2.imread("cells.png", cv2.IMREAD_GRAYSCALE)
    blurred = cv2.GaussianBlur(original, (7, 7), 0)
    count = show_step(original, blurred, "Original", "Gaussian Blur", "Step 1: Blur")
    print("{:<50} {:>10}".format("Gaussian Blur", count))

    # 2) Histogram Equalization + Contrast Stretch + Gamma
    stretched = read_image("cells.png")  # contains stretch + gamma
    count = show_step(
        blurred,
        stretched,
        "Gaussian Blur",
        "Histogram Equalization + Contrast Stretch + Gamma",
        "Step 2: Stretch + Gamma"
    )
    print("{:<50} {:>10}".format("Contrast Stretch + Gamma", count))

    # 3) Threshold
    thresh = apply_threshold(stretched)
    count = show_step(stretched, thresh, "Preprocessed", "Threshold", "Step 3: Threshold")
    print("{:<50} {:>10}".format("Threshold", count))

    # 4) Opening (noise removal)
    opened = remove_noise(thresh)
    count = show_step(thresh, opened, "Threshold", "Opening", "Step 4: Opening")
    print("{:<50} {:>10}".format("Opening", count))

    # 5) Flood Fill (hole filling)
    filled = flood_fill_holes(opened)
    count = show_step(opened, filled, "Opening", "Flood Fill", "Step 5: Flood Fill")
    print("{:<50} {:>10}".format("Flood Fill", count))

    # 6) Large Opening (remove small objects / separate touching cells)
    opened2 = large_opening(filled)
    count = show_step(filled, opened2, "Flood Fill", "Large Opening", "Step 6: Large Opening")
    print("{:<50} {:>10}".format("Large Opening", count))

    print("\n--- Pipeline Finished ---\n")


if __name__ == "__main__":
    pipeline()