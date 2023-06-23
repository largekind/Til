---
title: "パケット通信方式まとめ"
date: 2023-04-05T00:00:00+09:00
tags: ["InfoEngineer", "Network"]
categories: ["InfoEngineer"]
---
# パケット通信方式まとめ

## ATM : Asynchronous Transfer Mode

Async : 非同期 Sync(同期)の逆

非同期転送モード

高速通信のために送信データを固定セルに分割してやり取りする方式

ATMでは交換制御パラメタに「VCI(Virtual Channel Identifier)」を使用

## パケット交換方式

多種多様なパケットに対応するため、可変長のサイズで送受信を行う方式


パケット交換では交換制御パラメタに「LCN(Logical Channel Number)」を使用

## 交換制御パラメタ

接続相手を識別するための情報