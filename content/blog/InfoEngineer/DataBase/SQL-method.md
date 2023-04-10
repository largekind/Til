---
title: "SQL"
date: 2023-04-05T00:00:00+09:00
tags: [InfoEngineer,DataBase]
categories: [InfoEngineer]
---
# SQL

SQLで出てきて、よく忘れてる構文まとめ

## GRANT

※GRANT : 許す
複数のユーザーに対して、オブジェクトに関する特定の権限を付与するSQL

> GRANT 権限名 ON オブジェクト名
>　　　　TO { ユーザ名 | ロール名 | PUBLIC }
>　　　　[ WITH GRANT OPTION ]

アクセス権限取り消しの場合はREVOKE

## UNIQUE

unique : uni- 1つの + -icus  ～に関連する -> 唯一の

データベースにデータを追加したり更新する際に、列や列のグループに格納される値が表内のすべての行で一意となるように要求する制約

NULL は許すが、同じ値は許さない

## CHECK

追加・更新されるデータが問題ないかチェックする字句

## REFERENCES

reference : re- 後ろに + fero 生む = refer 言及する + -ence : 名詞化 ->  注意、出典  参照 リファレンス

その名の通り、外部キーの制約。2つの表間に関係を持たせ、外部参照されるテーブルに格納されるデータを制御する字句

## RESTRICT 

restrict : re- 後ろに + strict 押す -> 制限する

外部参照される側のレコードが解除、更新される時の動作を指定する字句
