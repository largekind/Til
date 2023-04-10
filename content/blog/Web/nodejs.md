---
title: "Nodejs"
date: 2023-04-05T00:00:00+09:00
tags: [Web]
categories: [Web]
---
# Nodejs

Webブラウザ以外でもjavascriptを実行できるようにするための実行環境

## インストール方法

dockerですでに提供されている環境使えばよい

## REPL (Read-Eval-Print Loop)

nodeだけで実行するとpythonやrubyであるインタプリタみたいなプロンプト（REPL）を使うことができる

> node

対話型のウィンドウが開くので、いろいろ簡単な式を試したいときに使用できる

## profile

以下でプロファイルツールを使用できる
どこで時間がかかっているのか、メモリ使用量などを出力できる

> node --prof app.js

その後、出てくるファイルを以下のようにnodeに渡せば解析、
読めるような形に出力してくれる

> node --prof-process isolate-XXX.log
