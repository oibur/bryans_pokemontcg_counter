import json
import os

'''Loops through a sets json dictionary and returns the Dex# for all Pokemon in that set as a list'''
def append_dex_number(set_json):
    dex_list = []
    for item in set_json:
        try:
            dex_list.append(item["nationalPokedexNumbers"])
        except KeyError:
            pass
    return dex_list