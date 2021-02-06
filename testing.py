import json

base_set = open('cards\Base.json','r')
cards = base_set.read()

obj = json.loads(cards)
print(obj['name'])