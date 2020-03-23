import requests
def getDataFromWynncraft():
    e = requests.get("https://api.wynncraft.com/public_api.php?action=territoryList")
    f = e.json()
    return f

def getSubAPI(mode):
    f = getDataFromWynncraft()
    return f["territories"][str(mode)]["guild"]

def checkISNerfuria(data):
    if data == "Nerfuria":
        return True
    else:
        return False

def getNumber():
    a = requests.get("https://api.wynncraft.com/public_api.php?action=guildStats&command=Nerfuria")
    b = a.json()
    return(b["territories"])

def checkClaim(name):
    x = getSubAPI(name)
    if checkISNerfuria(x)==True:
        return "claimed 🟢"
    else: return "not claimed 🔴"
checkClaim("Maro Peaks")