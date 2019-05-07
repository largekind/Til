#library load
from bs4 import BeautifulSoup

#解析したいHTML
html = """
<html><body>
    <h1>スクレイピングとは？</h1>
    <p>Web ページを解析すること</p>
    <p>任意の個所を抽出</p>
</body></html>
"""

#HTML解析
soup = BeautifulSoup(html,'html.parser')

#任意の場所を抽出
h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling

#上で抽出したテキストを表示
print("h1 =" + h1.string)
print("p =" + p1.string)
print("p ="+ p2.string)