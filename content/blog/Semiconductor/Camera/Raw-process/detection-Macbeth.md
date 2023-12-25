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