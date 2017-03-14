from bs4 import BeautifulSoup
import urllib.request
with urllib.request.urlopen("http://starwars.wikia.com/wiki/Category:Jedi_Commanders") as url:
    r = url.read()
soup = BeautifulSoup(r, "html.parser")
jediPage = soup.get_text()
parsejedi(jediPage)
#print(soup.prettify()[1102:1618]) #prints based on some section
#print(soup.find_all('a')) # should print anything under the tag
#soup.prettify() #prints the whole html page
#print(soup.get_text()) # just prints the text

def parsejedi(htmltxt):
    htmltxt
    num = 0
    print("Jedi Generals Parsed " + num)
    return

