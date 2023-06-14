---
title: "Demosaic"
date: 2023-05-23T21:22:37+09:00
categories : ["Semiconductor"]
tags : ["Semiconductor","Camera", "Raw-process"]
---

# Demosaic

## 概要

デモザイク処理のこと。Bayer配列をどうにかしてRGBの見える画像の表示形式に落とし込む処理

## 種類

デモザイクを行う処理には以下の手法がある
- 線形補完
  - BiLinear A/B
- 色空間を変換して処理
  - AHD (Adaptive Homogeneity-Directed)
- 色差分散での処理
  - DLMMSE
- 機械学習 
  - AIRD
その他もろもろ。

詳細は次の記事が参考になる。
[デモザイクアルゴリズムうんちく](http://optical-learning-blog.realop.co.jp/?eid=44)
