import discord
import datetime
import asyncio
import urllib
import json
from random import randint

from commands.commandslist import CommandLists as command
from config import TOKEN

def get_data(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as fp:
            mybytes = fp.read()
            mystr = mybytes.decode("utf-8")
            fp.close()
            mystr=json.loads(mystr) 
            return mystr
    except:
        return get_data(url)
def randomgame():
    a = randint(1, 10000)
    if a <= 4000:
        return "You got Emeralds in loot chest(40%)"
    elif a <= 6500:
        return "You got Emeralds with Common items(25%)"
    elif a <= 8000:
        return "You got Emeralds with Unique items(15%)"
    elif a <= 9000:
        return "You got Emeralds with Rare items(10%)"
    elif a <= 9800:
        return "You got Emeralds with Legendary items(8%)"
    elif a <= 9990:
        return "You got Emeralds with Fabled items(1.9%)"
    else: return "Mythic Boom!!!!"


def getDataFromWynncraft():
    e = get_data("https://api.wynncraft.com/public_api.php?action=territoryList")
    return e

def getSubAPI(mode):
    f = getDataFromWynncraft()
    return f["territories"][str(mode)]["guild"]

def checkISNerfuria(data):
    if data == "Nerfuria":
        return True
    else:
        return False

def getNumber():
    a = get_data("https://api.wynncraft.com/public_api.php?action=guildStats&command=Nerfuria")
    return(a["territories"])
def checkClaim(name):
    x = getSubAPI(name)
    if checkISNerfuria(x)==True:
        return "🟢"
    else: return "🔴"

#############NIA####################################################

def claimMaro():
    return checkClaim("Maro Peaks")

def claimSelchar():
    return checkClaim("Selchar")

def claimdeadNW():
    return checkClaim("Dead Island North West")

def claimdeadNE():
    return checkClaim("Dead Island North East")

def claimdeadSE():
    return checkClaim("Dead Island South East")

def claimdeadSW():
    return checkClaim("Dead Island South West")

def claimRegular():
    return checkClaim("Regular Island")

def claimSkeins():
    return checkClaim("Skiens Island")

def claimNodguj():
    return checkClaim("Nodguj Nation")

def claimDujgon():
    return checkClaim("Dujgon Nation")

def claimIcy():
    return checkClaim("Icy Island")

def claimSanta():
    return checkClaim("Santa's Hideout")

def claimMage():
    return checkClaim("Mage Island")

def claimPirate():
    return checkClaim("Pirate Town")

def claimZhight():
    return checkClaim("Zhight Island")

def claimBear():
    return checkClaim("The Bear Zoo")

def claimRooster():
    return checkClaim("Rooster Island")

################################################################################

####################################FFA#########################################

def claimDetlas():
    return checkClaim("Detlas")

def claimBob():
    return checkClaim("Bob's Tomb")

def claimBattle():
    return checkClaim("Battle Tower")

def claimHerb():
    return checkClaim("Herb Cave")

def claimJungle():
    return checkClaim("Jungle Lake")

def claimTemple():
    return checkClaim("Temple of Legends")

def claimCinfras():
    return checkClaim("Cinfras")

def claimHive():
    return checkClaim("Hive")

def claimQira():
    return checkClaim("Qira's Battle Room")

def claimThesead():
    return checkClaim("Thesead")

def claimLavaLake():
    return checkClaim("Lava Lake")

def claimLavaLakeB():
    return checkClaim("Lava Lake Bridge")

def claimMolten():
    return checkClaim("Molten Reach")

def claimRBU():
    return checkClaim("Raider's Base Upper")

def claimRBL():
    return checkClaim("Raider's Base Lower")
################################################################################

#################################SE############################################

def claimSilentRoad():
    return checkClaim("The Silent Road")

def claimBrokenRoad():
    return checkClaim("The Broken Road")

def claimWormTunnel():
    return checkClaim("Worm Tunnel")

def claimGray():
    return checkClaim("Gray Zone")

def claimForgotten():
    return checkClaim("Forgotten Town")

def claimForest():
    return checkClaim("Forest of Eyes")

def claimSinister():
    return checkClaim("Sinister Forest")

def claimLutho():
    return checkClaim("Lutho")

def claimSludge():
    return checkClaim("Paths of Sludge")

def claimToxicD():
    return checkClaim("Toxic Drip")

def claimToxicC():
    return checkClaim("Toxic Caves")

def claimVoid():
    return checkClaim("Void Valley")

def claimGate():
    return checkClaim("Gateway to Nothing")

def claimSacrifice():
    return checkClaim("Sacrifice")

def claimBizarre():
    return checkClaim("Bizarre Passage")

def claimTheGate():
    return checkClaim("The Gate")

##############################################################################
##############################################################################
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
    async def TeriMessage():
        y = getNumber()
        sendChannel = client.get_channel(696636247015161906)
        if int(y) >= 17:
            while not client.is_closed:
                await sendChannel.send("✅ We have all own claims")
                await asyncio.sleep(30)
        else: await sendChannel.send("❌ We don't have all own claims")
    client.loop.create_task(TeriMessage())
    cmd=cuts(command,message.content)
    if cmd.command=='!help':
        embed = discord.Embed(title="Help commands for bot", description="Lists of commands", color=14803455)
        embed.add_field(name= "Command Lists", value= "!n -> Shows Nerfuria's Territories\n!ffa -> Shows FFA Territories\n!se -> Shows Silent Expanse Territories\n!loot -> loot game")
        await message.channel.send(embed=embed)
    if cmd.command == '!n':
        await message.channel.send("Fetching API wait....")
        niaEmbed = discord.Embed(title="Lists of NIA Teritories", description="Show teritories that claimed or not", color=14803455)
        niaEmbed.set_footer(text= f"Nerfuria has territories total of {getNumber()}")
        niaEmbed.add_field(name="**NIA Territories**", value=claimMaro() + " Maro peaks\n" + claimSelchar() + " Selchar\n"
        + claimdeadNW() + " Dead Island North West\n" + claimdeadNE() + " Dead Island North East\n"+ claimdeadSW() + " Dead Island South West\n"
        + claimdeadSE() + " Dead Island South East\n" + claimRegular() + " Regular Island\n" + claimSkeins() + " Skiens Island\n"
        + claimNodguj() + " Nodguj Nation\n" + claimDujgon() + " Dujgon Nation\n" + claimIcy() + " Icy Island\n"
        + claimSanta() + " Santa's Hideout\n" + claimMage() + " Mage Island\n" + claimPirate() + " Pirate Town\n"
        + claimZhight() + " Zhight Island\n" + claimBear() + " The Bear Zoo\n" + claimRooster() + " Rooster Island\n")
        await message.channel.send(embed=niaEmbed)
    if cmd.command == "!ffa":
        await message.channel.send("Fetching API wait...")
        ffaEmbed = discord.Embed(title="Lists of FFA Territories", description="Show FFA Territories", color=3447003)
        ffaEmbed.add_field(name="**Wynn Province**", value=claimDetlas() + " Detlas\n" + claimBob() + " Bob's Tomb\n" + claimBattle() + " Battle Tower\n"
        + claimHerb() + " Herb Cave\n" + claimJungle() + " Jungle Lake\n" + claimTemple() + " Temple of Legends")
        ffaEmbed.add_field(name="**Gavel Province**", value=claimCinfras() + " Cinfras\n" + claimHive() + " Hive\n"
        + claimQira() + " Qira's Battle Room\n" + claimThesead() + " Thesead\n" + claimLavaLake() + " Lava Lake\n" + claimLavaLakeB() + " Lava Lake Bridge\n"
        + claimMolten() + " Molten Reach\n" + claimRBL() + " Raider's Base Lower\n" + claimRBU() + " Raider's Base Upper")
        await message.channel.send(embed=ffaEmbed)
    if cmd.command == "!se":
        await message.channel.send("Fetching API wait...")
        seEmbed = discord.Embed(title="List of SE Territories", description="Show SE Territories", color=16776960)
        seEmbed.add_field(name="**Silent Expanse**", value=claimSilentRoad() + " The Silent Road\n" + claimBrokenRoad() + " The Broken Road\n"
        + claimWormTunnel() + " Worm Tunnel\n" + claimGray() + " Gray Zone\n" + claimForgotten() + " Forgotten Town\n" + claimForest() + " Forest of Eyes\n"
        + claimSinister() + " Sinister Forest\n" + claimLutho() + " Lutho\n" + claimSludge() + " Paths of sludge\n" + claimToxicD() + " Toxic Drip\n"
        + claimToxicC() + " Toxic Cave\n" + claimVoid() + " Void Valley\n" + claimGate() + " Gateway to Nothing\n" + claimSacrifice() + " Sacrifice\n"
        + claimBizarre() + "Bizzare Passage\n" + claimTheGate() + " The Gate")
        await message.channel.send(embed=seEmbed)
    if cmd.command == "!loot":
        await message.channel.send(randomgame())
client.run(TOKEN)
