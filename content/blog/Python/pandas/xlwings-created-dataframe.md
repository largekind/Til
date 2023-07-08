---
title: "Xlwings Created Dataframe"
date: 2023-07-06T21:28:29+09:00
categories: ["Python"]
tags: ["Python", "pandas"]
---
#  xlwingsを使用してPandas DataFrameを作成する

## 概要
xlwingsを使用してExcelファイルからデータを読み込み、それをPandasのDataFrameに保存する方法を示す。

この方法では、各Excelファイルの最初の3行を無視し、それ以降の行のデータを取得する。

'#'で始まる行は無視され、それ以外の行のデータはDataFrameに追加される。

## サンプルコード
```python
import xlwings as xw
import pandas as pd
import os

# 読み込むExcelファイルのリスト
files = ['file1.xlsx', 'file2.xlsx', 'file3.xlsx']

# データを保存するための空のDataFrameを作成

df = pd.DataFrame()

for file in files:
    # Excelファイルを開く
    book = xw.Book(file)
    sheet = book.sheets['Sheet1']

    # シートの使用中の範囲を取得（最初の3行を無視）
    used_range = sheet.used_range
    data_range = used_range[3:]

    # セルの値を取得し、DataFrameに追加
    data = [[cell.value for cell in row] for row in data_range if row[0].value is None or not str(row[0].value).startswith('#')]
    df = df.append(pd.DataFrame(data), ignore_index=True)

    # Excelファイルを閉じる
    book.close()

# DataFrameを表示
print(df)
```