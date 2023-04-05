from bs4 import BeautifulSoup

html = """
<html><body>
<div id = "meigen">
    <h1>トルストイの名言</h1>
    <ul class = "items">
        <li>何時こころなんちゃら</li>
        <li>虚弱なんたら</li>
        <li>つよいよー</li>
    </ul>
</div>
</body></html>
"""

# html 解析
soup = BeautifulSoup(html,"html.parser")

#必要箇所をCSSクエリで取る
h1 = soup.select_one("div#meigen > h1").string
print("h1 =",h1)

#List部分取得
li_list = soup.select("div#meigen > ul.items > li")
for li in li_list:
    print("li =", li.string)