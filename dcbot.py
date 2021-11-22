import discord
import asyncio
import procbridge as pb






client = discord.Client()
bridge = pb.Client('127.0.0.1', 8000)



@client.event
async def on_ready():
    print('Discord')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    for msg in bridge.request("update", "all"):
        await message.channel.send(msg)
    bridge.request("fetched", "all")
    print(message.content)
    print(message.author)
    print(message.channel)
    send = str(message.author).split('#')[0] + " in " + str(message.channel) + ":\n" + str(message.content)
    bridge.request("send", send)





def run():
    client.run("")

run()
