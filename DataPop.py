#################################################################
# Project By: Alan Padilla Chua
# This script basically takes in pages from the starwars wiki
# gets the names and will eventually populate a database
# with the names of Jedi, Clones, Driods, And Other Characters
# eventually I want to use these names to create a name generator
#################################################################
import urllib.request

from bs4 import BeautifulSoup


def parsejedi(htmltxt):
    htmltxt.split(" ")
    num = 0
    print("Jedi Generals Parsed " + str(num))
    num += 1
    return

with urllib.request.urlopen("http://starwars.wikia.com/wiki/Category:Jedi_Commanders") as url:
    r = url.read()
soup = BeautifulSoup(r, "html.parser")
jediPage = soup.get_text()


#parsejedi(jediPage)
#print(soup.prettify()[1102:1618]) #prints based on some section
#print(soup.find_all('a')) # should print anything under the tag
#soup.prettify() #prints the whole html page
#print(soup.get_text()) # just prints the text



