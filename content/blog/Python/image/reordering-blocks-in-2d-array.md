---
title: "Reordering Blocks in 2d Array"
date: 2023-07-03T22:01:10+09:00
categories: ["Python"]
tags: ["Python", "image"]
---
# Reordering Blocks in 2d Array

## 概要

このTILでは、2次元配列をNxMのブロックに分割し、各ブロック内の要素の順序を任意に入れ替える方法を記述する。

この方法は、画像処理におけるピクセルの並び替えや、特定のパターンに基づくデータの並び替えなど、様々な場面で利用可能。

## サンプルコード

```python
import numpy as np

def rearrange_array(array, new_order):
    # new_orderが2次元配列でなければエラーを返す
    if len(new_order.shape) != 2:
        raise ValueError("new_order must be a 2D array")

    # ブロックの高さと幅を取得
    block_height, block_width = new_order.shape

    # new_orderの最大値がブロックの要素数を超えていないことを確認
    if new_order.max() >= block_height * block_width:
        raise ValueError(f"new_order {new_order.max()} contains an index that is out of bounds for the block size({block_height},{block_width}) = {block_height*block_width}")
    # 入力配列の高さと幅を取得
    height, width = array.shape

    # 並び替え後の配列を格納するための配列を作成
    rearranged_array = np.empty_like(array)

    # 入力配列をブロックごとに処理
    for i in range(0, height, block_height):
        for j in range(0, width, block_width):
            # ブロックを取得
            block = array[i:min(i+block_height, height), j:min(j+block_width, width)].flatten()

            # ブロックの要素を新しい順序に並べ替え
            rearranged_block = block[new_order.flatten()[:block.size]]

            # 並べ替えたブロックを新しい配列に戻す
            rearranged_array[i:min(i+block_height, height), j:min(j+block_width, width)] = rearranged_block.reshape((min(block_height, height-i), min(block_width, width-j)))

    return rearranged_array
```

## 使用例

```python
# 入力配列
array = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])

# 新しい順序
new_order = np.array([[0, 2, 1, 3], [8, 10, 9, 11], [4, 6, 5, 7], [12, 14, 13, 15]])

# 配列を並び替え
rearranged_array = rearrange_array(array, new_order)

print(rearranged_array)
```