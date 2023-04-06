---
title: "BNF : Backus–Naur form"
date: 2023-04-05T00:00:00+09:00
tags: [InfoEngineer,Software]
---
# BNF : Backus–Naur form

バッカス・ナウア記法

以下のような記法
(以下の例であれば、a,b,cから成る文になる)
``` 
SYmbol := <rule> | <rule><syntax>
rule := a|b|c
```

繰り返しで使われる文などの表現をいくつかのBNFで組み合わせて作成する記法