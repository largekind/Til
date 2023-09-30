---
title: "Add Colums in MultiIndex table"
date: 2023-09-30T21:17:10+09:00
categories: ["Python"]
tags: ["Python", "pandas"]
---
# マルチインデックスを持つテーブルへ列を追加する方法

## 概要

通常、マルチインデックスを持つデータ(例:ピボットテーブル)に列を追加する場合、pandasの制約によって弾かれる

そのため、別途列を追加したい場合の方法をまとめる

## 方法

以下のようなテーブルを持つとする

``` python
data = {
    'ID': ['ID1', 'ID1', 'ID2', 'ID2'],
    'TEST': ['TEST1', 'TEST2', 'TEST1', 'TEST2'],
    'DATA': ['DATA_A', 'DATA_B', 'DATA_A', 'DATA_B'],
    'Val': [10, 20, 30, 40]
    'Info': ['Info1', 'Info1', 'Info2', 'Info2']
}
df = pd.DataFrame(data)
```

上記に対してpivot_tableを作成してマルチインデックス持ちのDataframeを作成する
```
# ピボットテーブルの作成
pivot_df = df.pivot_table(index='ID', columns=['TEST', 'DATA'], values='Val', aggfunc='first')
```
そうすると、以下のようなテーブルとなる
``` text
      | TEST | TEST1  | TEST2 | 
      | DATA | DATA_A | DATA_B|
ID           |        |       |
-------------------------------
ID1          |  10    |  20   |
ID2          |  30    |  40   |
```
上記に対して、Infoという列を追加したい場合は以下になる
``` python
# Info列の追加
info_series = df.drop_duplicates('ID').set_index('ID')['Info']
pivot_df['Info'] = info_series
```

これはpivot_tableがIndexとしているIDが重複していたりする場合に追加できないため、
正確に列追加するようにするための処理となる

## 最終コード
```
import pandas as pd

# ダミーデータの作成
data = {
    'ID': ['ID1', 'ID1', 'ID2', 'ID2'],
    'TEST': ['TEST1', 'TEST2', 'TEST1', 'TEST2'],
    'DATA': ['DATA_A', 'DATA_B', 'DATA_A', 'DATA_B'],
    'Val': [10, 20, 30, 40],
    'Info': ['Info1', 'Info1', 'Info2', 'Info2']
}
df = pd.DataFrame(data)

# ピボットテーブルの作成
pivot_df = df.pivot_table(index='ID', columns=['TEST', 'DATA'], values='Val', aggfunc='first')

# Info列の追加
info_series = df.drop_duplicates('ID').set_index('ID')['Info']
pivot_df['Info'] = info_series

# Excelファイルへの出力
pivot_df.to_excel("/mnt/data/pivot_table_output.xlsx")
```