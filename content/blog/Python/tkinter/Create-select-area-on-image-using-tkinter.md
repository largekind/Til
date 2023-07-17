---
title: "Create Select Area on Image Using Tkinter"
date: 2023-07-11T23:51:39+09:00
categories: ["Python"]
tags: ["Python", "tkinter"]
---
# Create Select Area on Image Using Tkinter

## 概要

画像のディレクトリを選んで、そこから矩形領域のアノテーションを作り保存したいための備忘録

## サンプルコード

クラス整理等はされてないので、また必要になったら行う。

``` python
import cv2
import numpy as np
from tkinter import filedialog, Tk, Button, Canvas, Label, StringVar
from tkinter import ttk
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
        self.image = None
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
        self.image = data.reshape((height, width))
        return self.image

    # WBおよびRGBの平均を計算
    def calculate_wb(self, annotation):
        # アノテーションから矩形領域を取得
        x1, y1, x2, y2 = map(int, annotation)
        region = self.image[y1:y2, x1:x2]

        # 各色チャンネルの平均値を取得
        r = np.mean(region[::2, ::2])  # R
        gr = np.mean(region[::2, 1::2])  # Gr
        gb = np.mean(region[1::2, ::2])  # Gb
        b = np.mean(region[1::2, 1::2])  # B

        # R:G:B = R':1:B' となる R' と B' を計算
        g = (gr + gb) / 2  # G
        r_ratio = g / r
        b_ratio = g / b

        return r, gr, gb, b, r_ratio, b_ratio

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
    def rearrange_array(self, array, new_order):
        # new_orderが2次元配列でなければエラーを返す
        if len(new_order.shape) != 2:
            raise ValueError("new_order must be a 2D array")

        # ブロックの高さと幅を取得
        block_height, block_width = new_order.shape

        # 入力配列の高さと幅を取得
        height, width = array.shape

        # 並び替え後の配列を格納するための配列を作成
        rearranged_array = np.empty_like(array)

        # 割り切れないことが分かっている場合は先に警告
        if (height % block_height != 0) or (width % block_width != 0):
            print(f"This image is not divisible by the specified ordinal array ({height},{width}) % ({block_height},{block_width}) = ({height % block_height}, {width % block_width})")

        # 入力配列をブロックごとに処理
        for i in range(0, height, block_height):
            for j in range(0, width, block_width):
                # ブロックを取得
                block = array[i:i+block_height, j:j+block_width]

                # ブロックの形状がnew_orderの形状と一致しない場合、new_orderを調整
                if block.shape != new_order.shape:
                    new_order_resized = new_order[:block.shape[0], :block.shape[1]].copy()
                    #print("new_order resize:",new_order_resized)
                    unique_elements = new_order_resized.flatten()
                    unique_elements.sort()
                    for idx, element in enumerate(unique_elements):
                        new_order_resized[new_order_resized == element] = idx
                else:
                    new_order_resized = new_order

                # ブロックの要素を新しい順序に並べ替え
                rearranged_block = block.flatten()[new_order_resized.flatten()]

                # 並べ替えたブロックを新しい配列に戻す
                rearranged_array[i:i+block_height, j:j+block_width] = rearranged_block.reshape(block.shape)

        return rearranged_array
    # bayerへの変換処理
    def rearrange_bayer(self, bayer_order):
        # ベイヤー配列の順番に基づいて画素の並び替えを行う処理
        if bayer_order == "Bayer":
            return
        elif bayer_order == "Quad":
            new_order = np.array([[0, 2, 1, 3], [8, 10, 9, 11], [4, 6, 5, 7], [12, 14, 13, 15]])
        else:
            raise ValueError("Invalid Bayer order")

        # 画像更新
        self.image = self.rearrange_array(self.image, new_order)


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

        # WB情報を表示する Label ウィジェットの作成
        self.wb_info = StringVar()
        Label(self.root, textvariable=self.wb_info, justify='left').pack(side="top")

        # Canvasウィジェットの作成
        self.canvas = Canvas(self.root, width=MAX_WIDTH, height=MAX_HEIGHT)
        self.canvas.pack()

        # ベイヤー配列の順番を選択するためのコンボボックスを作成
        self.bayer_order = StringVar()
        self.bayer_order.set("Bayer")  # デフォルト値を設定

        self.bayer_order_combobox = ttk.Combobox(self.root, values=["Bayer","Quad"], state='disabled', textvariable=self.bayer_order)
        self.bayer_order_combobox.pack()

        self.bayer_order.trace('w', self.bayer_order_changed)  # 選択が変更されたときにコールバック関数を呼び出す

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

    def scale_box(self, img, width, height):
        """指定した大きさに収まるように、アスペクト比を固定して、リサイズする。"""
        h, w = img.shape[:2]
        aspect = w / h
        if width / height >= aspect:
            nh = height
            nw = round(nh * aspect)
        else:
            nw = width
            nh = round(nw / aspect)

        dst = cv2.resize(img, dsize=(nw, nh))
        self.scale_w = nw / w
        self.scale_h = nh / h
        return dst


    def show_image(self, image):
      #コンボボックス有効化
      self.bayer_order_combobox.config(state= 'normal')
      # 画像のリサイズ（アスペクト比を保つ）
      image = self.scale_box(image, MAX_HEIGHT, MAX_WIDTH)

      # 画像をTkinterのPhotoImage形式に変換
      image = Image.fromarray(image)
      self.photo = ImageTk.PhotoImage(image)

      # Canvas上に画像を表示
      self.canvas.config(width=image.width, height=image.height)  # Canvasのサイズを画像に合わせる
      self.canvas.create_image(0, 0, image=self.photo, anchor='nw')
      self.canvas.image = self.photo  # 参照を保持して画像が消えないようにする

    def draw_annotation(self, annotation):
        # アノテーションを描画
        x1, y1, x2, y2 = annotation
        x1, x2 = sorted([int(x1 * self.scale_w), int(x2 * self.scale_w)])
        y1, y2 = sorted([int(y1 * self.scale_h), int(y2 * self.scale_h)])
        if hasattr(self.canvas, 'rectangle'):
            self.canvas.delete(self.canvas.rectangle)
        self.canvas.rectangle = self.canvas.create_rectangle(x1, y1, x2, y2)

    def bayer_order_changed(self, *args):
        # Viewから直接Modelのメソッドを呼び出す
        self.controller.model.rearrange_bayer(self.bayer_order.get())
        self.show_image(self.controller.model.image)

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
        self.view.show_image(image)
        self.view.file_info.set(f'File: {file_path}\nSize: {original_width}x{original_height}')
        if file_path in self.model.annotations:
            self.view.draw_annotation(self.model.annotations[file_path])
        self.model.rearrange_bayer(self.view.bayer_order.get())  # 新たな画像に対して並び替えを実行

    def start_rectangle(self, event):
        # 矩形領域の開始点を記録
        self.view.canvas.start_x = min(max(event.x, 0), self.view.canvas.winfo_width())
        self.view.canvas.start_y = min(max(event.y, 0), self.view.canvas.winfo_height())
        # 新しい矩形領域を作成
        if hasattr(self.view.canvas, 'rectangle'):
            self.view.canvas.delete(self.view.canvas.rectangle)
        self.view.canvas.rectangle = self.view.canvas.create_rectangle(event.x, event.y, event.x, event.y)

    def draw_rectangle(self, event):
        # 矩形領域の大きさを更新
        self.view.canvas.coords(self.view.canvas.rectangle, self.view.canvas.start_x, self.view.canvas.start_y, min(max(event.x, 0), self.view.canvas.winfo_width()), min(max(event.y, 0), self.view.canvas.winfo_height()))

    def end_rectangle(self, event):
        # 矩形領域の終点を記録
        self.view.canvas.end_x = min(max(event.x, 0), self.view.canvas.winfo_width())
        self.view.canvas.end_y = min(max(event.y, 0), self.view.canvas.winfo_height())
        # アノテーション情報の保存
        x1, x2 = sorted([self.view.canvas.start_x / self.view.scale_w, self.view.canvas.end_x / self.view.scale_w])
        y1, y2 = sorted([self.view.canvas.start_y / self.view.scale_h, self.view.canvas.end_y / self.view.scale_h])
        annotations = [int(x1), int(y1), int(x2), int(y2)]
        self.model.annotations[self.model.files[self.model.current_index]] = annotations
        self.model.save_annotations()

        # WB情報の表示
        r, gr, gb , b ,r_prime, b_prime = self.model.calculate_wb(annotations)
        self.view.wb_info.set(f'Avg RGB = (R: {r:.3f}, Gr: {gr:.3f}, Gb: {gb:.3f} , B: {b:.3f})\n WB RGB = (R: {r_prime:.2f} ,G : 1, B: {b_prime:.2f})')

    # 選択した矩形領域の座標を表示
        self.view.rect_info.set(f'Rectangle: {x1:.2f},{y1:.2f} to {x2:.2f},{y2:.2f}')

    # 画素配列入れ替えイベント
    def bayer_order_changed(self, *args):
        # コンボボックスで選択されたベイヤー配列の順番を取得
        bayer_order = self.view.bayer_order.get()
        file_path = self.model.files[self.model.current_index]

        # 並び替えた画像を取得
        image = self.model.rearrange_image(file_path, bayer_order)
        original_height, original_width = image.shape

        # 並び替えた画像を表示
        self.view.show_image(image, original_height, original_width)


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
        annotation = self.annotations[image_path]  # image_pathをキーとしてアノテーションを取得

        # 画像を読み込み、前処理を行う
        image = read_image(image_path)
        image = image * 255
        image = image.astype(np.uint8)
        image = np.stack([image, image, image], axis=-1)
        image = Image.fromarray(image)
        image = self.transform(image)

        return image, annotation

# アノテーション情報を読み込む
with open('annotations.json', 'r') as f:
    annotations = json.load(f)

# データセット・データローダの作成
image_paths = list(annotations.keys())  # アノテーション情報から画像パスを取得
dataset = MyDataset(image_paths, annotations)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

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
    nn.Identity()  # 出力をそのまま返す
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