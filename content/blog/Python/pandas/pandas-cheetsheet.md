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

## 特定の条件に基づいて、値を設定する

基本はwhere関数を用いる

以下のような構成をしている

> np.where(条件,真の場合に入れたい値,負の場合に入れたい値)

また、pd上で納めたい場合はapplyとlambdaを用いて、以下のように値を設定することが可能

具体的には以下のようなコード

``` python
df.apply(lambda x: 1 if x == 'A' else 0)
```

## ソート

indexでのソートはdf.sort_index()、値でのソートはdf.sort_values()になる

sort_values()であれば以下のようなコード リストで渡せばソートの優先度が決められる
``` python
df.sort_values(by=["hoge","fuga"])
```

## インデックスの初期化

reset_index()を使用。引数のdrop=Trueを入れておかないと、元のインデックスが"index"の名前を持つ列として追加される
```
df.reset_index(drop=True)
```

## 特定のカラム抽出

以下。二重かっこになるのに要注意

``` python
 df[['A','B','C']]
```

## 特定行の値が一致する箇所を取得

2通りの方法

### 1.条件式を使用するパターン

``` python
df = df[df['data'] == 'A']
```

### 2.queryを使用するパターン

``` python
df = df.query('data == "Friday"')
```

他にもいろいろ条件式が使えるので、その都度対応する。