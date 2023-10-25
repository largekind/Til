---
title: "Extract MultiLine Cell in Excel"
date: 2023-10-25T21:28:23+09:00
categories: ["Python"]
tags: ["Python", "pandas"]
---
# セル内に複数行を持つ場合のDataframe化

## 概要

excel セル内に複数行を持つデータを単純に取り込むのはpandasのread_excelではできない。

そのため、openpyxlを用いて直接アクセスし、データを取り込む方法を記載する

## サンプルコード

サンプルでは使用範囲のH列、３行目以降を取り込む

``` python
import openpyxl
import pandas as pd

# Excelファイルを読み込む
wb = openpyxl.load_workbook('data.xlsx')

# アクティブなシートを取得する
sheet = wb.active

# 空のDataFrameを作成する
df = pd.DataFrame()

# 使用されているセルの範囲を特定する
min_row = max(3, sheet.min_row)  # 3行目以降
max_row = sheet.max_row

# H列の使用されているセルを処理する
for row_idx in range(min_row, max_row + 1):
    cell = sheet.cell(row=row_idx, column=8)
    # セルのデータを複数行に分割する
    lines = cell.value.split('\n') if cell.value else []
    # 分割したデータをスペース区切りでDataFrameに追加する
    for line in lines:
        data = line.split()
        df = df.append([data], ignore_index=True)

# ファイルを閉じる
wb.close()

# DataFrameを表示する
print(df)

```