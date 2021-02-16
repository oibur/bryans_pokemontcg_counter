import json
import os

my_list = []

for filename in os.listdir('cards'):
    with open(filename) as each_set:
        cards = json.load(str('cards/') + each_set)

print(cards)
