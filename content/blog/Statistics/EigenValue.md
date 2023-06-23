---
title: "固有値・固有ベクトル"
date: 2023-04-05T00:00:00+09:00
tags: ["Statistics"]
categories: ["Statistics"]
---
# 固有値・固有ベクトル

## 概要

以下の式が成立するベクトル。
Aに$u_i$掛けると$\lambda$倍になるベクトル
$$
A_{u_i} = \lambda u_i
$$

## 固有値・固有ベクトル求め方

1. $det(A - \lambda I) =0$を解いて固有値$\lambda$を求める
    - $I$ : 単位行列
2. $A_{u_i} = \lambda u_i$の$\lambda$に値を入れて、さらに$u_i$を$x$を用いて仮置きして連立方程式を解く
3. 特定の$x$値を$t$とおいて方向のベクトルとして回答する