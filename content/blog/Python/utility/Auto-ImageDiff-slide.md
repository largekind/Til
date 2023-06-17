---
title: "画像比較用のスライド自動作成方法"
date: 2023-06-16T23:46:59+09:00
categories : ["Python"]
tags : ["Python"]
draft : true
---

# 画像比較用のスライド自動作成方法

## 概要

何らかの理由で同じ階層で構成されている２つのディレクトリ内にある画像を比較、
Powerpointにまとめたい場合の自動作成方法を記述する

## サンプルコード

python-pptxを使えばpowerPointを自動的に操作可能

以下のようなコードとなるが、コード未検証なので要検証

``` python
import os
from pptx import Presentation
from pptx.util import Inches, Pt

# 既存のプレゼンテーションを開く
prs = Presentation('template.pptx')

# ディレクトリ"A"と"B"のパス
dir_A = 'A'
dir_B = 'B'

# ディレクトリ"A"と"B"のサブディレクトリを取得
subdirs_A = sorted([d for d in os.listdir(dir_A) if os.path.isdir(os.path.join(dir_A, d))])
subdirs_B = sorted([d for d in os.listdir(dir_B) if os.path.isdir(os.path.join(dir_B, d))])

# スライドのサイズを取得
slide_width = prs.slide_width
slide_height = prs.slide_height

# 画像を配置するエリアの大きさを設定 (スライドサイズの80%を使用)
content_width = slide_width * 0.8
content_height = slide_height * 0.8

# 画像の配置を始める位置を設定 (スライドの中央に画像エリアがくるように調整)
start_left = (slide_width - content_width) / 2
start_top = (slide_height - content_height) / 2

# 各サブディレクトリに対応する画像をスライドに追加
for subdir_A, subdir_B in zip(subdirs_A, subdirs_B):
    # サブディレクトリ内の画像ファイルを取得
    images_A = sorted([f for f in os.listdir(os.path.join(dir_A, subdir_A)) if f.endswith('.png')])
    images_B = sorted([f for f in os.listdir(os.path.join(dir_B, subdir_B)) if f.endswith('.png')])

    # 画像が1枚だけの場合と複数枚の場合でレイアウトを変更
    if len(images_A) == 1 and len(images_B) == 1:
        # 画像が1枚だけの場合、横並びに配置
        layout = 'horizontal'
        num_images = 2
    else:
        # 画像が複数枚の場合、上下に配置
        layout = 'vertical'
        num_images = max(len(images_A), len(images_B))

    # 最初のスライドのレイアウトを新しいスライドのレイアウトとして使用
    slide_layout = prs.slide_layouts[0]  # レイアウトのインデックスは適切なものに変更してください
    slide = prs.slides.add_slide(slide_layout)

    # スライドに画像を追加
    for i in range(num_images):
        # 画像の位置とサイズを計算
        image_width = content_width / num_images
        image_height = content_height / (1 if layout == 'horizontal' else 2)
        left = start_left + image_width * i
        if layout == 'horizontal':
            top_A = start_top
            top_B = start_top + image_height
        else:
            top_A = start_top
            top_B = start_top

        # 画像をスライドに追加
        if i < len(images_A):
            img_A = images_A[i]
            slide.shapes.add_picture(os.path.join(dir_A, subdir_A, img_A), left, top_A, image_width, image_height)
        if i < len(images_B):
            img_B = images_B[i]
            slide.shapes.add_picture(os.path.join(dir_B, subdir_B, img_B), left, top_B, image_width, image_height)

# プレゼンテーションを保存
prs.save('output.pptx')


```

