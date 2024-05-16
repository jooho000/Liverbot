import discord
from discord.ext import commands
from typing import Final
import os
from discord import Intents, Client, File
from easy_pil import Editor, load_image_async, Font
from responses import handle_response

bot = commands.Bot(command_prefix='>', intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.change_presence(status = discord.Status.online, activity = discord.Activity(type = discord.ActivityType.playing, name='Esclavo del Liver'))
    print(f'{bot.user} is now running!')

@bot.event
async def on_member_join(member):

    channel = member.guild.system_channel

    background = Editor("LiverBot.py\pic1.jpg")
    profile_image = await load_image_async(str(member.avatar.url))

    profile = Editor(profile_image).resize((1200,1200)).circle_image()
    poppins = Font.poppins(size=200, variant="bold")
    poppins_small = Font.poppins(size=100, variant="light")

    background.paste(profile, (1175,150))

    background.text((1775,1350), f"llego un/a gei al server!", color="white", font=poppins, align='center')
    background.text((1775,1600), f"{member.name}#{member.discriminator}", color="white", font = poppins_small, align='center')

    file = File(fp=background.image_bytes, filename="LiverBot.py\pic1.jpg")
    await channel.send(f"llego un/a gei {member.mention}!")
    await channel.send(file=file)

@bot.event
async def on_member_leave(member):

    channel = member.guild.system_channel

    background = Editor("LiverBot.py\pic1.jpg")
    profile_image = await load_image_async(str(member.avatar.url))

    profile = Editor(profile_image).resize((1200,1200)).circle_image()
    poppins = Font.poppins(size=200, variant="bold")
    poppins_small = Font.poppins(size=100, variant="light")

    background.paste(profile, (1175,150))

    background.text((1775,1350), f"se fue un/a gei del server", color="white", font=poppins, align='center')
    background.text((1775,1600), f"{member.name}#{member.discriminator}", color="white", font = poppins_small, align='center')

    file = File(fp=background.image_bytes, filename="LiverBot.py\pic1.jpg")
    await channel.send(f"llego un/a gei {member.mention}!")
    await channel.send(file=file)

async def send_message(message, user_message):
    if not user_message:
        print("Message was empty becasue intents were not enabled")
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
    
    try:
        response: str = handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message,user_message)

bot.run("")
