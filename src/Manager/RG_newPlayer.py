import MG_Data as MD
class RegistNewPlayer:
    def __init__(self, name):
        self

    def RGStatus():
        D = {"name":"Base","HP":100,"RAM":100,"CLOCK":1,"ATK":10,"INT":10,"CONC":0,"DEF":10,"AGI":10,"LUK":10,"EXP":0,"LV":1}
        MD.MGDataJson.JsonWriter("PlayerData", D)

    def RGPlayerName(name):
        D = MD.MGDataJson.JsonReader("PlayerData")
        D["name"] = name
        MD.MGDataJson.JsonWriter("PlayerData", D)


    print("初期ステータスを登録...")
    RGStatus()
    print("登録完了")
    RGPlayerName(input("     プレイヤーの名前を入力してください     "))
    print("登録完了")