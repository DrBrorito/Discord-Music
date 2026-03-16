#bot music
import discord
from discord.ext import commands #setup commands 
bot = commands.Bot(command_prefix ='!', intents=discord.Intents.all())
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
#test command but not really command
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


@bot.command()
async def join(ctx):

    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()

        await ctx.send(f"joined Musica")
    else:
        await ctx.send("Ur a meany")


bot.run('MTQ4MzE5ODI3MTQyOTAyMTc1OA.GFfsbH.YZpSeMbevPgaNnTJKt1KcT6qZRjdpl5hjPuB4w')


