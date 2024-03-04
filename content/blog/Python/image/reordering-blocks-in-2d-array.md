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

def tile_array(tile, shape):
    """
    指定されたタイルから、指定された形状の配列を生成する。
    タイルは形状に応じて繰り返され、必要に応じてトリミングされる。

    Parameters:
    tile : ndarray
        繰り返し使用される2次元タイル。
    shape : tuple
        生成される配列の形状（高さ、幅）。

    Returns:
    ndarray
        タイルが繰り返された配列。
    """
    tile_height, tile_width = tile.shape
    array_height, array_width = shape
    repeat_height = -(-array_height // tile_height)  # ceilを使うためのトリック
    repeat_width = -(-array_width // tile_width)
    tiled_array_large = np.tile(tile, (repeat_height, repeat_width))
    tiled_array = tiled_array_large[:array_height, :array_width]
    return tiled_array

def rearrange_data_according_to_pattern(base_arr, rearrangement_pattern):
    """
    ベース配列を再配置パターンに従って再配置する。

    Parameters:
    base_arr : ndarray
        再配置される元の配列。
    rearrangement_pattern : ndarray
        再配置に使用されるパターン。

    Returns:
    ndarray
        再配置された配列。
    """
    rearranged_data = np.empty_like(base_arr, dtype=object)
    flat_base = base_arr.flatten()
    flat_pattern = rearrangement_pattern.flatten()
    for index, value in enumerate(flat_pattern):
        rearranged_data.flat[index] = flat_base[value]
    return rearranged_data

def adjust_pattern_for_overflow(original_pattern, target_shape):
    """
    オーバーフローを考慮してパターンを調整する。

    Parameters:
    original_pattern : ndarray
        元の再配置パターン。
    target_shape : tuple
        対象のブロック形状。

    Returns:
    ndarray
        調整された再配置パターン。
    """
    # base_shapeからNxMの連番配列を生成
    NxM = np.arange(np.prod(original_pattern.shape)).reshape(original_pattern.shape)
    # target_shapeからPxQの連番配列を生成
    PxQ = np.arange(np.prod(target_shape)).reshape(target_shape)
    
    # マッピングテーブルの作成
    mapping_table = {}
    for i in range(min(original_pattern.shape[0], target_shape[0])):
        for j in range(min(original_pattern.shape[1], target_shape[1])):
            mapping_table[NxM[i, j]] = PxQ[i, j]
    adjusted_pattern = np.searchsorted(list(mapping_table), original_pattern)[:target_shape[0],:target_shape[1]]
    
    return adjusted_pattern

def blockwise_rearrange_with_adjusted_pattern(large_data, original_pattern):
    """
    ブロック単位でデータを再配置する。オリジナルのパターンは必要に応じて調整される。

    Parameters:
    large_data : ndarray
        再配置される大きなデータ配列。
    original_pattern : ndarray
        元の再配置パターン。

    Returns:
    ndarray
        再配置されたデータ配列。
    """
    N, M = large_data.shape
    P, Q = original_pattern.shape
    rearranged_data = np.empty_like(large_data, dtype=object)
    
    for i in range(0, N, P):
        for j in range(0, M, Q):
            end_i = min(i + P, N)
            end_j = min(j + Q, M)
            block = large_data[i:end_i, j:end_j]
            
            if block.shape == original_pattern.shape:
                block_pattern = original_pattern
            else:
                block_pattern = adjust_pattern_for_overflow(original_pattern, block.shape)
            
            rearranged_block = rearrange_data_according_to_pattern(block, block_pattern)
            rearranged_data[i:end_i, j:end_j] = rearranged_block
    
    return rearranged_data
```

## 使用例

```py
# 以下の例では、タイル配列を生成し、特定のパターンに従って再配置する
tile_4x4 = np.array([
    ["R1", "R2", "Gr1", "Gr2"],
    ["R3", "R4", "Gr3", "Gr4"],
    ["Gb1", "Gb2", "B1", "B2"],
    ["Gb3", "Gb4", "B3", "B4"]
])
# Quad -> Bayerに入れ替え
input_array = tile_array(tile_4x4, (16, 15))
original_pattern_example = np.array([
    [0, 2, 1, 3],
    [8, 10, 9, 11],
    [4, 6, 5, 7],
    [12, 14, 13, 15]
])

rearranged_input_array = blockwise_rearrange_with_adjusted_pattern(input_array, original_pattern_example)
print(rearranged_input_array)

```