---
title: "Analysis Bin Macbeth"
date: 2024-01-09T22:58:38+09:00
draft: true
---

# Analysis Bin Macbeth

## 概要

通常マクベスの分析検討を行う

## サンプル

``` python
import cv2
import numpy as np
from colour import XYZ_to_Lab, RGB_to_XYZ, sRGB_COLOURSPACE
from colour_checker_detection import detect_colour_checkers_segmentation

def analyze_macbeth_chart(image_path, area_percentage):
    """
    Analyze a Macbeth Chart in an image by detecting each patch and computing statistics.

    :param image_path: Path to the image containing a Macbeth Chart.
    :param area_percentage: Percentage of the area to analyze in the center of each patch.
    :return: A dictionary containing the average RGB, standard deviation, and L*a*b* values for each patch.
    """
    # Load and decode the image
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Detect the colour checker
    detected_checkers = detect_colour_checkers_segmentation(image)

    # Analyze each detected checker
    results = []
    for checker in detected_checkers:
        swatches = checker['swatches']
        stats = []

        for swatch in swatches:
            # Calculate the center area of the swatch based on the specified percentage
            h, w = swatch.shape[:2]
            center_h, center_w = int(h * area_percentage / 100), int(w * area_percentage / 100)
            start_h, start_w = (h - center_h) // 2, (w - center_w) // 2
            center_area = swatch[start_h:start_h + center_h, start_w:start_w + center_w]

            # Compute statistics
            avg_rgb = np.mean(center_area, axis=(0, 1))
            std_rgb = np.std(center_area, axis=(0, 1))
            
            # Convert RGB to L*a*b*
            xyz = RGB_to_XYZ(avg_rgb / 255, sRGB_COLOURSPACE.whitepoint, sRGB_COLOURSPACE.whitepoint, sRGB_COLOURSPACE.RGB_to_XYZ_matrix)
            lab = XYZ_to_Lab(xyz, sRGB_COLOURSPACE.whitepoint)

            stats.append({
                'average_rgb': avg_rgb,
                'std_rgb': std_rgb,
                'lab': lab
            })

        results.append(stats)

    return results

# 例: 画像のパスを指定し、各パッチの中心50%の領域を分析する
# image_path = 'path_to_image_with_macbeth_chart.jpg'
# analyze_macbeth_chart(image_path, 50)


```

まとまった情報をplotする仕組みは以下

``` python
import matplotlib.pyplot as plt

def plot_lab_colour_space(lab_values):
    """
    Plot the L*a*b* values in the colour space and connect them with lines.

    :param lab_values: List of L*a*b* values for each patch.
    """
    a_values = [lab[1] for lab in lab_values]
    b_values = [lab[2] for lab in lab_values]

    plt.figure(figsize=(10, 10))
    plt.scatter(a_values, b_values, c='black')
    
    # Connecting the points with lines
    for i in range(len(lab_values) - 1):
        plt.plot([a_values[i], a_values[i + 1]], [b_values[i], b_values[i + 1]], 'r-')
    
    plt.xlabel('a*')
    plt.ylabel('b*')
    plt.title('L*a*b* Colour Space')
    plt.grid(True)
    plt.show()

# 使用例
# results = analyze_macbeth_chart('path_to_image_with_macbeth_chart.jpg', 50)
# lab_values = [patch['lab'] for patches in results for patch in patches]
# plot_lab_colour_space(lab_values)

```