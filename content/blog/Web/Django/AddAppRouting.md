---
title: "ルーティングの追加法"
date: 2023-04-05T00:00:00+09:00
tags: [Web,Django]
categories: [Web]
---
# ルーティングの追加法

作成したappにルーティングを追加する方法

以下の流れのサイトを組むことを前提とする
 > Apps --- Aapp --- Bsite

1. Aappにurls.py追加。その先のルーティングを作成
``` python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Bsite/', views.predict, name='predict'),
]
```
2. Apps/urls.pyに上記Aappのurls.pyをInclude
``` python
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Aapp/', include('Aapp.urls')),
]
```