---
title: "Reverse Proxy"
date: 2024-03-10T21:07:25+09:00
categories: ["InfoEngineer"]
tags: ["InfoEngineer", "Security"]
---
# Reverse Proxy

## 概要

リバースプロキシ

クライアントとWebサーバの間に位置して、Webサーバの代理としてリクエストを受け取り、そのリクエストをWebサーバに中継する仕組み

間に1つプロキシが挟まることで、アクセス制御や認証などの機能を持たせればセキュリティ向上が可能

イメージ図
```
クライアント -----> [リバースプロキシ] ---(中継)---> Webサーバ
```