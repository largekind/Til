---
title: "ColorChecker Detection"
date: 2023-05-24T21:34:24+09:00
categories : ["Python"]
tags : ["utility","Camera", "Raw-process"]
draft: true
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

