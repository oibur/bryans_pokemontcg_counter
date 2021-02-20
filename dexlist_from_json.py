import json
import os

def append_dex_number(set_json):
    '''Loops through a sets json dictionary and returns the Dex# for all Pokemon in that set as a list'''
    dex_list = []
    for item in set_json:
        try:
            dex_list.append(item["nationalPokedexNumbers"])
        except KeyError:
            pass
    return dex_list