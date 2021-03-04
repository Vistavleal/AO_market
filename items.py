item_deps = {
        "T3_BAG": ["T3_CLOTH", "T3_LEATHER"],
        "T4_BAG": ["T4_CLOTH", "T4_LEATHER"],
        "T5_BAG": ["T5_CLOTH", "T5_LEATHER"],
        "T6_BAG": ["T6_CLOTH", "T6_LEATHER"],
        "T7_BAG": ["T7_CLOTH", "T7_LEATHER"],
        "T8_BAG": ["T8_CLOTH", "T8_LEATHER"],
        }

with open('items.txt', 'r') as file:
    item_id = file.readline()

complex_items = [
        "T4_BAG", "T5_BAG", "T6_BAG", "T7_BAG", "T8_BAG", "T3_BAG",
        ]

city_numb = 2

priority_list = []

_in_game_name = {
        "T3_BAG": "T3 Bag",
        "T4_BAG": "T4 Bag",
        "T5_BAG": "T5 Bag",
        "T6_BAG": "T6 Bag",
        "T7_BAG": "T7 Bag",
        "T8_BAG": "T8 Bag",

        "T3_CAPE": "T3 Cape",
        "T4_CAPE": "T4 Cape",
        "T5_CAPE": "T5 Cape",
        "T6_CAPE": "T6 Cape",
        "T7_CAPE": "T7 Cape",
        "T8_CAPE": "T8 Cape",

        "T3_ARMOR_CLOTH_SET1": "T3 Scholar robe",
        "T4_ARMOR_CLOTH_SET1": "T4 Scholar robe",
        "T5_ARMOR_CLOTH_SET1": "T5 Scholar robe",
        "T6_ARMOR_CLOTH_SET1": "T6 Scholar robe",
        "T7_ARMOR_CLOTH_SET1": "T7 Scholar robe",
        "T8_ARMOR_CLOTH_SET1": "T8 Scholar robe",

        "T3_ARMOR_CLOTH_SET2": "T3 Cleric robe",
        "T4_ARMOR_CLOTH_SET2": "T4 Cleric robe",
        "T5_ARMOR_CLOTH_SET2": "T5 Cleric robe",
        "T6_ARMOR_CLOTH_SET2": "T6 Cleric robe",
        "T7_ARMOR_CLOTH_SET2": "T7 Cleric robe",
        "T8_ARMOR_CLOTH_SET2": "T8 Cleric robe",

        "T3_ARMOR_CLOTH_SET3": "T3 Mage robe",
        "T4_ARMOR_CLOTH_SET3": "T4 Mage robe",
        "T5_ARMOR_CLOTH_SET3": "T5 Mage robe",
        "T6_ARMOR_CLOTH_SET3": "T6 Mage robe",
        "T7_ARMOR_CLOTH_SET3": "T7 Mage robe",
        "T8_ARMOR_CLOTH_SET3": "T8 Mage robe",

        "T4_ARMOR_CLOTH_ROYAL": "T4 Royal robe",
        "T5_ARMOR_CLOTH_ROYAL": "T5 Royal robe",
        "T6_ARMOR_CLOTH_ROYAL": "T6 Royal robe",
        "T7_ARMOR_CLOTH_ROYAL": "T7 Royal robe",
        "T8_ARMOR_CLOTH_ROYAL": "T8 Royal robe",

}
