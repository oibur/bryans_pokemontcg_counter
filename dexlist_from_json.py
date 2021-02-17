import json
import os

'''Loops through each sets json dictionary and appends the Dex# value of each Pokemon to master_list'''
def append_dex_number(set_json):
    dex_list = []
    for item in set_json:
        try:
            dex_list.append(item["nationalPokedexNumber"])
        except KeyError:
            pass
    return dex_list