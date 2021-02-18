import json
import os

from dexlist_from_json import append_dex_number as adn

'''Loops through json files in a directory and uses adn to compile a master list'''
def master_dexlist(setnames):
    total_appearances = []
    for name in setnames:
        try:
            with open(name) as setname:
                cards = json.load(setname)
                total_appearances += adn(cards)
        except UnicodeDecodeError:
            pass
    total_appearances.sort()
    return total_appearances
