---
title: "Pandas Cheetsheet"
date: 2023-11-08T21:30:03+09:00
categories: ["Python"]
tags: ["Python", "pandas"]
---
# Pandas Cheetsheet

## 概要

忘れがちなpandasの処理のチートシート

## ユニークな要素を抽出、カウントする

> pandas.Series.value_counts()

## カラムの名前を辞書に基づいて変更する

```python
import pandas as pd

# DataFrameを作成
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# カラム名を変更する辞書を作成
rename_dict = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

# renameメソッドを使ってカラム名を変更
df.rename(columns=rename_dict, inplace=True)
```

## カラムの中にある値を辞書に基づいて置き換える

mapとreplaceの2通りがある。
主な違いは以下の通り
- map
  - 元のSeriesに存在する全ての値が辞書のキーに一致しなければ、その値はNaN（つまり、欠損値）に置き換え
- replace
  - 置き換え対象の値が辞書に含まれない場合、元の値は変更されない

コードは以下の通り
``` python
# mapメソッドの使用例
df['column'] = df['column'].map(replace_dict)

# replaceメソッドの使用例
df['column'] = df['column'].replace(replace_dict)
```