import discord
import datetime
import configparser
from commands.cr_Exceptions import cr_Exception
from commands.cr_Server import cr_Server
from commands.cr_Typewritter import cr_Typewritter
from modules.cr_Fun import *
from discord.ext import commands

# init vars
config = configparser.ConfigParser()
config.read('./cr_config.ini')
bot_name = config.get("config","bot_name")
server_name = config.get("config","server_name")
cfg_channel = int(config.get("config","channel_id"))
err_channel = int(config.get("config","error_id"))
godfather = config.get("config","godfather")
owners = int(config.get("config","owners"))
admins = int(config.get("config","admins"))
mods = int(config.get("config","mods"))
token = config.get("config","token")
embed_color = 0xeace37

# discord part
activity = discord.Game(name=f';pomoc | {server_name}')
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=";", activity=activity, status=discord.Status.idle, intents=intents)
client.remove_command("help")

# events
@client.event
async def on_ready():
    channel = client.get_channel(cfg_channel)
    embedVar = discord.Embed(title="Bot został uruchomiony", description=str(datetime.datetime.utcnow()), color=0x00ff00)
    await channel.send(embed=embedVar)

@client.event
async def on_command_error(ctx, error):
    channel = client.get_channel(cfg_channel)
    try:
        embed_title = f'Błąd'
        field1_name = f'Wystąpił błąd podczas wykonywania komendy.'
        field1_value = (
            f'Jeśli problem będzie się powtarzał prosimy o kontakt z Administracją.'
        )
        embedVar = discord.Embed(title=embed_title, color=0xff0000)
        embedVar.add_field(name=field1_name, value=field1_value, inline=False)
        await channel.send(embed=embedVar)
    except Exception as e:
        await cr_Exception(client, err_channel, str(e))

# commands
@client.command()
async def cat(ctx):
    channel = client.get_channel(cfg_channel)
    try:
        cat = GetCat()
        embed_title = f'**Wylosowano kociaka**'
        embedVar = discord.Embed(title=embed_title, color=embed_color)
        embedVar.set_image(url=cat)
        await channel.send(embed=embedVar)
    except Exception as e:
        await cr_Exception(client, err_channel, str(e))

@client.command()
async def dog(ctx):
    channel = client.get_channel(cfg_channel)
    try:
        dog = GetReddit('dogpictures')
        embed_title = f'**Wylosowano psiaka**'
        embedVar = discord.Embed(title=embed_title, color=embed_color)
        embedVar.set_image(url=dog)
        await channel.send(embed=embedVar)
    except Exception as e:
        await cr_Exception(client, err_channel, str(e))

@client.command()
async def linuxmeme(ctx):
    channel = client.get_channel(cfg_channel)
    try:
        meme = GetReddit('linuxmemes')
        embed_title = f'**Memy o Linuksie**'
        embedVar = discord.Embed(title=embed_title, color=embed_color)
        embedVar.set_image(url=meme)
        await channel.send(embed=embedVar)
    except Exception as e:
        await cr_Exception(client, err_channel, str(e))

@client.command()
async def windowsmeme(ctx):
    channel = client.get_channel(cfg_channel)
    try:
        meme = GetReddit('windowsmemes')
        embed_title = f'**Memy o Windowsie**'
        embedVar = discord.Embed(title=embed_title, color=embed_color)
        embedVar.set_image(url=meme)
        await channel.send(embed=embedVar)
    except Exception as e:
        await cr_Exception(client, err_channel, str(e))

@client.command()
async def plmeme(ctx):
    channel = client.get_channel(cfg_channel)
    try:
        meme = GetReddit('Polska_wpz')
        embed_title = f'**Polskie memy z Reddita**'
        embedVar = discord.Embed(title=embed_title, color=embed_color)
        embedVar.set_image(url=meme)
        await channel.send(embed=embedVar)
    except Exception as e:
        await cr_Exception(client, err_channel, str(e))

@client.command()
async def meme(ctx):
    channel = client.get_channel(cfg_channel)
    try:
        meme = GetReddit('memes')
        embed_title = f'**Memy z Reddita**'
        embedVar = discord.Embed(title=embed_title, color=embed_color)
        embedVar.set_image(url=meme)
        await channel.send(embed=embedVar)
    except Exception as e:
        await cr_Exception(client, err_channel, str(e))

@client.command()
async def papameme(ctx):
    channel = client.get_channel(cfg_channel)
    try:
        meme = GetPapiez()
        channel = client.get_channel(cfg_channel)
        embed_title = f'**Papa Meme from API by Mopsior**'
        embedVar = discord.Embed(title=embed_title, color=embed_color)
        embedVar.set_image(url=meme)
        await channel.send(embed=embedVar)
    except Exception as e:
        await cr_Exception(client, err_channel, str(e))

@client.command()
async def unixporn(ctx):
    channel = client.get_channel(cfg_channel)
    try:
        unixporn = GetReddit('unixporn')
        embed_title = f'**r/unixporn**'
        embedVar = discord.Embed(title=embed_title, color=embed_color)
        embedVar.set_image(url=unixporn)
        await channel.send(embed=embedVar)
    except Exception as e:
        await cr_Exception(client, err_channel, str(e))

@client.command()
async def wallpaper(ctx):
    channel = client.get_channel(cfg_channel)
    try:
        wp = GetWallpaper()
        embed_title = f'**Wylosowano tapetkę**'
        embedVar = discord.Embed(title=embed_title, color=embed_color)
        embedVar.set_image(url=wp)
        await channel.send(embed=embedVar)
    except Exception as e:
        await cr_Exception(client, err_channel, str(e))

# init
if __name__ == '__main__':
    client.add_cog(cr_Server(client, bot_name, owners, admins, mods, cfg_channel, embed_color))
    client.add_cog(cr_Typewritter(client))
    client.run(token) 