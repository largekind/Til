---
title: "ディスクの調子が悪い場合のトラブルシューティング"
date: 2023-04-05T00:00:00+09:00
tags: [Windows]
categories: [Windows]
---
# ディスクの調子が悪い場合のトラブルシューティング

1. 以下のコマンド実行、ハードディスクのエラーチェックを行う
>chkdsk c: /r

通常のエラーチェックとは違い、Win環境内も見る

2. Dism実行。Winのシステムファイル故障がないか確認
> DISM.exe /Online /Cleanup-image /Restorehealth

3. sfc使って再修復
> sfc /scannow