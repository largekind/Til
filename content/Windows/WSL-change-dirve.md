# WSLのドライブ変更法

## ドライブの移動

1. 以下のコマンドを使用してドライブの情報をexportする
> wsl --export WSL環境名 出力ファイル.tar
2. ディストリブーションを消しておく
> wsl --unregister ディストリビューション名(Ubuntu等) 
3. 移動先の場所へimport
> wsl --import WSL環境名 [仮想ディレクトリのパス] exportしたWSLファイル.tar --version 2

## ホームディレクトリの変更

**ユーザーのデフォルト指定変更前に行うこと**
ホームディレクトリ変更するユーザー名でログインしていると変更不可なので注意

1. rootユーザーで入って以下コマンド実行
> usermod -d (変更先ホームDirectory) (ユーザー名)

## ユーザーのデフォルト指定変更

初期状態だとユーザーがroot固定という面倒なことになる。

そのため、通常ユーザを作成する手順を記載する

1. ユーザーを作成する 以下コマンド実行
> sudo useradd ユーザー名
2. /etc/wsl.confに最初にログインするユーザーを追記する 
``` bash
# /etc/wsl.confに記載
[user]
default = larksiper
```