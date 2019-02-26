import urllib.request as req
import os.path,random
import json

#json data download
url = ""
savename = "hyakunin.json"
if not os.path.exists(url):
    req.urlretrieve(url,savename)

#json analysis
data = json.load(open(savename,"r",encoding="utf-8"))

#random output
r = random.choice(data)
print(r['kami'],r['simo'])