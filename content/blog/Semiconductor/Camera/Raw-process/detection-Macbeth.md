---
title: "Detection Macbeth"
date: 2023-12-17T20:03:09+09:00
draft: True
categories: ["Semiconductor"]
tags: ["Semiconductor", "Camera", "Raw-process"]
---
# Detection Macbeth

## 概要

マクベスの検出検討を行う

## 仮ソース

``` python
import cv2
import numpy as np

def detect_macbeth_chart(grayscale_image):
    # 平滑化を行い、誤判定を減らす
    blurred = cv2.GaussianBlur(grayscale_image, (5, 5), 0)
    
    # エッジ検出
    edges = cv2.Canny(blurred, 50, 150)
    
    # 輪郭検出
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # マクベスチャートの輪郭を見つける
    macbeth_contours = []
    for contour in contours:
        # 近似した輪郭を取得
        approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
        # 四角形かつ直線的な輪郭を探す
        if len(approx) == 4 and cv2.isContourConvex(approx):
            _, _, w, h = cv2.boundingRect(approx)
            aspect_ratio = float(w) / h
            if 1.3 < aspect_ratio < 1.7:  # マクベスチャートのおおよそのアスペクト比
                macbeth_contours.append(approx)
    
    return macbeth_contours

# グレースケール画像の読み込み
grayscale_image = load_grayscale_image('path_to_raw_image.raw')

# 2次元データを扱うために適切な形状に変換
grayscale_image = grayscale_image.reshape((*grayscale_image.shape, 1))

# マクベスチャートの検出
macbeth_contours = detect_macbeth_chart(grayscale_image[..., 0])

# 検出結果の表示
for contour in macbeth_contours:
    # 検出された輪郭を元の画像に描画
    cv2.polylines(grayscale_image, [contour], True, (255), 2)

def auto_canny(image, sigma=0.33):
    # 画像の中央値を計算
    v = np.median(image)
    
    # 閾値を自動的に決定
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    
    # Cannyエッジ検出を適用
    edged = cv2.Canny(image, lower, upper)
    
    return edged

```

watershedを用いた版

``` python
import cv2
import numpy as np

def apply_watershed(grayscale_image):
    # ノイズ除去のための平滑化
    blurred = cv2.GaussianBlur(grayscale_image, (5, 5), 0)

    # Sure background areaの特定
    dilated = cv2.dilate(blurred, np.ones((7, 7), np.uint8), iterations=2)

    # Sure foreground area（前景）の特定
    dist_transform = cv2.distanceTransform(blurred, cv2.DIST_L2, 5)
    _, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

    # Unknown region（不明な領域）の特定
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(dilated, sure_fg)

    # ラベリング
    _, markers = cv2.connectedComponents(sure_fg)

    # ウォーターシェッドのマーカーとして1を足す（背景は0のため）
    markers = markers + 1

    # Unknown regionに対して0のマーカーを設定
    markers[unknown == 255] = 0

    # ウォーターシェッド変換を適用
    markers = cv2.watershed(cv2.cvtColor(grayscale_image, cv2.COLOR_GRAY2BGR), markers)

    return markers

def detect_macbeth_chart(grayscale_image):
    markers = apply_watershed(grayscale_image)
    
    # マクベスチャートの領域を見つけるための輪郭検出
    macbeth_contours = []
    for label in np.unique(markers):
        if label == 0 or label == -1:
            continue

        mask = np.zeros(grayscale_image.shape, dtype="uint8")
        mask[markers == label] = 255

        cnts, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if cnts:
            largest_contour = max(cnts, key=cv2.contourArea)
            macbeth_contours.append(largest_contour)

    return macbeth_contours

# 画像を読み込む
# 実際には画像ファイルから読み込んだグレースケール画像データを使用します。
grayscale_image = np.random.rand(800, 600) * 255
grayscale_image = grayscale_image.astype(np.uint8)

# マクベスチャートの検出
macbeth_contours = detect_macbeth_chart(grayscale_image)

# 結果の表示
for contour in macbeth_contours:
    cv2.drawContours(grayscale_image, [contour], -1, (255), 2)

cv2.imshow('Detected Macbeth Chart', grayscale_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

```
template matchingを使う版テスト

``` python
import cv2
import numpy as np

def find_macbeth_patches(image, template):
    # テンプレートマッチングでマクベスチャートの位置を特定
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv2.minMaxLoc(result)

    # テンプレートのサイズ
    t_height, t_width = template.shape[:2]

    # パッチのサイズを計算（マクベスチャートは通常6x4のグリッド）
    patch_width = t_width / 6
    patch_height = t_height / 4

    # 各パッチの座標を計算
    patches = []
    for i in range(6):
        for j in range(4):
            top_left = (max_loc[0] + i * patch_width, max_loc[1] + j * patch_height)
            bottom_right = (top_left[0] + patch_width, top_left[1] + patch_height)
            patches.append((top_left, bottom_right))

    return patches

# テンプレートと画像の読み込み
# ここではダミーデータを生成しています
image = np.random.rand(800, 600) * 255
image = image.astype(np.uint8)
template = np.random.rand(100, 150) * 255
template = template.astype(np.uint8)

# マクベスチャートの各パッチの座標を見つける
macbeth_patches = find_macbeth_patches(image, template)

# 各パッチを描画
for top_left, bottom_right in macbeth_patches:
    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

# 結果の表示
cv2.imshow('Macbeth Chart Patches', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

```