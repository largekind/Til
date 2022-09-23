# HTTPサーバー建て方(Python + docker)

超簡単にサーバーを立てる方法

1. 適当にサーバー用のディレクトリ作成、index.htmlを置く
2. docker-composeに以下追加。docker上のポートとホストPCのポートをつなぐ
``` docker
    ports:
      - "8000:8000"
```
3.  作成したディレクトリは以下で以下コマンド実行
> python -m http.server 8000
