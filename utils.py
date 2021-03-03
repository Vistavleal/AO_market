from items import *

def alg_KPP(m_data):
    i = -1
    for iter in m_data:
        i += 1
        for item in complex_items:
            if iter["city"] == "Caerleon" and iter['quality'] == 1:
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


def sort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[0][1]
        less = [i for i in list[1:] if i[1] <= pivot]
        greater = [i for i in list[1:] if i[1] > pivot]
        return sort(less) + [pivot] + sort(greater)
