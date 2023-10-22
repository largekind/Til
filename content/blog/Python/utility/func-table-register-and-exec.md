---
title: "Func Table Register and Exec"
date: 2023-10-22T22:48:11+09:00
---

# 関数テーブルの使用法とテーブルへの自動登録

## 概要

辞書のキーに関数やメソッドを動的にマッピング、関数テーブルを作成する方法を記載する。
さらに、デコレータを利用することで、関数やメソッドを辞書に自動登録し、動的に呼び出す仕組みもサンプルとして記載する。

## サンプルコード

### 1. 基本的な関数テーブルの作成

```python
def hoge_execute():
    print("hogehoge")

def piyo_execute():
    print("piyopiyo")

# 関数テーブルの作成
function_table = {
    "hoge": hoge_execute,
    "piyo": piyo_execute
}

# 使用例
name = "hoge"
function_table[name]()
```

### 2. メソッドに対してデコレータを用いて関数テーブルに自動登録

```python
strategy_dict = {}

def register_table(func):
    strategy_dict[func.__name__] = func
    return func

class GroupA_Strategy:
    @register_table
    def hoge_execute(self):
        print("hogehoge")

    @register_table
    def piyo_execute(self):
        print("piyopiyo")

# 使用例
name = "hoge_execute"
strategy_method = strategy_dict.get(name)
if strategy_method:
    strategy_instance = GroupA_Strategy()
    strategy_method(strategy_instance)
```

### 3. クラスに対してデコレータを用いて関数テーブルに自動登録

```python
strategy_dict = {}

def register_tables(cls):
    for name, method in cls.__dict__.items():
        if callable(method):
            strategy_dict[name] = method
    return cls

@register_tables
class GroupA_Strategy:
    def hoge_execute(self):
        print("hogehoge")

    def piyo_execute(self):
        print("piyopiyo")

# 使用例
name = "hoge_execute"
strategy_method = strategy_dict.get(name)
if strategy_method:
    strategy_instance = GroupA_Strategy()
    strategy_method(strategy_instance)
```