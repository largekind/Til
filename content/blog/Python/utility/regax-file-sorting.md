---
title: "Regax File Sorting"
date: 2023-05-19T22:08:01+09:00
categories: ["Python"]
tags: ["utility", "Python"]
---
# Regax File Sorting

## 概要

正規表現でファイル名やディレクトリ名を抽出し、データをソートする仕組みを考える

ついでにDataFrame化するパターンも記載する

## サンプルコード

``` python
import pandas as pd
import os , re
def create_new_path(filepath, pattern_list):
    new_dir = []  # 新しいディレクトリ名を格納するリスト
    new_file = []  # 新しいファイル名を格納するリスト
    filename, file_extension = os.path.splitext(os.path.basename(filepath))  # 入力ファイル名と拡張子を取得
    directory = "."  # ディレクトリの初期値を設定

    for pattern, is_file, is_dir in pattern_list:
        # パターンが正規表現かどうかを確認
        if "<" in pattern:
            # 正規表現の場合、パターンに一致する部分を抽出
            match = re.search(pattern, filename, re.I)
            if match:
                # 一致した部分をファイル名から削除
                filename = filename.replace(match.group(), '', 1)
                # ディレクトリとして追加
                if is_dir:
                    new_dir.append(match.group())
                # ファイル名として追加
                if is_file:
                    new_file.append(match.group())
        else:
            # 正規表現でない場合、そのまま新しいパスに追加
            if is_dir:
                new_dir.append(pattern)
            if is_file:
                new_file.append(pattern)

    # 新しいディレクトリとファイル名を作成
    new_dir_path = os.path.join(directory, *new_dir)
    new_file_path = '_'.join(new_file) + file_extension

    print("新しいディレクトリのパス:", new_dir_path)
    print("新しいファイル名:", new_file_path)
    print("コピー先 : ", os.path.join(new_dir_path,new_file_path))
    


def create_dataframe_from_path(filepath, pattern_list):
    data_list = []  # すべての辞書を格納するリスト
    for path in filepath:
        data_dict = {}  # 1つのファイルの情報を格納する辞書
        filename = path

        for pattern, is_file, is_dir in pattern_list:
            if "<" in pattern:
                match = re.search(pattern, filename,re.I)
                if match:
                    filename = filename.replace(match.group(), '', 1)
                    # ここではパターンをディレクトリやファイル名に追加するだけでなく、辞書にも保存する
                    for key, value in match.groupdict().items():
                        data_dict[key] = value
        # パス情報を追加
        data_dict['Path'] = path
        # 1つのファイルに対してすべてのパターンをチェックした後、辞書をリストに追加
        data_list.append(data_dict)

    # 辞書のリストからデータフレームを作成
    df = pd.DataFrame(data_list)

    return df

# 関数のテスト
filepaths = [
    "./folder/B101_C223_D554_E777-F888_SWON.txt",
    "./folder/A101_D554_E777-F888_SWOFF.txt",
    "./SWON/b101_C223_A554_G24testH33.bin",
    "./SwON/B101_C223_A554_G24testH33.txt",
]  

pattern_list = [
    ("aiueo", False, True),  # 'aiueo' をディレクトリに追加
    (r"(?P<A>A\d+)", True , True),  # 'A' と数字をファイル名とディレクトリの両方に追加
    (r"(?P<B>B\d+)", True , False),  # 'B' と数字をファイル名に追加
    (r"(?P<C>C\d+)", False ,True),  # 'C' と数字をディレクトリに追加
    (r"(?P<D>D\d+)", True, False ),  # 'D' と数字をファイル名に追加
    (r"(?P<E>E\d+)-(?P<F>F\d+)", True , True),  # 'E' と数字、'F' と数字をファイル名とディレクトリの両方に追加
    (r"(?P<G>G\d+)test(?P<H>H\d+)", True, True),  # 'G' と数字、'H' と数字をファイル名とディレクトリの両方に追加
    (r"SW(?P<SW>(?:ON|OFF))", True , False),  # 'ON' または 'OFF' をファイル名に追加
]
# データフレームを作成して確認
df = create_dataframe_from_path(filepaths, pattern_list)
print(df)
# 新しいパスを作成して確認
for path in filepaths:
    print(path)
    create_new_path(path, pattern_list)
    print()

```