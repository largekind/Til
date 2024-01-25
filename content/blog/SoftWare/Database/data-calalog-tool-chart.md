---
title: "Data Calalog Tool Chart"
date: 2024-01-18T23:37:41+09:00
draft: True
categories: ["SoftWare"]
tags: ["SoftWare", "Database"]
---
# データカタログツールの比較

## 概要

各データカタログツールの比較を行う。また行った結果の根拠もまとめる

## 星取表

| ツール          | Python連携 | データ追加/削除の簡易性 | 環境構築の簡易性 | スケーラビリティ | 拡張性とカスタマイズ | コミュニティサポート | テキストベースのデータ統合の容易さ | 日本語サポート | 学習コスト | ライセンス   |
|-----------------|------------|-----------------------|----------------|----------------|-------------------|------------------|-----------------------------|----------------|------------|------------|
| Apache Atlas    | 低         | 低                    | 低             | 高             | 高               | 高              | 中                          | 低             | 高         | Apache 2.0 |
| Amundsen        | 中         | 低                    | 中             | 中             | 高               | 中              | 低                          | 低             | 中         | Apache 2.0 |
| CKAN            | 高         | 高                    | 高             | 高             | 中               | 高              | 高                          | 中             | 低         | AGPL-3.0   |
| Metabase        | 中         | 中                    | 高             | 中             | 中               | 中              | 中                          | 低             | 低         | AGPL-3.0   |
| DataHub         | 中         | 中                    | 中             | 高             | 高               | 中              | 中                          | 低             | 中         | Apache 2.0 |
| OpenMetadata    | 中         | 中                    | 中             | 高             | 高               | 中              | 中                          | 低             | 中         | Apache 2.0 |

## 比較情報

調査中

### Apache Atlas

- Python連携 : 低
  - もともとJavaとして記載されており、Python APIの提供はあるが全機能の網羅はされておらず限定的
  - [Python API](https://github.com/apache/atlas/tree/master/intg/src/main/python)
- データ追加/削除の簡易性 : 高
  - 情報不足
- 環境構築の簡易性 
  - Apacheのインストールは、多くのOSで簡単に行うことができる
- スケーラビリティ 
  - スケーラブルなデータベースをサポート
- 拡張性とカスタマイズ 
  - Apacheはモジュールを通じて機能を追加したり拡張したりすることができる
  - [Apache Atlas | Cloudera.](https://jp.cloudera.com/products/open-source/apache-hadoop/apache-atlas.html.)
- コミュニティサポート 
  - Apache Atlas コミュニティが一応存在するらしいが、提供されたURLは全然違う製品だったりして信憑性不明
- テキストベースのデータ統合の容易さ 
  - 情報なし
- 日本語サポート 
  - 皆無
- 学習コスト
  - Qiitaなどで一部だけ情報があったりするが、余り良いものではない
  - 公式ドキュメントは存在するが、独特な動作等があるらしくコスト高
  - [Document](https://atlas.apache.org/#/)

### Amundsen
### CKAN
### Metabase
### DataHub
### OpenMetadata