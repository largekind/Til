---
title: "Listの内容からDataFrameを抽出する方法"
date: 2023-05-29T23:37:29+09:00
categories: ["Python"]
tags: ["pandas", "Python", "utility"]
---
# Listの内容からDataFrameを抽出する方法

## 概要

Listに一致する情報からDataFrameの情報を抽出する情報をまとめる

## 方法(丸め誤差気にしない場合)

IntやStrといった、丸め誤差を気にしなくてよい型に対しての比較である場合、pd.isin()が使用できる

以下サンプルコード

``` python
import pandas as pd

# DataFrameの作成
df = pd.DataFrame(["A","B","C","D","E","F","G"])
# 特定のリスト
values_list = ["A","D","E"]

# Index Aにリストの要素が存在するかどうかを調べる
matches = df.isin(values_list)

print(df.loc[matches.any(axis=1)])
```

## 方法(丸め誤差がある場合)

floatといった浮動小数点の場合、isinなどは使えないため代わりにnp.iscloseを用いて抽出を行う

サンプルコード
``` python

import pandas as pd
import numpy as np

# データの作成
data = {
    'A': [x / 10.0 for x in range(1, 101)],
    'B': [x * 0.4 for x in range(1, 101)],
    'C': list('ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 4)[:100]
}

df = pd.DataFrame(data)
print(df)

# 特定のリスト
values_list = np.array([0.6, 0.8, 1.0])

# Index Aのデータとリストの各要素の差の絶対値が許容範囲内にあるかどうかを調べる
matches = np.isclose(df['A'].values, values_list[:, None], atol=1e-8).any(axis=0)

# 一致する行を抽出
df_matched = df[matches]
print(df_matched)
```