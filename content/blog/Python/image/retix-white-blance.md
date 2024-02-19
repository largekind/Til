---
title: "Retix White Blance"
date: 2024-02-17T21:08:15+09:00
draft: True
categories: ["Python"]
tags: ["Python", "image"]
---
# Retinex理論に基づくホワイトバランス調整の実装

## 概要

Retinex理論は理論に基づき、デジタル画像におけるホワイトバランス（WB）調整のための手法を実装する。

### サンプルコード

```python
import cv2
import numpy as np

def single_scale_retinex(img, sigma):
    tmp_img = np.float64(img) + 1.0
    retinex = np.log10(tmp_img) - np.log10(cv2.GaussianBlur(tmp_img, (0, 0), sigma))
    return cv2.normalize(retinex, None, 0, 255, cv2.NORM_MINMAX)

def retinex_with_adjustment(img, sigma=300):
    img_retinex = single_scale_retinex(img, sigma)
    img_retinex = np.uint8(np.clip(img_retinex, 0, 255))
    # ホワイトバランス調整をさらに適用
    result = cv2.cvtColor(img_retinex, cv2.COLOR_BGR2LAB)
    max_l, max_a, max_b = np.max(result, axis=(0, 1))
    L, A, B = cv2.split(result)
    L = L * (255 / max_l)
    result = cv2.merge([L, A, B])
    result = cv2.cvtColor(result, cv2.COLOR_LAB2BGR)
    return result

# 画像読み込み
img = cv2.imread('path_to_your_image.jpg')
# ホワイトバランス調整を適用
wb_adjusted_img = retinex_with_adjustment(img)

# 結果表示
cv2.imshow('Original', img)
cv2.imshow('WB Adjusted', wb_adjusted_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## 説明

このコードは、画像に対して単一スケールRetinexアルゴリズムを適用し、その後、色空間をLABに変換してからLチャネル（明度）を調整し、ホワイトバランスを改善する。`sigma`パラメータは、GaussianBlurにおけるぼかしの程度を制御し、Retinexの効果を調整する。