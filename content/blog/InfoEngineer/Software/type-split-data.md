---
title: "テキストデータの比較とExcel出力自動化"
date: 2024-03-30T20:08:47+09:00
---
# テキストデータの比較とExcel出力自動化

## 概要

二つのテキストファイル内のパラメータとその値を比較し、差分をExcelファイルに出力する自動化スクリプトの作成について。特に、パラメータ名に`type`情報が含まれ、ファイル間で異なる`type`を持つ場合の比較を考慮する。

## 処理手順

1. **データの読み込み**: テキストデータから必要な情報（パラメータ名、値、`type`情報）を抽出。
2. **データの正規化**: `type`情報がないパラメータに`_type0`を追加し、パラメータ名を正規化する。
3. **データ比較**: 正規化されたパラメータ名を基にして、ファイル間の値を比較し、差分を抽出する。
4. **Excelへの出力**: 差分情報をExcelファイルに整理して出力。ブロック名でグループ化し、折りたたみ可能な形式で整理する。

## 技術的詳細

- **正規表現の使用**: パラメータ名から`type`情報を抽出し、正規化するために正規表現を使用。
- **`pandas`ライブラリ**: 差分情報をDataFrameとして管理し、Excelファイルに出力するために使用。
- **`openpyxl`ライブラリ**: Excelファイルの生成、編集、ブロックごとの折りたたみ設定に使用。

## 実装上の考慮点

- パラメータ名に複数の`_`が含まれる場合や、`type`情報が途中にある場合に対応するため、適切な正規表現パターンの選定が重要。
- Excel出力時には、読みやすさを考慮してブロック名ごとにデータをグループ化し、カラム幅を内容に応じて調整する。
- 大量のパラメータを扱う場合、処理効率とメモリ使用量に注意する。

## コード例

```python
import re
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.worksheet.dimensions import ColumnDimension, DimensionHolder

# データの読み込みと正規化
def parse_data_with_regex(file_data):
    data_dict = {}
    pattern = re.compile(r"(.+?)(_type\d+)?(_|$)")
    for line in file_data.strip().split("\n"):
        parts = line.split()
        key, value = parts[0], parts[1]
        match = pattern.match(key)
        if match:
            base_key = match.group(1)
            type_info = match.group(2) if match.group(2) else "_type0"
            normalized_key = f"{base_key}{type_info}"
            data_dict[normalized_key] = value
    return data_dict

# データ比較
def compare_data(data_a, data_b):
    diff_results = []
    data_a_map = {item['normalized_key']: item for item in data_a}
    data_b_map = {item['normalized_key']: item for item in data_b}
    all_keys = set(data_a_map.keys()) | set(data_b_map.keys())
    for key in all_keys:
        item_a = data_a_map.get(key)
        item_b = data_b_map.get(key)
        if item_a and item_b:
            if item_a['value'] != item_b['value']:


                diff_results.append({'key': key, 'value_a': item_a['value'], 'value_b': item_b['value'], 'status': 'Different values'})
        elif item_a:
            diff_results.append({'key': key, 'value_a': item_a['value'], 'value_b': 'N/A', 'status': 'Missing in B'})
        else:
            diff_results.append({'key': key, 'value_a': 'N/A', 'value_b': item_b['value'], 'status': 'Missing in A'})
    return diff_results

from openpyxl.worksheet.dimensions import ColumnDimension
# Excelファイルへの出力
def output_to_excel(diff_results):
# 新しいExcelファイルの作成とデータの書き込み
  wb = Workbook()
  ws = wb.active

# タイトル行の追加
  titles = ["Block Name", "Parameter A", "Parameter B", "Value A", "Value B", "Comparison Result"]
  ws.append(titles)

# ブロック名ごとにデータと折りたたみを設定
  current_block = None
  block_start_row = 2  # タイトル行の次から開始
  for row_data in formatted_diff:
      if current_block != row_data['Block Name']:
          if current_block is not None:
              # 前のブロックを折りたたむ
              ws.row_dimensions.group(block_start_row, ws.max_row - 1, hidden=True)
          current_block = row_data['Block Name']
          block_start_row = ws.max_row + 1  # 新しいブロックの開始行

      # データ行の追加
      ws.append([row_data['Block Name'], row_data['Parameter A'], row_data['Parameter B'],
                 row_data['Value A'], row_data['Value B'], row_data['Comparison Result']])

# 最後のブロックも折りたたむ
  ws.row_dimensions.group(block_start_row, ws.max_row, hidden=True)

# カラム幅の設定
  for col in ws.columns:
       max_length = max(len(str(cell.value)) for cell in col)
       adjusted_width = (max_length + 2) * 1.2
       ws.column_dimensions[col[0].column_letter].width = adjusted_width

# 改修したExcelファイルの保存（パス指定）
  formatted_excel_output_path_corrected = "/mnt/data/formatted_difference_report_corrected.xlsx"
  wb.save(filename=formatted_excel_output_path_corrected)

# 保存したファイルのパスを表示
formatted_excel_output_path_corrected
# 実際のデータ処理と出力の例
file_a_data = """
# ここにファイルAのデータを設定
"""
file_b_data = """
# ここにファイルBのデータを設定
"""
parsed_data_a = parse_data_with_regex(file_a_data)
parsed_data_b = parse_data_with_regex(file_b_data)
diff_results = compare_data(parsed_data_a, parsed_data_b)
output_path = output_to_excel(diff_results)
print(f"差分レポートが {output_path} に出力されました。")
```

このコード例は、テキストデータの読み込み、正規化、比較、およびExcelファイルへの出力を行う基本的な流れを示しています。具体的な実装には、データの形式や必要な処理の詳細に応じて調整が必要です。