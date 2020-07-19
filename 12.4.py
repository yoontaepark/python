# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))-1 #position의 경우 0부터 시작인데, 첫사람을 1로 가정하므로 3번째 사람은 실제로 '2'를 찾아줘야 함
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
Sequence = []
# Retrieve all of the anchor tags
tags = soup('a')
for i in range(count):
    link = tags[position].get('href', None)
    print("Retrieving:",link)
    Sequence.append(tags[position].contents[0])
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
print(Sequence[-1])  #getting last name [-1]
