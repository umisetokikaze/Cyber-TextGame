import MG_Status as SM
import MG_Inventory as IM
class RegistNewPlayer:
    def __init__(self) -> None:
        pass

    def RGPlayerName(name):
        SM.MGStatus.StatusSet("name", name)

    SM.MGStatus.InitStatus()
    IM.PlayerInventory.InitInv()
    RGPlayerName(input("     プレイヤーの名前を入力してください     "))