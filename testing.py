import json
import os

from json_to_list import append_dex_number as adn

with open('cards\Base.json') as base_set:
    cards1 = json.load(base_set)

adn(cards1)

with open('cards\Jungle.json') as base_set:
    cards2 = json.load(base_set)

adn(cards2)

print


#import the data to be used as list
    #using import json
    #using external API

#repeat for all json files
    #can I do all at once, or write a function to loop throuhg files?

#modify the list down to just ["name":"nationalPokedexNumber"]

#count the occurance of each pokemon and return sorted list

#Visualize the data in a graph sorted by Dex#
