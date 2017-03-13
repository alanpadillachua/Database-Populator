from bs4 import BeautifulSoup
import urllib.request
with urllib.request.urlopen("http://starwars.wikia.com/wiki/Category:Jedi_Commanders") as url:
    r = url.read()
soup = BeautifulSoup(r, "html.parser")

print(type(soup))



