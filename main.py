import json
import time
import requests
import subprocess

from utils import *
from utils import output, sort_outdated

"""
Thetford
Fort Sterling
Lymhurst
Bridgewatch
Martlock
BlackMarket
"""

url = 'https://www.albion-online-data.com/api/v2/stats/prices/' + \
item_id + \
'?locations=BlackMarket,Caerleon&qualities=1'
r = requests.get(url, allow_redirects=False)

open ('AO_bd.json', "wb").write(r.content)

with open('AO_bd.json', 'r') as file:
    data = json.load(file)

sort_outdated(data)

# Представление бд в читаемой форме
with open('AO_bd.json', 'w') as file:
    json.dump(data, file, indent=3)


#for iter in data:
#    if iter["city"] not in 'Black Market':
#        print ("{:<25} SELL: {:<10} BUY: {:<10} QUALITY: {:<5}".format(
#                iter['item_id'],
#                iter['sell_price_min'],
#                iter["buy_price_max"],
#                iter["quality"]
#                ))


#alg_KPP(data)
#alg_KDPD(data)

#sort(priority_list)
#output(priority_list)

