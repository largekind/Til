---
title: "Calculating White Balance From Rgb"
date: 2023-06-30T23:43:19+09:00
---

# RGB値からホワイトバランスを計算する方法

## 概要
RGB値からホワイトバランスを計算する方法を紹介する。画像処理で色補正を行う際に使用される。

## サンプルコード
```python
import numpy as np

# RGB値の例
rgb_values = np.array([[255, 200, 150], [100, 200, 300], [50, 200, 350]])

# RGB値の平均を取得
average_rgb = np.mean(rgb_values, axis=0)

# Gの値が1になるようにR、Bの比率を計算
white_balance = average_rgb / average_rgb[1]
```

