#自作 適当にざくアクの防具データを取り込めるかの実験用
from bs4 import BeautifulSoup
import urllib.request as req
#tr.atwiki_tr~~ → 各要素
##wikibody > table:nth-child(9) > tbody:nth-child(2) > tr.atwiki_tr_even.atwiki_tr_2 > td:nth-child(2) > a
#wikibody > table:nth-child(9)#wikibody > table:nth-child(9) > tbody:nth-child(2)
#wikibody > table:nth-child(9)
url = "https://www34.atwiki.jp/zakuaku/pages/22.html"
res = req.urlopen(url)

#tableの取得
soup = BeautifulSoup(res,"html.parser")
tablelist = soup.select("table > tr")

#print(tablelist)
for tr in tablelist:
    tr.select("td")
    for li in tr:
        print(li)