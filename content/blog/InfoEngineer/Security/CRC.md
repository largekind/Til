---
title: "CRC :Cyclic Redundancy Check"
date: 2023-04-05T00:00:00+09:00
tags: ["InfoEngineer", "Security"]
categories: ["InfoEngineer"]
---
# CRC :Cyclic Redundancy Check


巡回冗長検査

誤り検出方式の１つで、主にデータ転送などに伴う偶発的な誤りの検出によく使わる

送信データから生成多項式によって誤り検出用のデータを付加して送信、受信側で同じ生成多項式を使用してデータを除算し、その余りを比較照合することによって受信データの誤り・破損を検出する