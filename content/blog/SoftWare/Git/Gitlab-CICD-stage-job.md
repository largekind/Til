---
title: "Gitlab CI/CD ステージを使用したジョブの順次実行"
date: 2023-06-26T21:25:59+09:00
---

# Gitlab CI/CD ステージを使用したジョブの順次実行

## 概要

GitLab CI/CDのステージを利用してジョブの実行順序を制御する。ステージを分けることでジョブを順次実行させる手法を解説する。

## サンプルコード

以下にジョブを順次実行させるための`.gitlab-ci.yml`設定ファイルの例を示す:

```yaml
stages:
  - stage1
  - stage2

job1:
  script: echo "This is job 1."
  stage: stage1

job2:
  script: echo "This is job 2."
  stage: stage2
```

この設定では、`job1`が`stage1`ステージ、`job2`が`stage2`ステージに配置されている。

これにより、`job1`が終了した後でなければ`job2`は開始されない。

