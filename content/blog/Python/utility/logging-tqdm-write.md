---
title: "ログ出力中にtqdmでの進捗表示を行う"
date: 2023-10-18T22:54:42+09:00
---

# ログ出力中にtqdmでの進捗表示を行う

## 概要

例えば別の関数でprint()などを使ってログ表示中に、下部などにtqdmで進捗を表示し続けたい場合の備忘録

## 方法

printをオーバーライドしてtqdm.write()に置き換える

## サンプルコード

``` python
import builtins
from tqdm import tqdm
import time

# tqdm.write()を使用するカスタムprint関数の定義
def custom_print(*args, **kwargs):
    tqdm.write(*args, **kwargs)

# builtins.printをオーバライド
builtins.print = custom_print

# testモジュールをインポート
from test import func

# テスト
for i in tqdm(range(5)):
    func()

```

また、exeなどのログに対して対応したい場合は以下を用いる

``` py

# 別のexe処理などをtqdmで進捗表示させる場合
def run_command(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    for line in process.stdout:
        tqdm.write(line.strip())

```
