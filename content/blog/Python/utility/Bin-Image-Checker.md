---
title: "バイナリのような画像を監視、表示するツール"
date: 2023-06-12T23:32:38+09:00
categories : ["Python"]
tags : ["Python","utility","Camera"]
---

# バイナリ画像監視ツール

## 概要

何らかの理由でバイナリで定義された画像(例:RAWデータ)をリアルタイムで監視したい時のためのツールを記載する

## 構造

通常のpython環境で使えるように、tkinterベースで作成

## コード全体

``` python
import os
import threading
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

# 監視対象のファイル形式
patterns = ["*.bin"]  # バイナリファイル

# バイナリデータからNumPy配列を作成する関数
def binary_to_np_array(binary_data):
    # バイナリデータの解析はバイナリデータの形式に依存
    # 以下は仮の処理として、バイナリデータをuint8型の一次元NumPy配列に変換し、それを100x100の2次元配列に変形する例
    np_array = np.frombuffer(binary_data, dtype=np.uint8).reshape((100, 100))
    return np_array

class ImageHandler(PatternMatchingEventHandler):
    def __init__(self, app, patterns):
        super().__init__(patterns=patterns)
        self.app = app

    def on_modified(self, event):
        # ファイルの変更があるたびに呼び出される
        # 対象ファイルをバイナリモードで開き、全データを読み込む
        with open(event.src_path, 'rb') as f:
            binary_data = f.read()
        # バイナリデータをNumPy配列に変換
        np_array = binary_to_np_array(binary_data)
        # GUIの画像表示を更新
        self.app.update_image(np_array)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # フォルダ選択ボタンの作成
        self.folder_btn = tk.Button(self)
        self.folder_btn["text"] = "監視するフォルダを選択"
        self.folder_btn["command"] = self.choose_folder
        self.folder_btn.pack(side="top")

        # 画像表示用のラベルの作成
        self.image_label = tk.Label(self)
        self.image_label.pack(side="top")

    def choose_folder(self):
        # フォルダ選択ボタンのクリック時に呼び出される
        # フォルダ選択ダイアログを表示
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            # フォルダが選択されたら、そのフォルダの監視を開始
            self.start_watching()

    def start_watching(self):
        # 監視を開始する処理
        # watchdogのObserverとイベントハンドラを作成し、監視をスタート
        event_handler = ImageHandler(self, patterns)
        self.observer = Observer()
        self.observer.schedule(event_handler, self.folder_path, recursive=True)
        self.observer.start()

    def update_image(self, np_array):
        # 画像表示を更新する処理
        # NumPy配列からPILのImageオブジェクトを作成し、それをtkinterのPhotoImageに変換
        image = Image.fromarray(np_array)
        photo = ImageTk.PhotoImage(image)
        # ラベルの画像を更新
        self.image_label.config(image=photo)
        # ラベルがPhotoImageオブジェクトを参照し続けるように、参照を保持
        self.image_label.image = photo

root = tk.Tk()
app = Application(master=root)

def on_close():
    # ウィンドウが閉じられる時に呼び出される
    # フォルダの監視を停止し、ウィンドウを閉じる
    if hasattr(app, 'observer'):
        app.observer.stop()
        app.observer.join()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)
app.mainloop()

```