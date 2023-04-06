---
title: "双方向RNN (Bi-directional RNN)"
date: 2023-04-05T00:00:00+09:00
tags: [Python,AI,RNN]
---
# 双方向RNN (Bi-directional RNN)

過去 -> 未来だけでなく、未来 -> 過去への方向も考慮して学習したRNN

最後に結論が来る文章など、後ろから文を読んだほうが有効な場合などで使用される。

## pythoch上での実装

``` python
import torch
from torch import nn

# 各パラメータ類
input_dim = 24 #入力ベクトル
output_dim = 24 #出力ベクトル
embed_dim = 200 #埋め込みベクトル(RNNに入力する特徴ベクトル)
hidden_dim = 200 #隠れ層のユニット数(ベクトル)
nb_layers = 2 #RNN層の数

# モデルの定義
embed_fc = nn.Linear(input_dim, embed_dim) #1つ目の全結合
bidirectional_rnn = nn.RNN(input_size = embed_dim, hidden_size = hidden_dim, num_layers = nb_layers, bidirectional = True) #双方向RNNとして定義
fc = nn.Linear(hidden_dim * 2, output_dim) #RNNから出力された物をoutput_dimにまとめる全結合層 双方向のため次元はhidden_dim*2となる

# 順伝播処理
def forward(X):
  # X : 入力データ 次元は(seq_len :時系列長, batch_size , input_dim)

  #RNNに入力出来るようにembed_dimの次元へまとめる(埋め込みベクトル化)
  emb = embed_fc(X) 
  #RNNへ入力、その時の出力と次への隠れ層出力を受け取る
  output, hn = bidirectional_rnn(emb)
  # 出力のshape : (input_size ,batch_size, 2*hidden_dim)となる
  print(output.shape)
  #次の隠れベクトルのshape : (RNNのユニット数*2 , batch_size, hidden_dim)となる。
  #※隠れベクトルなのでinput_sizeは関係なし
  print(hn.shape)
  
  # 系列全体に対する表現ベクトルが必要な場合の特徴表現
  # 最終的な隠れ層のベクトルを用いて結合するのでhnを用いる
  seq_feature = torch.cat((hn[-2,:,:],hn[-1,:,:]),dim=1)

```
