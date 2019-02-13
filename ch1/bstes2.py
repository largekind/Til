from bs4 import BeautifulSoup

html = """
<html><body>
    <h1 id = "title">スクレイピングとは？</h1>
    <p id = "body">Web ページを解析すること</p>
    <p>任意の個所を抽出</p>
</body></html>
"""

#HTML解析
soup = BeautifulSoup(html,'html.parser')

# findで取り出す
title = soup.find(id = "title")
body = soup.find(id = "body")

#text 表示
print("#titile ="+ title.string)
print("#body =" + body.string)

