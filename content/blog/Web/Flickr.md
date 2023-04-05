# Flickr 

海外の写真共有アプリ
[link](https://www.flickr.com/)

APIを使用することで画像収集が可能になる

## 環境構築

以下実行

``` bash
pip install flickrapi
```

## pythonでの実行方法

flickrapiをimportして使用する。
詳細はdocumentでも検索

``` python
# 必要情報のインポート
from flickrapi import FlickrAPI

key,secret = 適当に必要な情報を格納(APIとして取得しておく)

# API取得用のインスタンスを作成
savedir = "./" + keyword
flicker = FlickrAPI(key, secret, format='parsed-json')

# 画像の検索
result = flicker.photos.search(
  text = keyword, # 検索ワード
  per_page = 400, # 検索するページ数
  media = 'photos', #検索する媒体 画像/動画etc
  sort = 'relevance', # 画像のソート順
  extras = 'url_q, license', #その他 必要情報
)
```
