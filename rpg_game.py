import os
import json
import random

# Data Folders
DATA_FOLDER = "data/"
CHARACTER_FILE = DATA_FOLDER + "characters.json"
GUILD_FILE = DATA_FOLDER + "guilds.json"

if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

# ------------------------------- LOAD & SAVE CHARACTERS -------------------------------
def load_characters():
    """Load character data from a file or return an empty dictionary."""
    if os.path.exists(CHARACTER_FILE):
        with open(CHARACTER_FILE, "r") as file:
            return json.load(file)
    return {}

def save_characters():
    """Save all characters to a JSON file."""
    with open(CHARACTER_FILE, "w") as file:
        json.dump(characters, file, indent=4)

# Load characters when bot starts
characters = load_characters()

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
                f"🏰 Guild: {self.guild or 'Ninguna'}")

    def save(self):
        """Save this character to the global character dictionary and file."""
        characters[self.name] = self.__dict__
        save_characters()

    @staticmethod
    def load(name):
        """Load a character from stored data."""
        if name in characters:
            data = characters[name]
            return Character(**data)
        return None

# ------------------------------- GAME FUNCTIONS -------------------------------
def createCharacter(name):
    """Create a new character and save to file."""
    HP = random.randint(100, 1000)
    power = random.randint(1, 50)
    money = random.randint(100, 500)
    maxHP = HP
    new_character = Character(name, HP, power, money, maxHP)
    new_character.save()
    return new_character

def handleRequest(message):
    """Handle RPG commands from the bot."""
    content = message.split(' ')
    name = content[1]
    command = content[2]

    character = Character.load(name)

    if command == "crear":
        if character:
            return "❌ Ya existe un personaje con ese nombre."
        character = createCharacter(name)
        return f"✅ Personaje creado:\n{character.display_info()}"

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

    return "❌ Comando inválido."

# ------------------------------- GUILD SYSTEM -------------------------------
def load_guilds():
    """Load guilds from file or return an empty dictionary."""
    if os.path.exists(GUILD_FILE):
        with open(GUILD_FILE, "r") as file:
            return json.load(file)
    return {}

def save_guilds():
    """Save the current guild dictionary to a file."""
    with open(GUILD_FILE, "w") as file:
        json.dump(guilds, file, indent=4)

# Load guilds when bot starts
guilds = load_guilds()

def handle_guild_request(message):
    """Handle Guild system commands."""
    content = message.split(' ')
    name = content[1]
    action = content[2]

    if action == "crear":
        if name in guilds:
            return "❌ Esa guild ya existe."
        guilds[name] = []
        save_guilds()
        return f"✅ La guild {name} ha sido creada!"

    if action == "unirse":
        guild_name = content[3]
        if guild_name not in guilds:
            return "❌ Esa guild no existe."
        if name in guilds[guild_name]:
            return f"❌ {name} ya está en la guild {guild_name}."
        guilds[guild_name].append(name)
        save_guilds()
        return f"✅ {name} se ha unido a la guild {guild_name}!"

    if action == "salir":
        for guild, members in guilds.items():
            if name in members:
                members.remove(name)
                save_guilds()
                return f"✅ {name} ha salido de la guild {guild}."
        return "❌ No estás en ninguna guild."

    if action == "info":
        guild_name = content[3]
        if guild_name not in guilds:
            return "❌ Esa guild no existe."
        return f"🏰 **Guild: {guild_name}**\nMiembros: {', '.join(guilds[guild_name])}"

    return "❌ Comando de guild inválido."
