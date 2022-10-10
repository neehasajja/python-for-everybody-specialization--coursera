# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
url = input('Enter - ')
html = urlopen(url,).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
numlist = list()
for tag in tags:
    # Look at the parts of a tag
    y = str(tag)
    num = re.findall('[0-9]+',y)
    numlist = numlist + num

sum = 0
for i in numlist:
    sum = sum + int(i)

print(sum)
