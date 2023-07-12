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
