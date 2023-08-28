---
title: "基本的なAIモデルの処理作成の流れ"
date: 2023-08-27T22:12:02+09:00
categories: ["Python"]
tags: ["Python", "pytorch"]
---
# 基本的なAIモデルの処理作成の流れ

## 概要

毎回忘れてしまう、pytorchを用いた基本的なAI処理（画像分類）の作成の流れを列挙する

基本的には以下の流れである
1. データセットを定義
2. modelの定義
3. 学習処理の作成
4. 推論処理の作成

## データセットの定義

当然、学習するにはデータセットが必要なため、その定義方法を簡単にまとめる

構造が以下のようにクラスがディレクトリで分類されている場合はImageFolderで適用可能
``` tree
train
├─A
├─B
├─C
└─D
```

``` python
dataset = datasets.ImageFolder('Path')
```

その後、以下のようにデータ分割 今回であればtrain/val/testを0.7/0.15/0.15にした場合、以下のような感じ
``` python
# 訓練データ、検証データ、テストデータに分割
num_data = len(dataset)
train_size = int(0.7 * num_data)
val_size = int(0.15 * num_data)
test_size = num_data - train_size - val_size

train_dataset, val_dataset, test_dataset = random_split(dataset, [train_size, val_size, test_size])

# データローダの作成
train_loader = DataLoader(train_dataset, batch_size=batch_size)
val_loader = DataLoader(val_dataset, batch_size=batch_size)
test_loader = DataLoader(test_dataset, batch_size=batch_size)

```