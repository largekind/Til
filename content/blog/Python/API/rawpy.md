---
title: "Rawpy"
date: 2023-05-11T23:37:57+09:00
categories : ["Python"]
tags : ["API","Camera", "Semiconductor"]
---
# Rawpy
## 概要

RAW画像に対する読み込みや処理を行うためのライブラリ群

もともとlibrawと呼ばれるRAW画像のデコーダーをPythonで利用できるようにラップしたライブラリの模様

rawpyを使用すると、RAW画像ファイルを読み込み、色や露出の補正を行ったり、
画像を他のフォーマット（例：JPEG、PNG、TIFFなど）に変換したりすることができる

## 使用法

基本的な処理のサンプルコードを列挙する

### 画像の読み込み

``` python
import rawpy
raw = rawpy.imread('sample.ARW')
```

### 配列への変換

※np.ndarray型

raw_imageでそのまま上記型が返ってくる

```python
raw_array = raw.raw_image
```

### 黒レベル補正

以下関数で黒レベルの情報が取得できる
``` python
blc = raw.black_level_per_channel
```

### パターン配列取得

``` python
pattern = raw.raw_pattern
```

### ホワイトバランス取得

``` python
wb = np.array(raw.camera_whitebalance)
```

### カラーマトリクス取得

取れない場合はexiftoolを用いて取ってきて、自分で定義すること

``` python
color_matrix = raw.color_matrix
```
