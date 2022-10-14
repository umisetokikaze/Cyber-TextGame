from MG_Data import MGDataJson as MDJ
class BaseItem():
    def __init__(self) -> None:
        pass

    def getItemData():
        D = MDJ.JsonReader("ItemsData")
        return D
    def setItemData(self,name, Dat):
        D = self.getItemData()
        D["ItemsData"][name] = Dat
        MDJ.JsonWriter(D)
