# Image Normalizetion 

ネットワークが深くなると、非線形変換の繰り返しによりデータ分布が変わることがある（**内部の共変量シフト**）

それらを抑抑するための正規化をまとめる。

主に以下4種類が存在する

## Batch Normalization

全てのバッチごとに正規化(平均0、分散1化)する処理  
各ノードの値をミニバッチ単位で正規化して、スケールをそろえる（バッチ正規化）  
**正則化としても機能する** (L2正則化やDrropoutの必要性が小さくなる)

## Layer Normalization

レイヤーごとに正規化を行う処理  
オンライン学習やRNNで使用する

## Instance Normalization

各チャネルで独立で画像の縦横方向のみで平均・分散をとる  
画像分野ではバッチ正規化の代わりで注目されている

## Group Normalization

チャネルをG個でグルーピングしてLayer Normalizatoin/Instance Normalizationの中間的な正規化を行う  
セグメンテーションなどで利用

