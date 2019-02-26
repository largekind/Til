from bs4 import BeautifulSoup
import urllib.request as req 
import os.path

#xml download
url = ""
savename = "shelter.xml"
if not os.path.exists(savename):
    req.urlretrieve(url,savename)

#BeautifulSoupで解析
xml = open(savename,"r",encoding="utf-8")
soup = BeautifulSoup(xml,'html.parser')

#データを各区で確認
info = {}
for i in soup.find_all("shelter"):
    name = i.find('name').string
    ward = i.find('ward').string
    addr = i.find('address').string
    note = i.find('note').string

    if not (word in info):
        info[ward] = []
    info[word].append(name)

#区ごとで防災拠点表示
for word in info.keys():
    print("+",word)
    for name in info[ward]:
        print("| - ",name)
