import MG_Data as MD
#statusManager
class MGStatus:
    def __init__(self) -> None:
        pass

    def StatusSet(StatusName, Status):
        D = MD.MGDataJson.JsonReader("PlayerData")
        D["BaseData"][StatusName] = Status
        MD.MGDataJson.JsonWriter("PlayerData", D)