---
title: "Bat上でファイルを選択させる方法"
date: 2023-05-14T21:15:31+09:00
categories : ["Windows"]
tags : ["Windows","shell"]
---

# Bat上でファイルを選択させる方法

## 概要

bat実行時、CUI上で特定のファイルを選択できるようにする方法

サンプルコードを記載する

## サンプルコード

``` bat
@echo off
setlocal enabledelayedexpansion

set "DIRECTORY=.\directory"

:: ユーザーにファイル選択を促すメッセージを表示
echo リストからファイルを選択してください:
echo.

set "index=1"
:: 特定のディレクトリ内のすべてのファイルをリストし、選択肢として表示
for %%f in (%DIRECTORY%\*) do (
    echo !index!. %%~nxf
    set "file!index!=%%~f"
    set /a "index+=1"
)

echo.
:: ユーザーに選択したいファイルの番号を入力させる
set /p "choice=選択するファイルの番号を入力してください: "

:: 選択されたファイルを特定
set "selected_file=!file%choice%!"

echo.
:: 選択されたファイルのパスを表示
echo 選択されたファイル: %selected_file%
pause

endlocal
```