# SQL

SQLで出てきて、よく忘れてる構文まとめ

## GRANT

※GRANT : 許す
複数のユーザーに対して、オブジェクトに関する特定の権限を付与するSQL

> GRANT 権限名 ON オブジェクト名
>　　　　TO { ユーザ名 | ロール名 | PUBLIC }
>　　　　[ WITH GRANT OPTION ]

アクセス権限取り消しの場合はREVOKE
