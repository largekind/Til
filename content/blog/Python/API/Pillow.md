---
title: "Pillow"
date: 2023-04-05T00:00:00+09:00
---
# Pillow

よく使う画像読み込み用のPythonライブラリ
Python Imaging Library を略してPILと呼ぶ

## 使用法

PILでImageオブジェクトを取ってきて画像を読み込み、
各処理を行わせればよい

``` python
from PIL import Image

path = "画像パス"
image = Image.open(path)

image.convert("RGB") #RGB変換

data = np.asarray(image) #np配列化
```

