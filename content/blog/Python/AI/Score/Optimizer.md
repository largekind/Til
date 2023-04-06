---
title: "最適化手法"
date: 2023-04-05T00:00:00+09:00
tags: [Python,AI,Score]
---
# 最適化手法

## SGD

確率的勾配降下法とも。最初の最適化手法

$\eta$ : 学習率
$L$ : 損失関数

$$
\theta _{t+1} = \theta _t -\eta \frac{\partial L}{\partial \theta _t }
$$

## Mometum

SGDの改良版。SGDにモーメンタムによる減衰処理が入る

$$
v_{t+1} = \alpha v_t -\eta \frac{\partial L}{\partial \theta _t } \\
\theta _{t+1} = \theta _t + v_{t+1}
$$

## Nesterov's Momentum

ネステロフのモーメンタム。
Momentumの改良版

$$
v_{t+1} = \alpha v_t -\eta \frac{\partial L}{\partial(\theta _t + \alpha v_t)} \\
\theta _{t+1} = \theta _t + v_{t+1}
$$

ただし実装が面倒なので、通常は以下の計算を用いる
$$
v_{t+1} = \alpha v_t -\eta \frac{\partial L}{\partial\Theta _t}\\
\Theta _{t+1} = \Theta _t + \alpha^2 v_t - (1 + \alpha)\eta \frac{\partial L}{\partial\Theta _t}
$$

## AdaGrad

Adamの前任となった最適化法

SGDが学習の後半で振動する問題を解決するため、
学習率を勾配の二乗和を用いて徐々に減衰させる手法を取り入れたもの

$$
h_{t+1l} = h_t + \frac{\partial L}{\partial \theta_t} \times  \frac{\partial L}{\partial \theta_t}   \\
\theta _{t+1l} = \theta _t -\eta \frac{1}{\epsilon + \sqrt{h_{t+1}}} + \frac{\partial L}{\partial\Theta _t}
$$

## RMSProp

AdaGradに割合的な考えを入れた最適化手法

古い勾配情報を一定確率で忘れることで学習率を調整する手法が入っている

$$
h_{t+1l} = \rho h_t + (1-\rho) \frac{\partial L}{\partial \theta_t} \times  \frac{\partial L}{\partial \theta_t}   \\
\theta _{t+1l} = \theta _t -\eta \frac{1}{\sqrt{\epsilon + h_{t+1}}} + \frac{\partial L}{\partial\Theta _t}
$$


## Adam

一番よく使われる最適化手法

$$
m_{t+1} = \rho _1m_1 + (1-\rho _1) + \frac{\partial L}{\partial\Theta _t} \\
v_{t+1} = \rho _2v_1 + (1-\rho _1) + \frac{\partial L}{\partial\Theta _t} \frac{\partial L}{\partial\Theta _t}
$$
