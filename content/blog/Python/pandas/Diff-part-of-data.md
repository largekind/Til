---
title: "部分的なDataFrameの比較と差分行の抽出"
date: 2023-06-22T22:02:49+09:00
categories : ["Python"]
tags : ["Python","pandas"]
---

# 部分的なDataFrameの比較と差分行の抽出

## 概要

2つのPandas DataFrameがあり、そのうちの1つは一部のデータがNoneである場合、Noneでない部分だけを対象にした比較を行いたい。

また、Noneでない部分で一致しない行を抽出したい。以下にその方法を示す。

## サンプルコード

```
import pandas as pd
import numpy as np

# あなたの実際のデータを用いてDataFrameを作成する
dataA = pd.DataFrame(...)
dataB = pd.DataFrame(...)

# dataBからNone（またはNaN）を含む行を削除する
dataB_filtered = dataB.dropna()

# dataAとdataB_filteredの一部が一致しているかを確認し、
# 一致しない行のマスク（True/FalseのDataFrame）を作成する
mask = dataA.loc[dataB_filtered.index, dataB_filtered.columns] != dataB_filtered

# 一致しない行を含むDataFrameを作成する
data_diff = dataB_filtered[mask.any(axis=1)]
```