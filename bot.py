import os
import json
import random
import discord
from discord.ext import commands
from scraper import scrape_comps
from rpg_game import handleRequest, handle_guild_request
from image_generator import create_welcome_image

# Cargar el token del bot
DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
if not DISCORD_TOKEN:
    raise ValueError("DISCORD_BOT_TOKEN no está definido en las variables de entorno.")

# Configurar el bot con intents
intents = discord.Intents.default()
intents.message_content = True  # Requerido para comandos basados en mensajes
intents.members = True  # Requerido para detectar nuevos miembros
bot = commands.Bot(command_prefix="!", intents=intents)

# ------------------------------------------
# Eventos de inicio del bot
# ------------------------------------------
@bot.event
async def on_ready():
    """Se ejecuta cuando el bot está en línea."""
    print(f"✅ El bot está en línea como {bot.user}")

@bot.event
async def on_member_join(member):
    """Maneja la llegada de nuevos miembros y envía una imagen de bienvenida."""
    print(f"📢 Nuevo miembro detectado: {member.name}")

    WELCOME_CHANNEL_ID = 1342798289401151488  # Reemplaza con el ID de tu canal de bienvenida
    channel = bot.get_channel(WELCOME_CHANNEL_ID)

    if not channel:
        print(f"❌ No se encontró el canal de bienvenida con ID: {WELCOME_CHANNEL_ID}.")
        return

    avatar_url = member.display_avatar.url  # Funciona en todos los casos
    image_path = create_welcome_image(member.name, avatar_url)
    file = discord.File(image_path, filename="welcome.png")

    try:
        await channel.send(f"🎉 ¡Bienvenido a la comunidad, {member.mention}!", file=file)
        print("✅ Mensaje de bienvenida enviado correctamente.")
    except Exception as e:
        print(f"❌ Error enviando mensaje de bienvenida: {e}")

# ------------------------------------------
# Comandos generales
# ------------------------------------------
@bot.command()
async def ayuda(ctx):
    """Muestra todos los comandos disponibles."""
    help_message = (
        "**🛠️ Bot RPG - Lista de Comandos**\n\n"

        "**📜 Comandos de RPG:**\n"
        "`!rpg <nombre_de_personaje> crear` - 🏗️ Crea un nuevo personaje.\n"
        "`!rpg <nombre_de_personaje> stats` - 📊 Muestra las estadísticas del personaje.\n"
        "`!rpg <nombre_de_personaje> aventura` - ⚔️ Ve de aventura y enfréntate a enemigos.\n"
        "`!rpg <nombre_de_personaje> descansar` - 🏨 Descansa en una posada para recuperar HP.\n\n"
        
        "**🏰 Comandos de Gremios:**\n"
        "`!guild <nombre_del_gremio> crear` - 🏰 Crea un nuevo gremio.\n"
        "`!guild <nombre_de_personaje> unirse <nombre_del_gremio>` - 🤝 Únete a un gremio existente.\n"
        "`!guild <nombre_de_personaje> salir` - 🚪 Sal de un gremio.\n"
        "`!guild <nombre_del_gremio> info` - 📜 Muestra la lista de miembros del gremio.\n\n"

        "**⚔️ Generador de Builds (League of Legends):**\n"
        "`!build` - 🎮 Genera una build aleatoria de League of Legends.\n\n"

        "**🔹 Composiciones de Teamfight Tactics:**\n"
        "`!TFT` - 🔹 Muestra las mejores composiciones actuales de TFT.\n\n"

        "**👋 Sistema de Bienvenida:**\n"
        "`!test_channel` - ⚙️ Verifica si el bot puede enviar mensajes en el canal de bienvenida.\n\n"

        "**📥 Descargar el bot:**\n"
        "`!descargar` - 🔗 Obtén el código fuente del bot en GitHub.\n\n"

        "**🔹 Comandos Adicionales:**\n"
        "`!ayuda` - ℹ️ Muestra esta lista de comandos.\n"
    )
    await ctx.send(help_message)

@bot.command()
async def descargar(ctx):
    """Proporciona un enlace al repositorio de GitHub del bot."""
    await ctx.send("🔗 **Descarga Liverbot aquí:** [GitHub Repository](https://github.com/jooho000/Liverbot)")

# ------------------------------------------
# Comandos de RPG y Gremios
# ------------------------------------------
@bot.command()
async def rpg(ctx, name: str, command: str, *args):
    """Maneja los comandos del juego RPG."""
    message = f"rpg {name} {command} {' '.join(args) if args else ''}"
    response = handleRequest(message)
    await ctx.send(response)

@bot.command()
async def guild(ctx, name: str, action: str, *args):
    """Maneja los comandos del sistema de gremios."""
    message = f"guild {name} {action} {' '.join(args) if args else ''}"
    response = handle_guild_request(message)
    await ctx.send(response)

# ------------------------------------------
# Generador de Builds de League of Legends
# ------------------------------------------
def load_items():
    with open("data/items.json", "r", encoding="utf-8") as file:
        return json.load(file)

items_data = load_items()
lolItems = items_data.get("lolItems", [])
botas = items_data.get("botas", [])

@bot.command()
async def build(ctx):
    """Genera una build aleatoria de League of Legends."""
    if len(lolItems) < 5:
        await ctx.send("❌ No hay suficientes ítems disponibles en la base de datos.")
        return

    build_items = random.sample(lolItems, 5)
    chosen_boots = random.choice(botas) if botas else "Sin botas disponibles"
    build_items.append(chosen_boots)

    build_message = "**🛡️ Build Aleatoria para League of Legends:**\n"
    for item in build_items:
        build_message += f"- {item}\n"

    await ctx.send(build_message)

# ------------------------------------------
# Composiciones de Teamfight Tactics
# ------------------------------------------
@bot.command()
async def TFT(ctx):
    """Obtiene composiciones de Teamfight Tactics y las envía en un mensaje embed."""
    comps_data = scrape_comps(limit=5)

    if not comps_data or "error" in comps_data[0]:  
        await ctx.send(f"❌ **Error:** {comps_data[0]['error']}" if comps_data else "❌ No se encontraron composiciones.")
        return

    embed = discord.Embed(title="🔹 Composiciones de Teamfight Tactics", color=discord.Color.blue())

    for idx, comp in enumerate(comps_data[:5], start=1):
        comp_name = comp["composition"]
        units = "\n".join([f"🔹 {champ}" for champ in comp["units"]])
        embed.add_field(name=f"🛡️ {idx}. {comp_name}", value=f"**⚔️ Campeones:**\n{units}", inline=False)

    await ctx.send(embed=embed)

# ------------------------------------------
# Comandos de prueba
# ------------------------------------------
@bot.command()
async def test_channel(ctx):
    """Verifica si el bot puede enviar mensajes en el canal de bienvenida."""
    WELCOME_CHANNEL_ID = 1342798289401151488
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        await channel.send("✅ Este es el canal de bienvenida.")
    else:
        await ctx.send("❌ No se pudo encontrar el canal de bienvenida. Verifica el ID.")

# Ejecutar el bot
bot.run(DISCORD_TOKEN)
