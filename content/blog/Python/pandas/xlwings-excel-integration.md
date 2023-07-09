---
title: "Xlwings_excel_integration"
date: 2023-07-06T21:27:49+09:00
categories: ["Python"]
tags: ["Python", "pandas"]
---
# xlwingsを使用して複数のExcelファイルを統合する
## 概要

## 概要
xlwingsを使用して複数のExcelファイルからデータを読み込み、それらを1つのExcelファイルにまとめる方法を示す。

この方法では、各Excelファイルの最初の3行を無視し、それ以降の行のデータをまとめるExcelファイルに書き込む。

'#'で始まる行は無視され、それ以外の行のデータはまとめるExcelファイルに書き込む。

## サンプルコード
```python
import xlwings as xw
import os

# まとめるExcelファイルを新規作成
summary_book = xw.Book()
summary_sheet = summary_book.sheets[0]

# まとめるExcelファイルの次に書き込む行
next_row = 1

# 読み込むExcelファイルのリスト
files = ['file1.xlsx', 'file2.xlsx', 'file3.xlsx']

# ヘッダー情報をまとめるExcelファイルに書き込む
header_book = xw.Book(files[0])
header_sheet = header_book.sheets['Sheet1']
header_range = header_sheet.range('1:3')

for row in header_range:
    for i, cell in enumerate(row):
        summary_cell = summary_sheet.range((next_row, i+1))
        summary_cell.value = cell.value
        summary_cell.api.Font.Color = cell.api.Font.Color
        summary_cell.api.Interior.Color = cell.api.Interior.Color
    next_row += 1

header_book.close()

for file in files:
    # Excelファイルを開く
    book = xw.Book(file)
    sheet = book.sheets['Sheet1']

    # シートの使用中の範囲を取得（最初の3行を無視）
    used_range = sheet.used_range
    data_range = used_range[3:]

    # セルの値と書式を取得し、まとめるExcelファイルに書き込む
    for row in data_range:
        # '#'で始まる行を無視
        if row[0].value is None or not str(row[0].value).startswith('#'):
            for i, cell in enumerate(row):
                summary_cell = summary_sheet.range((next_row, i+1))
                summary_cell.value = cell.value
                summary_cell.api.Font.Color = cell.api.Font.Color
                summary_cell.api.Interior.Color = cell.api.Interior.Color
            next_row += 1

    # Excelファイルを閉じる
    book.close()

# まとめたExcelファイルを保存
summary_book.save('summary.xlsx')
summary_book.close()
```