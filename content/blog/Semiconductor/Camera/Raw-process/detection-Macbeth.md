---
title: "Detection Macbeth"
date: 2023-12-17T20:03:09+09:00
draft: true
---

# Detection Macbeth

## 概要

マクベスの検出検討を行う

## 仮ソース

``` python
import cv2
import numpy as np

def detect_macbeth_chart(image):
    # グレースケール画像に変換
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # エッジ検出
    edges = cv2.Canny(grayscale, 50, 150)
    
    # 輪郭検出
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # マクベスチャートの検出
    macbeth_contours = []
    for contour in contours:
        # 近似輪郭を取得
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        # 四角形（マクベスチャートは通常24のスウォッチを持つ矩形）
        if len(approx) == 4:
            # 比率チェック (例: 4:6)
            _, _, w, h = cv2.boundingRect(approx)
            aspect_ratio = float(w) / h
            if 1.3 < aspect_ratio < 1.7:  # マクベスチャートのおおよそのアスペクト比
                macbeth_contours.append(approx)
    
    # 検出されたマクベスチャートの輪郭を画像に描画
    if macbeth_contours:
        for contour in macbeth_contours:
            cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
    
    return image, macbeth_contours

# 画像を読み込み
image = cv2.imread('/mnt/data/IMG_1967.png')

# マクベスチャートを検出
processed_image, macbeth_contours = detect_macbeth_chart(image)

# 結果を表示
if macbeth_contours:  # マクベスチャートが見つかった場合のみ
    cv2.imshow('Detected Macbeth Chart', processed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

```