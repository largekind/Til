---
title: "評価関数"
date: 2023-08-20T23:06:45+09:00
categories: ["DXQuest"]
tags: ["DXQuest", "AI_Beginner"]
---
# 評価関数

## 概要

- 学んだこと
  - 評価関数
    - モデルの性能を定量的に表すための関数
    - タスクに応じて適切な評価関数を作成する必要がある
    - 予測精度とKPIが関連付けられれば、費用対効果を作れられる
  - 代表的なタスクと使用する評価関数
    - 回帰
      - MSRやR^2係数など
    - 分類
      - Accurary/Precision/Recall/AUC/F値など
    - 推薦・検索
      - mAP@N/nDCGなど
    - 物体(領域)検出
      - IOU/mAP