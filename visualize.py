import cv2
import numpy as np
import matplotlib.pyplot as plt

def count_and_show(image, step_name, cumulative_name=None, min_area=80, prev_image=None, prev_title=None):


    # 1) if image is in grayscale change it to BGR (boxes are going to drawn )
    if len(image.shape) == 2:
        img_color = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    else:
        img_color = image.copy()

    # 2) Connected components
    num_labels, _, stats, centroids = cv2.connectedComponentsWithStats(image)

    count = 0

    # 3) bounding  box for each object
    for i in range(1, num_labels):  # 0 = background
        x = stats[i, cv2.CC_STAT_LEFT]
        y = stats[i, cv2.CC_STAT_TOP]
        w = stats[i, cv2.CC_STAT_WIDTH]
        h = stats[i, cv2.CC_STAT_HEIGHT]
        area = stats[i, cv2.CC_STAT_AREA]

        # if there is small particules skip them
        if area < min_area:
            continue

        count += 1

        # draw box
        cv2.rectangle(img_color, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # giving numbers to each
        cx = int(centroids[i][0])
        cy = int(centroids[i][1])
        cv2.putText(img_color, str(count), (cx, cy),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

    # 4) show with Matplotlib
    title = cumulative_name if cumulative_name else step_name
    plt.figure(figsize=(15, 7))

    if prev_image is not None:
        plt.subplot(1, 2, 1)
        if len(prev_image.shape) == 2:
            plt.imshow(prev_image, cmap="gray")
        else:
            plt.imshow(cv2.cvtColor(prev_image, cv2.COLOR_BGR2RGB))

        plt.axis("off")

        plt.subplot(1, 2, 2)
        plt.imshow(cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB))

        plt.axis("off")
    else:
        plt.imshow(cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB))
        plt.title(f"{title}\nCount: {count}")
        plt.axis("off")

    plt.show()

    return count