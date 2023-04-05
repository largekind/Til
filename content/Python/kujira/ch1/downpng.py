import urllib.request

#design url and save pass
url = "http://uta.pw/shodou/img/28/214.png"
savename = "tes.png"

#download
urllib.request.urlretrieve(url,savename)
print("Saved!\n")