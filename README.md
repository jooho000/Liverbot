# 🏰 Bot RPG para Discord
Un **bot de RPG totalmente interactivo** para Discord que permite a los jugadores **crear personajes, unirse a gremios, luchar contra enemigos y subir de nivel**.  
Los gremios y personajes se **guardan de forma persistente**, por lo que el progreso nunca se perderá, incluso si el bot se reinicia.

---

## **📌 Características**
✅ **Sistema de Personajes** → Crea, sube de nivel y guarda tu personaje  
✅ **Sistema de Gremios** → Crea, únete y gestiona gremios  
✅ **Batallas & Eventos** → Enfréntate a enemigos, descansa en posadas y gana recompensas  
✅ **Generador de Builds** → Obtén una build aleatoria de League of Legends  
✅ **Datos Persistentes** → Los personajes y gremios se guardan en JSON  
✅ **Juego Personalizable** → Modifica la lógica del juego fácilmente  

---

## **🔧 Instalación**
### **1️⃣ Instalar Dependencias**
Asegúrate de tener Python instalado y luego ejecuta:
```sh
pip install discord json requests
```

### **2️⃣ Configurar Variables de Entorno**
Crea un archivo `.env` o configura tu **token del bot de Discord** manualmente:
```sh
export DISCORD_BOT_TOKEN="tu-bot-token-aquí"
```
O en Windows CMD:
```sh
set DISCORD_BOT_TOKEN=tu-bot-token-aquí
```

### **3️⃣ Ejecutar el Bot**
```sh
python3 bot.py
```

---

## **🎮 Guía de Comandos**
El bot tiene tres sistemas principales:  
**1️⃣ Sistema RPG** (Creación de personajes, Batallas, Descanso)  
**2️⃣ Sistema de Gremios** (Creación, Gestión e Información de Gremios)  
**3️⃣ Generador de Builds** (League of Legends)  

---

### **📜 1️⃣ Comandos del Sistema RPG**
| Comando | Descripción |
|---------|-------------|
| `!rpg <nombre_de_personaje> crear` | Crea un nuevo personaje |
| `!rpg <nombre_de_personaje> stats` | Muestra las estadísticas del personaje |
| `!rpg <nombre_de_personaje> aventura` | Ir de aventura (batallas o encontrar objetos) |
| `!rpg <nombre_de_personaje> descansar` | Descansa en una posada (restaura HP, cuesta oro) |

**💡 Ejemplo de Uso:**
```sh
!rpg MiPersonaje crear
!rpg MiPersonaje stats
!rpg MiPersonaje aventura
!rpg MiPersonaje descansar
```

---

### **🏰 2️⃣ Comandos del Sistema de Gremios**
| Comando | Descripción |
|---------|-------------|
| `!guild <nombre_del_gremio> crear` | Crea un nuevo gremio |
| `!guild <nombre_de_personaje> unirse <nombre_del_gremio>` | Únete a un gremio |
| `!guild <nombre_de_personaje> salir` | Sal del gremio |
| `!guild <nombre_del_gremio> info` | Muestra los miembros del gremio |

**💡 Ejemplo de Uso:**
```sh
!guild Dragones crear
!guild MiPersonaje unirse Dragones
!guild Dragones info
!guild MiPersonaje salir
```

---

### **⚔️ 3️⃣ Comando de Generador de Builds**
| Comando | Descripción |
|---------|-------------|
| `!build` | Genera una build aleatoria de League of Legends |

**💡 Ejemplo de Uso:**
```sh
!build
```
**Respuesta del Bot:**
```
🛡️ Build Aleatoria para League of Legends:
- Fuerza de la Naturaleza
- El Tormento de Liandry
- Filo de la Noche
- Arcoescudo Inmortal
- Jak'Sho, el Proteico
- Botas de Mercurio
```

---

## **📂 Estructura de Archivos & Almacenamiento de Datos**
El bot **guarda automáticamente todos los personajes y gremios** para asegurarse de que **el progreso no se pierda** si el bot se reinicia.

```
📦 RPG-Bot/
 ┣ 📂 data/               # Almacena los datos de personajes, gremios y builds
 ┃ ┣ 📜 characters.json   # Guarda las estadísticas de los personajes
 ┃ ┣ 📜 guilds.json       # Guarda la información de los gremios
 ┃ ┣ 📜 items.json        # Guarda los ítems de League of Legends
 ┣ 📜 bot.py              # Lógica principal del bot de Discord
 ┣ 📜 rpg_game.py         # Mecánicas del juego RPG
 ┣ 📜 README.md           # Instrucciones y guía de uso
```

| Tipo de Datos | Archivo |
|--------------|---------|
| Personajes | `data/characters.json` |
| Gremios | `data/guilds.json` |
| Ítems de LoL | `data/items.json` |

Si el bot **se detiene**, todos los personajes, gremios y builds **seguirán guardados**.

---

## **📌 Ejemplo de Juego**
### **1️⃣ Creando un Personaje**
```sh
!rpg MiPersonaje crear
```
**Respuesta del Bot:**
```
✅ Personaje creado:
🧙 MiPersonaje
⭐ Nivel: 1
❤️ HP: 500/500
⚔️ Poder: 30
💰 Oro: 200
📈 EXP: 0
🎒 Items: Ninguno
🏰 Gremio: Ninguno
```

### **2️⃣ Ir de Aventura**
```sh
!rpg MiPersonaje aventura
```
**Posibles Resultados:**
- 🏆 **Encuentras un cofre con tesoro!**
- ⚔️ **Peleas contra un goblin!**
- 🔥 **Te encuentras con un jefe poderoso!**

### **3️⃣ Generar una Build de LoL**
```sh
!build
```
**Respuesta del Bot:**
```
🛡️ Build Aleatoria para League of Legends:
- Fuerza de la Naturaleza
- El Tormento de Liandry
- Filo de la Noche
- Arcoescudo Inmortal
- Jak'Sho, el Proteico
- Botas de Mercurio
```

---

## **🛠 Próximas Funcionalidades**
✅ **Batallas PvP** → Peleas entre jugadores  
✅ **Sistema Avanzado de Inventario** → Equipar armas, intercambiar objetos  
✅ **Jefes & Mazmorras** → Enfréntate a enemigos épicos  
✅ **Batallas de Gremios** → Compite contra otros gremios  
✅ **Mejoras en el Generador de Builds** → Builds basadas en campeones específicos  

---

## **🚀 Opciones de Implementación**
Puedes desplegar el bot en **servicios en la nube** para que funcione 24/7:
- **[Railway](https://railway.app/)**
- **[Replit](https://replit.com/)**
- **[Heroku](https://www.heroku.com/)**
- **[AWS EC2](https://aws.amazon.com/ec2/)**

---

## **❓ ¿Necesitas Ayuda?**
Si necesitas **más funcionalidades, personalización o ayuda para desplegar el bot**, ¡pregunta y te ayudaré! 🚀
