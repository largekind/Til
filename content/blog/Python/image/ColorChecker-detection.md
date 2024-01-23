---
title: "ColorChecker Detection"
date: 2023-05-24T21:34:24+09:00
categories: ["Python"]
tags: ["utility", "Camera", "Raw-process", "Python"]
---
# ColorChecker Detection

## 概要

カラーチェッカー(マクベスチャートなど)が出来るAPI

[Github](https://github.com/colour-science/colour-checker-detection)

## インストール方法

単純にpipでインストール可能

> pip install colour-checker-detection

以下依存関係があるので注意。あらかじめ揃えておくのが良い

``` txt
python >= 3.8, < 4
colour-science >= 4
imageio >= 2, < 3
numpy >= 1.19, < 2
opencv-python >= 4, < 5
scipy >= 1.5, < 2
```

## 使用法

詳細は[ドキュメントを参照](https://colour-checker-detection.readthedocs.io/en/latest/reference.html)

[使用例](https://github.com/colour-science/colour-checker-detection/blob/master/colour_checker_detection/examples/examples_detection.ipynb)

## 関数説明

### 座礁取得

以下を実行すると、そのままDataColourCheckersCoordinatesSegmentationと呼ばれるtupleベースのデータが返ってくる模様。
以下使用例
``` python
import os
from colour import read_image
from colour_checker_detection import ROOT_RESOURCES_TESTS
# テスト用のパス作成
path = os.path.join(
    ROOT_RESOURCES_TESTS,
    "colour_checker_detection",
    "detection",
    "IMG_1967.png",
)
image = read_image(path)
colour_checkers_coordinates_segmentation(image)  
''' 以下実行結果
(array([[ 369,  688],
       [ 382,  226],
       [1078,  246],
       [1065,  707]]...)
'''
```

大きい画像サイズだとresizeで怒られる。その場合、working_width/heightを以下のように引数で与えて対応する
> colour_checkers_coordinates_segmentation(image, working_width = 5000)  

### DataColourCheckersCoordinatesSegmentation

※ChatGPT4情報

カラーチェッカーの検出データを保持するためのクラス

このクラスは次の属性を持つ

- colour_checkers: カラーチェッカーのバウンディングボックス（つまり、適切な数のswatchを持つクラスタ）。
- clusters: 検出されたswatchのクラスタ。
- swatches: 検出されたswatch。
- segmented_image: 閾値を超えた/セグメント化された画像。

※swatch : 色見本のこと。マクベスチャート上ならパッチのこと