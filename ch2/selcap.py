from selenium import Webdriver

url = "https://www.aozora.gr.jp/cards/000081/files/46268_23911.html"

#PhantomJSは既にseleniumでは非推奨なのでgeckoDriver(Firefox)を用いる
#何故かChoromeDriverは自環境でcondaが必ず破損するので回避　原因不明
browser = Webdriver.Firefox()

#暗黙的な待機
browser.implicitly_wait(3)

#URL読み込み
browser.get(url)

#画面キャプチャ
browser.save_screenshot("Web.png")

#ブラウザ終了
browser.quit()