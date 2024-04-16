---
title: "Amudsen"
date: 2024-04-13T21:57:20+09:00
categories: ["SoftWare"]
tags: ["SoftWare", "Database"]
---
# Amudsen

## 概要

データカタログツールの一種。pythonベースで作成されている

南極点を最初に発見したノルウェーの探検家ロアール・アムンセンにちなんで付けられているらしい

- [詳細](https://www.amundsen.io/amundsen/)
- [日本語記事](https://dev.classmethod.jp/articles/getting-started-with-amundsen/)

## Quick Start

以下に書いてることをそのまま実施
- [リンク](https://www.amundsen.io/amundsen/installation/)

databuilderと呼ばれるデータ作成処理の中に、サンプルのデータ作成pythonの例が入ってるので、  
その内容を実施していく

``` bash
 $ git clone --recursive https://github.com/amundsen-io/amundsen.git
 # For Neo4j Backend
 $ docker-compose -f docker-amundsen.yml up
 # For Atlas
 $ docker-compose -f docker-amundsen-atlas.yml up
 # databuilderへ移動してサンプルデータを読込
 $ cd amudsen/databuilder
 $ python3 -m venv venv
 $ source venv/bin/activate
 $ pip3 install --upgrade pip
 $ pip3 install -r requirements.txt
 $ python3 setup.py install
 $ python3 example/scripts/sample_data_loader.py
```

その結果、以下のリンクでsampleデータに対する情報が見れるようになる
> http://localhost:5000/

## Data lineageの有効化

- [参考リンク](https://atlan.com/amundsen-data-lineage-set-up/)

面倒な手続きが多い...