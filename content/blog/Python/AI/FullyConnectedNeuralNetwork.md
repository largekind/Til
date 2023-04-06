---
title: "全結合ニューラルネットワーク"
date: 2023-04-05T00:00:00+09:00
tags: [Python,AI]
---
# 全結合ニューラルネットワーク

全ての変数を使って計算する層(Affineレイヤ)を積み重ねて作るネ  ットワーク

計算がアフィン変換に似ていることから命名

## 定義と初期化処理

基本的にあるアフィンから見た入力と出力を指定、初期化する処理を行う

``` python
import numpy as np

# Activation関連
def relu(X):
  return np.maximum(0,X)

def softmax(X):
  X= X - np.max(X, axis=1, keepdims = True)
  return np.exp(X)/np.sum(np.exp(X),axis=1,keepdims=True)

def relu_backward(Z,delta):
  delta[Z==0] = 0

def cross_entropy_error(y,t):
  batch_size = y.shape[0][0]
  return -np.sum(t * np.log(y + 1e-7)/ batch_size)

# 全結合ネットワーク
class FullyConnectionNeuralNetwork():
  # 初期化
  def __init__(self, layer_units: list):
    self.n_iter = 0
    self.t_ = 0
    self.layer_units = layer_units #各層のノード数を格納したリスト
    self.n_layers_ = len(layer_units) #レイヤ数
    # パラメータの初期化
    self.coefs_ = [] #係数 重みのこと
    self.intercepts_ = [] #切片 バイアスのこと
    # 全レイヤーに対して実行
    for i in range(self.n_layers_ -1):
      #自身の入力側ノードとその次の出力側ノードに対して係数/切片の初期化を実行
      coef_init , intercept_init = self._init_coef(layer_units[i],layer_units[i+1]) 
      #各重みとバイアスを保存
      self.coefs_.append(coef_init)
      self.intercepts_.append(intercept_init)
      
      #重み勾配の初期化
      self.coef_grads_ = [np.empty((n_in_, n_out)) for  n_in_, n_out_ in zip(layer_units[:-1],layer_units[1:])]
      
      #バイアス勾配の初期化
      self.intercept_grads_ = [np.empty(n_out) for  n_out_ in layer_units[1:]]

    def _init_coef(self, n_in: int, n_out: int):
      """
      ある層間のパラメータを初期化
      n_in : 入力側ノード数
      n_in : 出力側ノード数
      """
      std = np.sqrt(2/n_in)
      coef_init = np.random.randn(n_in,n_out) + std #正規化の式
      intercept_init = np.zeros(n_out) #バイアスの初期化 出力先のノードの数だけバイアスがあるので、その数だけ初期化

      return coef_init, intercept_init

```

## 順伝播処理

順伝搬の処理。次の層が隠れ層なら活性化関数にrelu、出力層ならsoftmax関数を指定する

``` python
def _forward(self, activations: list):
  #activations : 各層の出力をまとめたリスト shape : (バッチサイズ , 次元)
  
  affile = [None] * (self.n_layers_ -1)
  for i in range(self.n_layers_ - 1):
    #アフィン変換 H = XW + Bになり、X: activations W:coef(重み/係数) B:intercepts_(切片/バイアス)となる
    affile[i] = np.dot(activations,self.coefs_[i]) + self.intercepts_
    
    #次層が出力層/隠れ層かでActivationを変える
    if (i + 1) == (self.n_layers_ -1):
      #出力層
      activations[i + 1] = softmax(affine[i])
    else:
      #隠れ層
      activations[i + 1] = relu(affine[i])

    return activations
```

## 勾配+逆伝搬

最終層から入口へ勾配が伝搬していく

$H = XW+B$に対して、重みの勾配$\frac{\delta W}{\delta L} = X^T\frac{\delta L}{\delta H}$

入力の勾配$\frac{\delta X}{\delta L} = \frac{\delta L}{\delta H}W^T$で与えられることから実装を行う

纏めると以下の式になる
$$
{\begin{align}
\frac{\partial f}{\partial \boldsymbol{X}} &= \frac{\partial f}{\partial \boldsymbol{Y}} \cdot W^T  \\
\frac{\partial f}{\partial W} &= \boldsymbol{X}^T \cdot \frac{\partial f}{\partial \boldsymbol{Y}}    \\
\frac{\partial f}{\partial \boldsymbol{b}} &= \frac{\partial f}{\partial \boldsymbol{Y}}   \\
\end{align}
}
$$

導出は結結面倒なので以下のqiitaを参照

https://qiita.com/masatomix/items/0678e56e56af27efa110

``` python
#勾配の算出
def _grad(self, j, activations, deltas):
  #係数(重み)の勾配はdot(x^T,delta)、Xはactivations、deltaは勾配なので、そこから計算する
  self.coef_grads_[j] = np.dot(activations[j].T , deltas[j])
  #切片(バイアス)の勾配は勾配の総和となる
  self.intercept_grads_[j] = np.sum(deltas[j],axis=0)

# 逆伝搬
def _backward(self, t, activations):
  # t : 正解ラベル shape=(バッチ,出力層ノード数)
  # activation : list 各層の出力を収めたもの

  deltas = [None] * (self.n_layers_ -1) #勾配
  last = self.n_layers - 2 #出力層の1つ手前のindex

  #交差エントロピーとsoftmaxを用いて勾配算出
  n_samples = t.shape[0]
  deltas[last] = (activations[-1] - t) / n_samples #出力層に出ている予測値と正解ラベルの差をサンプル数で割る
  
  #出力層の1つ手前のパラメータの勾配を算出
  self.grad(last,activations,delta)
  
  #残りのパラメータの勾配を産出
  for i in range(self.n_layers -2 ,0 , -1)
    # 入力(activations)の勾配算出 (1)式からdeltaと重みの転置した物の内積になる
    deltas[i-1] = np.dot(delta[i],self.coefs_[i].T)
    
    # ReLUの勾配 i-1番目から出力されたi番目の入力とそれに付随する1つ前の勾配から求める
    relu_backward(activations[i], deltas[i-1])
    
    # パラメータの勾配 i-i番目の勾配を求める
    self._grad(i-1, activations, deltas)
    
  return

```