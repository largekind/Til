# テンプレートファイル

特定のhtmlに処理を入れ込んだり、挿入するような仕組み

DTL : Django Template language　を用いて作成する


## タイトル追加

``` html
{% block title %} ページタイトル {%endblock}
```