---
title: "RFM Analysis"
date: 2024-02-17T22:11:16+09:00
draft: True
categories: ["DXQuest"]
tags: ["DXQuest", "utility"]
---
# RFM Analysis

## 概要

以下3つの指標で顧客をグループ分けする分析手法
- Recency : 最終購入日
- Frequency : 購入頻度
- Monetary : 購入金額

## 分析手順

1. 期限決め
2. 各顧客に対するRFM指標を算出
3. ランク付けする RxFxMでもRxFでもよい
4. 上記ランクで顧客を識別

## 必要データ

- POS : いつどこで何が買われたか
- ID-POS : 上記 + IDによる誰なのかの情報
