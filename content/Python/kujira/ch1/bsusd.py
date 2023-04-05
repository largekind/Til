from bs4 import BeautifulSoup
import urllib.request as req 

#HTML取得
url  = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code=USDJPY=X"
res = req.urlopen(url)

#HTML解析
soup = BeautifulSoup(res,"html.parser")

#データ取得
price = soup.select_one(".stoksPrice").string
print("usd/jpy=",price)