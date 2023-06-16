---
title: "正規表現のリストを用いてディレクトリ化する方法"
date: 2023-05-17T00:39:34+09:00
tags: [Python, Regax, utility]
categories: [Python]
---

# 正規表現のリストから情報を抽出し辞書に格納する方法

## 概要

グループで別れた各情報からディレクトリを作成する方法

元ネタは[正規表現から辞書作成](RegaxList.md)の情報になる。

group(0)で取ることでグループにマッチした情報の全体情報が得られるので、その方法を用いれば可能となる

## サンプルコード

``` python
import re
import os
import pandas as pd

filename = '10.0m_SWON_A-B_124.31ms.csv'

pattern_list = [
    ('Aiueo', True),
    (r'(?P<Mator>\d+\.\d+|\d+)\s*m', False),
    (r'(?P<Sec>\d+\.\d+|\d+)\s*ms', False),
    (r'(?P<GroupA>[A-Z]+)-(?P<GroupB>[A-Z]+)', True),
    (r'SW(?P<SW>ON|OFF)', True),
]

match_list = []
dirname = "./"
for pattern, dir_enable in pattern_list:
    match = re.search(pattern, filename)
    if match:
        match_dict = match.groupdict()
        match_list.append(match_dict)
        if dir_enable:
            # ディレクトリ名を正規表現に従って作成
            match_str = match.group(0)
            dirname = os.path.join(dirname, match_str)
    else:
        for group in re.findall('\(\?P\<(\w+)\>', pattern):
            match_list.append({group: None})
        # ディレクトリのみ追加のパターン
        if dir_enable:
            dirname = os.path.join(dirname, pattern)

if match_list:
    result = {key: value for match in match_list for key, value in match.items()}
    print(pd.DataFrame([result]))
    print(dirname)

```

