---
title: "Devops"
date: 2023-11-26T21:30:55+09:00
categories: ["SoftWare"]
tags: ["SoftWare"]
---
# Devops

## 概要

Devopsとは何か、その必要性やツールについてまとめる

## Depopsの必要性

- DevOps
  - develop(開発) + operation(運用) = devops 
  - 開発担当と運用担当が密に連携して、柔軟かつスピーディにシステム開発を行う手法
  - クラウドコンピューティングやコンテナ技術などの普及によって、急速に展開が進んでいる
- DevOpsの目標  
  - スピード性・品質・持続性のある改善が目標
  - 目標達成のために自動化とコミュニケーションが必要となる
- HWとDevOps
  - ChatGPTに聞いた内容。具体的にDevOpsをHW関係の企業が入れた一例として以下のようなものがある
  - [導入事例](https://www.novelvista.com/blogs/news/10-companies-successfully-implemented-devops)
  - 半導体企業にも導入事例がある。おそらくデータの分析・解析などが主となる。[リンク](https://www.nitorinfotech.com/case-study/cloud-based-solution-for-semiconductor-company/)
  
## Devopsの主要プロセス

- アジャイル開発
  - 小さくリリースを繰り返すというもの。これをDevOpsで運用することでテストなどの自動化、ソフトの高品質化が行われている
  - ウォータフォールとは真逆のやつ。ソフト重視のものが多い認識
- デプロイ
  - ソフトの開発計画を立て、本番環境へ展開すること
- cI/cDプロセス
  - CI : Continuous Integration
    - コードの変更を加えるために、共有のコードベースに統合し自動的にテストを行うプロセスのこと
    - これにより問題の早期発見などが出来る
  - CD : Continuous Delivery
    - ビルド・テストが成功したコードを自動的にリリースすること
- DevOpsにおけるリリース
  - 小さな変更を頻繁にリリースすることで、問題が発生した時のリスク低減と問題の早期発見を行うのが主となる
  - 自動テストとデプロイを活用して、リリースプロセスの高速化と品質確保を目指している
