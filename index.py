import discord
import requests
import datetime

from config import TOKEN
from commands.commandslist import CommandLists as command

def maropeaks():
    e = requests.get("https://api.wynncraft.com/public_api.php?action=territoryList")
    f = e.json()
    return f["territories"]["Maro Peaks"]["guild"]

def checkmaro():
    x = maropeaks()
    if x == "Nerfuria":
        return "true"
    else:
        return "false"

def selchar():
    e = requests.get("https://api.wynncraft.com/public_api.php?action=territoryList")
    f = e.json()
    return f["territories"]["Selchar"]["guild"]

def checkselchar():
    x = selchar()
    if x == "Nerfuria":
        return "true"
    else:
        return "false"

def deadNW():
    e = requests.get("https://api.wynncraft.com/public_api.php?action=territoryList")
    f = e.json()
    return f["territories"]["Dead Island North West"]["guild"]

def checkdeadNW():
    x = deadNW()
    if x == "Nerfuria":
        return "true"
    else:
        return "false"

def deadNE():
    e = requests.get("https://api.wynncraft.com/public_api.php?action=territoryList")
    f = e.json()
    return f["territories"]["Dead Island North East"]["guild"]

def checkdeadNE():
    x = deadNE()
    if x == "Nerfuria":
        return "true"
    else:
        return "false"

def deadSE():
    e = requests.get("https://api.wynncraft.com/public_api.php?action=territoryList")
    f = e.json()
    return f["territories"]["Dead Island South East"]["guild"]

def checkdeadSE():
    x = deadSE()
    if x == "Nerfuria":
        return "true"
    else:
        return "false"

def deadSW():
    e = requests.get("https://api.wynncraft.com/public_api.php?action=territoryList")
    f = e.json()
    return f["territories"]["Dead Island South West"]["guild"]

def checkdeadSW():
    x = deadSW()
    if x == "Nerfuria":
        return "true"
    else:
        return "false"

def regular():
    e = requests.get("https://api.wynncraft.com/public_api.php?action=territoryList")
    f = e.json()
    return f["territories"]["Regular Island"]["guild"]

def checkregular():
    x = regular()
    if x == "Nerfuria":
        return "true"
    else:
        return "false"

def skiens():
    e = requests.get("https://api.wynncraft.com/public_api.php?action=territoryList")
    f = e.json()
    return f["territories"]["Skiens Island"]["guild"]

def checkskiens():
    x = skiens()
    if x == "Nerfuria":
        return "true"
    else:
        return "false"

def nodguj():
    e = requests.get("https://api.wynncraft.com/public_api.php?action=territoryList")
    f = e.json()
    return f["territories"]["Nodguj Nation"]["guild"]

def checknodguj():
    x = nodguj()
    if x == "Nerfuria":
        return "true"
    else:
        return "false"

def dujgon():
    e = requests.get("https://api.wynncraft.com/public_api.php?action=territoryList")
    f = e.json()
    return f["territories"]["Dujgon Nation"]["guild"]

def checkdujgon():
    x = dujgon()
    if x == "Nerfuria":
        return "true"
    else:
        return "false"

def icy():
    e = requests.get("https://api.wynncraft.com/public_api.php?action=territoryList")
    f = e.json()
    return f["territories"]["Icy Island"]["guild"]

def checkicy():
    x = icy()
    if x == "Nerfuria":
        return "true"
    else:
        return "false"

def santa():
    e = requests.get("https://api.wynncraft.com/public_api.php?action=territoryList")
    f = e.json()
    return f["territories"]["Santa's Hideout"]["guild"]

def checksanta():
    x = santa()
    if x == "Nerfuria":
        return "true"
    else:
        return "false"

def mage():
    e = requests.get("https://api.wynncraft.com/public_api.php?action=territoryList")
    f = e.json()
    return f["territories"]["Mage Island"]["guild"]

def checkmage():
    x = mage()
    if x == "Nerfuria":
        return "true"
    else:
        return "false"

def pirate():
    e = requests.get("https://api.wynncraft.com/public_api.php?action=territoryList")
    f = e.json()
    return f["territories"]["Pirate Town"]["guild"]

def checkpirate():
    x = pirate()
    if x == "Nerfuria":
        return "true"
    else:
        return "false"

def zhight():
    e = requests.get("https://api.wynncraft.com/public_api.php?action=territoryList")
    f = e.json()
    return f["territories"]["Zhight Island"]["guild"]

def checkzeight():
    x = zhight()
    if x == "Nerfuria":
        return "true"
    else:
        return "false"

def bear():
    e = requests.get("https://api.wynncraft.com/public_api.php?action=territoryList")
    f = e.json()
    return f["territories"]["The Bear Zoo"]["guild"]

def checkbear():
    x = bear()
    if x == "Nerfuria":
        return "true"
    else:
        return "false"

def rooster():
    e = requests.get("https://api.wynncraft.com/public_api.php?action=territoryList")
    f = e.json()
    return f["territories"]["Rooster Island"]["guild"]

def checkrooster():
    x = rooster()
    if x == "Nerfuria":
        return "true"
    else:
        return "false"

def tree():
    e = requests.get("https://api.wynncraft.com/public_api.php?action=territoryList")
    f = e.json()
    return f["territories"]["Tree Island"]["guild"]

def checktree():
    x = tree()
    if x == "Nerfuria":
        return "true"
    else:
        return "false"

def getNumber():
    a = requests.get("https://api.wynncraft.com/public_api.php?action=guildStats&command=Nerfuria")
    b = a.json()
    return(b["territories"])

maro = checkmaro()
selchar = checkselchar()
deadNW = checkdeadNW()
deadNE = checkdeadNE()
deadSE = checkdeadSE()
deadSW = checkdeadSW()
regular = checkregular()
skiens = checkskiens()
nodguj = checknodguj()
dujgon = checkdujgon()
icy = checkicy()
santa = checksanta()
mage = checkmage()
pirate = checkpirate()
zhight = checkzeight()
bear = checkbear()
rooster = checkrooster()
tree = checktree()

def claimMaro():
    if maro == "true":
            return "claimed 🟢"
    else: return "not claimed 🔴"

def claimSelchar():
    if selchar == "true":
            return "claimed 🟢"
    else: return "not claimed 🔴"

def claimdeadNW():
    if deadNW == "true":
            return "claimed 🟢"
    else: return "not claimed 🔴"

def claimdeadNE():
    if deadNE == "true":
        return "claimed 🟢"
    else: return "not claimed 🔴"

def claimdeadSE():
    if deadSE == "true":
        return "claimed 🟢"
    else: return "not claimed 🔴"

def claimdeadSW():
    if deadSW == "true":
        return "claimed 🟢"
    else: return "not claimed 🔴"

def claimRegular():
    if regular == "true":
        return "claimed 🟢"
    else: return "not claimed 🔴"

def claimSkeins():
    if skiens == "true":
        return "claimed 🟢"
    else: return "not claimed 🔴"

def claimNodguj():
    if nodguj == "true":
        return "claimed 🟢"
    else: return "not claimed 🔴"

def claimDujgon():
    if dujgon == "true":
        return "claimed 🟢"
    else: return "not claimed 🔴"

def claimIcy():
    if icy == "true":
        return "claimed 🟢"
    else: return "not claimed 🔴"

def claimSanta():
    if santa == "true":
        return "claimed 🟢"
    else: return "not claimed 🔴"

def claimMage():
    if mage == "true":
        return "claimed 🟢"
    else: return "not claimed 🔴"

def claimPirate():
    if pirate == "true":
        return "claimed 🟢"
    else: return "not claimed 🔴"

def claimZhight():
    if zhight == "true":
        return "claimed 🟢"
    else: return "not claimed 🔴"

def claimBear():
    if bear == "true":
        return "claimed 🟢"
    else: return "not claimed 🔴"

def claimRooster():
    if rooster == "true":
        return "claimed 🟢"
    else: return "not claimed 🔴"

def claimTree():
    if tree == "true":
        return "claimed 🟢"
    else: return "not claimed 🔴"

client = discord.Client()

class cuts():
    def __init__(self,cmd,command,value=''):
        self.command=command
        self.value=''
        com=cmd
        for n in range(0,len(com)):
            if com[n] in self.command[0:len(com[n])]:
                self.value=self.command[len(com[n]):len(self.command)]
                self.command=self.command[0:len(com[n])]
        if self.value=='':
            self.value='No Command'

@client.event
async def on_ready():
    print('Bot is Ready')
@client.event
async def on_message(message):
    cmd=cuts(command,message.content)
    if cmd.command=='!help':
        embed = discord.Embed(title="Help commands for bot", description="Lists of commands", color=14803455)
        await message.channel.send(embed=embed)
    if cmd.command == '!n':
        teriEmbed = discord.Embed(title="Lists of Teritories", description="Show teritories that claimed or not", color=14803455)
        teriEmbed.set_footer(text= f"Nerfuria has territories total of {getNumber()}")
        teriEmbed.timestamp(datetime.datetime)
        teriEmbed.add_field(name="**Territories**", value="Maro peaks is " + claimMaro() + "\nSelchar is " + claimSelchar()
        + "\nDead Island North West is " + claimdeadNW() + "\nDead Island North East is " + claimdeadNE() + "\nDead Island South West is " + claimdeadSW()
        + "\nDead Island South East is " + claimdeadSE() + "\nRegular Island is " + claimRegular() + "\nSkeins Island is " + claimSkeins()
        + "\nNodguj Nation is " + claimNodguj() + "\nDujgon Nation is " + claimDujgon() + "\nIcy Island is " + claimIcy()
        + "\nSanta's Hideout is " + claimSanta() + "\nMage Island is " + claimMage() + "\nPirate Town is " + claimPirate()
        + "\nZhight Island is " + claimZhight() + "\nThe Bear Zoo is " + claimBear() + "\nRooster Island is " + claimRooster()
        + "\nTree Island is " + claimTree())
        await message.channel.send(embed=teriEmbed)

client.run(TOKEN)