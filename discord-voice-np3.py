#bot music git broken, I hate git, git is broken, this is why I never git, git is evil
from concurrent.futures import waitn #I dont recall adding this

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
@bot.command() #Do not touch works amazing, nvm going convert it to local files too long for the android vr player api json
async def rick(ctx):
    if ctx.voice_client and not ctx.voice_client.is_playing():
        await ctx.send (f'Get ricked roll loser')
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" #fetches the audio raw file
        info = ydl.extract_info(url, download=False) #creates the raw url
        raw_url = info['url']
        ctx.voice_client.play(discord.FFmpegPCMAudio(raw_url)) #plays raw url
    else:
        await ctx.send(f'Do !join to have me join call first')
    

@bot.command() #kinda working but cant hear the sound
async def play(ctx, file):
    if ctx.voice_client and not ctx.voice_client.is_playing():
        await ctx.send(f'Playing ur local music from {file}')
        ctx.voice_client.play(discord.FFmpegPCMAudio(file)) 
    
    else:
       if not ctx.voice_client and ctx.voice_client.is_playing(): 
            await ctx.send(f'Audio is playing and some how the bot isnt in a channel')      
        else:
            if not ctx.voice_client:
                await ctx.send(f'Im not in a voice channel summon me by doing !join')
            else:
                await ctx.send(f'Audio is playing right now, try again when audio ia done playing')


bot.run('MTQ4MzE5ODI3MTQyOTAyMTc1OA..YUPHwJ92ne1Zlli2l48uF4BJdDOncZGGgDHB3E')
client.run('.GZCJSQ.YUPHwJ92ne1Zlli2l48uF4BJdDOncZGGgDHB3E') #kinda useless lol