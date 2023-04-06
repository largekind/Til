---
title: "稼働率の計算まとめ"
date: 2023-04-05T00:00:00+09:00
---
# 稼働率の計算まとめ

## MTBF : Mean Time Between Failures

平均故障間隔

そのまま故障する間隔となるので、各故障時間を$t_i$とすると、以下の式となる

$$MTBF = \frac{1}{n}\sum^{n}_{t=1}t_i$$

## MTBR :Mean Time Between Repair

平均復旧時間

そのまま復旧にかかった時間の間隔となるので、各修理時間を$r_i$とすると、以下の式となる

$$MTBR = \frac{1}{n}\sum^{n}_{r=1}r_i$$
## 稼働率

故障するまでの間隔を故障したときの復旧時間の合計で割った値が稼働率になる

> MTBF / (MTBF + MTBR)