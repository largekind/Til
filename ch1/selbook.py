from bs4 import BeautifulSoup
fp = open("books.html",encoding="utf-8")
soup = BeautifulSoup(fp,"html.parser")

#CSSセレクタで検索
#ラムダ式 lambda 引数:実行式 の形で作れる 無名関数
sel = lambda q : print(soup.select_one(q).string)

sel("#nu") #idがnu
sel("li#nu") #liタグ、id=nu
sel("#bible #nu")#id=bible下のid=nu
sel("ul#bible > li#nu")
sel("li[id=nu]")
sel("li:nth-of-type(4)")