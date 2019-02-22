#作詞掲示板へログイン→取得
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

#User & Pass set
USER = "JS-TESTER"
PASS = "ipCU12ySxI"

#セッション開始
session = requests.session()

#ログイン
login_info = {
    "username_mmlbbs6": USER, #User
    "password_mmlbbs6": PASS,
    "back": "index.php",
    "mml_id": "0"
}
url_login = "https://uta.pw/sakusibbs/users.php?action=login&m=try"
res = session.post(url_login,data=login_info)
res.raise_for_status() #エラー時ここで例外発生

# マイページのURLピックアップ
soup = BeautifulSoup(res.text,"html.parser")
a = soup.select_one(".islogin a")
if a is None:
    print("Not get Mypage")
    quit()
#相対URL -> 絶対URLへ
url_mypage = urljoin(url_login,a.attrs["href"]) #attrs["href"] -> attrsプロパティでhrefタグを取得
print("Mypage=",url_mypage)

#Access Mypage
res = session.get(url_mypage)
res.raise_for_status()

#お気に入りの詩を列挙
soup = BeautifulSoup(res.text,"html.parser")
links = soup.select("#favlist li > a")
for a in links:
    href = a.attrs["href"]
    title = a.get_text()
    print("-",title,">",href)

