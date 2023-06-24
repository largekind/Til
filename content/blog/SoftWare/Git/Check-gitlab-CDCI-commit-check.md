---
title: "Determining Whether to Commit in a GitLab CI/CD Job"
categories: ["SoftWare"]
tags: ["GitLab", "CI/CD"]
---

# GitLab CI/CDジョブでのコミット有無の判定

## 概要

GitLab CI/CDジョブの一部として実行するスクリプトで、特定のファイルに変更があるかどうかを判断し、変更がある場合のみコミットを行う方法を解説する。

## コミット有無の判定とコミットの実行

Gitで管理されているリポジトリにおいて、特定のファイルに変更があるかどうかを判断するには、`git diff`コマンドを使用することができる。このコマンドは、ファイルの現在の状態と最後のコミットとを比較し、その差分を出力する。

`git diff --quiet`コマンドを使用すると、差分が存在しない場合（つまり、ファイルに変更がない場合）は何も出力せず、差分が存在する場合（つまり、ファイルに変更がある場合）は非ゼロの終了ステータスを返す。

これを利用して、次のようなスクリプトを作成することができる：

```bash
git diff --quiet || git commit -m "Update README.md"
```

このスクリプトは、README.mdファイルに変更がある場合のみコミットを行う。変更がない場合は、コミットは行われずにジョブは正常終了する。

また、git pushを行う際にも、同様の理由で何もコミットがない場合にはpushを行わないようにすることができる。そのため、このスクリプトは次のように拡張することができる

```bash
git diff --quiet || (git commit -m "Update README.md" && git push origin $CI_COMMIT_REF_NAME)
```


