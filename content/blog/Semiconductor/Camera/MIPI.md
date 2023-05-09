---
title: "NIPI : Mobile Industry Processor Interface"
date: 2023-05-04T22:11:55+09:00
tags: [Semiconductor, Camera]
categories: [Semiconductor]
---

# NIPI : Mobile Industry Processor Interface

## 概要

モバイルに内臓されるプロセッサーとカメラなどの外部機器を接続するために作られた規格

以下２つのインターフェースを持つ
- CSI
- CCI

## CSI : Camera Serial Interface

映像データ転送に特化したプロトコルとなる。

以下の特徴を持つ
1. 単方向
2. 再送なし
3. 他データも転送可能

## CCI : Camera Control Intarface

カメラモジュール制御のインターフェースでI2Cとも互換性を持つ

以下の特徴を持つ
1. I2C互換 SCLとSDAで構成されている
2. 双方向でのデータ転送が可能

## パケット構造

ロングパケットとショートパケットをLPS(Low Power State : 低レベル信号)で挟むような構造

イメージとしては以下の通り。

> [ショートパケット] - [LPS] - [ロングパケット] - [LPS] - [ロングパケット] - [LPS] - [ショートパケット]

## D-PHY 

MIPIの物理層を示すインターフェース規格

LPS用の低速モードや高速モードの通信がある。

詳細は次の情報を参照 [D-PHY](https://engineering-university.yamasee-otto.com/mipi-dphy/)
