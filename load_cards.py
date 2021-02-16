import json

import os

path_to_json = 'cards'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

print(json_files)

#for file in json_files:
#    with open(file) as sets:
#        print(sets)