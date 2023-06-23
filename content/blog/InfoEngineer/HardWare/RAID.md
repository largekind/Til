---
title: "RAID : Redundant Arrays of Inexpensive Disks"
date: 2023-04-05T00:00:00+09:00
tags: ["InfoEngineer", "Hardware", "HardWare"]
categories: ["InfoEngineer"]
---
# RAID : Redundant Arrays of Inexpensive Disks

複数台のハードディスクを組み合わせて、仮想的な1台のハードディスクとして運用、冗長性を高める技術

よく忘れやすいので、「スミスはスパスパスパ」と覚える

## RAID0

**ス**トライピング 

HDDに対してデータを分散して書き込みする

ただデータ分散させてるだけであり、誤り検出とかができてないので「0」とされる模様

## RAID1

**ミ**ラーリング

HDDに対して同じデータを書き込む

当然、同じデータを書き込むので冗長性はクリアできる

## RAID2

**ス**トライピング + **ハ**ミング符号

## RAID3-5

RAID3以降はほぼ同じ。

**ス**トライピング + **パ**リティになる。

- RAID3 : **ス**トライピング + **パ**リティ(ビット)
- RAID4 : **ス**トライピング + **パ**リティ(ブロック)
- RAID5 : **ス**トライピング + **パ**リティ(ブロック+分散)