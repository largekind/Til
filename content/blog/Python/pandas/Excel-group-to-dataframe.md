---
title: "Excel Group to Dataframe"
date: 2023-06-15T21:20:09+09:00
categories: ["Python"]
tags: ["Python", "pandas"]
---
# Excel Group to Dataframe

## 概要

よくある、各グループごとに要素がまとめられたExcelに対して、
グループごとのデータをDataFrameにまとめる方法を記述する。

## データ例

以下のような形の表となる

| SW  | 列1    | 列2     | 列3    | 列4    | 列5    |
|-----|-------|--------|-------|-------|-------|
| ON  | グループA |        |       |       |       |
| ON  | A値1_1 | A値2_1  | A値3_1 | A値4_1 | A値5_1 |
| ON  | A値1_2 | A値2_2  | A値3_2 | A値4_2 | A値5_2 |
| OFF | A値1_3 | A値2_3  | A値3_3 | A値4_3 | A値5_3 |
| OFF | A値1_4 | A値2_4  | A値3_4 | A値4_4 | A値5_4 |
| OFF | A値1_5 | A値2_5  | A値3_5 | A値4_5 | A値5_5 |
| ON  | グループB |        |       |       |       |
| ON  | B値1_1 | B値2_1  | B値3_1 | B値4_1 | B値5_1 |
| OFF | B値1_2 | B値2_2  | B値3_2 | B値4_2 | B値5_2 |
| OFF | B値1_3 | B値2_3  | B値3_3 | B値4_3 | B値5_3 |
| OFF | B値1_4 | B値2_4  | B値3_4 | B値4_4 | B値5_4 |
| ON  | B値1_5 | B値2_5  | B値3_5 | B値4_5 | B値5_5 |
| ON  | グループC |        |       |       |       |
| OFF | C値1_5 | C値2_5  | C値3_5 | C値4_5 | C値5_5 |
| OFF | C値1_5 | C値2_5  | C値3_5 | C値4_5 | C値5_5 |
| ON  | グループD |        |       |       |       |
| ON  | D値1_1 | D値2_1  | D値3_1 | D値4_1 | D値5_1 |
| ON  | D値1_2 | D値2_2  | D値3_2 | D値4_2 | D値5_2 |
| OFF | D値1_3 | D値2_3  | D値3_3 | D値4_3 | D値5_3 |

## サンプルコード

``` python
import pandas as pd

# Excelデータの読み込み。適切なファイルパスとシート名を指定すること。
df = pd.read_excel('testd.xlsx', sheet_name='Sheet1', header=4)

print("---読み込んだExcelデータ---")
print(df)
print("\n\n")
# 新規データフレームの作成。列は指定のものとする。
new_df = pd.DataFrame(columns=df.columns.insert(1, "グループ"))

# グループ名と値の新規データフレームへの追加。
group = None
for idx, row in df.iterrows():
    # '列1'以外のすべての列が空か否かの確認。
    if row.iloc[2:].isnull().all():
        group = row['列1']
    elif row['SW'] == 'ON':
        new_row = pd.DataFrame({'グループ': group, **row.to_dict()}, index=[0])  # 列ごとに値を追加。
        new_df = pd.concat([new_df, new_row], ignore_index=True)  # 新しい行を追加。

# 新規データフレームの出力。
print("---作成したデータ--")
print(new_df)
```

## 出力結果

``` bash

---読み込んだExcelデータ---
     SW     列1      列2     列3     列4     列5
0    ON  グループA     NaN    NaN    NaN    NaN
1    ON  A値1_1  A値2_1   A値3_1  A値4_1  A値5_1
2    ON  A値1_2   A値2_2  A値3_2  A値4_2  A値5_2
3   OFF  A値1_3   A値2_3  A値3_3  A値4_3  A値5_3
4   OFF  A値1_4   A値2_4  A値3_4  A値4_4  A値5_4
5   OFF  A値1_5   A値2_5  A値3_5  A値4_5  A値5_5
6    ON  グループB     NaN    NaN    NaN    NaN
7    ON  B値1_1  B値2_1   B値3_1  B値4_1  B値5_1
8   OFF  B値1_2   B値2_2  B値3_2  B値4_2  B値5_2
9   OFF  B値1_3   B値2_3  B値3_3  B値4_3  B値5_3
10  OFF  B値1_4   B値2_4  B値3_4  B値4_4  B値5_4
11   ON  B値1_5   B値2_5  B値3_5  B値4_5  B値5_5
12   ON  グループC     NaN    NaN    NaN    NaN
13  OFF  C値1_5   C値2_5  C値3_5  C値4_5  C値5_5
14  OFF  C値1_5   C値2_5  C値3_5  C値4_5  C値5_5
15   ON  グループD     NaN    NaN    NaN    NaN
16   ON  D値1_1  D値2_1   D値3_1  D値4_1  D値5_1
17   ON  D値1_2   D値2_2  D値3_2  D値4_2  D値5_2
18  OFF  D値1_3   D値2_3  D値3_3  D値4_3  D値5_3



---作成したデータ--
   SW   グループ     列1      列2     列3     列4     列5
0  ON  グループA  A値1_1  A値2_1   A値3_1  A値4_1  A値5_1
1  ON  グループA  A値1_2   A値2_2  A値3_2  A値4_2  A値5_2
2  ON  グループB  B値1_1  B値2_1   B値3_1  B値4_1  B値5_1
3  ON  グループB  B値1_5   B値2_5  B値3_5  B値4_5  B値5_5
4  ON  グループD  D値1_1  D値2_1   D値3_1  D値4_1  D値5_1
5  ON  グループD  D値1_2   D値2_2  D値3_2  D値4_2  D値5_2
```