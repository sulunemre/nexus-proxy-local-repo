from bs4 import BeautifulSoup
import urllib.request as urllib2
import re

html_page = urllib2.urlopen("https://pypi.org/simple/")
soup = BeautifulSoup(html_page, features="html.parser")

with open("pipAllPackagesList.txt", "w") as fout:
    for link in soup.findAll('a'):
        fout.write(link.string + "\n")

print("Pip metadata is ready.")
