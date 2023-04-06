# pythonのマニュアルを再帰的にダウンロードしてゆく
##include

import os.path  # パスに関連するやつ,sleep,正規表現
import re
import time
from os import makedirs  # ディレクトリ作成用
from urllib.parse import *
from urllib.request import *

from bs4 import BeautifulSoup

#HTMLの解析を行ったかを判断する変数
proc_files = {}

# HTML内にあるリンクを抽出
def enum_links(html,base):
    soup = BeautifulSoup(html,"html.parser")
    links = soup.select("link[rel='stylesheet']") #CSSリンク
    links += soup.select("a[href]")#a hrefタグ
    result = []
    #href属性を取り出し、リンクを絶対パスへ
    for a in links:
        #href属性を取り出し絶対パス化
        href = a.attrs['href']
        url = urljoin(base,href)
        #resultへ追加
        result.append(url)
    #リンクの絶対パス配列を返す
    return result

# ファイルをダウンロード保存する関数
def download_file(url):
    o = urlparse(url)
    #保存するファイルパスを作成
    savepath = "./" + o.netloc + o.path
    #"/"パスならindex.html
    if re.search(r"/$",savepath):
        savepath += "index.html"
    #作成したパスからディレクトリ名へ
    savedir = os.path.dirname(savepath)
    #すでにダウンロード済みかexistで判断
    if os.path.exists(savepath): return savepath
    #ダウンロード先のディレクトリ作成
    if not os.path.exists(savedir):
        print("mkdir=",savedir)        
        makedirs(savedir)
    #ファイルダウンロード 例外処理でtry,except用いる
    try:
        print("download=",url)
        urlretrieve(url,savepath)
        time.sleep(1)#サーバー側に負荷させないように１秒置きにする
        return savepath
    except:
        #何らかのエラーが発生した場合ダウンロード失敗とする
        print("ダウンロード失敗:",url)
        return None

#HTMLを解析してダウンロードする関数
def analize_html(url,root_url):
    savepath = download_file(url)
    #is ->オブジェクト"id"が等価か調べる
    if savepath is None: return
    #オブジェクト in リストオブジェクト ->オブジェクトがリストに含まれているかどうか
    if savepath in proc_files: return #解析済みなら処理しない
    
    proc_files[savepath] = True
    print("analize_html=",url)
    #リンク抽出
    html = open(savepath,"r",encoding="utf-8").read()
    links = enum_links(html,url)

    for link_url in links:
        #リンクがルート以外のパスなら無視
        if link_url.find(root_url) != 0:
            if not re.search(r".css$",link_url): continue
        #HTMLかどうか
        if re.search(r".(html|htm)$",link_url):
            #再帰的にHTMLを解析
            analize_html(link_url,root_url)
            continue
        #それ以外
        download_file(link_url)

#直接実行する場合
if __name__ == "__main__":
    #urlを丸ごとダウンロード
    url = "http://docs.python.jp/3.5/library/"
    analize_html(url,url)
