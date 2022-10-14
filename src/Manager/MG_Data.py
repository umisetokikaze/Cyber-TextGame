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

    def PlayerDataRW(self,Mode,data):
        if Mode == "w":
            self.JsonWriter("PlayerData","")
        if Mode == "r":
            output = self.JsonReader("PlayerData",data)
            return output

    def ItemDataRW(self,Mode,data):
        if Mode == "w":
            self.JsonWriter("ItemData","")
        if Mode == "r":
            output = self.JsonReader("ItemData",data)
            return output



