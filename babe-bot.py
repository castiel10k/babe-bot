from datetime import datetime


import discord
import asyncio
import random

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)

jokesList = ["1", "2", "3"]
funAnswers = ["1", "2", "3"]

guild_id = 

personA = 
personB = 
personC = 
personD = 
personE = 

tfters= [personB, personD, personA]

channelTFT = 
channelKP = 

personDDictionnary = ['1', '2', '3']

greenbotID = 
babebotID = 
kpbotID = 
botList = [ kpbotID, babebotID, greenbotID ]

missList = ['1', '2', '3']
picList = [ '1.png', '2.png', '3.png' , '4.png' , '5.png']
akbuList = [ '1', '2', '3']
ftgList = [ '1', '2', '3']

@client.event
async def on_ready():
    await asyncio.sleep(0.21)
    print(f'We have logged in as {client.user}')



@client.event
async def on_message(message : discord.Message):
    await asyncio.sleep(0.21)
    print(message.content.lower())
    if message.content.lower() is not None:
        msg = message.content.lower()

        if message.author.id == personC and msg.startswith('test'):
            await message.author.send('welcome message')
            await asyncio.sleep(0.21)



        if message.author.id not in botList:
            ran = random.randint(1,100)
            #,datetime.now().strftime("%H:%M:%S %d/%m/%Y")
            print(ran,message.author.display_name)
            if ran == 1:
                print('----------------1%----------------')
                await message.channel.send(random.choice(ftgList))
                channel2 = client.get_channel(channelKP)
                await channel2.send('<@'+str(babebotID)+'> +1')
                await asyncio.sleep(0.21)

            if message.author.id == personC and msg.startswith('message'):
                await message.channel.send(random.choice(missList))
                await asyncio.sleep(0.21)

            if message.author.id == personD and msg.lower() in personDDictionnary:
                await message.channel.send(random.choice(ftgList))
                await asyncio.sleep(0.21)

            if message.mentions:
                for m in message.mentions:
                    if m.id == personE:
                        await message.channel.send('message')
                        await asyncio.sleep(0.21)

            if msg == 'tell me a joke':
                await message.channel.send(random.choice(jokesList))
                await asyncio.sleep(0.21)

            if ' quoi ' in msg.lower():
                await message.channel.send(random.choice(akbuList))   
                await asyncio.sleep(0.21)

            if msg.startswith('1') or msg.startswith('2') or msg.startswith('3'):
                msg = random.choice(funAnswers)
                await message.channel.send(msg)
                await asyncio.sleep(0.21)

                if msg == "1":
                    await message.channel.send(file=discord.File(random.choice(picList)))
                    await asyncio.sleep(0.21)
        

    #if message.content.startswith('ear p '):
    #    await message.channel.send('green play ' + message.content[6:])

@client.event
async def on_member_join(member : discord.Member):
    await asyncio.sleep(0.21)
    print(member)
    await member.send('welcome pm')
    #role = discord.utils.get(member.server.roles, id="")
    #await member.add_roles(member, role)

@client.event
async def on_voice_state_update(member : discord.Member, before : discord.VoiceState, after : discord.VoiceState):
    await asyncio.sleep(0.21)

    if before.channel != channelTFT and after.channel == channelTFT and True == False:
        print(member.id)
        print(tfters)
        print(member.id in tfters)
        if member.id in tfters:
            await asyncio.sleep(0.21)
            await member.edit(mute = True)
            await asyncio.sleep(5)
            await member.edit(mute = False)
            await asyncio.sleep(0.21)
            '''
            else:
                guild = client.get_guild(guild_id)
                for m in tfters:
                    member = guild.get_member(m)
                    await asyncio.sleep(0.21)
                    await member.edit(mute = True)
                    await asyncio.sleep(5)
                for m in tfters:
                    member = guild.get_member(m)
                    await asyncio.sleep(0.21)
                    await member.edit(mute = False)'''
                    

@client.event
async def on_message_edit(before : discord.Message, after : discord.Message):
    if not after.embeds: 
        await asyncio.sleep(0.21)
        if after.author.id not in botList and after.channel.id != channelKP:
            await after.channel.send(after.author.mention + ' i see what you did there :)')

@client.event
async def on_message_delete (message : discord.Message):
    await asyncio.sleep(0.21)
    if message.author.id not in botList and message.channel.id != channelKP:
        await message.channel.send(message.author.mention + ' 👀 ')


client.run('key')