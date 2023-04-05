---
title: "Cron"
date: 2023-04-06T00:00:00+09:00
lastmod: "2023-04-06"
---
# Cron

定期的に特定のコマンドを実行させたい時に使用するプロセスのコマンド

## 流れ

1. 以下のコマンド実行
``` bash
crontab -e 
```
2. エディタ選択
3. 以下の形式で実行させたいコマンドを入力
``` cron
# m h  dom mon dow   command
# 分 時 日 月 曜日  実行したいコマンド
```
4. 以下でcronサービス実行
> service cron start