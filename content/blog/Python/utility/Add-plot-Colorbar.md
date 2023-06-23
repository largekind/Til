---
title: "大量のグラフに色付けする方法"
date: 2023-04-20T23:18:18+09:00
tags: ["matplotlib", "Python", "utility"]
categories: ["Python"]
---
# グラフに色付けする方法

## 概要

matplotlibで大量のグラフに色付け、またその色にどの値が対応するかを記載する

具体的には以下の流れ
1. カラーマップを用意 いろいろカラーマップが用意されているので、次の[カラーマップのドキュメント](https://matplotlib.org/stable/tutorials/colors/colormaps.html)を参照
> cmap = plt.get_cmap("plasma")
2. カラーマップに対して、正規化オブジェクトを使用。これにより、色と値の対応付けを行う。
> norm = mcolors.Normalize(vmin=min_value, vmax=max_value)
3. データをプロットする。あらかじめ作成したcmapとnormに対して、対応する値を渡す
> color = cmap(norm(value))
> plt.plot(x_values, y_values, color=color)
4. matplotlib.cm.ScalarMappableクラスを使用して、カラーマップと正規化オブジェクトを持つオブジェクトを作成
> sm = cm.ScalarMappable(cmap=cmap, norm=norm)
5. Matplotlibのバージョンが3.1.0未満の場合、ScalarMappableオブジェクトに空のデータ配列を設定
> sm.set_array([])
6. カラーバーを出力させる
> cbar = plt.colorbar(sm)



## サンプルコード

適当に指数関数を表示するやつ。

```
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.cm as cm

def exponential(x):
    return np.exp(x)

# x軸の値
x_values = np.linspace(-1, 1, 10000)

# グラフの数
num_plots = 300

# シフトの最小値と最大値を定義
min_shift = 0
max_shift = num_plots

# カラーマップを作成 (hsvを使用)
cmap = plt.get_cmap("hsv")

# カラーマップに正規化オブジェクトを適用
norm = mcolors.Normalize(vmin=min_shift, vmax=max_shift)

# グラフのプロット
fig, ax = plt.subplots()

for i in range(num_plots):
    y_values = exponential(x_values + i)  # x_valuesにi値を加える
    
    # カラーバーに従って色を取得
    color = cmap(norm(i))
    
    # データのプロット
    ax.plot(x_values, y_values, color=color, linewidth=1)

# カラーバーを追加
sm = cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([]) # matplotlibのバージョンが古い場合は追記しておく
cbar = plt.colorbar(sm)
cbar.set_label('Shift')

# グラフの設定
plt.title("Exponential Function with different shifts")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()
```