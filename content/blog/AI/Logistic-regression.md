---
title: "ロジスティック回帰"
date: 2023-04-05T00:00:00+09:00
tags: [Python,AI]
categories: [AI]
---
# ロジスティック回帰

2クラス分類でよく用いられる回帰モデルの一種

モデルの出力$\hat{y}$を確率値$p(y=1|x)$で扱えるようにしている

学習では$y_n$を目的変数とすると、以下の負の尤度関数が最小になるように学習する
$$
-\sum_{n}(y_n\log\hat{y_n} + (1-y_n)\log(1-\hat{y_n}))
$$

オッズは以下の式になる
$$
\frac{\hat{y}}{1-\hat{y}} = exp(w^Tx +b)
$$