---
title: "DX What"
date: 2023-07-29T21:44:24+09:00
categories: ["DXQuest"]
tags: ["DXQuest", "DXLiteracy", "DX_Beginner"]
---
# DX What

## 概要

DXにおける何がDXで必要かの動画講座で学んだことを箇条書きで簡潔にまとめていく

## 社会におけるデータ

- 学んだこと
  - 身のさまざまな場面でデータは発生する
    - カメラ、POS、口頭での通話など
  - データの構造
    - 属性(区分)と値(数値や文字列)が紐づいている状態
    - IndexとValの関係性
  - データは大きく3種類
    - 構造化データ
      - CSV/xlsxといった表形式にしたもの
    - 非構造化データ
      - メールや画像等
    - 半構造化データ
      - XMLやHTMLといったメタデータ
  - 取得方法に応じて一次データ、二次データがある
    - 一次データ
      - 目的に応じて直接取集したデータ
    - 二次データ
      - 別の目的で収集されたデータを再利用することで得られるデータ
      - すでに公開されているデータセットなどもここ

## データの活用

- 学んだこと
  - データの活用の重要性
    - データを活用することで、主観的な判断から客観的、合理的で正確な判断がしやすくなる
  - データ判断のパターン
    - モニタリング
      - KPI/KGTといった指標を用いて目標管理をする
    - 事実の探索
      - データから新しい事実、知見を探る
    - 仮説検証
      - 経験則をデータで裏付けする
    - 予測
      - 過去のパターンから将来予測
  - データ活用のプロセス
    - 以下の流れ
      1. 計画
      2. データ収集
      3. データ整理
      4. 分析
      5. 判断
    - 各々の対応はどうしても人力になるので、それに応じたスキルが必須
    - ChatGPTでもデータ整理・分析は自動化できるが、出た結果の判断は人間なので、どちらにせよ知識は必要
  - データ活用のスキルは「扱う」「読む」「説明する」の3スキルになる

## データを扱う

- 学んだこと
  - データの扱うためにやることは以下の内容
    1. データの前処理
        - 加工・抽出など。一番面倒な作業など。一番面倒な作業。ほぼ8割を占める
        - ChatGPTである程度自動化できたと思うが、業務機密データなどは渡せないのでどちらにせよ人力…
        - 前処理を間違えると全部が狂うので要注意
    2. データの管理
        - データベースの査定など。SQLなど様々
        - DBMSが大抵いたるところで使われる

## データを読む

- 学んだこと
  - 基本統計量
    - Min/Max/Avg/Median/Sigmaなど
    - 指標を用いて「比較」することデータの変化をつかむ必要がある
  - データの可視化が必須
    - 平均の落とし穴などの件
  - 統計情報の正しい理解
    - 母集団の選択も間違えないようにする必要がある
      - 生存バイアスなどもこの件
    - 疑似相関などもある
      - 飲酒が多くなると犯罪率が多くなるといった誤った認識など(実際の原因は不況といった別要因)
      
## データの説明

- 学んだこと
  - 可視化することで、データを直感的に理解できるようになる
  - 可視化のグラフにはいろいろ種類がある
    - 棒グラフ
    - 折れ線グラフ
    - データチャート
    - 散布図
    - 円グラフ
    - クロス集計表
    - 星取表
  - 表現に使用するグラフの選定は適切に行う必要がある
    - グラフ選定を間違えると間違った関係性や誇張・矮小化となる
    - マスコミがよくやるやつ
    - 情報不足や過度な装飾もある。不要な3Dグラフ使用や、縦軸横軸の情報が抜けているなど
    
## デジタル技術の基礎知識

### コンピュータ・ネットワーク

- 学んだこと
  - 超基礎的なPCの構成内容。ソフト/ハードから始まり、CPU/RAM/HDD/IOなどの話
    - ソフトの構成要素
      - SW/MiddleWare/OS/HWの構成など
    - ネットワークの基礎情報
      - LAN/WANの話。LANはともかくWAN(Wide Area Network)はよく忘れやすいので注意
      - インターネットはWANが総合接続されたネットワーク
    - ネットワーク機器の話
      - Router/Swith/FileWallの話など。これも基礎的
    - Wifiと5G
      - Wi-fi : Wireless Fidelity
        - よく使われるが略称が出てこないやつ
      - 5G
        - GはGenarationの意味。第5世代のモバイル通信。LTE(4G)から発展したもの

### クラウド

- 学んだこと
  - ネットを用いてサービスやコンピュータ資源を活用する仕組み
    - 例 : メール、ドライブなど 大抵はSaaS製品
    - 当然ネット経由なので、オフラインで利用できないなどデメリットもある
  - クラウドの提供形態としてSaaS/PaaS/IaaSがある
    - SaaS : アプリまでクラウドが管理 SlackとかOffice 365とか
    - PaaS : ミドルウェアまでクラウドが管理 GAEとかAzureとか
    - IaaS : HWまでの必要最低限の部分がクラウドが管理 AWS/GCPとか

### AI

- 学んだこと
  - Artifical Intelligence
    - データを処理して判断させること。たいてい特化型
    - 教師あり/なし学習や強化学習がある
  - なぜAIを活用したいのか、目的を明確化する必要がある
    - AIを使うことを目的にしないようにする！