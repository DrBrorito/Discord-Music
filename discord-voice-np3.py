#bot music git broken, I hate git, git is broken, this is why I never git, git is evil
 #I dont recall adding this, cuz I didnt

import discord
import asyncio
import yt_dlp
from discord.ext import commands #setup commands 

ydl = yt_dlp.YoutubeDL({'format': 'bestaudio', 'noplaylist': True}) #setups the downloader for music

bot = commands.Bot(command_prefix ='!', intents=discord.Intents.all())
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

url = "https://discord.com/api/v10/applications/1483198271429021758/"
json = {
    "name": "Join",
     "type": 1,
     "description": "Joins a voice channel",
     "options": [
         {
             "name": "channel",
             "description": "Makesbot join a voice channel of your choice",
             "type": 3,
             "required": True,
             "choices": [
                 {"name": "Chating",
                  "value": "1473797375003725907"
                  },
                  {"name": "Cookieness",
                   "value": "1473076548822241424"
                   },
                   {"name": "AFK",
                    "value": "1388978113308004436"
                    }
             ]
         },
     ]
     headers = {
         "Authorization": "Bot MTQ4MzE5ODI3MTQyOTAyMTc1OA.GZCJSQ.YUPHwJ92ne1Zlli2l48uF4BJdDOncZGGgDHB3E"
     }
     r = requests.post(url, headers=headers, json=json)
 }    
 #Tried adding slash commands, invil json error :(
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
        file = "rick.mp3" #Updated to use an mp3 rather than YouTube
        ctx.voice_client.play(discord.FFmpegPCMAudio(file)) #plays raw url
    else:
        await ctx.send(f'Do !join to have me join call first, or Im playing audio rightnow')
    

@bot.command() 
async def play(ctx, file):
    if ctx.voice_client and not ctx.voice_client.is_playing():
        await ctx.send(f'Playing ur local music from {file}')
        ctx.voice_client.play(discord.FFmpegPCMAudio(file)) 
    
    else: 
        await ctx.send(f'Audio is playing and or the Bot is not in the call')      
       

@bot.command()
async def stop(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.stop()
        await ctx.send(f'Stopped the Party')


@bot.command()
async def helps(ctx):
    
    await ctx.send(f'To have Bot Join Voice channel do !Join')
    asyncio.sleep(.2) #I really tried time.sleep, I am so stupid
    await ctx.send(f'To have bot Leave voice channel do !disconnect')
    asyncio.sleep(.2)
    await ctx.send(f'To have bot Rick roll people do !rick')
    asyncio.sleep(.2)
    await ctx.send(f'To have bot play local files do !play <File Path>')
    asyncio.sleep(.2)
    await ctx.send(f'To have bot stop the music do !stop')
    asyncio.sleep(.2)
    await ctx.send(f'Do "!helps" if you need help with commands')


bot.run('.GZCJSQ.YUPHwJ92ne1Zlli2l48uF4BJdDOncZGGgDHB3E')
client.run('MTQ4MzE5ODI3MTQy67OTAyMTc1OA.GZCJSQ.YUPHwJ92ne1Zlli2l48uF4BJdDOncZGGgDHB3E') #kinda useless lol