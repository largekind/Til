---
title: "emmet"
date: 2023-04-05T00:00:00+09:00
tags: [Web,html]
categories: [Web]
---
# emmet

htmlを滅茶苦茶書きやすくするVscode付属の機能

## Installation

Vscodeの設定欄にある以下2つを有効化
``` json
"emmet.triggerExpansionOnTab": true, //Tabでのemmet補完
"emmet.useInlineCompletions": true,  //emmetのInline補完
```

## HTML5スタート

以下のように入力
> html:5

すると、以下のようにテンプレートが入力される
``` html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  
</body>
</html>
```
