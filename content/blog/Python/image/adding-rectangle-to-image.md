---
title: "Adding Rectangle to Image"
date: 2023-06-30T23:45:18+09:00
categories: ["Python"]
tags: ["Python", "image"]
---
# 画像に矩形領域を追加する方法

## 概要
画像に矩形領域を追加する方法を紹介する。画像処理で特定の領域を強調表示する際に使用される。

## サンプルコード
```python
import cv2

# 画像の読み込み
image = cv2.imread('path_to_your_image')

# 矩形領域を画像に描画 以下座標は適時変えること
cv2.rectangle(image, (start_x, start_y), (end_x, end_y))
```