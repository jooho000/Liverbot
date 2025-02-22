import os
import json
import random

# Data Folders
DATA_FOLDER = "data/"
CHARACTER_FILE = DATA_FOLDER + "characters.json"
GUILD_FILE = DATA_FOLDER + "guilds.json"

if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

# ------------------------------- LOAD & SAVE FUNCTIONS -------------------------------
def load_data(file, default_value):
    """Carga datos desde un archivo JSON o devuelve un valor predeterminado."""
    if os.path.exists(file):
        with open(file, "r") as f:
            return json.load(f)
    return default_value

def save_data(file, data):
    """Guarda datos en un archivo JSON."""
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

# Cargar personajes y gremios al iniciar
characters = load_data(CHARACTER_FILE, {})
guilds = load_data(GUILD_FILE, {})

# ------------------------------- CHARACTER CLASS -------------------------------
class Character:
    def __init__(self, name, HP, power, money, maxHP, level=1, EXP=0, guild=None, items=None):
        self.name = name
        self.HP = HP
        self.maxHP = maxHP
        self.power = power
        self.money = money
        self.level = level
        self.EXP = EXP
        self.guild = guild
        self.items = items if items else []

    def display_info(self):
        return (f"🧙 **{self.name}**\n"
                f"⭐ Nivel: {self.level}\n"
                f"❤️ HP: {self.HP}/{self.maxHP}\n"
                f"⚔️ Poder: {self.power}\n"
                f"💰 Oro: {self.money}\n"
                f"📈 EXP: {self.EXP}\n"
                f"🎒 Items: {', '.join(self.items) if self.items else 'Ninguno'}\n"
                f"🏰 Gremio: {self.guild or 'Ninguno'}")

    def save(self):
        """Guarda este personaje en el diccionario global y en archivo."""
        characters[self.name] = self.__dict__
        save_data(CHARACTER_FILE, characters)

    @staticmethod
    def load(name):
        """Carga un personaje desde el diccionario de datos."""
        if name in characters:
            data = characters[name]
            return Character(**data)
        return None

# ------------------------------- GUILD CLASS -------------------------------
class Guild:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members if members else []

    def add_member(self, player_name):
        """Añade un miembro al gremio."""
        if player_name not in self.members:
            self.members.append(player_name)
            self.save()
    
    def remove_member(self, player_name):
        """Elimina un miembro del gremio."""
        if player_name in self.members:
            self.members.remove(player_name)
            self.save()

    def display_info(self):
        """Muestra la información del gremio."""
        return (f"🏰 **{self.name}**\n"
                f"👥 Miembros: {', '.join(self.members) if self.members else 'Vacío'}")

    def save(self):
        """Guarda este gremio en el diccionario global y archivo."""
        guilds[self.name] = self.__dict__
        save_data(GUILD_FILE, guilds)

    @staticmethod
    def load(name):
        """Carga un gremio desde los datos."""
        if name in guilds:
            data = guilds[name]
            return Guild(**data)
        return None

# ------------------------------- RPG SYSTEM -------------------------------
def createCharacter(name):
    """Crea un nuevo personaje."""
    if name in characters:
        return "❌ Ya existe un personaje con ese nombre."

    HP = random.randint(100, 1000)
    power = random.randint(1, 50)
    money = random.randint(100, 500)
    character = Character(name, HP, power, money, HP)
    character.save()
    return f"✅ Personaje creado:\n{character.display_info()}"

def handleRequest(message):
    """Maneja comandos de RPG."""
    content = message.split(' ')
    name = content[1]
    command = content[2]

    character = Character.load(name)

    if command == "crear":
        return createCharacter(name)

    if not character:
        return "❌ No hay personaje con ese nombre."

    if command == "stats":
        return character.display_info()

    if command == "descansar":
        if character.money >= 50:
            character.HP = character.maxHP
            character.money -= 50
            character.save()
            return f"💤 Descansaste en la posada y recuperaste toda tu vida!\nOro restante: {character.money}"
        return "❌ No tienes suficiente oro."

    if command == "aventura":
        return handleAdventure(character)

    return "❌ Comando inválido."

# ------------------------------- ADVENTURE SYSTEM -------------------------------
def load_events():
    """Carga la lista de eventos desde el archivo JSON."""
    EVENT_FILE = "data/events.json"
    
    if not os.path.exists(EVENT_FILE):
        print("❌ Error: El archivo de eventos no existe.")
        return []

    with open(EVENT_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

events = load_events()  # Cargar eventos al iniciar el bot

def handleAdventure(character):
    """Eventos aleatorios de aventura cargados desde un archivo JSON."""
    if not events:
        return "❌ No hay eventos de aventura disponibles."

    event = random.choice(events)
    
    title = event["title"]
    description = event["description"]
    effects = event["effects"]

    applied_effects = {}

    # Aplicar efectos
    if "HP" in effects:
        hp_change = random.randint(effects["HP"][0], effects["HP"][1])
        character.HP = max(0, min(character.HP + hp_change, character.maxHP))
        applied_effects["HP"] = hp_change

    if "money" in effects:
        money_change = random.randint(effects["money"][0], effects["money"][1])
        character.money = max(0, character.money + money_change)
        applied_effects["money"] = money_change

    if "EXP" in effects:
        exp_change = random.randint(effects["EXP"][0], effects["EXP"][1])
        character.EXP += exp_change
        applied_effects["EXP"] = exp_change

    if "power" in effects:
        power_change = random.randint(effects["power"][0], effects["power"][1])
        character.power += power_change
        applied_effects["power"] = power_change

    if "items" in effects:
        for item in effects["items"]:
            character.items.append(item["name"])
            if "power" in item:
                character.power += random.randint(item["power"][0], item["power"][1])
            if "HP" in item:
                character.HP = max(0, min(character.HP + random.randint(item["HP"][0], item["HP"][1]), character.maxHP))
            if "EXP" in item:
                character.EXP += random.randint(item["EXP"][0], item["EXP"][1])

    # Guardar cambios
    character.save()

    # Crear el mensaje de resultado
    effect_texts = []
    for key, value in applied_effects.items():
        if key == "HP":
            effect_texts.append(f"❤️ HP: {'+' if value > 0 else ''}{value}")
        elif key == "money":
            effect_texts.append(f"💰 Oro: {'+' if value > 0 else ''}{value}")
        elif key == "EXP":
            effect_texts.append(f"📈 EXP: {'+' if value > 0 else ''}{value}")
        elif key == "power":
            effect_texts.append(f"⚔️ Poder: {'+' if value > 0 else ''}{value}")
        elif key == "items":
            effect_texts.append(f"🎒 Item: {value}")

    effect_text = "\n".join(effect_texts)

    return f"🎲 **{title}**\n{description}\n\n📜 Resultado:\n{effect_text}\n\n{character.display_info()}"

# ------------------------------- GUILD SYSTEM -------------------------------
def handle_guild_request(message):
    """Maneja comandos de gremios."""
    content = message.split(' ')
    action = content[2]

    if action == "crear":
        guild_name = content[1]
        if guild_name in guilds:
            return f"❌ El gremio **{guild_name}** ya existe."

        new_guild = Guild(guild_name)
        new_guild.save()
        return f"✅ Se ha creado el gremio **{guild_name}**."

    if action == "unirse":
        player_name = content[1]
        guild_name = content[3]

        player = Character.load(player_name)
        guild = Guild.load(guild_name)

        if not player:
            return "❌ No existe un personaje con ese nombre."
        if not guild:
            return "❌ No existe un gremio con ese nombre."
        if player.guild:
            return f"❌ Ya estás en **{player.guild}**. Debes salir antes de unirte a otro."

        guild.add_member(player.name)
        player.guild = guild_name
        player.save()

        return f"✅ **{player_name}** se ha unido al gremio **{guild_name}**."

    if action == "salir":
        player_name = content[1]
        player = Character.load(player_name)

        if not player:
            return "❌ No existe un personaje con ese nombre."
        if not player.guild:
            return "❌ No estás en ningún gremio."

        guild = Guild.load(player.guild)
        if not guild:
            return "❌ No se encontró el gremio."

        guild.remove_member(player_name)
        player.guild = None
        player.save()

        return f"🚪 **{player_name}** ha salido del gremio."

    if action == "info":
        guild_name = content[1]
        guild = Guild.load(guild_name)

        if not guild:
            return "❌ No existe un gremio con ese nombre."

        return guild.display_info()

    return "❌ Comando de gremio inválido."

