# 🏰 Liverbot - Bot de RPG para Discord

Liverbot es un bot de RPG interactivo para Discord que permite a los jugadores **crear personajes, unirse a gremios, luchar contra enemigos y subir de nivel**.  
Los gremios y personajes se **guardan de forma persistente**, por lo que el progreso nunca se perderá, incluso si el bot se reinicia.

---

## **📌 Características**
✅ **Sistema de Personajes** → Crea, sube de nivel y guarda tu personaje  
✅ **Sistema de Gremios** → Crea, únete y gestiona gremios  
✅ **Batallas & Eventos** → Enfréntate a enemigos, descansa en posadas y gana recompensas  
✅ **Generador de Builds** → Obtén una build aleatoria de League of Legends  
✅ **Generador de Composiciones de TFT** → Consulta las mejores composiciones de TFT  
✅ **Sistema de Bienvenida** → Genera tarjetas personalizadas para nuevos miembros  
✅ **Datos Persistentes** → Los personajes y gremios se guardan en JSON  
✅ **Juego Personalizable** → Modifica la lógica del juego fácilmente  

---

## **🔧 Instrucciones de Instalación**
### **1️⃣ Crear un Entorno Virtual**
Primero, crea y activa un entorno virtual para mantener las dependencias aisladas.

#### **En Windows:**
```sh
python -m venv venv
venv\Scripts\activate
```

#### **En macOS/Linux:**
```sh
python3 -m venv venv
source venv/bin/activate
```

---

### **2️⃣ Instalar Dependencias**
Asegúrate de tener Python instalado y luego instala las librerías necesarias:

```sh
pip install -r requirements.txt
```

Si `requirements.txt` no existe, instala las librerías manualmente:
```sh
pip install discord json requests pillow selenium
```

---

### **3️⃣ Configurar Variables de Entorno**
Crea un archivo `.env` o configura el **token del bot de Discord** manualmente:

#### **En macOS/Linux:**
```sh
export DISCORD_BOT_TOKEN="tu-token-aquí"
```

#### **En Windows (CMD):**
```sh
set DISCORD_BOT_TOKEN=tu-token-aquí
```

---

### **4️⃣ Ejecutar el Bot**
```sh
python bot.py
```

---

## **🎮 Guía de Comandos**
El bot tiene cinco sistemas principales:  
**1️⃣ Sistema RPG** (Creación de personajes, batallas, descanso)  
**2️⃣ Sistema de Gremios** (Creación, gestión e información de gremios)  
**3️⃣ Generador de Builds** (League of Legends)  
**4️⃣ Generador de Composiciones de TFT** (Consulta las mejores composiciones)  
**5️⃣ Sistema de Bienvenida** (Tarjetas de bienvenida personalizadas)  

---

### **📜 Comandos del Sistema RPG**
| Comando | Descripción |
|---------|-------------|
| `!rpg <nombre_de_personaje> crear` | Crea un nuevo personaje |
| `!rpg <nombre_de_personaje> stats` | Muestra las estadísticas del personaje |
| `!rpg <nombre_de_personaje> aventura` | Ir de aventura (batallas o encontrar objetos) |
| `!rpg <nombre_de_personaje> descansar` | Descansa en una posada (restaura HP, cuesta oro) |

---

### **🏰 Comandos del Sistema de Gremios**
| Comando | Descripción |
|---------|-------------|
| `!guild <nombre_del_gremio> crear` | Crea un nuevo gremio |
| `!guild <nombre_de_personaje> unirse <nombre_del_gremio>` | Únete a un gremio |
| `!guild <nombre_de_personaje> salir` | Sal del gremio |
| `!guild <nombre_del_gremio> info` | Muestra los miembros del gremio |

---

### **⚔️ Comando de Generador de Builds**
| Comando | Descripción |
|---------|-------------|
| `!build` | Genera una build aleatoria de League of Legends |

---

### **🔹 Generador de Composiciones de TFT**
El bot obtiene las **mejores composiciones de Teamfight Tactics (TFT)** desde MetaTFT.

| Comando | Descripción |
|---------|-------------|
| `!TFT` | Consulta las 5 mejores composiciones de TFT y sus campeones |

Cuando se usa este comando, el bot recopila **las mejores composiciones meta de MetaTFT** y las muestra en un formato estructurado.

Ejemplo de salida:
```
🔹 **Composiciones de TFT**
🛡️ 1. Invocadores y Magos
⚔️ Campeones: Ahri, Soraka, Lux, Taric, Syndra, Vel'Koz

🛡️ 2. Guardianes y Luchadores
⚔️ Campeones: Nasus, Sett, Jax, Garen, Riven, Warwick
```

---

### **👋 Sistema de Bienvenida**
El bot **da la bienvenida automáticamente** a los nuevos miembros enviando una imagen personalizada con su **nombre y avatar**.

#### **🔹 Comando de Prueba**
Puedes probar la función de bienvenida con:
```sh
!test_channel
```
El bot enviará un mensaje de bienvenida en el canal designado.

#### **📌 Configuración del Canal de Bienvenida**
1. **Asegúrate de que el bot tenga permisos** para enviar mensajes e imágenes en el canal de bienvenida.
2. **Configura el ID del canal de bienvenida** en `bot.py`.

---

## **📂 Estructura de Archivos & Almacenamiento de Datos**
El bot **guarda automáticamente todos los personajes, gremios y builds**, así como las imágenes de bienvenida.

```
📦 RPG-Bot/
 ┣ 📂 data/               # Almacena datos de personajes, gremios y builds
 ┃ ┣ 📜 characters.json   # Guarda las estadísticas de los personajes
 ┃ ┣ 📜 guilds.json       # Guarda la información de los gremios
 ┃ ┣ 📜 items.json        # Guarda los ítems de League of Legends
 ┃ ┣ 📜 welcome_background.jpg  # Imagen de fondo para la bienvenida
 ┣ 📜 bot.py              # Lógica principal del bot de Discord
 ┣ 📜 rpg_game.py         # Mecánicas del juego RPG
 ┣ 📜 scraper.py          # Scraping de TFT desde MetaTFT
 ┣ 📜 image_generator.py  # Generación de imágenes de bienvenida
 ┣ 📜 README.md           # Instrucciones y guía de uso
 ┣ 📜 requirements.txt    # Archivo de dependencias
```

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
