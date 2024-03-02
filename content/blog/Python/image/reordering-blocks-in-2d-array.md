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

def apply_rearrangement_with_overflow_jp(input_array, pattern):
    # 入力配列と同じ形状と型で出力配列を初期化
    output_array = np.empty_like(input_array)
    rows, cols = input_array.shape
    p_rows, p_cols = pattern.shape
    
    # パターンをフラット化して簡単にアクセス
    flat_pattern = pattern.flatten()
    
    # 入力配列の各要素に対して新しいインデックスを計算
    for i in range(rows):
        for j in range(cols):
            # ブロックの位置を決定
            block_row, block_col = i // p_rows, j // p_cols
            
            # ブロック内の位置を計算
            within_block_row, within_block_col = i % p_rows, j % p_cols
            
            # 入れ替えパターンに基づいて新しい位置を決定
            # パターンサイズを超えないようにする
            if within_block_row * p_cols + within_block_col < len(flat_pattern):
                new_pos = flat_pattern[within_block_row * p_cols + within_block_col]
                
                # フラットパターン位置に基づいて新しい行と列を計算
                new_row = block_row * p_rows + new_pos // p_cols
                new_col = block_col * p_cols + new_pos % p_cols
                
                # 新しい位置が入力配列の次元を超えないようにする
                if new_row < rows and new_col < cols:
                    output_array[i, j] = input_array[new_row, new_col]
                else:
                    output_array[i, j] = input_array[i, j]
            else:
                # 位置が入れ替えパターンを超える場合、元の要素を保持
                output_array[i, j] = input_array[i, j]
    
    return output_array

# 4x4の入力データ定義
tile_4x4 = np.array([
    ["R1", "R2", "Gr1", "Gr2"],
    ["R3", "R4", "Gr3", "Gr4"],
    ["Gb1", "Gb2", "B1", "B2"],
    ["Gb3", "Gb4", "B3", "B4"]
])

def tile_array(tile, shape):
    """
    指定されたタイルを使用して、指定された形状の2次元配列を生成する。
    タイルのサイズが指定された形状にぴったり合わない場合でも適用できるように修正されています。
    
    Parameters:
    - tile: 2次元のNumPy配列（タイル）
    - shape: タイルを並べる配列の形状（height, width）
    
    Returns:
    - tiled_array: タイルが並べられ、必要に応じてトリミングされた2次元配列
    """
    tile_height, tile_width = tile.shape
    array_height, array_width = shape
    
    # タイルを繰り返す回数を計算（切り上げることで、目的のサイズを超えるようにします）
    repeat_height = -(-array_height // tile_height)  # ceilを使うためのトリック
    repeat_width = -(-array_width // tile_width)
    
    # タイルを繰り返して大きな配列を生成
    tiled_array_large = np.tile(tile, (repeat_height, repeat_width))
    
    # 目的の形状にトリミング
    tiled_array = tiled_array_large[:array_height, :array_width]
    
    return tiled_array


# タイル状に並べた配列を生成（例として7x7の配列を生成）
input_array= tile_array(tile_4x4, (7, 7))

# 4x4の入れ替えパターンを定義
rearrangement_pattern = np.array([
    [0, 2, 1, 3],
    [8, 10, 9, 11],
    [4, 6, 5, 7],
    [12, 14, 13, 15]
])

# 入れ替えを含むオーバーフロー部分を適用
rearranged_output_improved = apply_rearrangement_with_overflow_jp(input_array, rearrangement_pattern)
print(rearranged_output_improved)
```