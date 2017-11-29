import math
import discord
import asyncio
import re

client=discord.Client()

with open(key) as f:
	key = f.read()

@client.event
async def on_ready():
    print ('Logged in as')
    print (client.user.name)
    print(client.user.id)
    print('-----')
    
@client.event
async def on_message(message):
    if message.content.find('!') != -1 and message.content[1] != "@" :
        number = int(re.search('-?\d+', message.content).group())
        if message.content.find('-') != -1:
            await client.send_message(message.channel, "You can't take the factorial of a negative number!")
        elif (number > 807):
            await client.send_message(message.channel, 'That factorial is too large for Discord!')
        else:
            numberFac=math.factorial(number)
            await client.send_message(message.channel, numberFac)
        print (message.author)
        print (message.content.find("!"))
        print (message.content)
client.run(key)
