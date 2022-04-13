from cgitb import text
from msilib.schema import Component
from urllib import response
from webbrowser import get
import discord
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle
from discord.utils import get

bot = commands.Bot(command_prefix = "$", intents = discord.Intents.all())

@bot.event
async def on_message(m):
    # Сотрудник оставил скрины выполнения заказа
    if m.channel.id == 930875636799651860:
        sc_channel = bot.get_channel(932199109471916053)
        cs_channel = bot.get_channel(931231413913653390)
        user = m.author
        head = get(m.guild.roles, id=930772824040276020)
        await sc_channel.send(f"{head.mention}, {user.mention} Оставил скрины:\n__\n{m.content}\n__")
        await cs_channel.send(f"{user.mention} Оставил скрины:\n__\n{m.content}\n__")
        await m.delete()
    # Пересылание заказа в чат сотрудникам + кнопка принятия заказа
    if m.channel.id == 930860014590107648:
        # Если middle/senior то в высший чат
        if "Middle" in m.content:
            my_channel = bot.get_channel(930870896107860031)
            bd_channel = bot.get_channel(931194312794992641)
            await bd_channel.send(m.content)
            await my_channel.send(
            content = m.content,
            components = [
                Button(style=ButtonStyle.green, label = "Принять заказ")
            ]
        )
        # Если Junior то в низший чат
        if "Junior" in m.content:
            my_channel = bot.get_channel(930806171223339018)
            bd_channel = bot.get_channel(931194312794992641)
            await bd_channel.send(m.content)
            await my_channel.send(
            content = m.content,
            components = [
                Button(style=ButtonStyle.green, label = "Принять заказ")
            ]
        )
        # Форма заказа
        if m.content == "$form":
            await m.channel.send("Форма:\n```Пришел новый заказ!\nИгра: @Игра\nРанг: @Ранг\nПодробности: *Подробности*\nДедлайн: с **.**.** по **.**.**\nОплата: *Сумма*\n*Идентификатор канала*```\nВнимание, не забудте перед вводом идентификатора и отправки сообщения проверить правильность заказа!")
            
    response = await bot.wait_for("button_click", check = lambda i: i.message.id == m.id)
    # Сообщение о взятие заказа
    if response.channel.id == 930870896107860031:
        my_channel = bot.get_channel(931423249210966056)
        bd_channel = bot.get_channel(931423918990979113)
        user = response.author
        head = get(m.guild.roles, id=930772824040276020)
        await my_channel.send(f"{head.mention}, {user.mention} Откликнулся на заказ!\n__\n{m.content}\n__")
        await bd_channel.send(f"{user.mention} Откликнулся на заказ!\n__\n{m.content}\n__")
        await response.message.delete()
    # Сообщение о взятие заказа
    if response.channel.id == 930806171223339018:
        my_channel = bot.get_channel(931423249210966056)
        bd_channel = bot.get_channel(931423918990979113)
        user = response.author
        head = get(m.guild.roles, id=930772824040276020)
        await my_channel.send(f"{head.mention}, {user.mention} Откликнулся на заказ!\n__\n{m.content}\n__")
        await bd_channel.send(f"{user.mention} Откликнулся на заказ!\n__\n{m.content}\n__")
        await response.message.delete()
        
@bot.event
async def on_ready():
    DiscordComponents(bot)
    print("Ready")
    
bot.run("***")