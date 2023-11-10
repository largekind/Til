---
title: "Lambda"
date: 2023-11-10T23:27:28+09:00
---

# Lambda

## 概要

無名関数のこと。わざわざ関数名もいらないような関数を作りたいときに使用

## 使用法

pythonだと以下

> lambda (引数) : (数式)

例えば、pandasのapplyなどと組み合わせて以下のようなものが作れる

例 : Dataの値がAまたはBの時に1、それ以外は0
``` pyhon
train_df['Result'] = train_df['Data'].apply(lambda x: 1 if (x=='A') or (x=='B') else 0)

```
