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

savedir = "./" + keyword
flicker = FlickrAPI(key, secret, format='parsed-json')

result = flicker.photos.search(
  text = keyword,
  per_page = 400,
  media = 'photos',
  sort = 'relevance',
  extras = 'url_q, license',
)
```
