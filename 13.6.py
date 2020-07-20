import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)  #url 뒤에다 추가 url 붙여주기

    print('Retriveing', url)
    uh = urllib.request.urlopen(url, context=ctx)  #get data from url that I requested
    data = uh.read().decode() #decoding(쉽게...압축해제)
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)    #transfer data into dictionary
    except:
        js = None

    print(data)  #뭔지 모를때는 그냥 print를 해서 데이터를 쭉 읽어본다음 판단한다(place_id가 어디에 있는지 몰라서 확인해보고 코드 추가 작성)

    if not js or 'status' not in js or js['status'] != 'OK':
        print('===== Failure To Retrive =====')
        print(data)
        continue

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)

    location = js['results'][0]['formatted_address']
    print(location)

    place_id = js['results'][0]['place_id']   #원하는 place_id 부분을 찾아서
    print(place_id)                           #출력한다 
