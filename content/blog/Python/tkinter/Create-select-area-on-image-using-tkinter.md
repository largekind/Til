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
``` python
import cv2
import numpy as np
from tkinter import filedialog, Tk, Button, Canvas
import json
from PIL import Image, ImageTk

MAX_HEIGHT = 600
MAX_WIDTH = 1200

# ダイアログから画像ファイルを選択
def select_files():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilenames()
    return file_path

# 2d ndarrayで画像を読み込む独自関数
def read_image(file_path):
    # 画像読み込み処理を記述
    # ここでは一時的にランダムな配列を生成しています
    image = np.random.rand(1024, 1024)
    return image

# 画像を表示するための関数
def show_image(image):
    # 画像のリサイズ（アスペクト比を保つ）
    height, width = image.shape
    new_height = MAX_HEIGHT
    new_width = int(new_height * width / height)
    if new_width > MAX_WIDTH:
        new_width = MAX_WIDTH
        new_height = int(new_width * height / width)
    image = cv2.resize(image, (new_width, new_height))

    # 画像をTkinterのPhotoImage形式に変換
    image = Image.fromarray(image)
    photo = ImageTk.PhotoImage(image)

    # Canvas上に画像を表示
    canvas.create_image(0, 0, image=photo, anchor='nw')
    canvas.image = photo  # 参照を保持して画像が消えないようにする

def save_annotation(file_path, annotations):
    # アノテーション情報をJSON形式で保存
    with open(f'{file_path}_annotation.json', 'w') as f:
        json.dump(annotations, f)

def next_image():
    global current_index, files
    current_index += 1
    current_index = current_index % len(files)  # リストの範囲内に保つ

    # 新しい画像を表示
    show_image(read_image(files[current_index]))

def previous_image():
    global current_index, files
    current_index -= 1
    current_index = current_index % len(files)  # リストの範囲内に保つ

    # 新しい画像を表示
    show_image(read_image(files[current_index]))

def start_rectangle(event):
    # 矩形領域の開始点を記録
    canvas.start_x = event.x
    canvas.start_y = event.y

    # 新しい矩形領域を作成
    canvas.rectangle = canvas.create_rectangle(event.x, event.y, event.x, event.y)

def draw_rectangle(event):
    # 矩形領域の大きさを更新
    canvas.coords(canvas.rectangle, canvas.start_x, canvas.start_y, event.x, event.y)

def end_rectangle(event):
    # 矩形領域の終点を記録
    canvas.end_x = event.x
    canvas.end_y = event.y

    # アノテーション情報の保存
    annotations = {'x1': canvas.start_x, 'y1': canvas.start_y, 'x2': canvas.end_x, 'y2': canvas.end_y}
    save_annotation(files[current_index], annotations)

if __name__=='__main__':
    # ファイル選択
    files = select_files()
    current_index = 0

    # Tkinterウィンドウの作成
    root = Tk()

    # 前/次ボタンの作成
    Button(root, text="Next", command=next_image).pack(side="right")
    Button(root, text="Previous", command=previous_image).pack(side="right")

    # Canvasウィジェットの作成
    canvas = Canvas(root, width=MAX_WIDTH, height=MAX_HEIGHT)
    canvas.pack()

    # マウスイベントのバインド
    canvas.bind("<Button-1>", start_rectangle)
    canvas.bind("<B1-Motion>", draw_rectangle)
    canvas.bind("<ButtonRelease-1>", end_rectangle)

    # 初期画像の表示
    show_image(read_image(files[current_index]))

    # イベントループ開始
    root.mainloop()

```