# docker コマンド一覧


| コマンド	| 目的 |
| ---- | ---- |
|docker-compose up -d|	Docker コンテナを起動する|
|docker-compose exec app bash	|コンテナの中のコンソールに入る[^1]|
|docker-compose ps -a	|コンテナの一覧を見る|
|docker-compose down	|コンテナを終了・破棄する|

[^1]: 以下では無いので要注意 **composeを忘れないようにする**
    > docker exec app bash
