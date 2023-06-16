---
title: "DataFrameのデータ分割方法"
date: 2023-05-01T21:24:00+09:00
categories : [Python]
tags : [Python, pandas]
---

# DataFrameのデータ分割方法

## 概要

データフレームのデータをN分割したい時の方法を記述する

## 方法

pd.cutを用いることで、N分割した場合の条件分岐が取得できる

> pd.cut(df, N)

上述を用いたものに対してkeyで取得して、それらの情報を用いれば
データを取得できる

以下サンプルコード
``` python
import pandas as pd

# DataFrameを作成する
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'B': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
})

# 列'A'をN分割する
n = 3
df['A_group'] = pd.cut(df['A'], n)

# A_groupでグループ分けし、DataFrameを分割する
df_grouped = dict(tuple(df.groupby('A_group')))
keys = list(df_grouped.keys())

#print(df_grouped)
# 結果を表示する
for i in range(n):
    print(f'Group{i+1}:')
    print(df_grouped[keys[i]])

```