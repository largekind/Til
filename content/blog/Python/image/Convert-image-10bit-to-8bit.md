---
title: "Convert Image 10bit to 8bit"
date: 2023-06-30T23:33:10+09:00
---

# 10ビットデータを8ビットに変換する方法

## 概要

10ビットデータを8ビットに変換する方法を紹介する。

## サンプルコード
```python
import numpy as np

# dth, start_x + crop_width)1ght, start_y + crop_height)0ビットデータの例
data_10bit = np.array([1023, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1, 0])

# データを8ビットにスケーリング
data_8bit = (data_10bit / 1023).astype(np.float16)
```
