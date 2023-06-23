---
title: "DirectoryDivide"
date: 2023-05-27T21:26:53+09:00
categories: ["Python"]
tags: ["Python", "utility"]
---
# ディレクトリごとでのファイル分割方法

## 概要

特定の抽出したパスをディレクトリごとに分割してリストで保持する方法を記載する

## 方法

辞書を用いて、ディレクトリごとにキーを作成し分割させる。

以下サンプルコードである

``` python
import glob

csv_paths = glob.glob("./test_directory/**/*.csv",recursive=True)

# ディレクトリごとに分割
csv_paths_per_directory = defaultdict(list)
for path in csv_paths:
    directory = os.path.dirname(path)  # ディレクトリ名を抽出
    csv_paths_per_directory[directory].append(path)

# 結果の表示
for directory, paths in csv_paths_per_directory.items():
    print(f"Directory: {directory}")
    print(f"Paths: {paths}")
```