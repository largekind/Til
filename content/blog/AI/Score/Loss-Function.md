---
title: "損失関数まとめ"
date: 2023-04-05T00:00:00+09:00
tags: [Python,AI,Score]
categories: [AI]
---
# 損失関数まとめ

逆誤差伝搬時に予測と正解の誤差を求めるため、よく使うLossのまとめ。

損失と言うが、**マイナス値ではないので注意**

損失関数で求めた値が段々小さくなる方向で学習を進めている

## MSE (平均二乗誤差)

Mean Squared Error

名前の通り、二乗の平均を求める損失関数

$$
MSE( y_i, \hat{y_i}) = \displaystyle \frac{ 1 }{ n } \sum_{i = 1}^{ n } (y_i – \hat{y_i})^2
$$

## MAE (平均絶対誤差)

Mean Absolute Error

絶対値の平均を取る損失関数

$$
MAE( y_i, \hat{y_i}) = \displaystyle \frac{ 1 }{ n } \sum_{i = 1}^{ n } | y_i – \hat{y_i} |
$$

## SSE (二乗和誤差関数)

Sum of Squared Error

予測と政界の誤差の二乗値を計算し、その総和を取る損失関数。
MSEが平均を取るのに対し、こちらは総和

$$
SSE( y_i, \hat{y_i}) = \displaystyle  \sum_{i = 1}^{ n } (y_i – \hat{y_i})^2
$$

## CE (交差エントロピー誤差)

クラス分類とかでよく使われる損失関数。

予測と正解が近いほど1、遠いほど0を示す交差エントロピーを利用している。

マイナスを掛けることで、予測と正解が近いほど値が小さくなるように調整している

$$
E = -\displaystyle \sum_{ k }^{  } t_k \log y_k
$$
