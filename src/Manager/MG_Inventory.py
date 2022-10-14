from MG_Data import MGDataJson as MD

class PlayerInventory:

    def __init__(self) -> None:
        pass

    def InitInv():
        D = MD.PlayerDataRW("r", "")
        D["Inventory"] = {"none":"none",}
        MD.PlayerDataRW("w", D)
