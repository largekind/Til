---
title: "Tqdm Copytree"
date: 2023-12-29T10:33:13+09:00
categories: ["Python"]
tags: ["Python", "utility"]
---
# Tqdm Copytree

## 概要

進捗表示させながら再帰的にコピーする仕組みを記載する

## コード

``` python
import os
import shutil
from tqdm import tqdm

def get_file_list(src, ignore=None):
    """ ソースディレクトリ内のファイルリストを生成する """
    file_list = []
    for root, dirs, files in os.walk(src):
        if ignore is not None:
            ignored = ignore(root, files)
            files = [f for f in files if f not in ignored]
        file_list.extend(os.path.join(root, file) for file in files)
    return file_list

def copy_with_progress(src, dst, file_list):
    """ ファイルをコピーしながら進捗を表示する """
    for file in tqdm(file_list, desc="Copying files", unit="file"):
        dst_file = os.path.join(dst, os.path.relpath(file, src))
        os.makedirs(os.path.dirname(dst_file), exist_ok=True)
        shutil.copy2(file, dst_file)

def copytree_with_progress(src, dst, ignore=None):
    """ コピー関数、進捗を表示しながらディレクトリをコピーする """
    file_list = get_file_list(src, ignore)
    copy_with_progress(src, dst, file_list)

# コピー元とコピー先のパス
source_path = 'path/to/source'
destination_path = 'path/to/destination'

# ignoreパターン（例：tmpファイルとlogファイルを無視）
ignore_patterns = shutil.ignore_patterns('*.tmp', '*.log')

# コピー処理を実行
copytree_with_progress(source_path, destination_path, ignore=ignore_patterns)
```