---
title: "yarnインストール時のトラブルシューティング"
date: 2023-04-06T00:00:00+09:00
lastmod: "2023-04-06"
---
# yarnインストール時のトラブルシューティング

## 問題

以下のようなエラーが発生し、yarn addができない
``` js
yarn add v1.22.18
error Missing list of packages to add to your project.
info Visit https://yarnpkg.com/en/docs/cli/add for documentation about this command.
bot-todo@cbd4f3501aa4:/bot-todo$ yarn add @slack/bolt
yarn add v1.22.18
info No lockfile found.
[1/4] Resolving packages...
[2/4] Fetching packages...
[3/4] Linking dependencies...
error An unexpected error occurred: "EPERM: operation not permitted, copyfile '/home/bot-todo/.cache/yarn/v6/npm-@slack-oauth-2.5.4-94882a57068ae837720291ab875fe08d276ace77-integrity/node_modules/@slack/oauth/README.md' -> '/bot-todo/node_modules/@slack/oauth/README.md'".
info If you think this is a bug, please open a bug report with the information provided in "/bot-todo/yarn-error.log".
```

## 原因

WSL2の権限回りが問題でchmodなどで付与したlinuxのファイルパーティションの権限が正常通りに動作しなくなっているため。

[詳細リンク](https://alessandrococco.com/2021/01/wsl-how-to-resolve-operation-not-permitted-error-on-cloning-a-git-repository)

## 対策法

リンク参照。wslのマウント系の設定を主導で復旧させる。

1. WSL配下の"/etc/wsl.conf"がなければ作成
2. 上記の設定ファイルを管理者権限付与したエディタで開いて追加
``` conf
[automount]
options = "metadata"
```
3. ファイルを保存して、WLSを一度シャットダウン PowerShell上で以下実行
> wsl --shutdown
4. wsl再起動