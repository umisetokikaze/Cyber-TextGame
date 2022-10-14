import json
from collections import OrderedDict
import pprint

class MGDataJson:
    def __init__(self):
        self

    def JsonWriter(jsonName, data):
        with open("data/"+jsonName+".json", "w") as f:
            json.dump(data, f, indent=4 ,ensure_ascii=False)

    def JsonReader(jsonName):
        with open("data/"+jsonName+".json", "r") as f:
            data = json.load(f)
        return data

