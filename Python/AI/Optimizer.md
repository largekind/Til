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
