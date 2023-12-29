---
title: "Pyenv Install Bat"
date: 2023-12-29T09:48:22+09:00
draft: true
---

# Pyenv Install Bat

## 概要

pyenvをインストールするbatを作成しようとした備忘録

## コード

``` bat
@echo off

:: pyenvのインストール
echo Installing pyenv...
pip install pyenv-win --target %USERPROFILE%\.pyenv\pyenv-win

:: 環境変数PYENV_ROOTの設定
set PYENV_ROOT=%USERPROFILE%\.pyenv\pyenv-win

:: PYENV_ROOTが未設定の場合にのみ設定
powershell -Command "if ([System.Environment]::GetEnvironmentVariable('PYENV_ROOT', [System.EnvironmentVariableTarget]::User) -eq $null) {[System.Environment]::SetEnvironmentVariable('PYENV_ROOT', '%PYENV_ROOT%', [System.EnvironmentVariableTarget]::User)}"

:: PATHにpyenvが含まれていなければ追加
powershell -Command "$envPath = [System.Environment]::GetEnvironmentVariable('PATH', [System.EnvironmentVariableTarget]::User); if (-not $envPath.Contains('%PYENV_ROOT%\bin')) {[System.Environment]::SetEnvironmentVariable('PATH', '%PYENV_ROOT%\bin;' + $envPath, [System.EnvironmentVariableTarget]::User)}"

:: pyenvの初期化
call %PYENV_ROOT%\bin\pyenv init -

echo pyenv installation and setup completed.
```