import random

def handle_response(message):
    p_message = message.lower()

    myGames = ["Portal", "Portal2", "GTAV", "Valorant", "League of Legends",
                "Fallout: New Vegas", "Bioshock", "Mass Effect", "Assasin's Creed",
               "CSGO", "Dead By Daylight", "Terraria", "Dead Space 2", "Mario Kart Tour", 
               "Super Mario Galaxy 2", "Manhunt 2", "Pokemon Platinum", "Tales of Zestria",
               "Forza Horizon 5", "Call of Duty", "Animal Crossing", "Fortnite", "Minecraft",
               "Genshin Impact", "Roblox", "Apex Legends", "Team Fight Tactics"]
    
    lolItems = ["Relicario de los Solari", "Renovador de piedra lunar", "Ecos de Helia",
                "Redencion", "Bendicion de Mikael", "Pebetero Ardiente", "Mandato Imperial", 
                "Baculo de Agua Fluyente", "Corazon de Hielo", "Umbral del Invierno", 
                "Mascara Abisal", "Cituron Cohete Hextech", "Colmillo del Serpiente", 
                "Cadenas de Anatema", "Cetro de Crytsal de Rylai", "Espada de la Penumbra",
                "Vara de las Edades", "Guantelete de Hijo de Hielo", "Egida de Fuego Solar", "Cota de Espinas", "Daga de Statik", 
                "Maldad", "Espada Fantasma de Yoummuu", "Presagio de Randuin", "Enfoque del Horizaonte",
                "Esfera del Amanecer", "Oportunidades", "Desesperacion Eterna", "Bailarin Espectral", "Huracan del Runnan", "Al Filo de la Cordura", 
                "Fauces del Malmortius", "Filo de la Noche", "Fuerza de la Naturaleza",
                "Sierraespada Quimpunk", "Resplandor Vacio", "Criptorretono", "Rukerno Kaenico", "Baculo del Arcangel", "manamune", 
                "Apariencia Espiritual", "Saqueador de Esencias", "Placa del Hombre Muerto", "Descarga Tormentosa",
                "Acompanante de Luden", "Cicloespada Voltaica", "Recordatorio Mortal", "Recuerdos del Lord Dominik", "Guantelete de Sterak", 
                "Cuchilla Oscura", "Placa Hexpermiantal", "Corazon de Acero", "canon de fuego rapido", "Diente de Nashor",
                "Espadafuria de Guinsoo", "Baculo del Vacio", "Cimitarra Mercurial","Terminus", 
                "Impulso Cosmico", "El tormento de Liandry", "Matakrakens", "Arcoescudo Inmortal", "Arco Axiomatico", "Arrogancia",
                "Armadura de Warmog", "Maldicion del Liche", "Velo de la Banshee", "Lanza de Shojin", "Agrietador", "Cielo Desgarrado",
                "El Coleccionista", "Filo de la tormenta", "Espada del Rey Arruinado", "Lumbria", "Danza de la Muerte",
                "Jak'Sho, el Proteico", "Rencor de Serylda", "Reloj de Arena de Zhonya", "Filo del Infinito", "Hidra Voraz", "Hidra Titanica",
                "RompeAvances", "Cuchillas Raudas de Navori", "Hidra Profana", "Fuerza de la Trinidad", "La Sanguinaria", "Sombrero Mortifero de Rabadon"]

    pulpoURL = ["https://mysliceofmexico.files.wordpress.com/2022/03/000-octopus-on-the-griddle.jpg?w=720", "https://gdaysouffle.com/wp-content/uploads/2017/12/Pulpo-2-of-2-1-of-1.jpg",
                "https://assets.wsimgs.com/wsimgs/ab/images/dp/recipe/202411/0006/img31l.jpg", "https://www.webconsultas.com/sites/default/files/styles/wch_image_schema/public/media/2022/10/07/pulpo_p.jpg",
                "https://juliaeats.com/wp-content/uploads/2019/02/pulpo-a-la-gallega-cdmx.jpeg?w=1024&h=758", "https://m.media-amazon.com/images/I/61H9b5F-0-L._AC_UF1000,1000_QL80_.jpg",
                "https://cielitorosado.com/wp-content/uploads/2022/07/ENSALADA-DE-PULPO-sm.jpg", "https://ml3bmzdppwng.i.optimole.com/cb:lIJf~c5e4/w:auto/h:auto/q:mauto/https://pescaderiatenreiro.es/wp-content/uploads/2021/10/Pulpo-roca.jpg",
                "https://www.thespruceeats.com/thmb/sHQbZpx1-YFi33lCA1syJN1vIQA=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/galician-style-octopus-recipe-3083727-step-03-085f2265c180470fb0c0a30475cfd5e3.jpg",
                "https://img.chefkoch-cdn.de/rezepte/2313751369001734/bilder/670890/crop-960x540/pulpo-a-la-murciana.jpg", "https://www.eatperu.com/wp-content/uploads/2021/02/step-7-chop-octopus-pulpo-flesh.jpg",
                "https://i2.wp.com/www.galiciatips.com/nl/files/2020/10/pulpo.jpg?resize=300%2C236&ssl=1", "https://www.gob.mx/cms/uploads/article/main_image/136171/pulpo.jpg",
                "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR7uSWNPyTr0SSSgAPT43OlakVhTqPm3Vi3s3YjYx4Xzg&s", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-cwexu0hiEWToA1xpp75tslWANfHFWIB56xvXacMXOQ&s",
                "https://cdn.recetasderechupete.com/wp-content/uploads/2016/07/Cocer-pulpo.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSh_aGB_rZf-eWPKbtebeLBQgwPrmhWthv1HYSrjdAL3g&s"]
    
    horaDeLigoleyenURL = ["https://tenor.com/view/ara-anime-eyebrow-up-gif-15721758", "https://tenor.com/view/dinkdonk-dink-gif-23136125", "https://tenor.com/view/hippy-ayaka-gif-22867277"
                          , "https://tenor.com/view/uwu-raiden-ei-gif-25331540", "https://tenor.com/view/zhongli-dance-phut-hon-genshin-impact-gif-20000532", "https://tenor.com/view/zhongli-mem-gif-24517525",
                          "https://tenor.com/view/anime-dance-doll-gif-14813413", "https://tenor.com/view/patapata-gif-941360629596385757", "https://tenor.com/view/sousou-no-frieren-frieren-beer-friren-%D1%84%D1%80%D0%B8%D1%80%D0%B5%D0%BD-gif-14322219776376419169"]
    
    myResponses = ["de quien eres?", "recomiendame un juego", "dame un build", "dame un item", "adivina mi color", "tira un dado", "te amo", 
                   "estoy triste", "cara o escudo", "dile a via que se calle", "eres gay?", "que es (tu opcion)", "estas despierto?", "prende el server", "dame un pulpo", 
                   "comiendo pulpo", "hola via", "despierten es hora de ligoleyen"]
    
    if p_message == "!manual":
        tempString = "Respondere con la frase: liverbot acompanado con: "
        for response in myResponses:
            tempString += ", " + response
        tempString += "."
        return tempString

    if p_message == "liverbot de quien eres?":
        return "Del LiverOil (JH)"
    
    if p_message == "liverbot recomiendame un juego":
        return random.choice(myGames)
    
    if p_message == "liverbot dame un build":        
        botas = ["Botas de rapidez", "Botas Ionicas de Lucidez", "Botas de Movilidad", "Grebas del Berserker", 
                 "Botas del Hechicero", "punteras de Acero Revestidas", "Botas de Mercurio"]
        
        build = random.sample(lolItems,5)
        build.append(random.choice(botas))
        return build

    if p_message == "liverbot dame un item":
        return random.choice(lolItems)

    if "liverbot adivina mi color" in p_message:
        myColors = ["negro", "negro carbon", "negro por dentro", "negro azabache", "https://tenor.com/view/dark-gif-22147668"]
        return random.choice(myColors)
    
    if p_message == "liverbot tira un dado":
        return random.randint(1,6)
    
    if p_message == "liverbot te amo":
        return "No amo zorras, lo siento"
    
    if p_message == "liverbot estoy triste":
        tristResponses = ["Abraza un zapato con suela", "Ya no estes triste", "A ok", "por gei", "Come pasta, te recomiendo penne"]
        return random.choice(tristResponses)
    
    if p_message == "liverbot cara o escudo":
        coinURL = ["https://tenor.com/view/heads-coinflip-flip-a-coin-coin-coins-gif-21479854", "https://tenor.com/view/coins-tails-coin-flip-a-coin-coinflip-gif-21479856"]
        return random.choice(coinURL)
        
    if p_message == "liverbot dile a via que se calle":
        return "Viaagra callese"
    
    if p_message == "liverbot eres gay?":
        return "Yugo es el gei"
    
    if "liverbot que es" in p_message:
        queEsRes= ["clasista", "gay", "gay y homofobico", "xenofobo", "racista", "racista y negro", "https://tenor.com/view/dark-gif-22147668"]
        return random.choice(queEsRes)
    
    if p_message == "liverbot estas despierto?":
        return "desafortunadamente si :("
    
    if p_message == "gei":
        geiTuURL = ["https://tenor.com/view/naruto-funny-face-gif-12583199", "https://tenor.com/view/gay-d-gay-gif-26897914"]
        return "gei tu" + "\n" + random.choice(geiTuURL)
    
    if "prende el server" in p_message:
        return "prendelo tu gei"
    
    if "comiendo pulpo" in p_message:
        return "callese viaagra"
    
    if p_message == "liverbot dame un pulpo":
        return random.choice(pulpoURL)
    
    if p_message == "hola via":
        holaViaURL = ["https://cdn.discordapp.com/attachments/1210035283211591740/1234597655477485638/Screenshot_2024-04-29-16-08-09-591.jpg?ex=6631502a&is=662ffeaa&hm=60160cecb15e00d1b0ba0c679ae3ddd4a40617a91d0fb6ed19923dfc39bb3647&",
                      "https://tenor.com/view/viagra-viva-viva-viagra-commercial-ad-gif-22470357"]
        return random.choice(holaViaURL)
    
    if "despierten es hora de" in p_message:
        return random.choice(horaDeLigoleyenURL)