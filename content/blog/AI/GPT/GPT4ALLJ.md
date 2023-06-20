---
title: "GPT4ALLJ"
date: 2023-06-20T21:49:12+09:00
categories : ["AI"]
tags : ["AI","GPT"]
---

# GPT4ALLJ

## 概要

ローカルでも使用可能なChatGPTのモデル

商用も可能である

[github](https://github.com/marella/gpt4all-j)

## 導入

pipでinstall可能

> pip install gpt4all-j

モデルはwgetかリンクから取得する
> !wget https://gpt4all.io/models/ggml-gpt4all-j.bin

## 使用法(通常)

github引用。model.generate("テキスト")で、テキスト内容に応じた返答が来る
``` python
from gpt4allj import Model

model = Model('/path/to/ggml-gpt4all-j.bin')

print(model.generate('AI is going to'))
```

## LangChain使用の場合

モデルを用いたアプリ開発などで使用するLangChainとリンクさせたい場合、以下のような流れで使用可能

``` python
from gpt4allj.langchain import GPT4AllJ

llm = GPT4AllJ(model='/path/to/ggml-gpt4all-j.bin')

print(llm('AI is going to'))
```

詳細はgithubを参照