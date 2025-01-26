import os
import discord
from discord.ext import commands,tasks
from dotenv import load_dotenv
import requests
from openai import OpenAI

client = OpenAI()

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
  print(f'Bot conectado como: {bot.user}')

@bot.command(name='ping')
async def ping(ctx):
  latency = round(bot.latency *1000)
  await ctx.send(f'Pong! Latência: {latency}ms')

@bot.event
async def on_member_join(member):
  guild = member.guild
  if (guild.system_channel):
    bemvindo = discord.Embed(title="Bem vindo ao servidor!",
    description=f'Olá, {member.mention}, seja bem vindo ao {guild.name}')
  await guild.system_channel.send(embed=bemvindo)

@bot.command(name='hello')
async def hello(ctx):
  hello = discord.Embed(title="Um pouco mais sobre mim",
  description=f'Olá, eu sou um projeto pessoal de estudo desenvolvido pelo Gustavo!')
  hello.add_field(name='Comandos disponíveis', value="`!hello`, `!ping`, `!pesquise`", inline=False)

  hello.add_field(name='Minhas tecnologias', value="Python, Discord.py", inline=False)
  await ctx.send(embed=hello)

@bot.command(name='produto')
async def produto(ctx):
  produto = discord.Embed(title="**CURSO DE MARKETING DIGITAL**",
  description=f'Com este produto você aprenderá sobre como maximizar suas vendas',
  color=discord.Color.red()
    )

  produto.add_field(name='Link', value="https://cursomarketing.com.br", inline=True)
  produto.set_image(url="https://th.bing.com/th/id/OIP.obVcPVtP1tBnRWFEhF-yKAHaHa?rs=1&pid=ImgDetMain")
  produto.set_footer(text="Todos os direitos reservados.")
  await ctx.send(embed=produto)


@bot.command(name="pesquise")
async def chat(ctx, *, message):

    try:
        response = client.chat.completions.create(model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um assistente útil e amigável."},
            {"role": "user", "content": message},
        ])
        reply = response.choices[0].message.content
        await ctx.send(reply)
    except Exception as e:
        await ctx.send("Ocorreu um erro ao processar sua solicitação.")
        print(e)

bot.run(TOKEN)
