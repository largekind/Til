---
title: "モデルの使用テンソル型の修正方法"
date: 2023-04-05T00:00:00+09:00
tags: [Python,pytorch]
---
# モデルの使用テンソル型の修正方法

## 概要

以下のようなエラーが出てしまい、モデルのテンソルを変更したいときの方法を記載する

> RuntimeError: Input type (torch.cuda.DoubleTensor) and weight type (torch.cuda.FloatTensor) should be the same

## 対策

``` python
from torch import cuda
from model import Model #自作の何かしらの学習モデル

# GPU設定
device = 'cuda' if cuda.is_available() else 'cpu'
# Model()の後にメソッドチェーンで変換したい型へ変換してからGPU/CPUへ転送
model = Model().double().to(device)
```

