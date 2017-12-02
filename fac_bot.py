import math
import discord
import asyncio
import re
import conf
from decimal import Decimal

client=discord.Client()

@client.event
async def on_ready():
    print ('Logged in as')
    print (client.user.name)
    print(client.user.id)
    print('-----')

@client.event
async def on_message(message):
    if message.content.find('!') != -1 and message.content[message.content.find('!')-1] != "@" :
        number = int(re.search('-?\d+', message.content).group())
        if message.content.find('-') != -1:
            await client.send_message(message.channel, "You can't take the factorial of a negative number!")
        elif (number >= 10000) :
            await client.send_message(message.channel, "This factorial is too large to be computed in a reasonable amount of time!")
        elif (number > 6000):
            await client.send_message(message.channel, "This might take a while" + ", " + "@" + str(message.author) + ".")
            numberFac=math.factorial(number)
            numberFac = "{:.5E}".format(Decimal(numberFac))
            await client.send_message(message.channel, numberFac)
        elif (number > 15):
            numberFac=math.factorial(number)
            numberFac = "{:.5E}".format(Decimal(numberFac))
            await client.send_message(message.channel, numberFac)
        else:
            numberFac=math.factorial(number)
            await client.send_message(message.channel, numberFac)
        print (message.author)
        print (message.content.find("!"))
        print (message.content)

client.run(conf.key)
