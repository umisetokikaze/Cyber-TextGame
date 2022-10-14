from MG_Data import MGDataJson as MD
#statusManager
class MGStatus:
    def __init__(self) -> None:
        pass

    def InitStatus():
        D = {"BaseData":{"name":"Base","HP":100,"RAM":100,"CLOCK":1,"ATK":10,"INT":10,"CONC":0,"DEF":10,"AGI":10,"LUK":10,"EXP":0,"LV":1}}
        MD.PlayerDataRW("w",D)

    def StatusSet(StatusName, Status):
        D = MD.PlayerDataRW("r", "")
        D["BaseData"][StatusName] = Status
        MD.PlayerDataRW("w",D)