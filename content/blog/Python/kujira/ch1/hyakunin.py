#!/user/bin/env pythons3

#read library
import sys
import urllib.request as req #urlib.requestライブラリをreq名で利用
import urllib.parse as parse

# コマンドライン引数取得 要sysモジュール
if len(sys.argv) <= 1:
   print("USAGE: hyakunin.py (keyword)") 
   sys.exit()
keyword = sys.argv[1]

#パラメータにURIエンコード
API = "http://api.aoikujira.com/hyakunin/get.php"
query = {
    "fmt": "ini",
    "key": keyword
}
params = parse.urlencode(query)
url = API + "?" + params
print("url=",url)

# download
# with文で初期処理~終了処理を自動化してもらう
with req.urlopen(url) as r:
   b = r.read()
   data = b.decode('utf-8')
   print(data)
