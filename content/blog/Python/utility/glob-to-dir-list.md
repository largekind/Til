---
title: "ファイル群からディレクトリを抽出する"
date: 2023-06-22T21:15:57+09:00
categories: ["Python"]
tags: ["Python", "utility"]
---
# ファイル群からディレクトリの抽出する

## 概要

表題の通り。次のサンプルコードで実行可能

## サンプルコード

``` python
import os
import glob

# 'my_directory'内のテキストファイルを検索
txt_files = glob.glob('my_directory/**/*.txt', recursive=True)

# ファイルが存在するディレクトリを抽出
directories = {os.path.dirname(txt_file) for txt_file in txt_files}

# 結果を表示
for directory in directories:
    print(directory)
```