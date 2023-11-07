---
title: "Streamlining_string_concatenation"
date: 2023-11-07T21:27:36+09:00
---

# 条件分岐なしでの文字列結合

## 概要

例えばオプションの指定など、複数の条件を並列に並べながら文字列結合させたい場合の方法を記載する

## サンプルコード

リストで定義し、joinとfilterを用いて対応すれば条件分岐を並列で記述可能

```python
values = [
    f'{value_a} {value_b}',
    f'{value_c}' if condition_a else None,
    f'{value_d}' if condition_b else None,
]

result = ' '.join(filter(None, values))
```
