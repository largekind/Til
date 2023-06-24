---
title: "Pushing to a Repository in a GitLab CI/CD Job"
categories: ["SoftWare"]
date: 2023-06-24T21:56:39+09:00
---

# GitLab CI/CDジョブでのリポジトリへのプッシュ

## 概要

GitLab CI/CDジョブでは、特定のトークンを使用して、リポジトリへのプッシュを行うことが可能である。これには、リポジトリのURLにトークンを組み込む方法、あるいはgit remoteのURLを設定する方法がある。

## リポジトリへのプッシュ方法

リポジトリへのプッシュは次のように行うことができる：

1. `git remote add`を使用する方法：
    ```bash
    git remote add origin https://<access-token-name>:<access-token>@gitlab.com/myuser/myrepo.git
    ```
    ただし、この方法ではアクセストークンがプレーンテキストとして`.git\config`ファイルに保存される。これを避けるためには、"username"にアクセストークン名を、"password"にアクセストークンを提供し、git credentialシステムを使用することができる。

2. `git push`を直接使用する方法：
    ```bash
    git push https://gitlab-ci-token:<access_token>@gitlab.com/myuser/myrepo.git <branch_name>
    ```
    これは、異なるリポジトリへのプルとプッシュを行いたい場合に特に便利である。

3. `git remote set-url`を使用する方法：
    ```bash
    git remote set-url origin https://gitlab-ci-token:${ACCESS_TOKEN}@gitlab.com/<group>/<repo-name>.git
    ```
    この方法はアクセストークンを作成した後に使用することができる。
