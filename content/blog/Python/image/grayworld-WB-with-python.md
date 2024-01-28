---
title: "Grayworld WB with Python"
date: 2024-01-29T00:01:53+09:00
categories: ["Python"]
tags: ["Python", "image"]
---
# Grayworld White Balance with Python

## 概要

グレーワールド仮説に基づいたホワイトバランスのPythonコードを記載する

## サンプルコード

```python
import numpy as np
import rawpy

def white_balance_rggb(img):
    # R, Gr, Gb, B チャンネルを抽出
    R = img[:, :, 0]
    Gr = img[:, :, 1]
    Gb = img[:, :, 2]
    B = img[:, :, 3]

    # Gr と Gb を統合して G チャンネルを作成
    G = (Gr + Gb) / 2

    # 各チャンネルの平均値を計算
    avg_r = np.mean(R)
    avg_g = np.mean(G)
    avg_b = np.mean(B)

    # 全チャンネルの平均値
    avg = (avg_r + avg_g + avg_b) / 3

    # 各チャンネルを平均値でスケーリング
    R = np.minimum(R * (avg / avg_r), 255)
    G = np.minimum(G * (avg / avg_g), 255)
    B = np.minimum(B * (avg / avg_b), 255)

    # 結果としての RGB 画像を返す
    return np.stack((R, G, B), axis=2)

```