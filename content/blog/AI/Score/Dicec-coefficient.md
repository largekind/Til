---
title: "Dice係数"
date: 2023-04-05T00:00:00+09:00
tags: [Python,AI,Score]
categories: [AI]
---
# Dice係数

セマンティックセグメンテーションにて、IoUの改良verとして使われる評価関数

IoUの欠点である「２つの領域の面積の差が大きいほど値が小さく評価されてしまう」点をIoUの分母を２つの面積の領域の平均にすることで緩和した指標

以下の計算で求められる

$$
Dice(S_{true},S_{pred}) = \frac{2|S_{true}\cap S_{pred}|}{|S_{true}|+|S_{pred}|}
$$

IoUとは$IoU \leq Dice係数$の関係がある
