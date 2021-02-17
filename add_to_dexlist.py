import json
import os

from dexlist_from_json import append_dex_number as adn

joined_dexlist = []

def join_lists(*args):
    for name in args:
        with open(name) as setname:
            cards = json.load(setname)
            joined_dexlist += adn(cards)
            return joined_dexlist
            print(joined_dexlist)

join_lists('Base.json', 'Base Set 2.json')