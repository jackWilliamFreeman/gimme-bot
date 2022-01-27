import discord
import os

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity = discord.Activity(
                          type = discord.ActivityType.watching, 
                          name = 'for Sire to summon me'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if '!gimme'.encode('ascii', 'ignore') in message.content.lower().encode('ascii', 'ignore') and message.guild:
        await message.reply('Right Away Sire!', files = [discord.File('man.jpg')])

client.run(os.getenv('BOT_TOKEN'))
