---
title: "正規表現のリストから情報を抽出し辞書に格納する方法"
date: 2023-04-16T21:39:39+09:00
tags: [Python, Regax]
categories: Python
---

# 正規表現のリストから情報を抽出し辞書に格納する方法

## 概要

グループで別れた各情報を辞書でまとめて取得する方法を記載する
これを行えば、複数の情報が入ったデータを抽出し、データ化が可能となる

## コード

ChatGPTから聞いたもの。動作確認済みなので処理は問題ないはず

``` Python
# reモジュールをインポート
import re

# ファイル名を定義
filename = '10.0m_SWON_A-B_124.31ms.csv'

# マッチングパターンをリスト形式で定義。
# パターン毎にキャプチャグループにラベルを付けています。
patternList = [
    r'(?P<Mator>\d+\.\d+|\d+)\s*m',  # m単位の数値部分
    r'(?P<Sec>\d+\.\d+|\d+)\s*ms',  # ms単位の数値部分
    r'(?P<GroupA>[A-Z]+)-(?P<GroupB>[A-Z]+)',  # ハイフン区切りの大文字英字2文字
    r'SW(?P<SW>ON|OFF)'  # SWONまたはSWOFF
]

# パターン毎にマッチングを試み、マッチしたものをmatchListに格納する。
matchList = []
for pattern in patternList:
    match = re.search(pattern, filename)
    if match:
        matchList.append(match.groupdict())

# matchListがある場合は、辞書オブジェクトにまとめてresultに格納する。
# まとめて格納することで、各キャプチャグループ毎に異なるリストに格納せずに済む。
# resultを出力することで、マッチング結果が辞書オブジェクトとして得られる。
if matchList:
    result = {key: value for match in matchList for key, value in match.items()}
    print(result)
else:
    #もし正規表現に合致しないパターンがある場合はNoneを入れる 必要なければelse以降を削除すればよい
    for group in re.findall('\(\?P\<(\w+)\>', pattern):
        result[group] = None
    print("No match")
```