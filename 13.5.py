import urllib.request, urllib.parse, urllib.error
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while(True):
    address = input('Enter location : ')
    if len(address)<1:
        break

    print('Retrieving', address)
    url = urllib.request.urlopen(address)
    data = url.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    sum =  0
    for i in range(len(js['comments'])):
        sum += js['comments'][i]['count']

    print('Count : ', len(js['comments']))
    print('Sum', sum)
