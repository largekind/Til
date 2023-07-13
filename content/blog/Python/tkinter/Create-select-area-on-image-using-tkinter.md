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
from tkinter import filedialog, Tk, Button, Canvas, Label, StringVar
import json
from PIL import Image, ImageTk
import os
import glob
import struct

MAX_HEIGHT = 600
MAX_WIDTH = 1200

class Model:
    def __init__(self):
        # 初期化処理
        self.files = []
        self.current_index = 0
        self.annotations = {}
        self.original_height = 0
        self.original_width = 0
        self.photo = None

    def select_files(self):
        # ダイアログから画像ファイルを選択
        root = Tk()
        root.withdraw()
        dir_path = filedialog.askdirectory()
        self.files = glob.glob(os.path.join(dir_path, "*.bin"))

    def read_image(self, file_path):
        # ファイルをバイナリとして読み込む
        with open(file_path, 'rb') as f:
            # 先頭の32bitから画像の高さと幅を取得
            width = struct.unpack('H', f.read(2))[0]
            height = struct.unpack('H', f.read(2))[0]
            # 残りのデータを8ビットの画素データとして読み込む
            data = np.fromfile(f, dtype=np.uint16)

        # データを2Dのndarrayに変換
        image = data.reshape((height, width))
        return image

    def load_annotations(self):
        # アノテーション情報をJSON形式で読み込む
        try:
            with open('annotations.json', 'r') as f:
                self.annotations = json.load(f)
        except FileNotFoundError:
            self.annotations = {}

    def save_annotations(self):
        # アノテーション情報をJSON形式で保存
        with open('annotations.json', 'w') as f:
            json.dump(self.annotations, f)

class View:
    def __init__(self, controller):
        # 初期化処理
        self.controller = controller
        self.root = Tk()

        # ファイル選択ボタンの作成
        Button(self.root, text="Select Files", command=self.controller.select_files).pack(side="top")

        # ラベルの作成
        self.file_info = StringVar()
        self.file_info.set('No file selected')
        Label(self.root, textvariable=self.file_info).pack(side="top")

        # 矩形領域の座標表示ラベル
        self.rect_info = StringVar()
        Label(self.root, textvariable=self.rect_info).pack()

        # Canvasウィジェットの作成
        self.canvas = Canvas(self.root, width=MAX_WIDTH, height=MAX_HEIGHT)
        self.canvas.pack()


        # 前/次ボタンの作成
        self.next_button = Button(self.root, text="Next", command=self.controller.next_image, state='disabled')
        self.next_button.pack(side="bottom")
        self.prev_button = Button(self.root, text="Previous", command=self.controller.previous_image, state='disabled')
        self.prev_button.pack(side="bottom")

        # マウスイベントのバインド
        self.canvas.bind("<Button-1>", self.controller.start_rectangle)
        self.canvas.bind("<B1-Motion>", self.controller.draw_rectangle)
        self.canvas.bind("<ButtonRelease-1>", self.controller.end_rectangle)

    def enable_buttons(self):
        # 前/次ボタンを有効化
        self.next_button.config(state='normal')
        self.prev_button.config(state='normal')

    def show_image(self, image, original_height, original_width):
      # 画像のリサイズ（アスペクト比を保つ）
      screen_width = self.root.winfo_screenwidth()
      screen_height = self.root.winfo_screenheight()
      new_width = screen_width
      new_height = int(new_width * original_height / original_width)
      if new_height > screen_height:
          new_height = screen_height
          new_width = int(new_height * original_width / original_height)
      image = cv2.resize(image, (new_width, new_height))

      # 画像をTkinterのPhotoImage形式に変換
      image = Image.fromarray(image)
      self.photo = ImageTk.PhotoImage(image)

      # Canvas上に画像を表示
      self.canvas.config(width=new_width, height=new_height)  # Canvasのサイズを画像に合わせる
      self.canvas.create_image(0, 0, image=self.photo, anchor='nw')
      self.canvas.image = self.photo  # 参照を保持して画像が消えないようにする

    def draw_annotation(self, annotation, original_height, original_width):
        # アノテーションを描画
        x1, y1, x2, y2 = annotation
        x1 = int(x1 * MAX_WIDTH / original_width)
        y1 = int(y1 * MAX_HEIGHT / original_height)
        x2 = int(x2 * MAX_WIDTH / original_width)
        y2 = int(y2 * MAX_HEIGHT / original_height)
        if hasattr(self.canvas, 'rectangle'):
            self.canvas.delete(self.canvas.rectangle)
        self.canvas.rectangle = self.canvas.create_rectangle(x1, y1, x2, y2)

class Controller:
    def __init__(self):
        # 初期化処理
        self.model = Model()
        self.view = View(self)

    def select_files(self):
        # ファイル選択処理
        self.model.select_files()
        self.model.load_annotations()
        self.view.enable_buttons()
        self.show_image()

    def next_image(self):
        # 次の画像を表示
        self.model.current_index += 1
        self.model.current_index = self.model.current_index % len(self.model.files)  # リストの範囲内に保つ
        self.show_image()

    def previous_image(self):
        # 前の画像を表示
        self.model.current_index -= 1
        self.model.current_index = self.model.current_index % len(self.model.files)  # リストの範囲内に保つ
        self.show_image()

    def show_image(self):
        # 画像を読み込んで表示する
        file_path = self.model.files[self.model.current_index]
        image = self.model.read_image(file_path)
        original_height, original_width = image.shape
        self.view.show_image(image, original_height, original_width)
        self.view.file_info.set(f'File: {file_path}\nSize: {original_width}x{original_height}')
        if file_path in self.model.annotations:
            self.view.draw_annotation(self.model.annotations[file_path], original_height, original_width)

    def start_rectangle(self, event):
        # 矩形領域の開始点を記録
        self.view.canvas.start_x = event.x
        self.view.canvas.start_y = event.y

        # 新しい矩形領域を作成
        if hasattr(self.view.canvas, 'rectangle'):
            self.view.canvas.delete(self.view.canvas.rectangle)
        self.view.canvas.rectangle = self.view.canvas.create_rectangle(event.x, event.y, event.x, event.y)

    def draw_rectangle(self, event):
        # 矩形領域の大きさを更新
        self.view.canvas.coords(self.view.canvas.rectangle, self.view.canvas.start_x, self.view.canvas.start_y, event.x, event.y)

    def end_rectangle(self, event):
        # 矩形領域の終点を記録
        self.view.canvas.end_x = event.x
        self.view.canvas.end_y = event.y

        # アノテーション情報の保存
        image = self.model.read_image(self.model.files[self.model.current_index])
        original_height, original_width = image.shape
        x1 = self.view.canvas.start_x * original_width / MAX_WIDTH
        y1 = self.view.canvas.start_y * original_height / MAX_HEIGHT
        x2 = self.view.canvas.end_x * original_width / MAX_WIDTH
        y2 = self.view.canvas.end_y * original_height / MAX_HEIGHT
        annotations = [x1, y1, x2, y2]
        self.model.annotations[self.model.files[self.model.current_index]] = annotations
        self.model.save_annotations()

        # 選択した矩形領域の座標を表示
        self.view.rect_info.set(f'Rectangle: {x1:.2f},{y1:.2f} to {x2:.2f},{y2:.2f}')

if __name__=='__main__':
    controller = Controller()
    controller.view.root.mainloop()


```

上記を用いて学習するコードは以下

``` python
import torch
from torch import nn
from torchvision import models, transforms
from torch.utils.data import Dataset, DataLoader
import numpy as np
from PIL import Image
import json

# データセットの定義
class MyDataset(Dataset):
    def __init__(self, image_paths, annotations):
        self.image_paths = image_paths
        self.annotations = annotations

        # 画像の前処理を定義
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),  # MobileNetV2の入力サイズに合わせる
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),  # ImageNetの平均・標準偏差で正規化
        ])

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        image_path = self.image_paths[idx]
        annotation = self.annotations[idx]

        # 画像を読み込み、前処理を行う
        image = read_image(image_path)
        original_height, original_width = image.shape
        image = image * 255
        image = image.astype(np.uint8)
        image = np.stack([image, image, image], axis=-1)
        image = Image.fromarray(image)
        image = self.transform(image)

        # アノテーションの座標を正規化
        annotation = {
            'x1': annotation['x1'] / original_width,
            'y1': annotation['y1'] / original_height,
            'x2': annotation['x2'] / original_width,
            'y2': annotation['y2'] / original_height,
        }

        return image, annotation

# 学習済みMobileNetV2モデルの読み込み
model = models.mobilenet_v2(pretrained=True)

# 特徴抽出部分のパラメータをフリーズ（勾配計算しないように設定）
for param in model.features.parameters():
    param.requires_grad = False

# 分類部分を新たに定義
model.classifier = nn.Sequential(
    nn.Linear(in_features=1280, out_features=512),  # MobileNetV2の出力サイズが1280
    nn.ReLU(),
    nn.Dropout(0.2),
    nn.Linear(in_features=512, out_features=4),  # 出力サイズを4（矩形領域のx1, y1, x2, y2）にする
    nn.Sigmoid(),  # 出力を0から1の範囲にする
)

# 学習設定
criterion = nn.MSELoss()  # 回帰問題なので、損失関数は平均二乗誤差（MSE）を使用
optimizer = torch.optim.Adam(model.classifier.parameters())  # オプティマイザはAdamを使用

# データセット・データローダの作成（image_pathsとannotationsは適切なリストを使用）
dataset = MyDataset(image_paths, annotations)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

# 学習ループ
for epoch in range(100):  # エポック数は適宜調整
    for images, labels in dataloader:
        outputs = model(images)
        loss = criterion(outputs, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print(f'Epoch {epoch + 1}, Loss: {loss.item()}')

```

学習したモデルを用いた推論は以下

``` python
def predict(image_path, model):
    # 画像の読み込みと前処理
    image = read_image(image_path)
    original_height, original_width = image.shape
    image = image * 255
    image = image.astype(np.uint8)
    image = np.stack([image, image, image], axis=-1)
    image = Image.fromarray(image)
    transform = transforms.Compose([
        transforms.Resize((224, 224)),  # MobileNetV2の入力サイズに合わせる
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),  # ImageNetの平均・標準偏差で正規化
    ])
    image = transform(image)
    image = image.unsqueeze(0)  # バッチ次元の追加

    # 推論
    model.eval()  # モデルを評価モードに設定
    with torch.no_grad():
        outputs = model(image)
    
    # 出力を元の画像のサイズにスケールアップ
    outputs = outputs.squeeze(0)  # バッチ次元の削除
    outputs = {
        'x1': int(outputs[0].item() * original_width),
        'y1': int(outputs[1].item() * original_height),
        'x2': int(outputs[2].item() * original_width),
        'y2': int(outputs[3].item() * original_height),
    }

    return outputs
```

``` python
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 直接表示
def display_prediction(image_path, prediction):
    # 画像の読み込みとリサイズ
    image = read_image(image_path)
    image = image * 255
    image = image.astype(np.uint8)
    image = np.stack([image, image, image], axis=-1)
    image = Image.fromarray(image)
    image = image.resize((600, 1200))  # リサイズ

    # 予測された矩形領域の座標をリサイズに合わせてスケーリング
    scale_x, scale_y = 600 / original_width, 1200 / original_height
    prediction = {
        'x1': int(prediction['x1'] * scale_x),
        'y1': int(prediction['y1'] * scale_y),
        'x2': int(prediction['x2'] * scale_x),
        'y2': int(prediction['y2'] * scale_y),
    }

    # 予測された矩形領域を画像に描画
    fig, ax = plt.subplots(1)
    ax.imshow(image)
    rect = patches.Rectangle((prediction['x1'], prediction['y1']), prediction['x2'] - prediction['x1'], prediction['y2'] - prediction['y1'], linewidth=2, edgecolor='r', facecolor='none')
    ax.add_patch(rect)

    plt.show()

# 保存する場合
def save_prediction(image_path, prediction, save_path):
    # 画像の読み込みとリサイズ
    image = read_image(image_path)
    image = image * 255
    image = image.astype(np.uint8)
    image = np.stack([image, image, image], axis=-1)
    image = Image.fromarray(image)
    image = image.resize((600, 1200))  # リサイズ

    # 予測された矩形領域の座標をリサイズに合わせてスケーリング
    scale_x, scale_y = 600 / original_width, 1200 / original_height
    prediction = {
        'x1': int(prediction['x1'] * scale_x),
        'y1': int(prediction['y1'] * scale_y),
        'x2': int(prediction['x2'] * scale_x),
        'y2': int(prediction['y2'] * scale_y),
    }

    # 予測された矩形領域を画像に描画
    fig, ax = plt.subplots(1)
    ax.imshow(image)
    rect = patches.Rectangle((prediction['x1'], prediction['y1']), prediction['x2'] - prediction['x1'], prediction['y2'] - prediction['y1'], linewidth=2, edgecolor='r', facecolor='none')
    ax.add_patch(rect)

    # 画像の保存
    plt.savefig(save_path)
    plt.close(fig)  # フィギュアをクローズ


```


``` python
# 推論
image_path = 'path_to_your_image'
prediction = predict(image_path, model)

# 矩形領域の描画と表示
display_prediction(image_path, prediction)

```
