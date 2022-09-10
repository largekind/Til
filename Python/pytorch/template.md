# テンプレートファイル

特定のhtmlに処理を入れ込んだり、挿入するような仕組み

DTL : Django Template language　を用いて作成する


## タイトル追加

``` django
{% block title %} ページタイトル {%endblock}
```

## 外部ファイルの読み込み

ベースとなるhtmlに埋め込む形式で作成する場合の記載

``` django
{% extend 'base.html' %} 
{% block title %}タイトル名称{% endblock %}
{% block content%}
  contentブロック内に入れ込みたいhtml内容
{% endblock %}
```
