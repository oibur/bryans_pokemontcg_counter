import json
import os


json_files = [pos_json for pos_json in os.listdir() if pos_json.endswith('.json')]

print(json_files)
#for _ in json_files:
#    with open(_) as set_name:
#        sets = json.load(set_name)
#        print(len(sets))


