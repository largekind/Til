---
title: "Hugoの導入方法"
date: 2023-04-06T21:13:35+09:00
tags: ["linux"]
categories: [linux]
---

# Hugoの導入方法

## 概要

Markdownの情報をHTMLの形式で出力してくれるHugoの導入方法を記載する

## インストール方法

[URL](https://gohugo.io/getting-started/quick-start/)参照。

WSL2+ubuntu環境なので以下コマンドを実行する
> sudo apt install git hugo

## ローカルでのサーバー起動方法

以下のみでよい

> hugo server

## データの追加法

以下コマンド実行

> hugo new blog/XXXX.md

## ディレクトリ階層

```
(リポジトリ)/
├── archetypes/
│   └── default.md
├── assets/
├── content/
├── data/
├── layouts/
├── public/
├── static/
├── themes/
└── config.toml
```




