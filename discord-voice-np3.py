#bot music git broken, I hate git
import discord
from discord.ext import commands #setup commands 
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
        ctx.voice_client.play(discord.FFmpegPCMAudio('https://www.youtube.com/watch?v=dQw4w9WgXcQ')) #It needs special link to work 
        await ctx.send (f'Get ricked roll loser')

    
    else:
        await ctx.send(f'Do !join to have me join call first')
    

    @bot.command()
    async def play(url):
        if ctx.voice_client:
            await ctx.voice_client.play(discord.FFmpegPCMAudio(url)) #It needs special link to work bru it no work
        
            await ctx.send(f'Playing ur fav music from {url}')
        else:
            await ctx.send(f'STILL CANT PLAY IF NOT INT CALL')
bot.run('TokeEn')
client.run('token') #kinda useless lol