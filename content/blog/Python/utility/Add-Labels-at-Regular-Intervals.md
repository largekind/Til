---
title: "一定間隔でグラフに凡例を追加する方法"
date: 2023-04-20T23:56:43+09:00
tags: [matplotlib, Python, utility]
categories : [Python]

---

# 一定間隔でグラフに凡例を追加する方法

## 概要

大量にデータがあり、一定の感覚で凡例を追加してほしい場合の方法を記載する

具体的には以下の通りで対応する
1. データ総数の(rate)%ごとに凡例を追加する間隔を計算。total_numはデータ総数、rateは割合
> legend_interval = int(total_num * rate)
2. データをプロットする際に、現在のインデックス（またはグループ番号）がlegend_intervalで割り切れる場合、凡例を追加
``` Python

for i in range(total_num):
    y_values = func(i) #適当なデータ

    # 一定間隔で判例を追加
    if i % legend_interval == 0:
        plt.plot(x_values, y_values, color=color, label=f"func({i})")
    else:
        plt.plot(x_values, y_values, color=color)

```
## サンプルコード

一定間隔でGroupbyで分けたデータに対し、凡例とカラーバーを追加する

``` Python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.cm as cm

def exp_function(x, i):
    return np.exp(x + i)

x_values = np.linspace(0, 1, 100)
num_plots = 100

# ダミーのDataFrameを作成
data = {'x': np.repeat(x_values, num_plots), 'i': np.tile(np.arange(num_plots), 100), 'y': np.array([exp_function(x, i) for x, i in zip(np.repeat(x_values, num_plots), np.tile(np.arange(num_plots), 100))])}
df = pd.DataFrame(data)

# 'i'列でグループ化
grouped_df = df.groupby('i')

cmap = plt.get_cmap("viridis")
norm = mcolors.Normalize(vmin=0, vmax=grouped_df.ngroups)

# 凡例を追加する間隔を計算
legend_interval = int(grouped_df.ngroups * 0.1)

for i, (group, data) in enumerate(grouped_df):
    color = cmap(norm(group))

    if i % legend_interval == 0:
        plt.plot(data['x'], data['y'], color=color, label=f"exp({group})")
    else:
        plt.plot(data['x'], data['y'], color=color)

plt.title("Exponential Functions")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.legend()

plt.show()
```

