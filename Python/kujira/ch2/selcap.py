from selenium import webdriver 

url = "https://www.aozora.gr.jp/cards/000081/files/46268_23911.html"

# Chromeのドライバを得る
browser = webdriver.Chrome()
#暗黙的な待機
browser.implicitly_wait(3)

#URL読み込み
browser.get(url)

#画面キャプチャ
browser.save_screenshot("Web.png")

#ブラウザ終了
browser.quit()