from urllib import request, parse
from discord.ext import commands
import discord
import datetime
import re


# Configuracion
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all(),description='This is a helper bot.')


# Comandos
@bot.command()
async def saludar(ctx, name):
  await ctx.send(f'Hola {name}!')

@bot.command()
async def sumar(ctx, numOne: int, numTwo: int):
  await ctx.send(f'El resultado es: {numOne + numTwo}')

@bot.command()
async def informar(ctx):
  embed = discord.Embed(title=f'{ctx.guild.name}', 
  type= 'rich' ,description='Description of Embed message', timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_gold())

  embed.add_field(name='Server created at', value=f'{ctx.guild.created_at}')
  embed.add_field(name='Server Owner', value=f'{ctx.guild.owner}')
  embed.add_field(name='Server ID', value=f'{ctx.guild.id}')
  embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/0/03/ANTIGUO_ESCUDO_PE%C3%91AROL_MONTEVIDEO-5.png')

  await ctx.send(embed=embed)

@bot.command()
async def buscar(ctx, *, search):
  query_str = parse.urlcode({'search_query': search})
  petition = request.urlopen('http://www.youtube.com/results?' + query_str)
  result = re.findall('href=\"\\/watch\\?v=(.{11})', petition.read().decode())

  await ctx.send('htpps://www.youtube.com/watch?v=' + result[0])


# Eventos
@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Streaming(name='Tutorials', url='https://www.twitch.tv/accountname'))


# Inicializador
bot.run(""" TOKEN """)
