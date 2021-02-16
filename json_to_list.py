import json
import os

master_list = []

'''Loops through each sets json dictionary and appends the Dex# value of each Pokemon to a list'''
def append_dex_number(x):
    for item in x:
        try:
            master_list.append(item["nationalPokedexNumber"])
        except KeyError:
            pass
    return master_list


