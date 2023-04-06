---
title: "活性化関数まとめ"
date: 2023-04-05T00:00:00+09:00
tags: [Python,AI,Score]
---
# 活性化関数まとめ

## ステップ関数

階段関数とも。最適化が難しいため余り使用されない。

$$

{y = \left\{
  \begin{array}{cc}
    1 & (x \gt 0) \\
    0 & (x \le 0)
  \end{array}
\right.
}

$$

## ReLU

中間層における最適化で高い精度を誇る。

基本的に色んなNNで使用される認識。

- 順伝搬
$$ 
{y = \left\{
  \begin{array}{cc}
    x & (x \gt 0) \\
    0 & (x \le 0)
  \end{array}
\right.
}
$$
- 逆伝搬
$$
{y = \left\{
  \begin{array}{cc}
    1 & (x \gt 0) \\
    0 & (x \le 0)
  \end{array}
\right.
}
$$

## sigmoid

二値分類の出力やLSTMの箇所で使われる活性化関数

- 順伝搬
$$
{y = \cfrac{1}{1 + e^{-x}}}
$$
- 逆伝播
$$
{\cfrac{\partial y}{\partial x} = y(1 - y)
}
$$

## tanh

RNNやLSTMの隠れ層での活性化関数で使われているもの
- 順伝播
$$
{y = \tanh x = \cfrac{e^x - e^{-x}}{e^x + e^{-x}}
}
$$
- 逆伝播
$$
{\cfrac{\partial y}{\partial x} = \textrm{sech}^2 x = \cfrac{1}{\cosh^2 x} = \cfrac{4}{(e^x + e^{-x})^2} = 1 - tanh(x)^2
}
$$

## softmax

出力の総和が1になる活性化関数。クラス分類とかで使用されている

- 順伝播
$$
{y_i = \cfrac{e^{x_i}}{\displaystyle\sum_{k=1}^{n}{e^{x_k}}} \quad (i = 1, 2, \ldots, n)
}
$$

- 逆伝搬
$$
\cfrac{\partial y_i}{\partial x} = 
\begin{cases}
y_i - y_i^2 & (i = k)\\
-y_iy_k & (i \neq k)
\end{cases}
$$

${\displaystyle\sum_{k=1}^{n}{e^{x_k}}} $を求める時は各クラス毎の和であるため、np.sum(dx,axis=1,keepdims=1)で求める

