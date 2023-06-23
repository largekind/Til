---
title: "Tkinter"
date: 2023-06-12T23:14:34+09:00
categories: ["Python"]
tags: ["Python", "GUI", "API"]
---
# Tkinter

## 概要

Python標準で入っているGUIを作成するためのライブラリ

## 使用法

主に以下の流れで作成
1. Tkクラスを用いてメインウィンドウを作成
2. ウィジェット(ボタンやラベルなど操作できる部品)をウィンドウに追加
3. イベントループを開始

まとめると、以下のようなコードとなる。

``` python
import tkinter as tk

# メインウィンドウの作成
window = tk.Tk()

# ラベルウィジェットの作成と配置
label = tk.Label(window, text="Hello, Tkinter")
label.pack()

# イベントループの開始
window.mainloop()

```