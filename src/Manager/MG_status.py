from MG_Data import MGDataJson as MD
#statusManager
class MGStatus:
    def __init__(self) -> None:
        pass

    def InitStatus():
        
        MD.PlayerDataRW("w",D)

    def StatusSet(StatusName, Status):
        D = MD.PlayerDataRW("r", "")
        D["BaseData"][StatusName] = Status
        MD.PlayerDataRW("w",D)