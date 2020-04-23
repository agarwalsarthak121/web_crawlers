stockDict = {"Appolo Hospital" : 10,"Astral" : 5,"EnginersIndiaLtd":441,"HDFCBANK":7,"IRCON":100,"JUSTDIAL":20,"ONGC":50,"RADICO":20,"TCS":5,"VBL":30}

target_price = 0
for stock in stockDict:
    target = int(input("Enter Target Price for "+stock+" : "))
    target_price = target_price + target*stockDict[stock]

funds = int(input("Enter Funds Available : "))

print("Total Value : " + str(target_price + funds))
