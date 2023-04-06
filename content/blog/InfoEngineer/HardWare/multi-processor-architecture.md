---
title: "並列実行のアーキテクチャ"
date: 2023-04-05T00:00:00+09:00
tags: [InfoEngineer,HardWare]
---
# 並列実行のアーキテクチャ

## 表
| 略称   | 名称                                 | 概要               | 備考                                                        |
|------|------------------------------------|------------------|-----------------------------------------------------------|
| SISD | Single Instruction Single Data     | 単一の命令で単一のデータを処理  | 一番シンプル                                                    |
| SIMD | Single Instruction Multiple Data   | 単一の命令で複数のデータを処理  | pentiumプロセッサで採用                                           |
| MISD | Multiple Instruction Single Data   | 複数の命令で単一のデータを処理。 | 理論上は存在するが実装例はない。                                          |
| MIMD | Multiple Instruction Multiple Data | 複数の命令で複数のデータを処理  | 複数のプロセッサを搭載した並列コンピュータ環境が該当<br/>OSやコンパイラがMIMDに対応している必要がある。 |

## 覚え方

**(Simple/Multi)** _Instruction(命令数)_ + **(Simple/Multi)** + _Data(データ)_

Instructionが命令/Dataはデータなので、あとは単一/複数 命令かデータかを判別すればよい


