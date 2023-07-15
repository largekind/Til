---
title: "Create_comboBox"
date: 2023-07-14T23:16:32+09:00
categories: ["Python"]
tags: ["Python", "tkinter"]
---
# Create_comboBox

## 概要

tkinter上でコンボボックスを作る方法を記述する。
ついで、コンボボックスが選ばれたときにイベントを発行する処理も追記

## サンプルコード

``` python
import tkinter as tk
from tkinter import ttk
# 初期化処理
root = Tk()

# コンボボックスを作成
valstr = StringVar()
valstr.set("Hoge")  # デフォルト値を設定

combobox = ttk.Combobox(root, values=["Hoge","Fuga"], state='normal', textvariable=valstr)
combobox.pack()

valstr.trace('w', event_combox)  # 選択が変更されたときにコールバック関数を呼び出す
```
