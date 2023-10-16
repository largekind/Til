---
title: "Merge Single to MultiIndex"
date: 2023-10-16T21:21:02+09:00
draft: True
categories: ["Python"]
tags: ["Python", "pandas"]
---
# Merge Single to MultiIndex

## 概要

マルチインデックスを持つデータに対して、対応する一元のデータを結合したい場合の方法をまとめる

通常のマージだとレベル等で引っかかる

## コード

``` python
# サフィックスを抽出
dfA['C'] = dfA.index.str.split('_').str[-1]

# サフィックスをキーとしてdfBの値を取得
dfA['Val'] = dfA['C'].map(dfB.squeeze())

# 'C'列を削除
dfA = dfA.drop(columns='C')
```

## 詳細

- .map()メソッド
  - Seriesの各要素に関数や辞書、Seriesを適用するためのメソッド。
  - 対象のSeriesの要素をキーとして、引数に指定されたSeriesや辞書の値を取得する。
- squeeze()メソッド
  - DataFrameやSeriesの次元を縮約する。
  - 1列しか持たないDataFrameをSeriesに変換する場合に使用。
- マッピングの仕組み
  - .map()を使用する際、マッピングの基準となるSeriesや辞書が必要。
  - 今回は、dfB.squeeze()によって得られるSeriesを使用して、dfA['C']の値をマッピングの基準としている。