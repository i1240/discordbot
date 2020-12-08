import discord
import os
client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("어깨운동")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("어깨형님"):
        await message.channel.send("어깨운동중 쉿")
    if message.content.startswith("병진지니어스"):
        await message.channel.send("병진병진병진")
    if message.content.startswith("매직한마이콜"):
        await message.channel.send("라면라면라면")
    if message.content.startswith("병신"):
        await message.channel.send("지는ㅋ")
    if message.content.startswith("롤들어와"):
        await message.channel.send("종훈이년")
    if message.content.startswith("/병진"):
        pic = "./병진.jpg"
        await message.channel.send(file=discord.File(pic))
    if message.content.startswith("/성준"):
        pic1 = "./성준.jpg"
        await message.channel.send(file=discord.File(pic1))
    if message.content.startswith("/어"):
        pic2 = "./어.jpg"
        await message.channel.send(file=discord.File(pic2))
    if message.content.startswith("/종"):
        pic3 = "./종훈.jpg"
        await message.channel.send(file=discord.File(pic3))
        
acces_token = os.environ["BOT_TOKEN"]
client.run("access_token")
