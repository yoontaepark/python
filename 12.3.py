# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen   #beautifulsoup을 쓰기 위한 명령어
from bs4 import BeautifulSoup        #beautifulsoup을 쓰기 위한 명령어 
import ssl                           #beautifulsoup을 쓰기 위한 명령어

# Ignore SSL certificate errors
ctx = ssl.create_default_context()  #에러발생 제거용 
ctx.check_hostname = False          #에러발생 제거용 
ctx.verify_mode = ssl.CERT_NONE     #에러발생 제거용  

url = input('Enter - ')                   #링크를 넣어야 하므로, 넣을 자리를 만들어줌
html = urlopen(url, context=ctx).read()   #그 url에서 contents를 읽는다
soup = BeautifulSoup(html, "html.parser") #contents를 beautifulsoup으로 파싱한다

# Retrieve all of the anchor tags
tags = soup('span')                       #span 이라는 tags를 찾아서
sum = 0                                   #변수 0으로 초기화
for tag in tags:                          #모든 span 라인들을 찾아서
    sum=sum+int(tag.contents[0])          #content들을 더한다
print(sum)                                #더한 sum값을 출력한다. 
