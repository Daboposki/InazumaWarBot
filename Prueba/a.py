from random import randint
from PIL import Image
from collections import Counter
import tweepy
import time
import random
import _pickle as pickle
size = 400, 400
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

def contarVivos(lista):
    aux = 0;
    for item in lista:
        if(item.estaVivo):
            aux = aux + 1
    return aux

def fraseMayor2(nombre1, nombre2):
    aux = randint(0,14)
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
    else:
        return ("" + nombre1 + " le ha dado a " + nombre2 + " un jugo sospechoso. " + nombre2 + " se lo bebe y cae muerto.")

class Player:
    def __init__(self, nombre, foto, ratio, estaVivo):
        self.nombre = nombre
        self.foto = foto
        self.ratio = ratio
        self.estaVivo = estaVivo
        
    def kill(self, other): #No pone a True el estarVivo ni aumenta su poder
        other.estaVivo = False
        numVivos = contarVivos(PlayersList)
        frase = ""
        respuesta = ""
        if (numVivos>1):
            frase = fraseMayor2(self.nombre, other.nombre) + "\n" + "El poder de " + self.nombre + " ha sumentado a " + str(self.ratio) + ".\n" + str(numVivos) + " jugadores restantes."
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
        #api.update_with_media(imageRoute, status=frase)                                                    #ACTIVAR
        #api.update_status(respuesta, tweet.id)                                                             #ACTIVAR
        
    def suicidio(self): #No pone a False el estarVivo
        numVivos = contarVivos(PlayersList)
        frase = fraseSuicidio(self.nombre) + "\n"
        if(numVivos>1):
            frase = frase + + str(numVivos) + " jugadores restantes." 
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
        #api.update_with_media(imageRoute, status=frase)                                                    #ACTIVAR
        #api.update_status(respuesta, tweet.id)                                                             #ACTIVAR

    def resurreccion(self): #No pone a True el estarVivo
        numVivos = contarVivos(PlayersList)
        frase = fraseResurreccion(self.nombre) + "\n" + str(numVivos) + " combatientes restantes."
        new_im = Image.new('RGB', (400,400))
        im1 = Image.open(self.foto)
        im1 = im1.resize(size)
        resurrect = Image.open('pics/re.png')
        new_im.paste(im1, (0,0))
        new_im.paste(resurrect, (0,0), resurrect)
        imageRoute = 'test.jpg'
        new_im.save(imageRoute)
        respuesta = "@" + self.nombre
        print(frase + '\n')
        #api.update_with_media(imageRoute, status=frase)                                                    #ACTIVAR
        #api.update_status(respuesta, tweet.id)                                                             #ACTIVAR

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
vsList = [Image.open('vs/vs1.png'), Image.open('vs/vs2.png'), Image.open('vs/vs3.png'), Image.open('vs/vs4.png')]
save = open("save.dat", "rb")
PlayersList = pickle.load(save)
save.close()

print(str(PlayersList[0].estaVivo))
PlayersList[1].kill(PlayersList[0])
print(str(PlayersList[0].estaVivo))
