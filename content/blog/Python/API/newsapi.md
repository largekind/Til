---
title: "NewsAPI"
date: 2023-04-21T22:43:59+09:00
categories: [Python]
tags : [Python , API]
---

# NewsAPI

## 概要

[サイトのリンク](https://newsapi.org/)

ニュース情報を取得できるAPIの１つ。json形式で必要な情報を記述し、requestsを用いて処理を行うことで、
ほしい情報をリスト形式で返却してくれる

## サンプルコード

``` Python

import requests
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# NewsAPIキーを取得
API_KEY = "your_api_key_here"

def fetch_cryptocurrency_news(api_key):
    url = "https://newsapi.org/v2/everything"
    
    # Bitcoinに関連するニュースを検索
    parameters = {
        'q': '検索するキーワード',
        'language': 'en', #国 日本であればjp 米国ならen
        'sortBy': 'publishedAt', # ソート順
        'apiKey': api_key #APIキー
    }
    
    response = requests.get(url, params=parameters)
    data = response.json()
    
    # 必要なデータを抽出
    news_data = []
    for article in data['articles']:
        news = {
            'title': article['title'],
            'date': article['publishedAt'],
            'url': article['url']
        }
        news_data.append(news)
    
    return news_data

```