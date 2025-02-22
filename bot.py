import os
import json
import random
import discord
from discord.ext import commands
from scraper import scrape_comps
from rpg_game import handleRequest, handle_guild_request
from image_generator import create_welcome_image

# Cargar el token del bot desde las variables de entorno
DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
if not DISCORD_TOKEN:
    raise ValueError("DISCORD_BOT_TOKEN no está definido en las variables de entorno.")

# Configurar el bot con permisos adecuados
intents = discord.Intents.default()
intents.message_content = True  # Necesario para leer mensajes
intents.members = True  # Necesario para detectar nuevos miembros
bot = commands.Bot(command_prefix="!", intents=intents)

# Obtener el ID del canal de bienvenida desde variables de entorno
WELCOME_CHANNEL_ID = int(os.getenv("WELCOME_CHANNEL_ID", "0"))

# ------------------------------------------
# Evento: Cuando el bot está listo
# ------------------------------------------
@bot.event
async def on_ready():
    """Se ejecuta cuando el bot está en línea."""
    print(f"✅ El bot está en línea como {bot.user}")

@bot.event
async def on_member_join(member):
    """Maneja la llegada de nuevos miembros y envía una imagen de bienvenida."""
    print(f"📢 Nuevo miembro detectado: {member.name}")

    channel = bot.get_channel(WELCOME_CHANNEL_ID)

    if not channel:
        print(f"❌ No se encontró el canal de bienvenida con ID {WELCOME_CHANNEL_ID}.")
        return

    if not channel.permissions_for(channel.guild.me).send_messages:
        print(f"❌ No tengo permisos para enviar mensajes en {channel.name}.")
        return

    avatar_url = member.display_avatar.url
    image_path = create_welcome_image(member.name, avatar_url)
    file = discord.File(image_path, filename="welcome.png")

    try:
        await channel.send(f"🎉 ¡Bienvenido a la comunidad, {member.mention}!", file=file)
        print("✅ Mensaje de bienvenida enviado correctamente.")
    except Exception as e:
        print(f"❌ Error enviando mensaje de bienvenida: {e}")

# ------------------------------------------
# Comandos del RPG
# ------------------------------------------
@bot.command()
async def rpg(ctx, nombre: str, comando: str, *args):
    """Maneja los comandos del juego RPG."""
    mensaje = f"rpg {nombre} {comando} {' '.join(args) if args else ''}"
    try:
        respuesta = handleRequest(mensaje)
        await ctx.send(respuesta)
    except Exception as e:
        await ctx.send(f"❌ Error procesando el comando: {e}")

@bot.command()
async def aventura(ctx, nombre: str):
    """Inicia una aventura aleatoria para el personaje."""
    try:
        respuesta = handleRequest(f"rpg {nombre} aventura")
        await ctx.send(respuesta)
    except Exception as e:
        await ctx.send(f"❌ Error iniciando aventura: {e}")

# ------------------------------------------
# Sistema de Gremios
# ------------------------------------------
@bot.command()
async def guild(ctx, nombre: str, accion: str, *args):
    """Maneja los comandos del sistema de gremios."""
    mensaje = f"guild {nombre} {accion} {' '.join(args) if args else ''}"
    try:
        respuesta = handle_guild_request(mensaje)
        await ctx.send(respuesta)
    except Exception as e:
        await ctx.send(f"❌ Error en el sistema de gremios: {e}")

# ------------------------------------------
# Comando de Ayuda
# ------------------------------------------
@bot.command()
async def ayuda(ctx):
    """Muestra todos los comandos disponibles."""
    mensaje_ayuda = (
        "**🛠️ Bot RPG - Lista de Comandos**\n\n"

        "**📜 Comandos de RPG:**\n"
        "`!rpg <nombre_personaje> crear` - 🏗️ Crea un nuevo personaje.\n"
        "`!rpg <nombre_personaje> stats` - 📊 Muestra las estadísticas del personaje.\n"
        "`!rpg <nombre_personaje> descansar` - 🏨 Descansa en una posada para recuperar HP (cuesta 50 de oro).\n"
        "`!aventura <nombre_personaje>` - ⚔️ Inicia una aventura con eventos aleatorios.\n\n"

        "**🏰 Comandos de Gremios:**\n"
        "`!guild <nombre_gremio> crear` - 🏰 Crea un nuevo gremio.\n"
        "`!guild <nombre_personaje> unirse <nombre_gremio>` - 🤝 Únete a un gremio existente.\n"
        "`!guild <nombre_personaje> salir` - 🚪 Sal de un gremio.\n"
        "`!guild <nombre_gremio> info` - 📜 Muestra la información y miembros del gremio.\n\n"

        "**⚔️ Generador de Builds (League of Legends):**\n"
        "`!build` - 🎮 Genera una build aleatoria de LoL.\n\n"

        "**🔹 Composiciones de Teamfight Tactics:**\n"
        "`!TFT` - 🔹 Muestra las mejores composiciones de TFT.\n\n"

        "**🎲 Aventura y Eventos:**\n"
        "`!aventura <nombre_personaje>` - 🔥 Participa en una aventura con eventos aleatorios y gana recompensas.\n"
        "  🔹 Puedes ganar oro, EXP, objetos o incluso perder HP en eventos inesperados.\n\n"

        "**📥 Descargar el bot:**\n"
        "`!descargar` - 🔗 Obtén el código fuente en GitHub.\n\n"

        "**ℹ️ Otros Comandos:**\n"
        "`!ayuda` - 📖 Muestra esta lista de comandos.\n"
    )
    await ctx.send(mensaje_ayuda)


# ------------------------------------------
# Generador de Builds de League of Legends
# ------------------------------------------
def cargar_items():
    try:
        with open("data/items.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"❌ Error cargando items: {e}")
        return {"lolItems": [], "botas": []}

datos_items = cargar_items()
lolItems = datos_items.get("lolItems", [])
botas = datos_items.get("botas", [])

@bot.command()
async def build(ctx):
    """Genera una build aleatoria de League of Legends."""
    if len(lolItems) < 5:
        await ctx.send("❌ No hay suficientes ítems disponibles.")
        return

    build_items = random.sample(lolItems, 5)
    botas_elegidas = random.choice(botas) if botas else "Sin botas disponibles"
    build_items.append(botas_elegidas)

    mensaje_build = "**🛡️ Build Aleatoria para League of Legends:**\n"
    for item in build_items:
        mensaje_build += f"- {item}\n"

    await ctx.send(mensaje_build)

# ------------------------------------------
# Composiciones de Teamfight Tactics
# ------------------------------------------
@bot.command()
async def TFT(ctx):
    """Obtiene las mejores composiciones de TFT y las envía en un embed."""
    try:
        comps_data = scrape_comps(limit=5)

        if not comps_data or "error" in comps_data[0]:
            await ctx.send(f"❌ **Error:** {comps_data[0]['error']}" if comps_data else "❌ No se encontraron composiciones.")
            return

        embed = discord.Embed(title="🔹 Mejores Composiciones de TFT", color=discord.Color.blue())

        for idx, comp in enumerate(comps_data[:5], start=1):
            comp_name = comp["composition"]
            units = "\n".join([f"🔹 {champ}" for champ in comp["units"]])
            embed.add_field(name=f"🛡️ {idx}. {comp_name}", value=f"**⚔️ Campeones:**\n{units}", inline=False)

        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(f"❌ Error obteniendo composiciones de TFT: {e}")

# ------------------------------------------
# Descargar
# ------------------------------------------
@bot.command()
async def descargar(ctx):
    """Envía el enlace del código fuente en GitHub."""
    await ctx.send("🔗 Puedes descargar el código fuente del bot aquí: [GitHub - Liverbot](https://github.com/jooho000/Liverbot)")


# ------------------------------------------
# Iniciar el bot
# ------------------------------------------
bot.run(DISCORD_TOKEN)
