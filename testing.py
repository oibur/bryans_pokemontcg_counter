import json
import os

master_list = []
set_names = []

set_names = [pos_json for pos_json in os.listdir() if pos_json.endswith('.json')]
print(set_names)

from dexlist_from_json import append_dex_number as adn

with open('Base.json') as base:
    cards1 = json.load(base)
    master_list += adn(cards1)

with open('Ancient Origins.json') as jungle:
    cards2 = json.load(jungle)
    master_list += adn(cards2)

print(master_list)


#import the data to be used as list
    #using import json
    #using external API

#repeat for all json files
    #can I do all at once, or write a function to loop throuhg files?

#modify the list down to just ["name":"nationalPokedexNumber"]

#count the occurance of each pokemon and return sorted list

#Visualize the data in a graph sorted by Dex#
