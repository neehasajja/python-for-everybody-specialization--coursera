import urllib.request
from bs4 import BeautifulSoup

url = input("Enter url-")
rep = int(input("Enter repeat count:"))
pos = int(input('Enter position'))

while rep > 0:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    print("Retrieving:", tags[pos-1].get("href", None))
    url = tags[pos-1].get("href", None)
    rep = rep - 1
