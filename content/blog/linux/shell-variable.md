---
title: "shellScriptでの変数追加"
date: 2023-04-05T00:00:00+09:00
tags: ["linux"]
categories: ["linux"]
---
# shellScriptでの変数追加

.shなどで一時的に環境変数を用意したいときの備忘録

## 方法

以下のように追加するだけ。 **※スペースは入れないこと**
> val="aiueo"

その後、$マークで利用可能になる(2通りの方法がある)
> \${val}
> \$val