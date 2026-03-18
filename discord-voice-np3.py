#bot music git broken, I hate git, git is broken, this is why I never git
from concurrent.futures import wait

import discord
import yt_dlp
from discord.ext import commands #setup commands 

ydl = yt_dlp.YoutubeDL({'format': 'bestaudio', 'noplaylist': True}) #setups the downloader for music

bot = commands.Bot(command_prefix ='!', intents=discord.Intents.all())
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
#test command but not really command
#Kinda useless still
@client.event
async def on_read():
    print(f'We have logged in as {client.user}')

@client.event 
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# Voice setup

#Join code
@bot.command()
async def join(ctx):

    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()

        await ctx.send(f"Joined {channel}")
    else:
        await ctx.send("I cant Join calls with out you in it first")



#Discconect code, Im going do smth else for this
@bot.command()
async def disconnect(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect() #weird thing that some how works
        await ctx.send(f'Disconnected from call')


    else:
        await ctx.send(f'Im not in a call')



#start playing media
@bot.command()
async def rick(ctx):
    if ctx.voice_client:
        await ctx.send (f'Get ricked roll loser')
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" #fetches the audio raw file
        info = ydl.extract_info(url, download=False) #creates the raw url
        raw_url = info['url']
        ctx.voice_client.play(discord.FFmpegPCMAudio(raw_url)) #plays raw url
    else:
        await ctx.send(f'Do !join to have me join call first')
    

@bot.command()
async def play(ctx, url):#all code broken here thx youtube
    if ctx.voice_client:
        await ctx.send(f'PLaying ur Music from {url}')
        
        info = ydl.extract_info(url, download=False)
        raw_url = info['url']
        ctx.voice_client.play(discord.FFmpegPCMAudio(url)) #forgot about await
    else:
        await ctx.send(f'STILL CANT PLAY IF NOT INT CALL')



bot.run('MTQ4MzE5ODI3MTQyOTAyMTc1OA.GZCJSQ.hidden')
client.run('MTQ4MzE5ODI3MTQyOTAyMTc1OA.GZCJSQ.hidden') #kinda useless lol