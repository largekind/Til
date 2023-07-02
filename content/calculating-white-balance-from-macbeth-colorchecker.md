---
title: "Calculating White Balance From Macbeth Colorchecker"
date: 2023-07-01T21:08:19+09:00
---

# Macbeth ColorCheckerからホワイトバランスを計算する方法

## 概要

Macbeth ColorCheckerの特定のパッチからホワイトバランスを計算し、その結果を画像に描画する方法

## サンプルコード

```python
import cv2
import numpy as np
from colour_checker_detection import colour_checkers_coordinates_segmentation

# 画像を読み込む
image = cv2.imread('path_to_your_image')

# マクベスチャートの各パッチの座標情報を取得
colour_checkers = colour_checkers_coordinates_segmentation(image)

# 19番目のパッチの座標情報を取得
patch_19 = colour_checkers[0].patches[18].mask

# パッチの高さと幅
height, width = patch_19.shape

# 中央を基準に80%の領域を取得
crop_height, crop_width = int(height * 0.8), int(width * 0.8)
center_y, center_x = height // 2, width // 2
start_y = max(0, center_y - crop_height // 2)
start_x = max(0, center_x - crop_width // 2)
end_y = min(height, start_y + crop_height)
end_x = min(width, start_x + crop_width)

patch_19_cropped = patch_19[start_y:end_y, start_x:end_x]

# 80%の領域のRGB値を取得
rgb_values = image[patch_19_cropped]

# RGB値の平均を取得
average_rgb = np.mean(rgb_values, axis=0)

# Gの値が1になるようにR、Bの比率を計算
white_balance = average_rgb / average_rgb[1]

# 結果を表示
print('White Balance:', white_balance)

# 矩形領域を画像に描画
cv2.rectangle(image, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)

# WBの情報を画像に描画
text = 'WB: {:.2f} : 1 : {:.2f}'.format(white_balance[2], white_balance[0])
cv2.putText(image, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

# 画像を保存
cv2.imwrite('output.png', image)
```
