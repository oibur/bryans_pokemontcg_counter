import json
import os

from compile_dexlists import master_dexlist as md

occurences = dict()
set_names = [pos_json for pos_json in os.listdir() if pos_json.endswith('.json')]
data = md(set_names)

def ta_da(information):
    for dexnum in information: 
        if dexnum[0] in occurences: 
            occurences[dexnum[0]] = occurences[dexnum[0]] + 1
        else: 
            occurences[dexnum[0]] = 1

ta_da(data)

with open('Pokemon Occurences.txt', 'w') as outfile:
    json.dump(occurences, outfile, indent=4)