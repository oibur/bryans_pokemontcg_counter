import json

with open('cards\Base.json') as base_set:
    cards = json.load(base_set)

card_dict = cards[0]

for _ in card_dict:
    print(card_dict["name"])

#import the data to be used as list
    #using import json
    #using external API

#repeat for all json files
    #can I do all at once, or write a function to loop throuhg files?

#modify the list down to just ["name":"nationalPokedexNumber"]

#count the occurance of each pokemon and return sorted list

#Visualize the data in a graph sorted by Dex#
