---
title: "Adding Text to Image"
date: 2023-06-30T23:47:01+09:00
---

# 画像にテキスト情報を追加する方法

## 概要
画像にテキスト情報を追加する方法を紹介する。画像処理で特定の情報を表示する際に使用される。

## サンプルコード

```python
import cv2

# 画像の読み込み
image = cv2.imread('path_to_your_image')

# テキスト情報
text = 'This is a sample text.'

# テキスト情報を画像に描画
cv2.putText(image, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

# 画像の保存
cv2.imwrite('output.png', image)
```
このコードは、指定した位置にテキスト情報を描画し、その結果を画像として保存する。
