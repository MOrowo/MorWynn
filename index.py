import discord
import requests

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

def getNumber():
    a = requests.get("https://api.wynncraft.com/public_api.php?action=guildStats&command=Nerfuria")
    b = a.json()
    return(b["territories"])

maro = checkmaro()
selchar = checkselchar()

def claimMaro():
    if maro == "true":
            return "claimed"
    else: return "not claimed"

def claimSelchar():
    if selchar == "true":
            return "claimed"
    else: return "not claimed"

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
    if cmd.command == '!nerfuroo':
        teriEmbed = discord.Embed(title="Lists of Teritories", description="Show teritories that claimed or not", color=14803455)
        teriEmbed.set_footer(text= f"Nerfuria has territories total of {getNumber()}")
        teriEmbed.add_field(name="Territories", value="Maro peaks is " + claimMaro() + "\nSelchar is " + claimSelchar())
        await message.channel.send(embed=teriEmbed)
client.run(TOKEN)