from bs4 import BeautifulSoup
fp = open("fruits-vegetables.html",encoding="utf-8").read()
soup = BeautifulSoup(fp,"html.parser")

#CSS select
selone = lambda q : print(soup.select_one(q).string)
sel = lambda q , r: print(soup.select(q)[r].string)

selone("li:nth-of-type(8)")
selone("#ve-list > li:nth-of-type(4)")
sel("#ve-list > li[data-lo='us']",1)
sel("#ve-list > li.black",1)

#find method select
cond = {"data-lo":"us","class":"black"}
print(soup.find(id="ve-list").find("li",cond).string)