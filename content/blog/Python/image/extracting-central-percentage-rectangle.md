---
title: "Extracting Central Percentage Rectangle"
date: 2023-06-30T23:41:13+09:00
---

# 画像から中央のN%の矩形領域を取得する方法

## 概要

画像から中央のN%の矩形領域を取得する方法を紹介する。画像処理で特定の領域を対象にする際に使用される。

## サンプルコード

ここでは80%基準。必要であれば0.8を修正すること

```python
import cv2
import numpy as np

# 画像の読み込み
image = cv2.imread('path_to_your_image')

# 画像の高さと幅
height, width = image.shape[:2]

# 中央を基準に80%の領域を取得
crop_height, crop_width = int(height * 0.8), int(width * 0.8)
center_y, center_x = height // 2, width // 2
start_y = max(0, center_y - crop_height // 2)
start_x = max(0, center_x - crop_width // 2)
end_y = min(height, start_y + crop_height)
end_x = min(width, start_x + crop_width)

image_cropped = image[start_y:end_y, start_x:end_x]
```
