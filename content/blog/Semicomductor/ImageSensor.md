---
title: "Image Sensor"
date: 2023-04-09T22:17:43+09:00
tags: [Semiconductor]
categories: [Semiconductor]
---

# イメージセンサー

## 概要

光を電気信号に変換する半導体。
主にCCD/CMOSに大別される。

## 構造

基本的にはCCD/CMOSどちらも以下の構成

```
光 => (Lens) => (Color Filter) => (集光素子/フォトダイオード) 
```

## CCD Image Sensor

Charge Coupled Device Image Sensorの略

フォトダイオードで生成した殿下を画素間でバケツリレーのように転送して1つの暗譜で増幅するイメージセンサ

アンプが１つなので消費電力は高いが画質が高くなる

## CMOS Image Sensor

Complementary Metal Oxide Semiconductor Image Sensor

型とN型のMOSFETをディジタル回路（論理回路）で相補的に利用する回路方式(CMOS)で作られたイメージセンサ

基本的にはこちらが主流となっている

### 裏面照射型イメージセンサ

チップの裏面にもフォトセンサを付与、光を入射させることで感度を向上させたもの

### 積層型イメージセンサ

画素と信号処理の回路を別チップ化して、受講領域を広げたセンサ
