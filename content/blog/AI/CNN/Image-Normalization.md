---
title: "Image Normalizetion "
date: 2023-04-05T00:00:00+09:00
tags: ["Python", "AI", "CNN"]
categories: ["AI"]
---
# Image Normalizetion 

ネットワークが深くなると、非線形変換の繰り返しによりデータ分布が変わることがある（**内部の共変量シフト**）

それらを抑抑するための正規化をまとめる。

主に以下4種類が存在する

## Batch Normalization

バッチ正規化

全てのバッチごとに正規化(平均0、分散1化)する処理  
各ノードの値をミニバッチ単位で正規化して、スケールをそろえる（バッチ正規化）  
**正則化としても機能する** (L2正則化やDrropoutの必要性が小さくなる)

処理的には以下のようにバッチごと(axis=0)で正規化の計算が行われる

``` python
def Batch_Normalization(x,w):
  a = np.matmul(x,w)

  #平均と標準偏差を計算 x[バッチ数,次元]なので、axis=0で指定する
  mean = np.mean(axis=0, keepdims=True)
  std = np.std(axis=0, keepdims=True)
  
  #正規化
  a_normalized = (a - mean) / (std + 1e-8)
```

学習/検証/テストでそれぞれ以下のように使い分ける
- 学習時 : バッチ統計量
- 検証時 : 全体の移動統計量
- テスト時 : 全体の移動統計量

## Layer Normalization

レイヤー正規化

1つのサンプルにおけるレイヤーの隠れ層ごとに正規化を行う処理  
オンライン学習やRNNで使用する

処理的には以下のように隠れ層の1つ1つのデータに対して(axis=1)で正規化の計算が行われる

``` python
def Layer_Normalization(x,w):
  a = np.matmul(x,w)

  #平均と標準偏差を計算 x[バッチ数,次元]なので、各中身を指すaxis=1で指定する
  mean = np.mean(axis=1, keepdims=True)
  std = np.std(axis=1, keepdims=True)
  
  #正規化
  a_normalized = (a - mean) / (std + 1e-8)
```

## Instance Normalization

インスタンス正規化

各チャネルで独立で画像の縦横方向のみで平均・分散をとる  
画像分野ではバッチ正規化の代わりで注目されている

コード的にはチャネル方向で独立のため、高さと幅の次元を指定して平均/分散をとる処理になる

``` python
#x.shape : (バッチサイズM, チャネルC , 幅W, 高さH)
def instance_normalization(x):
  mean = np.mean(x,axis = (2,3)) #幅と高さの次元で平均を取る
  var = np.var(x,axis = (2,3)) #幅と高さの次元で平均を取る

  x_normad = (x-mean)/(np.sqrt(var) + 1e-8)
  return x_normad
```

## Group Normalization

グループ正規化

チャネルをG個でグルーピングしてLayer Normalizatoin/Instance Normalizationの中間的な正規化を行う  
セグメンテーションなどで利用