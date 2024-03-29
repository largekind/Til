---
title: "最尤推定量"
date: 2023-04-05T00:00:00+09:00
tags: ["Statistics"]
categories: ["Statistics"]
---
# 最尤推定量

手元のデータが、どの母パラメータに従う分布から得られる確率が最も高いかに基づいて考えられる推定量

ラメータθに従う分布の密度関数を$L(\theta;x)=f(x;\theta)$とする。尤度関数を$L(\theta;x)=f(x;\theta)$とすると、L(θ;x)を最大にするような推定量$\theta$を$\theta$の最尤推定量という。

## ベルヌーイ分布における最尤推定

$$
P(X =x) = p^x(1-p)^{1-x}
$$
なるとき、**最尤推定量は$x$となる**