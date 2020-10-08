import _pickle as pickle

class Player:
    def __init__(self, nombre, foto, ratio, estaVivo, kills):
        self.nombre = nombre
        self.foto = foto
        self.ratio = ratio
        self.estaVivo = estaVivo
        self.kills = kills

nombresArchivo = open("list.txt", "r")
PlayersList = []
nombres = nombresArchivo.readlines()
nombresArchivo.close()

for name in nombres :
    a = name.replace("\n","")
    aux = Player(a, "pics/" + a + '.jpg', 10, True, 0)
    PlayersList.append(aux)

for jugador in PlayersList:
    print( jugador.nombre + "  " + jugador.foto + "  " + str(jugador.ratio) + "  " + str(jugador.estaVivo) + "  " + str(jugador.kills) )

print(str(len(PlayersList)))
#fileOut = open("../Juego/save.dat", 'wb')
#pickle.dump(PlayersList, fileOut)
#fileOut.close()

fileOut = open("save.dat", 'wb')
pickle.dump(PlayersList, fileOut)
fileOut.close()

