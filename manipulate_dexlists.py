import json
import os

from compile_dexlists import master_dexlist as md

set_names = [pos_json for pos_json in os.listdir() if pos_json.endswith('.json')]

data = md(set_names)

print(len(data))