import json
import time
import requests


#url = 'https://www.albion-online-data.com/api/v2/stats/prices/T4_BAG?locations=Thetford,Caerleon&qualities=1'
#r = requests.get(url, allow_redirects=False)
#
#open ('AO_db.json', "wb").write(r.content)

with open('AO_db.json', 'r') as file:
    data = json.load(file)

with open('AO_db.json', 'w') as file:
    json.dump(data, file, indent=3)


