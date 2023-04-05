from urllib.parse import urljoin

base = "http://example.com/html/a.html"

ulj = lambda base, html: print(urljoin(base,html))

ulj(base,"b.html")
ulj(base,"sub/c.html")
ulj(base,"../index.html")
ulj(base,"../img/hoge.html")
ulj(base,"../css/hoge.css")

ulj(base,"/hoge.html")
ulj(base,"http://kujirahand.com/wiki")
ulj(base,"//uta.pw/shodou")