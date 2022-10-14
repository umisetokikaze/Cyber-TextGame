import MG_Data as MD
import MG_Status as SM
class RegistNewPlayer:
    def __init__(self) -> None:
        pass

    def RGStatus():
        D = {"BaseData":{"name":"Base","HP":100,"RAM":100,"CLOCK":1,"ATK":10,"INT":10,"CONC":0,"DEF":10,"AGI":10,"LUK":10,"EXP":0,"LV":1}}
        MD.MGDataJson.JsonWriter("PlayerData", D)

    def RGInv():
        D = MD.MGDataJson.JsonReader("PlayerData")
        D["Inventory"] = {"none":"none",}
        MD.MGDataJson.JsonWriter("PlayerData", D)

    def RGPlayerName(name):
        SM.MGStatus.StatusSet
    RGStatus()
    RGInv()
    RGPlayerName(input("     プレイヤーの名前を入力してください     "))