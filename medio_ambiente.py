import discord
from discord.ext import commands
import bot_logic2 
import asyncio
from bot_logic2 import chatbot_response

intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix= "$", intents=intents)

@bot.event
async def on_ready():
    print(f'Tu bot {bot.user} esta en linea!')

@bot.command()
async def saludar(ctx):
    await ctx.send("¡Hola! Soy tu bot ecológico, ¿en qué puedo ayudarte hoy?")

@bot.command()      
async def pregunta(ctx, *, mensaje: str):
    response = chatbot_response(mensaje)  
    await ctx.send(response) 

@bot.command()
async def triviaeco(ctx):
    pregunta, texto = bot_logic2.trivia_eco()  
    await ctx.send(texto)  

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel  
    try:
        respuesta_usuario = await bot.wait_for('message', check=check, timeout=30) 
        respuesta = bot_logic2.verificar_respuesta(pregunta, respuesta_usuario.content)  
        await ctx.send(respuesta)  
    except asyncio.TimeoutError:
        await ctx.send("El tiempo se acabó, ¡inténtalo de nuevo más tarde!")

@bot.command()
async def fraseeco(ctx):
    await ctx.send(bot_logic2.frase_eco())

@bot.command()
async def recomendacion_app(ctx):
    await ctx.send(bot_logic2.app_eco())

@bot.command()
async def consejoeco(ctx):
    await ctx.send(bot_logic2.consejo_eco())

@bot.command()
async def globalresiduos(ctx):
    await ctx.send(bot_logic2.dato_global_residuos())

@bot.command()
async def impactoeco(ctx):
    await ctx.send(bot_logic2.dato_impactante())
    
@bot.command()
async def consejo_casa(ctx):
    await ctx.send(bot_logic2.consejos_casa())

@bot.command()
async def consejo_escuela(ctx):
    await ctx.send(bot_logic2.consejos_escuela())

@bot.command()
async def consejo_redes(ctx):
    await ctx.send(bot_logic2.consejos_redes())

@bot.command()
async def retoeco(ctx):
    await ctx.send(bot_logic2.reto_ecologico())

@bot.command()
async def emojieco(ctx):
    await ctx.send(bot_logic2.gen_emoji_eco())

@bot.command()
async def ayuda(ctx):
    instrucciones = """
**Comandos del Bot Ecológico** 

`$saludar` – Te da la bienvenida.
`$pregunta [mensaje]` – Pregúntale algo al bot ecológico.
`$triviaeco` – Juega una trivia ecológica.
`$fraseeco` – Recibe una frase ecológica.
`$recomendacion_app` – Conoce una app ecológica recomendada.
`$consejoeco` – Un consejo verde para ti.
`$globalresiduos` – Dato global sobre residuos.
`$impactoeco` – Dato impactante sobre el medio ambiente.
`$consejo_casa` – Consejo ecológico para el hogar.
`$consejo_escuela` – Consejo ecológico para la escuela.
`$consejo_redes` – Consejo ecológico para redes sociales.
`$retoeco` – Acepta un reto ecológico.
`$emojieco` – Emojis con temática ecológica.

Usa estos comandos y conviértete en un defensor del planeta.
"""
    await ctx.send(instrucciones)

bot.run('')
