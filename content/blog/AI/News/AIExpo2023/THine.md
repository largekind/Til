---
title: "THine"
date: 2023-06-23T22:34:35
categories: ["AI"]
tags: ["AI", "News", "AIExpo2023"]
---
# THine

## 気になった理由

- エッジAIでの異常検知企業のため

## 見学内容

- エッジAIを用いた情報をクラウドAIでさらに処理、判断結果を出力するシステム
- LTE接続を用いて、野外などのネット環境がない場所でもクラウド接続ができるようにした

## 所感

- 内容自体は他企業でもあるようなエッジAI + クラウドAの組み合わせ
- 画質評価をAIでするような事例を知っているか確認したところ、以下の点で中々難しいのではという話を受けた
    - 画質というものの定量化がどういったものかが難しい
    - 画像をAIに入力する際、一定の画サイズに落とし込む処理があるため、その時に解像度の情報が消えてしまう
    - 格子状で画像をカットして巨大な画像を入力するモデルを使ったとしても、各情報が独立して入力されるため関係性が欠落してしまう
        - 入力として全体像と格子状カットした画像2つを入れ込むことで解決しないか？要検討