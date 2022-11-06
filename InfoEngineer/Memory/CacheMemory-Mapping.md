# メモリマッピング

キャッシュメモリに対してデータを割付する方式のまとめ

## ダイレクトマッピング (Direct Mapping)

1つのメモリブロックをキャッシュ内の単一の場所に割当する方式

基本的にはキャッシュメモリのブロック番号を以下で算出
> 主記憶のブロック番号 mod キャッシュメモリのブロック数

- メリット
  - 仕組みが単純なので速い
- デメリット
  - 演算して場所を決める方式のため、ヒット率が低い

## フルアソシアティブ (full associative)

associative : 連想

キャッシュメモリへの格納位置を演算で求めるのではなく、空いている場所を探し出しその位置にデータを保管する方式

- メリット
  - 空いてる場所に次々と入れるため、スペース効率が良い
- デメリット
  - 空いている場所を探索する必要があるため、速度に難がある
  - 装置の構造が複雑で実装も難しい

## セットアソシアティブ (set associative)

**ダイレクトマップとフルアソシアティブの中間にいるような方式**

連続したキャッシュブロックをセットとしてまとめ、
その中であればどこのブロックでも格納できるようにした方式

一定の計算式でセット番号を求め、セット内の空いている場所を探してその位置に格納する

セット内にN個のブロックを持つことを「Nウェイセットアソシアティブ」と呼ぶ

- メリット
  - メモリアドレスからキャッシュの格納位置が定まるため探索が容易
- デメリット
  - セットにするN個のブロックが多くなると回路・実装が複雑化する