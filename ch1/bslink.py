from bs4 import BeautifulSoup

html = """
<html><body>
    <u1>
    <li><a href="http://uta.pw">uta</a></li>
    <li><a href="http:/oto.chu.jp">oto</a></li>
    </u1>
</body></html>
"""

# html解析
soup = BeautifulSoup(html,'html.parser')

#find allですべて取る
links = soup.find_all("a")

#link 一覧
for a in links:
    href = a.attrs['href']
    text = a.string
    print(text,">",href)