---
title: "Category Dataframe to Xlsx Sheet"
date: 2023-06-25T22:42:27+09:00
categories: ["Python"]
tags: ["", "", "Python", "pandas"]
---
# カテゴリ分けされたDataframeを色付けしてxlsxのシートに出力する

## 概要

表題の通り。以下のようなDataframeがあった場合にカテゴリ分けして情報を出力する方法を記述する。

``` txt
    Sheet            Category   Name   Reg  Hoge
0  Sheet1  [大項目1, 中項目1, 小項目1]  Name1  Reg1  Reg1
1  Sheet1        [大項目1, 中項目2]  Name2  Reg2  Reg2
2  Sheet1              [大項目2]  Name3  Reg3  Reg3
3  Sheet2        [大項目1, 中項目1]  Name4  Reg4  Reg4
4  Sheet2  [大項目2, 中項目1, 小項目1]  Name5  Reg5  Reg5
```

上記のようなデータを以下のような形式に分け、項目ごとに色付けする

| |Sheet1| | |
|:----|:----|:----|:----|
| |大項目1| | |
| |中項目1| | |
| |小項目1| | |
| |Name1|Reg1|Reg1|
| |中項目2| | |
| |Name2|Reg2|Reg2|
| |大項目2| | |
| |Name3|Reg3|Reg3|
| |Sheet2| | |
| |大項目1| | |
| |中項目1| | |
| |Name4|Reg4|Reg4|
| |大項目2| | |
| |中項目1| | |
| |小項目1| | |
| |Name5|Reg5|Reg5|

## サンプルコード

``` py
from openpyxl import Workbook
from openpyxl.styles import PatternFill
from openpyxl.utils import get_column_letter

def process_dataframe(df, start_col = 2 ,start_row=1):
    # ワークブック初期化
    wb = Workbook()
    ws = wb.active
    
    # 色定義
    fill_blue = PatternFill(start_color="0000FF", end_color="0000FF", fill_type = "solid")
    fill_green = PatternFill(start_color="00FF00", end_color="00FF00", fill_type = "solid")
    fill_red = PatternFill(start_color="FF0000", end_color="FF0000", fill_type = "solid")
    fill_yellow = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type = "solid")

    current_sheet = None
    prev_category = []
    max_columns = len(df.columns)  # データフレームの列数
    
    for i, row in df.iterrows():
        if row['Sheet'] != current_sheet:
            # シート名の新しい行を追加
            for cell in ws[start_row: start_row + 1][0][:max_columns]:  # データ列の最大数まで色を付ける
                cell.fill = fill_blue
            ws.cell(row=start_row, column=start_col, value=row['Sheet'])
            current_sheet = row['Sheet']
            prev_category = [None] * len(row['Category'])  # シートが変わったときに前のカテゴリをリセット
            start_row += 1

        for level, item in enumerate(row['Category']):
            if len(prev_category) <= level:  # 必要に応じてprev_categoryを拡張
                prev_category.append(None)
            if item != prev_category[level]:  # このレベルのカテゴリが変わった場合のみ行を挿入
                color = fill_green if level == 0 else fill_red if level == 1 else fill_yellow
                ws.insert_rows(start_row)
                ws.cell(row=start_row, column=start_col, value=item)
                for cell in ws[start_row: start_row + 1][0][:max_columns]:  # データ列の最大数まで色を付ける
                    cell.fill = color
                start_row += 1
                prev_category[level] = item
                
        for j, col in enumerate(df.columns[2:], start=start_col):  # 'Sheet'と'Category'列をスキップ
            ws.cell(row=start_row, column=j, value=row[col])
        start_row += 1
    
    return wb
```

以下はテストコード

``` py
import pandas as pd

# Create a test dataframe
data = {
    'Sheet': ['Sheet1', 'Sheet1', 'Sheet1', 'Sheet2', 'Sheet2'],
    'Category': [['大項目1', '中項目1', '小項目1'], ['大項目1', '中項目2'], ['大項目2'], ['大項目1', '中項目1'], ['大項目2', '中項目1', '小項目1']],
    'Name': ['Name1', 'Name2', 'Name3', 'Name4', 'Name5'],
    'Reg': ['Reg1', 'Reg2', 'Reg3', 'Reg4', 'Reg5'],
    'Hoge': ['Reg1', 'Reg2', 'Reg3', 'Reg4', 'Reg5']
}

df = pd.DataFrame(data)
print(df)
# Process the dataframe
wb = process_dataframe(df,start_row = 5)

# Save the workbook
wb.save('test_output.xlsx')
```