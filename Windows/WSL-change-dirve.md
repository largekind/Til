# WSLのドライブ変更法

1. 以下のコマンドを使用してドライブの情報をexportする
> wsl --export WSL環境名 出力ファイル.tar
2. ディストリブーションを消しておく
> wsl --unregister ディストリビューション名(Ubuntu等) 
3. 移動先の場所へimport
> wsl --import WSL環境名 [仮想ディレクトリのパス] exportしたWSLファイル.tar --version 2
