---
title: "Windows Storeでインストールができなくなったトラブルシューティング"
date: 2023-04-05T00:00:00+09:00
tags: ["Windows"]
categories: ["Windows"]
---
# Windows Storeでインストールができなくなったトラブルシューティング

## 概要

急にWindowsで以下のエラーが発生し、Windows terminalが使えなくなった
> エラーコード：0x80070057

## 原因

VC++ 2012 Runtimeがなかったことによる、パラメータ不整合

## 解決策

上記VC++ 2012をインストールする