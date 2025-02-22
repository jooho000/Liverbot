import os
import json
import random
import discord
from discord.ext import commands
from rpg_game import handleRequest, handle_guild_request
from image_generator import create_welcome_image

# Load bot token
DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Set up bot with intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.members = True  # Required to detect new members
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ El bot está en línea como {bot.user}")

@bot.event
async def on_member_join(member):
    """Handles new members joining the server and sends a welcome image"""
    print(f"📢 Nuevo miembro detectado: {member.name}")  # Debugging message

    WELCOME_CHANNEL_ID = 1342798289401151488  # Replace with your actual welcome channel ID
    channel = bot.get_channel(WELCOME_CHANNEL_ID)

    if not channel:
        print("❌ No se encontró el canal de bienvenida. Verifica el ID.")
        return
    
    # Get the user's avatar
    avatar_url = member.avatar.url if member.avatar else member.default_avatar.url

    # Generate the welcome image
    image = create_welcome_image(member.name, avatar_url)

    try:
        await channel.send(
            f"¡Bienvenido a la comunidad, {member.mention}! 🎉", 
            file=discord.File(image, "welcome.png")
        )
        print("✅ Mensaje de bienvenida enviado correctamente.")
    except Exception as e:
        print(f"❌ Error enviando mensaje de bienvenida: {e}")


@bot.command()
async def rpg(ctx, name: str, command: str, *args):
    """Handles RPG game commands"""
    message = f"rpg {name} {command} {' '.join(args)}"
    response = handleRequest(message)
    await ctx.send(response)

@bot.command()
async def guild(ctx, name: str, action: str, *args):
    """Handles Guild system commands"""
    message = f"guild {name} {action} {' '.join(args)}"
    response = handle_guild_request(message)
    await ctx.send(response)

@bot.command()
async def ayuda(ctx):
    """Displays all available commands in Spanish"""
    help_message = (
        "**🛠️ Bot RPG - Lista de Comandos**\n\n"
        "**📜 Comandos de RPG:**\n"
        "`!rpg <nombre_de_personaje> crear` - 🏗️ Crea un nuevo personaje.\n"
        "`!rpg <nombre_de_personaje> stats` - 📊 Muestra las estadísticas del personaje.\n"
        "`!rpg <nombre_de_personaje> aventura` - ⚔️ Ve de aventura y enfréntate a enemigos o encuentra objetos.\n"
        "`!rpg <nombre_de_personaje> descansar` - 🏨 Descansa en una posada para recuperar HP (cuesta oro).\n\n"
        
        "**🏰 Comandos de Guilds:**\n"
        "`!guild <nombre_del_gremio> crear` - 🏰 Crea un nuevo gremio.\n"
        "`!guild <nombre_de_personaje> unirse <nombre_del_gremio>` - 🤝 Únete a un gremio existente.\n"
        "`!guild <nombre_de_personaje> salir` - 🚪 Sal de un gremio.\n"
        "`!guild <nombre_del_gremio> info` - 📜 Muestra la lista de miembros del gremio.\n\n"

        "**🔹 Comandos Adicionales:**\n"
        "`!help` - ℹ️ Muestra esta lista de comandos en español.\n"
    )
    await ctx.send(help_message)

# Load items from JSON file
def load_items():
    with open("data/items.json", "r", encoding="utf-8") as file:
        return json.load(file)

items_data = load_items()
lolItems = items_data["lolItems"]
botas = items_data["botas"]

@bot.command()
async def build(ctx):
    """Genera una build aleatoria de League of Legends"""
    build_items = random.sample(lolItems, 5)  # Selecciona 5 ítems aleatorios
    chosen_boots = random.choice(botas)  # Selecciona unas botas aleatorias
    build_items.append(chosen_boots)  # Agrega las botas a la build

    build_message = "**🛡️ Build Aleatoria para League of Legends:**\n"
    for item in build_items:
        build_message += f"- {item}\n"

    await ctx.send(build_message)

@bot.command()
async def test_channel(ctx):
    """Test if the bot can send messages in the welcome channel"""
    WELCOME_CHANNEL_ID = 1342798289401151488
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        await channel.send("✅ Este es el canal de bienvenida.")
    else:
        await ctx.send("❌ No se pudo encontrar el canal de bienvenida. Verifica el ID.")
        
# Run the bot
bot.run(DISCORD_TOKEN)
