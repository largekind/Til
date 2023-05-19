---
title: "Regax File Sorting"
date: 2023-05-19T22:08:01+09:00
categories : [""]
tags : ["",""]
draft: true
---

# Regax File Sorting

## 概要

正規表現でファイル名やディレクトリ名を抽出し、データをソートする仕組みを考える

## サンプルコード

``` python
import re
import os

def create_new_path(filepath, pattern_list):
    new_dir = []
    new_file = []
    filename = os.path.basename(filepath)
    directory = "."

    for pattern, is_file, is_dir in pattern_list:
        # check if the pattern is regex or not
        if "<" in pattern:
            # this is regex, we should match the pattern and extract the group
            match = re.search(pattern, filename)
            if match:
                # remove the matched part from the filename
                filename = filename.replace(match.group(), '', 1)
                if is_dir:
                    new_dir.append(match.group())
                if is_file:
                    new_file.append(match.group())
        else:
            # this is not regex, add the pattern to the new path as it is
            if is_dir:
                new_dir.append(pattern)
            if is_file:
                new_file.append(pattern)

    # join the new directory parts and the new filename parts with '/'
    new_dir_path = os.path.join(directory, *new_dir)
    new_file_path = '_'.join(new_file) + '.txt'

    print("New Directory Path:", new_dir_path)
    print("New Filename:", new_file_path)

filepaths = [
    "./folder/B101_C223_D554_E777-F888_SWON.txt",
    "./folder/A101_D554_E777-F888_SWOFF.txt",
    "./SWON/B101_C223_A554_G24testH33_SWON.txt",
]  
pattern_list = [
    ("aiueo", False, True),
    (r"(?P<A>A\d+)", True , True),
    (r"(?P<B>B\d+)", True , False),
    (r"(?P<C>C\d+)", False ,True),
    (r"(?P<D>D\d+)", True, False ),
    (r"(?P<E>E\d+)-(?P<F>F\d+)", True , True),
    (r"(?P<G>G\d+)test(?P<H>H\d+)", True, True),
    (r"(?P<SW>SW(?:ON|OFF))", True , False),
]

for path in filepaths:
    print(path)
    create_new_path(path, pattern_list)

```