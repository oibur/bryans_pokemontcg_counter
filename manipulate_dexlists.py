import json
import os

from compile_dexlists import master_dexlist as md

set_names = [pos_json for pos_json in os.listdir() if pos_json.endswith('.json')]
data = md(set_names)

occurences = {}

def count_occurences(information):
    for dexnum in information: 
        if dexnum[0] in occurences: 
            occurences[dexnum[0]] = occurences[dexnum[0]] + 1
        else: 
            occurences[dexnum[0]] = 1

count_occurences(data)

with open('pokedex.txt', 'r') as f:
    dex_names = [line.strip() for line in f]

def rename_keys(dict_, new_keys): 
    d1 = dict( zip( list(dict_.keys()), new_keys) )
    return {d1[oldK]: value for oldK, value in dict_.items()}

occurences = rename_keys(occurences, dex_names)

occurences = dict(sorted(occurences.items(), key=lambda item: item[1]))

with open('Pokemon Occurences.txt', 'w') as outfile:
    json.dump(occurences, outfile, indent=4)