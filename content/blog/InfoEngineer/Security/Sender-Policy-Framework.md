---
title: "Sender Policy Framework"
date: 2023-06-05T23:32:34+09:00
categories: ["InfoEngineer"]
tags: ["InfoEngineer", "Security"]
---
# SPF: Sender Policy Framework

## 概要

差出人のIPアドレスと送信元のメアドにあるドメインのSPFレコードをメールサーバーで検証する方式

つまり、IPアドレスから送信元が本当に問題ない場所なのかを確認する方式。

大企業とかであればIPがある程度絞れるのでなりすまし対策として効果があるが、差出人アドレスを査証してないような迷惑メールには効果がない問題もある