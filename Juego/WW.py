from random import randint
from PIL import Image
from collections import Counter
import tweepy
import time
import random
import _pickle as pickle

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""
size = 400, 400

def contarVivos(lista):
    aux = 0;
    for item in lista:
        if(item.estaVivo):
            aux = aux + 1
    return aux

def fraseResurreccion(nombre):
    aux = randint(0,5)
    if aux==0:
        return ("El jugador " + nombre + " es bendecido por el poder de Peabody y resucita.")
    elif aux==1:
        return (nombre + " decide que no es el momento de darse por vencido. \n" + nombre + " resucita.")
    elif aux==2:
        return ("Tras vencer a los demonios en lo más profundo del inframundo, " + nombre + " logra la resurreccion.")
    elif aux==3:
        return ("Se escucha un grito del cementerio. \n" + nombre + " no había pronunciado aún su última palabra.")
    elif aux==4:
        return ("Dios ofrece a " + nombre + " un traguito de ClarioCao, resucitándolo.")
    else:
        return (nombre + " no pudo terminar en vida su cruzada personal. \n" + nombre + " logra resucitar") 
def fraseSuicidio(nombre):
    aux = randint(0,5)
    if aux==0:
        return ("¡Oh no! ¡Al jugador " + nombre + " le han caído unas vigas del techo! ")
    elif aux==1:
        return ("El jugador "  + nombre + " ha tomado demasiada piedra Alius." + nombre + " cae muerto.")
    elif aux==2:
        return (nombre + " ha encontrado un cuaderno y ha decidido escribir su nombre en él. " + nombre + " muere de un infarto unos segundos después.")
    elif aux==3:
        return (nombre + " se ha levantado a las 10:56 y se ha perdido el capítulo de Orion.")
    elif aux==4:
        return ("El Naesquick no ha sentado bien a " + nombre + " y se muere.")
    else:
        return (nombre + " tropieza con una piel de plátano y se esnuca.")

def fraseMayor2(nombre1, nombre2):
    aux = randint(0,15)
    if aux==0:
        return ("" + nombre1 + " ha matado a " + nombre2 + ".")
    elif aux==1:
        return ("" + nombre1 + " ha asesinado a " + nombre2 + ".")
    elif aux==2:
        return ("" + nombre1 + " ha acuchillado hasta la muerte a " + nombre2 + ".")
    elif aux==3:
        return ("" + nombre2 + " ha sido asesinado por " + nombre1 + ".")
    elif aux==4:
        return ("" + nombre2 + " ha sido hallado muerto tras una pelea con " + nombre1 + ".")
    elif aux==5:
        return ("" + nombre2 + " ha sido acuchillado por " + nombre1 + ".")
    elif aux==6:
        return ("" + nombre1 + " le ha lanzado una piedra en la cabeza a " + nombre2 + " y " + nombre2 + " ha muerto.")
    elif aux==7:
        return ("" + nombre1 + " se ha acercado a abrazar a " + nombre2 + ", pero " + "" + nombre2 + " se ha caído por un acantilado tratando de huir.")
    elif aux==8:
        return ("" + nombre2 + " ha sido atropellado por el camion de " + nombre1 + ", que iba a 200km/h.")
    elif aux==9:
        return ("" + nombre1 + " ha tirado a " + nombre2 + " por las escaleras. " + nombre2 + " ha muerto.")
    elif aux ==10:
        return ("" + nombre2 + " cayó en una trampa mortal de " + nombre1 + ".")
    elif aux == 11:
        return ("" + nombre2 + " intenta robar los sets competitivos de " + nombre1 + ", pero falla en el intento y " + nombre1 + " lo asesina.")
    elif aux == 12:
        return ("" + nombre1 + " le ha dado un sillazo en la nuca a "+ nombre2 + ".")
    elif aux == 13:
        return ("Este día tenía que llegar, fue un placer. " + nombre1 + " bloquea a " + nombre2 + " y este cae debilitado.")
    elif aux == 14:
        return (nombre2 + " es pillado viendo Captain Tsubasa por " + nombre1 + " y lo lincha.")
    else:
        return ("" + nombre1 + " le ha dado a " + nombre2 + " un jugo sospechoso. " + nombre2 + " se lo bebe y cae muerto.")


class Player:
    def __init__(self, nombre, foto, ratio, estaVivo, kills):
        self.nombre = nombre
        self.foto = foto
        self.ratio = ratio
        self.estaVivo = estaVivo
        self.kills = kills
    def kill(self, other): #Pone a False el other.estarVivo y aumenta su poder
        other.estaVivo = False
        self.kills = self.kills + 1
        self.ratio = self.ratio + randint(1,3)
        numVivos = contarVivos(PlayersList)
        frase = ""
        respuesta = ""
        if (numVivos>1):
            frase = fraseMayor2(self.nombre, other.nombre) + "\n" + "El poder de " + self.nombre + " ha aumentado a " + str(self.ratio) + ", que ha acabado con " + str(self.kills) + " oponente(s).\n" + str(numVivos) + " inazumeros restantes."
        else:
            frase = "" + self.nombre + " ha matado a " + "" + other.nombre + ". " + "\n" + "" +  self.nombre + " ha vencido a su último rival."
        if(bool(random.getrandbits(1))):                    
            respuesta = "@" + self.nombre + ", @" + other.nombre
        else:
            respuesta = "@" + other.nombre + ", @" + self.nombre
        loadIm1 = Image.open(self.foto)
        loadIm2 = Image.open(other.foto)
        loadIm1 = loadIm1.resize(size)
        loadIm2 = loadIm2.resize(size)
        loadIm2 = loadIm2.convert('L')
        new_im = Image.new('RGB', (800,400))

        if(bool(random.getrandbits(1))): #El primer jugador que se muestre en la imagen es A
             new_im.paste(loadIm1, (0,0))
             new_im.paste(loadIm2, (400,0))
             X = Image.open('pics/X2.png') 
                    
        else: #El primer jugador que se muestre en la imagen es B
             new_im.paste(loadIm2, (0,0))
             new_im.paste(loadIm1, (400,0))
             X = Image.open('pics/X1.png')
        new_im.paste(X, (0,0), X)
        vsChose = random.choice(vsList)
        new_im.paste(vsChose, (0,0), vsChose)
        imageRoute = 'test.jpg'
        new_im.save(imageRoute)
        respuesta = ""
        if(bool(random.getrandbits(1))):
            respuesta = "@" + self.nombre + " , @" + other.nombre
        else:
            respuesta = "@" + other.nombre + " , @" + self.nombre
        print(frase)
        print(respuesta)
        api.update_with_media(imageRoute, status=frase)                                                    #ACTIVAR
        tweet = api.home_timeline()[0]                                                                     #ACTIVAR
        api.update_status(respuesta, tweet.id)                                                             #ACTIVAR
        
    def suicidio(self): #Pone a False el estarVivo 
        self.estaVivo = False
        numVivos = contarVivos(PlayersList)
        frase = fraseSuicidio(self.nombre) + "\n"
        if(numVivos>1):
            frase = frase + str(numVivos) + " jugadores restantes." 
        im1 = Image.open(self.foto)
        im1 = im1.resize(size)
        im1 = im1.convert('L')
        im1 = im1.convert('RGB')
        X = Image.open('X.png')
        im1.paste(X,(0,0),X)
        im1.convert('RGB')
        imageRoute = 'test.jpg'
        im1.save(imageRoute)
        respuesta = "@" + self.nombre
        print(frase)
        print(respuesta)
        
        api.update_with_media(imageRoute, status=frase)                                                    #ACTIVAR
        tweet = api.home_timeline()[0]                                                                     #ACTIVAR
        api.update_status(respuesta, tweet.id)                                                             #ACTIVAR

    def resurreccion(self): #Pone a True el estarVivo y pone el ratio a 10
        self.estaVivo = True
        self.ratio = randint(8,12)
        numVivos = contarVivos(PlayersList)
        frase = fraseResurreccion(self.nombre) + "\n" + "El poder de " + self.nombre + " es de " + str(self.ratio) + ". \n" + str(numVivos) + " combatientes restantes."
        new_im = Image.new('RGB', (400,400))
        im1 = Image.open(self.foto)
        im1 = im1.resize(size)
        resurrect = Image.open('pics/re.png')
        new_im.paste(im1, (0,0))
        new_im.paste(resurrect, (0,0), resurrect)
        imageRoute = 'test.jpg'
        new_im.save(imageRoute)
        respuesta = "@" + self.nombre
        print(frase)
        print(respuesta)
        
        api.update_with_media(imageRoute, status=frase)                                                    #ACTIVAR
        tweet = api.home_timeline()[0]                                                                     #ACTIVAR
        api.update_status(respuesta, tweet.id)                                                             #ACTIVAR

    def evento(self):
        aux = randint(0,3)
        frase = ""
        respuesta = "@" + self.nombre
        if(aux==0):
            self.ratio = self.ratio + 2
            frase = self.nombre + " se toma un escudito del Fortnite. \n" + "Su poder ha aumentado a " + str(self.ratio) + "."
        elif(aux==1):
            self.ratio = self.ratio + 3
            frase = self.nombre + " ha aprendido Ultratécnica. \n" + "Su poder ha aumentado a " + str(self.ratio) + "."
        elif(aux==2):
            self.ratio = self.ratio - 2
            if(self.ratio<1):
                self.ratio = 1
                frase = self.nombre + " se cae por las escaleras y pierde 2 de poder, pero está al mínimo. \n" + "Su poder es de 1."
            else:
                frase = self.nombre + " se cae por las escaleras. \n" + "Su poder se ha reducido a " + str(self.ratio) + "."
        else:
            self.ratio = self.ratio - 3
            if(self.ratio<1):
                self.ratio = 1
                frase = self.nombre + " sube de nivel, aprende Vagueza y pierde 3 de poder, pero está al mínimo. \n" + "Su poder es de 1."
            else:
                frase = self.nombre + " sube de nivel, aprende Vagueza y pierde 3 de poder. \n" + "Su poder se ha reducido a " + str(self.ratio) + "."
        new_im = Image.new('RGB', size)
        im1 = Image.open(self.foto)
        im1 = im1.resize(size)
        new_im.paste(im1, (0,0))
        imageRoute = 'test.jpg'
        new_im.save(imageRoute)
        print(frase)
        print(respuesta)
        
        api.update_with_media(imageRoute, status=frase)                                                    #ACTIVAR
        tweet = api.home_timeline()[0]                                                                     #ACTIVAR
        api.update_status(respuesta, tweet.id)                                                             #ACTIVAR
        
def fullKill(Lista):
    length = len(Lista)
    a = randint(0, length-1)
    b = randint(0, length-1)
    while(not Lista[a].estaVivo):
        a = randint(0, length-1)
    while((not Lista[b].estaVivo) or (b==a)):
        b = randint(0, length-1)
    aux = randint(1,Lista[a].ratio + Lista[b].ratio)
    
    if(aux<=Lista[a].ratio):
        Lista[a].kill(Lista[b])
    else:
        Lista[b].kill(Lista[a])
        
def fullSuicidio(Lista):
    length = len(Lista)
    a = randint(0, length-1)
    while(not Lista[a].estaVivo):
        a = randint(0, length-1)
    Lista[a].suicidio()
    
def fullResurreccion(Lista):
    length = len(Lista)
    a = randint(0, length-1)
    while(Lista[a].estaVivo):
        a = randint(0, length-1)
    Lista[a].resurreccion()

def fullEvento(Lista):
    length = len(Lista)
    a = randint(0, length-1)
    while(not Lista[a].estaVivo):
        a = randint(0, length-1)
    Lista[a].evento()

#INICIAR

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

vsList = [Image.open('vs/vs1.png'), Image.open('vs/vs2.png'), Image.open('vs/vs3.png'), Image.open('vs/vs4.png')]
save = open("save.dat", "rb")
PlayersList = pickle.load(save)
save.close()

if(contarVivos(PlayersList)==len(PlayersList)):
    frase = "¡COMIENZA LA INAZUMA BATTLE ROYALE!" + "\n" + str(len(PlayersList)) + " combatientes restantes."
    print(frase)
    api.update_status(frase)                                                                                   #ACTIVAR
    
while(contarVivos(PlayersList)>1):
    print(str(contarVivos(PlayersList)))
    suceso = randint(0,1000)
    vivos = contarVivos(PlayersList)
    if suceso<75 and vivos>4 :
        fullSuicidio(PlayersList)
    elif suceso>950 and vivos<len(PlayersList):
        fullResurreccion(PlayersList)
    else:
        fullKill(PlayersList)
        
    fileOut = open("save.dat", 'wb')
    pickle.dump(PlayersList, fileOut)
    fileOut.close()
    
    sigBigEv = randint(10,60)
    evento = randint(0,1000)
    print("")
    if evento<300 and contarVivos(PlayersList)>1:
        tiempoHastaEv = randint(20,50)
        sigBigEv = sigBigEv - tiempoHastaEv
        if sigBigEv<0:
            sigBigEv = randint(10,20)
        time.sleep(60 * tiempoHastaEv)                                                                        #ACTIVAR
        fullEvento(PlayersList)
    elif contarVivos(PlayersList)==1:
        sigBigEv = 0
        
    fileOut = open("save.dat", 'wb')
    pickle.dump(PlayersList, fileOut)
    fileOut.close()
    
    time.sleep(60 * sigBigEv)                                                                                #ACTIVAR
    print("")

i = 0
while(not PlayersList[i].estaVivo):
    i = i + 1
frase = PlayersList[i].nombre + " es el campeón de la INAZUMA BATTLE ROYALE." 
new_im = Image.new('RGB', size)
im1 = Image.open(PlayersList[i].foto)
im1 = im1.resize(size)
new_im.paste(im1, (0,0))
imageRoute = 'test.jpg'
new_im.save(imageRoute)
respuesta = "@" + PlayersList[i].nombre
print(frase + "\n")
print(respuesta)
api.update_with_media(imageRoute, status=frase)                                                    #ACTIVAR
tweet = api.home_timeline()[0]                                                                     #ACTIVAR
api.update_status(respuesta, tweet.id)                                                             #ACTIVAR
    
    
        
    
        
        








