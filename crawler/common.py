import json
import os

def dump_jsonfile(filename, json_str):
    with  open(filename,'w',encoding="utf-8") as f:
        json.dump(json_str,f)

def load_jsonfile(filename):
    if not os.path.exists(filename):
        return []
    else:
        with open(filename,'r') as f:
            data = json.load(f)
            return data