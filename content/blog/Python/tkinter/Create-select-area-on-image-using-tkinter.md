---
title: "Create Select Area on Image Using Tkinter"
date: 2023-07-11T23:51:39+09:00
draft: True
categories: ["Python"]
tags: ["Python", "tkinter"]
---
# Create Select Area on Image Using Tkinter

## 概要

画像のディレクトリを選んで、そこから矩形領域のアノテーションを作り保存したいための備忘録

## サンプルコード

工事中

```
import cv2
import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import json

# グローバル変数
image = None
start_x = None
start_y = None
end_x = None
end_y = None
image_path = None
image_index = 0
image_paths = []

def select_directory():
    global image_paths, image_index

    # ファイルダイアログを開き、ディレクトリを選択
    dirpath = filedialog.askdirectory()

    # ディレクトリ内の全ての画像ファイルのパスを取得
    image_paths = [os.path.join(dirpath, f) for f in os.listdir(dirpath) if f.endswith(('.png', '.jpg', '.jpeg'))]

    # 最初の画像を表示
    image_index = 0
    load_image()

def load_image():
    global image, image_path

    # 画像ファイルのパスを取得
    image_path = image_paths[image_index]

    # OpenCVを使用して画像を読み込む
    image = cv2.imread(image_path)

    # 画像をBGRからRGBに変換
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 画像をPIL形式に変換
    image_pil = Image.fromarray(image)

    # 画像をTkinter形式に変換
    image_tk = ImageTk.PhotoImage(image_pil)

    # 画像を表示
    image_label.config(image=image_tk)
    image_label.image = image_tk

def on_mouse_down(event):
    global start_x, start_y

    # 開始座標を記録
    start_x = event.x
    start_y = event.y

def on_mouse_up(event):
    global end_x, end_y, image

    # 終了座標を記録
    end_x = event.x
    end_y = event.y

    # 座標を出力
    print(f"開始: ({start_x}, {start_y}), 終了: ({end_x}, {end_y})")

    # 選択した領域を画像上に表示
    image_with_rectangle = cv2.rectangle(image.copy(), (start_x, start_y), (end_x, end_y), (255, 0, 0), 2)
    image_pil = Image.fromarray(image_with_rectangle)
    image_tk = ImageTk.PhotoImage(image_pil)
    image_label.config(image=image_tk)
    image_label.image = image_tk

def save_coordinates():
    global image_path, start_x, start_y, end_x, end_y

    # 座標を保存
    coordinates = {
        'start_x': start_x,
        'start_y': start_y,
        'end_x': end_x,
        'end_y': end_y
    }
    with open(f'{image_path}_coordinates.json', 'w') as f:
        json.dump(coordinates, f)

    # 次の画像を表示
    next_image()

def next_image():
    global image_index

    # 次の画像のインデックスを計算
    image_index = (image_index + 1) % len(image_paths)

    # 次の画像を表示
    load_image()

# Tkinterウィンドウを作成
window = tk.Tk()

# 画像を表示するラベルを作成
image_label = tk.Label(window)
image_label.pack()

# ディレクトリを選択するボタンを作成
select_button = tk.Button(window, text="ディレクトリを選択", command=select_directory)
select_button.pack()

# 座標を保存するボタンを作成
save_button = tk.Button(window, text="座標を保存", command=save_coordinates)
save_button.pack()

# マウスイベントを画像ラベルにバインド
image_label.bind("<Button-1>", on_mouse_down)
image_label.bind("<ButtonRelease-1>", on_mouse_up)

# Tkinterのイベントループを開始
window.mainloop()

```