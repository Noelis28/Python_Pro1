import discord
from discord.ext import commands
from bot_logic import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix= "$", intents=intents)

@bot.event
async def on_ready():
    print(f'Tu bot {bot.user} esta en linea!')
    
@bot.command()
async def saludar(ctx):
    await ctx.send("¡Hola! Soy tu bot, ¿en qué puedo ayudarte hoy?")
    
@bot.command()      
async def pregunta(ctx,*, mensaje:str):
    response = chatbot_response(mensaje)
    await ctx.send(response)

@bot.command()
async def emoji(ctx):
    await ctx.send(gen_emodji())
    
@bot.command()
async def coin(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def password(ctx):
    contraseña = gen_pass(10) 
    await ctx.send(f'Tu contraseña generada es: {contraseña}')


@bot.command()
async def hora(ctx):
    await ctx.send(f'La hora actual es: {get_current_time()}')

@bot.command()
async def randomnum(ctx, min_num: int, max_num: int):
    await ctx.send(f'Número aleatorio entre {min_num} y {max_num}: {random_number(min_num, max_num)}')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)
    
@bot.command()
async def joined(ctx, *, member: discord.Member):
    await ctx.send(f'{member} joined on {member.joined_at}')

bot.run ("")
