from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
import requests

def isDirectory(url):
    if(url.endswith('/')):
        return True
    else:
        return False

# Store XML links in a list
xmlLinks = []
# https://stackoverflow.com/a/51703468/5964489
def findLinks(url):
    page = requests.get(url).content
    bsObj = BeautifulSoup(page, 'html.parser')
    maybe_directories = bsObj.findAll('a', href=True)

    for link in maybe_directories:
        if(isDirectory(link['href'])):
            newUrl = url + link['href']
            findLinks(newUrl) #recursion happening here
        else:
            if(link['href'].endswith('maven-metadata.xml')):
                xmlLinks.append(url + link["href"])
                print(url + link["href"])


startUrl = "https://repo1.maven.org/maven2/ant/" # Remove ant on production
findLinks(startUrl)

# Parse XMLs and save group:artifact:version to a text file
with open('mavenAllPackagesList.txt', "w") as file:
    for item in xmlLinks:
        text = requests.get(item).text

        metadata = ""
        for line in text.splitlines():
            if line.startswith("  <groupId>"):
                metadata = metadata + line[11:-10]
            elif line.startswith("  <artifactId>"):
                metadata = metadata + ":" + line[14:-13]
        metadata = metadata + ":" + "use-latest-versions"
        file.write(metadata + "\n")
print("Maven metadata is ready.")        
