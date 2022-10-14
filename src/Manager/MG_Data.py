import json
from collections import OrderedDict
import pprint

class MGDataJson:
    def __init__(self) -> None:
        pass

    def JsonWriter(jsonName, data):
        with open("data/"+jsonName+".json", "w") as f:
            json.dump(data, f, indent=4 ,ensure_ascii=False)

    def JsonReader(jsonName):
        with open("data/"+jsonName+".json", "r") as f:
            data = json.load(f)
        return data

    def PlayerDataRW(Mode,data):
        if Mode == "r":
            with open("data/PlayerData.json", "r") as f:
                data = json.load(f)
            return data
        if Mode == "w":
            with open("data/PlayerData.json", "w") as f:
                json.dump(data, f, indent=4 ,ensure_ascii=False)
