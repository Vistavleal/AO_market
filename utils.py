from items import *
from items import _in_game_name
from datetime import datetime

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

def output(priority_list):
    print("{:>25}|{:>25}|{:>25}|{:>25}".format("item id", "income", "algorythm", "quality"))
    for i in range(len(priority_list)-1, -1, -1):
        if priority_list[i][2] == 0:
            print("{:>25}|{:>25}|{:>25}|{:>25}".format(
                    _in_game_name[priority_list[i][0]],
                    priority_list[i][1],
                    "KPP",
                    priority_list[i][3]
                )
            )
    for i in range(len(priority_list)-1, -1, -1):
        if priority_list[i][2] == 1:
            print("{:>25}|{:>25}|{:>25}|{:>25}".format(
                    _in_game_name[priority_list[i][0]],
                    priority_list[i][1],
                    "KDPD",
                    priority_list[i][3],
                )
            )


def sort_outdated(m_data):
    temp = datetime.now()
    temp_month = temp.month - 1
    if temp_month < 10:
        temp_month = "0" + str(temp_month)
        arg = "%Y-" + temp_month + "-%dT%H:%M:%S"
    else:
        arg = "%Y-" + str(month) + "-%dT%H:%M:%S"

    _date = temp.strftime(arg)
    for item in m_data:
        if item["sell_price_min_date"] < _date or \
                item["sell_price_min_date"] in "0001-01-01T00:00:00":
            item["sell_price_min"] = 999999999
        if item["buy_price_max_date"] < _date or \
                item["buy_price_max_date"] in "0001-01-01T00:00:00":
            item["buy_price_max"] = 0












