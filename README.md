# 🏰 Liverbot
Un **bot de RPG totalmente interactivo** para Discord que permite a los jugadores **crear personajes, unirse a Guilds, luchar contra enemigos y subir de nivel**.  
Los Guilds y personajes se **guardan de forma persistente**, por lo que el progreso nunca se perderá, incluso si el bot se reinicia.

---

## **📌 Características**
✅ **Sistema de Personajes** → Crea, sube de nivel y guarda tu personaje  
✅ **Sistema de Guilds** → Crea, únete y gestiona Guilds  
✅ **Batallas & Eventos** → Enfréntate a enemigos, descansa en posadas y gana recompensas  
✅ **Generador de Builds** → Obtén una build aleatoria de League of Legends  
✅ **Sistema de Bienvenida** → Genera tarjetas personalizadas para nuevos miembros  
✅ **Datos Persistentes** → Los personajes y Guilds se guardan en JSON  
✅ **Juego Personalizable** → Modifica la lógica del juego fácilmente  

---

## **🔧 Instalación**
### **1️⃣ Instalar Dependencias**
Asegúrate de tener Python instalado y luego ejecuta:
```sh
pip install discord json requests pillow
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
El bot tiene cuatro sistemas principales:  
**1️⃣ Sistema RPG** (Creación de personajes, Batallas, Descanso)  
**2️⃣ Sistema de Guilds** (Creación, Gestión e Información de Guilds)  
**3️⃣ Generador de Builds** (League of Legends)  
**4️⃣ Sistema de Bienvenida** (Tarjetas de bienvenida personalizadas)  

---

### **📜 1️⃣ Comandos del Sistema RPG**
| Comando | Descripción |
|---------|-------------|
| `!rpg <nombre_de_personaje> crear` | Crea un nuevo personaje |
| `!rpg <nombre_de_personaje> stats` | Muestra las estadísticas del personaje |
| `!rpg <nombre_de_personaje> aventura` | Ir de aventura (batallas o encontrar objetos) |
| `!rpg <nombre_de_personaje> descansar` | Descansa en una posada (restaura HP, cuesta oro) |

---

### **🏰 2️⃣ Comandos del Sistema de Guilds**
| Comando | Descripción |
|---------|-------------|
| `!guild <nombre_del_gremio> crear` | Crea un nuevo gremio |
| `!guild <nombre_de_personaje> unirse <nombre_del_gremio>` | Únete a un gremio |
| `!guild <nombre_de_personaje> salir` | Sal del gremio |
| `!guild <nombre_del_gremio> info` | Muestra los miembros del gremio |

---

### **⚔️ 3️⃣ Comando de Generador de Builds**
| Comando | Descripción |
|---------|-------------|
| `!build` | Genera una build aleatoria de League of Legends |

---

### **👋 4️⃣ Sistema de Bienvenida**
El bot **da la bienvenida automáticamente** a los nuevos miembros del servidor enviando una imagen personalizada con su **nombre y avatar**.  

📌 **Ejemplo de imagen generada:**
```
🎉 ¡Bienvenido, MiembroNuevo!
```
_(Imagen personalizada con su avatar y un fondo de bienvenida)_

#### **🔹 Comando de Prueba**
Puedes probar la función de bienvenida con:
```sh
!test_welcome
```
**Respuesta del Bot:**  
_(Envía una tarjeta de bienvenida con una imagen de prueba)_

#### **📌 Configuración del Canal de Bienvenida**
Para que el bot funcione correctamente, asegúrate de que:
1. **El bot tiene permisos para enviar mensajes e imágenes** en el canal de bienvenida.
2. **Se define el canal de bienvenida** en `bot.py` (puedes encontrar el `channel_id` en Discord).

Si no estás seguro del **ID del canal**, usa este comando en Discord (Modo Desarrollador activado):
```
/channelid
```
O puedes obtenerlo haciendo clic derecho en el canal y seleccionando **"Copiar ID"**.

---

## **📂 Estructura de Archivos & Almacenamiento de Datos**
El bot **guarda automáticamente todos los personajes, Guilds y builds**, así como las imágenes de bienvenida.

```
📦 RPG-Bot/
 ┣ 📂 data/               # Almacena los datos de personajes, Guilds y builds
 ┃ ┣ 📜 characters.json   # Guarda las estadísticas de los personajes
 ┃ ┣ 📜 guilds.json       # Guarda la información de los Guilds
 ┃ ┣ 📜 items.json        # Guarda los ítems de League of Legends
 ┃ ┣ 📜 welcome_background.jpg  # Imagen de fondo para la bienvenida
 ┣ 📜 bot.py              # Lógica principal del bot de Discord
 ┣ 📜 rpg_game.py         # Mecánicas del juego RPG
 ┣ 📜 image_generator.py  # Generación de imágenes de bienvenida
 ┣ 📜 README.md           # Instrucciones y guía de uso
```

---

## **🛠 Próximas Funcionalidades**
✅ **Batallas PvP** → Peleas entre jugadores  
✅ **Sistema Avanzado de Inventario** → Equipar armas, intercambiar objetos  
✅ **Jefes & Mazmorras** → Enfréntate a enemigos épicos  
✅ **Batallas de Guilds** → Compite contra otros Guilds  
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
