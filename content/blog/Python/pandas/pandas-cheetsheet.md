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

ちなみに図も出力できる模様  
例えばヒストグラムであれば以下のようにする
``` python
 pandas.Series.value_counts().plot(kind='hist')
```

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

条件式には&や|を用いるが、現状はor/andでもよい模様

## 時刻(datetime)での抽出

以下のようにdate_timeに条件式をかませることで可能

```python
filtered_df = train_df.query('date >= datetime.datetime(2011, 7, 20)  & date <= datetime.datetime(2011, 8, 31)')
```

## groupbyを用いた収集

以下のようなもので収集可能。複数指定したい場合はaggを用いる

> mean_by_group = データフレーム型.groupby('カラム1')['カラム2'].mean()

''' python
train_df.groupby('day_of_week')['count'].agg(['mean', 'median']).reset_index()
'''

## 複数の集約関数をカラムごとに使用

以下のようにaggを用いると可能

``` python
df.agg['sum','mean']
```

groupbyと組み合わせると、特定の値ごとに対して適用も可能
``` python
df.groupby('month').agg({
    'count': 'median',
    'temperature': 'mean'
}).reset_index()
```

## 特定カラムの欠損をサンプルごと削除

df.dropna()を用いれば可能。subset引数を用いれば、カラムも指定できる
``` python
df.dropna(subset=['A'])
```

## 棒グラフの表示

plt.bar()を使う

``` python
plt.bar(ユニーク配列、ユニーク要素の出現回数)
```

例えばdf.value_counts()で得たものを出力したいのであれば以下
```
df_plot = df.value_counts()
plt.bar(df_plot.index, df_plot.values)
```

## 箱ひげ図の表示

plt.boxplot(df)あるいはplot.box()で箱ひげ図が作成できる

```python 
import matplotlib.pyplot as plt

# カラム「age」の値について箱ひげ図を描画する
plt.boxplot(users['age']) # 方法1
df['age'].plot.box() # 方法2
users['age'].plot(kind="box") #方法3
plt.show()

```

## 要約情報の表示

df.info()を使う

行数、列数、各列の非欠損値の数、各列のデータ型、使用メモリ数が出力される

``` python
df.info()
```

## 欠損の穴埋め

fillna()を用いる

最頻値であればmode()を用いて以下のように穴埋めが可能

```python
df.fillna(df.mode()[0])
```

## インデックス,カラム名にアクセス

df.locを用いる

``` python
df.loc['インデックス名', 'カラム名']
```

## 正規表現に一致する行を抽出する

df.str.contains("正規表現",オプション)で可能

例えば以下なら大文字小文字を区別しない、Jから始まるbook_authorを取得できる。

``` python
filtered_df_without_query = books_df[books_df['book_author'].str.contains("^J", regex=True, case=False)]
```

- regax : 正規表現有効無効 デフォルトTrue
- case : 大文字小文字識別するか デフォルトTrue

## データフレームの共通するカラムを結合する

pd.mergeを使う

> pd.merge(df1,df2,on='カラム名', how='結合方法')

結合方法は以下の通り
- inner : 内部結合（default）
- left : 左外部結合
- right : 右外部結合

## データーフレームを任意の割合で分割する

scikit-learnライブラリにあるtrain_test_splitを使用する

``` python
    train_df, test_df = train_test_split(データフレーム, test_size=テストデータの割合)
```
