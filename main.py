import json
import time
import requests
import subprocess
import threading
import os

from utils import *

#def _start_AOdata():
#    print("Launching albiondata-client")
#    subprocess.Popen("ao_client")
#
#
#ao_data_project = threading.Thread(target=_start_AOdata)
#ao_data_project.start()
#
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


alg_KPP(data)
alg_KDPD(data)

sort(priority_list)

print("{:>25}|{:>25}|{:>25}|{:>25}".format("item id", "income", "algorythm", "quality"))
for i in range(len(priority_list)-1, -1, -1):
    if priority_list[i][2] == 0:
        print("{:>25}|{:>25}|{:>25}|{:>25}".format(priority_list[i][0], priority_list[i][1], "KPP", priority_list[i][3]))
for i in range(len(priority_list)-1, -1, -1):
    if priority_list[i][2] == 1:
        print("{:>25}|{:>25}|{:>25}|{:>25}".format(priority_list[i][0], priority_list[i][1], "KDPD", priority_list[i][3]))

