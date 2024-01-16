---
title: "NAPT : Network Address Port Translation"
date: 2023-04-05T00:00:00+09:00
tags: ["InfoEngineer", "Network"]
categories: ["InfoEngineer"]
---
# NAPT : Network Address Port Translation

プライベートIPアドレスとポート番号の組合せとグローバルIPアドレスとポート番号の組合せとの変換を行う

NAT : Network Address TranslationがプライベートIPアドレスとグローバルIPアドレスの1:1変換に対し、
NAPTはそれにポート番号が付随したものとなる

IPアドレスとポート番号が付随するため、内部ネットワークからインターネットにアクセスする利用者PCについて，インターネットからの不正アクセスを困難にすることができる。  
※記憶しているポート番号以外に宛てたパケットは宛先不明としてすべて破棄することで、不正アクセスを防止する