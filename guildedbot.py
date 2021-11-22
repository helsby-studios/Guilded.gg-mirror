import guilded
import asyncio
import procbridge as pb


client = guilded.Client()
msg = []
update = []


def delegate(method, args):
    global msg
    global update
    if method == 'send':
        msg.append(args)
        return "ok"
    elif method == 'update':
        return update
    elif method == 'fetched':

        update.clear()
        return "ok"

PORT = 8000
s = pb.Server('0.0.0.0', PORT, delegate)
s.start(daemon=False)
print("Server is on {}...".format(PORT))



@client.event
async def on_ready():
    print('Guilded')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    global msg
    global update
    for m in msg:
        await message.channel.send(m)
    msg.clear()
    print(message.content)
    print(message.author)
    print(message.channel)
    send = str(message.author).split('#')[0] + " in " + str(message.channel) + ":\n" + str(message.content)
    update.append(send)




def run():
    client.run("email", "passwd")

run()