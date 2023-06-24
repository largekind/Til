---
title: "GitLab Pipeline for Automatic Commits"
date: 2023-06-19T22:22:48+09:00
categories: ["SoftWare"]
tags: ["GitLab", "CI/CD", "automatic commit", "Software", "SoftWare", "Git"]
---
# GitLabのパイプラインでの自動コミット

## 注意

Chat-GPTでの自動生成したもの

## 概要

GitLabのパイプラインから自動的にコミットを作成する際には、GitLab CI/CD Job Tokenを用いることが可能。
このトークンは、パイプラインの実行時に自動的に生成され、そのパイプラインの実行が終了すると失効する。

## CI/CD Job Tokenとは

CI/CD Job Tokenは、GitLabがパイプラインのジョブが実行される前に生成する一意のトークンである。
このトークンは、特定のAPIエンドポイントに対する認証に使用することが可能である。

使用例としては、パッケージレジストリ、ジョブアーティファクトの取得、マルチプロジェクトパイプラインのトリガー、リリースとリリースリンク、などが挙げられる。

また、CI/CD Job Tokenを使ってプライベートプロジェクトのリポジトリをCI/CDジョブからクローンすることも可能である。ただし、現時点ではリポジトリへのプッシュはサポートされていない。

## パイプラインからの自動コミット

GitLabのパイプラインで自動コミットを行うためには、リモートリポジトリのURLを設定する際に、CI/CD Job Tokenを含む形式を用いる。具体的には以下のようにする。

```bash
git remote set-url origin https://gitlab-ci-token:${CI_JOB_TOKEN}@gitlab.example.com/<namespace>/<project>
```

このコマンドを実行すると、パイプラインからのgit pushが可能になる。ただし、パイプラインが終了するとトークンが失効するため、その後のpushは不可能になる。