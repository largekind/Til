---
title: "Crop and Concat Direction"
date: 2023-10-21T23:40:44+09:00
categories: ["Python"]
tags: ["Python", "image"]
---
# Crop and Concat Direction

## 概要

縦横に画像を特定のN%領域でクロップ、連結する場合の方法を記載する

## サンプルコード

``` python
import numpy as np

def crop_image(image, position='center', orientation='vertical', crop_percent=50):
    if crop_percent < 0 or crop_percent > 100:
        raise ValueError("crop_percent must be between 0 and 100")

    if orientation == 'vertical':
        width = image.shape[1]
        crop_width = int(width * crop_percent / 100)
        if position == 'center':
            start_col = (width - crop_width) // 2
        elif position == 'left':
            start_col = 0
        elif position == 'right':
            start_col = width - crop_width
        else:
            raise ValueError("Invalid position")
        return image[:, start_col:start_col + crop_width]

    elif orientation == 'horizontal':
        height = image.shape[0]
        crop_height = int(height * crop_percent / 100)
        if position == 'center':
            start_row = (height - crop_height) // 2
        elif position == 'top':
            start_row = 0
        elif position == 'bottom':
            start_row = height - crop_height
        else:
            raise ValueError("Invalid position")
        return image[start_row:start_row + crop_height, :]

def concatenate_images(images, orientation='vertical'):
    if orientation == 'vertical':
        return np.vstack(images)
    elif orientation == 'horizontal':
        return np.hstack(images)
    else:
        raise ValueError("Invalid orientation")

```

使用する場合は以下のような感じ。numpyを渡して連結すればよい

``` python
# サンプル画像の生成
image1 = np.random.rand(100, 200, 3)
image2 = np.random.rand(150, 250, 3)

# 画像のクロップ
cropped_image1 = crop_image(image1, position='center', orientation='vertical', crop_percent=50)
cropped_image2 = crop_image(image2, position='center', orientation='vertical', crop_percent=50)

# クロップした画像の連結
concatenated_image = concatenate_images([cropped_image1, cropped_image2], orientation='vertical')
```