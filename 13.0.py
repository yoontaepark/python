import urllib.request                         
import xml.etree.ElementTree as ET

url = input('Enter location: ')             #enter url: http://py4e-data.dr-chuck.net/comments_731540.xml
response = urllib.request.urlopen(url)      #save url
tree = ET.fromstring(response.read())       #use fromstring to transfer tree type(to use xml data)
total = sum([int(count.text) for count in tree.findall('comments/comment/count')])    #sum all text in comments/comment/count 
print(total)
