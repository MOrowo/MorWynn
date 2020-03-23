import discord
import requests
from datetime import datetime

from config import TOKEN
from commands.commandslist import CommandLists as command

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

def claimTree():
    return checkClaim("Tree Island")

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
        embed.add_field(name= "Command Lists", value= "!n -> Shows Nerfuria's Territories")
        await message.channel.send(embed=embed)
    if cmd.command == '!n':
        await message.channel.send("Fethcing API wait....")
        teriEmbed = discord.Embed(title="Lists of Teritories", description="Show teritories that claimed or not", color=14803455)
        teriEmbed.set_footer(text= f"Nerfuria has territories total of {getNumber()}")
        teriEmbed.add_field(name="**Territories**", value="Maro peaks is " + claimMaro() + "\nSelchar is " + claimSelchar()
        + "\nDead Island North West is " + claimdeadNW() + "\nDead Island North East is " + claimdeadNE() + "\nDead Island South West is " + claimdeadSW()
        + "\nDead Island South East is " + claimdeadSE() + "\nRegular Island is " + claimRegular() + "\nSkeins Island is " + claimSkeins()
        + "\nNodguj Nation is " + claimNodguj() + "\nDujgon Nation is " + claimDujgon() + "\nIcy Island is " + claimIcy()
        + "\nSanta's Hideout is " + claimSanta() + "\nMage Island is " + claimMage() + "\nPirate Town is " + claimPirate()
        + "\nZhight Island is " + claimZhight() + "\nThe Bear Zoo is " + claimBear() + "\nRooster Island is " + claimRooster()
        + "\nTree Island is " + claimTree())
        await message.channel.send(embed=teriEmbed)

client.run(TOKEN)