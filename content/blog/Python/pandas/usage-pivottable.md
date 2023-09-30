---
title: "Usage Pivottable"
date: 2023-09-30T21:17:42+09:00
draft: True
categories: ["Python"]
tags: ["Python", "pandas"]
---
# Usage Pivottable

## 概要

特定の値を列としたとき、どういう表になるかを作成するピボットテーブルをpandas上で行う方法を記述する

※ピボットテーブルは、データの再構成や要約を行い、特定の軸に沿った集計や分析を容易にするための表形式のデータ表示方法
スプレッドシートやデータベース、データ解析ツールなど、多くのソフトウェアで利用されている

具体的には、ピボットテーブルを使用すると、大量のデータを特定のカテゴリごとにグループ化して集計したり、複数のデータ属性に基づいてデータをクロス集計したりすることが可能となる

## 基本

``` python
import pandas
df = pd.Dataframe(<データ>)
df.pivot_table(index=<インデックスとする列>, columns=<カラムとする列>, values=<値とする列>, aggfunc=<集計関数>)
```

集計関数には以下が使用可能
- 基本的な統計関数:
  - sum: 合計
  - mean: 平均
  - median: 中央値
  - min: 最小値
  - max: 最大値
  - std: 標準偏差
  - var: 分散
  - count: カウント（非欠損値の数）
  - nunique: ユニークな値のカウント
  - first: 最初の非欠損値
- カスタム関数: 任意の関数をラムダ式や関数として指定できる。
  - 例: aggfunc=lambda x: sum(x) / len(x) (合計を要素数で割った値)
- 複数の関数: リストで複数の関数を指定することで、複数の集計を同時に行うことができる。
  - 例: aggfunc=['sum', 'mean', 'std']

## 使用例

``` python
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
```