# Image Normalizetion 

ネットワークが深くなると、非線形変換の繰り返しによりデータ分布が変わることがある（**内部の共変量シフト**）

それらを抑抑するための正規化をまとめる。

主に以下4種類が存在する

## Batch Normalization

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

## Layer Normalization

レイヤーごとに正規化を行う処理  

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

各チャネルで独立で画像の縦横方向のみで平均・分散をとる  
画像分野ではバッチ正規化の代わりで注目されている

## Group Normalization

チャネルをG個でグルーピングしてLayer Normalizatoin/Instance Normalizationの中間的な正規化を行う  
セグメンテーションなどで利用

