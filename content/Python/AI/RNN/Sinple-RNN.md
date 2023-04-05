# シンプルなRNNの実装

以下の流れで単語の数だけ次元を持つベクトルを低次元化(Embedding)し、
RNNに渡せるようにして学習を行う流れが基本となる
1. 単語(次元 : 単語の数)をembbeding層に渡し、単語埋め込みベクトルの次元に落とし込む
2. 単語埋め込みベクトルの次元を受け取り、RNNは中間状態の次元を出力

単語埋め込みベクトル : 特徴ベクトル。単語ベクトルをEmbeddingの処理でより小さい次元数に落とし込ませたベクトル

## RNNの基本的な計算式

RNNの中間層の出力は以下の式で与えられる

$$
h_i = \tanh(h_{t-1}W_h + x_iW_x + b)
$$

## 重みの初期化の実装

``` python
class SimpleRnnlm:
  def __init__(self, vocab_size, wordvec_size, hidden_size):
    # V : 単語ベクトルの次元
    # D : 単語埋め込みベクトルの次元
    # H : 中間状態ベクトルの次元
    V , D , H = vocab_size, wordvec_size, hidden_size
    rn = np.rondom.randn

    # 重みの初期化
    embed_W = rn(V, D).astype('f') #embedding後の特徴ベクトル 単語ベクトル -> 単語埋め込みベクトル
    rnn_Wx = rn(D , H).astype('f') #RNNの入力の重み 単語埋め込みベクトル -> 中間層ベクトル のため次元は(D,H)となる
    rnn_Wh = rn(H, H).astype('f') #RNNの中間層の重み。隠れ層 -> 隠れ層の次元なので(H,H)となる
    rnn_b = np.zeros(H) #バイアス。中間層の重みに付くので次元はH

    affine_W = rn(H,V).astype('f') #重みのアフィン変換 入力(N*T,H)の次元を最終的に(N,T,V)の形に落とし込むので (H,V)となる
    affine_b = np.zeros(V).astype('f') #バイアスのアフィン変換。ただ足すだけなので、次元はVになる
    
```
    
    