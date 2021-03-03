import json
import time
import requests
from items import *

city_numb = 2
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

open ('AO_db.json', "wb").write(r.content)

with open('AO_db.json', 'r') as file:
    data = json.load(file)

with open('AO_db.json', 'w') as file:
    json.dump(data, file, indent=3)

MARKET_TAX = 0.10

priority_list = []

def alg_KPP(m_data):
    # Анализируем следующие позиции:
    # Стоимость производства, налоги и стоимость продажи
    i = -1
    for iter in m_data:
        i += 1
        for item in complex_items:
            if iter["city"] == "Caerleon":
                if iter["item_id"] == item and "BAG" in iter["item_id"]:
                    craft_cost = 8 * (m_data[i+city_numb]["sell_price_min"] + m_data[i+city_numb*2]["sell_price_min"])
                    income = iter["buy_price_max"] - craft_cost
                    if income <= 0:
                        continue
                    else:
                        priority_list.append([iter["item_id"], income, 0, iter["quality"]])


def alg_KDPD(m_data):
    bm_prices = {}
    for iter in m_data:
        if iter["city"] in "Black Market":
            bm_prices[iter["item_id"]] = iter["buy_price_max"]
            continue

        income = bm_prices[iter["item_id"]] - iter["sell_price_min"]
        if income <= 0:
            continue
        else:
            priority_list.append([iter["item_id"], income, 1, iter["quality"]])

#alg_KPP(data)
alg_KDPD(data)


print("Item_id\t\t\tIncome\tAlgorythm\tQuality") for i in range(0,len(priority_list)):
    print(
            priority_list[i][0],"\t", priority_list[i][1], "\t", priority_list[i][2], "\t\t", priority_list[i][3]
            )
