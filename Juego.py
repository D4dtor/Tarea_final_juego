from Tablero import Tablero
from Mochila import Mochila
from Persona import Persona
from Lapiz import Lapiz

class Juego:
    def __init__(self):
        self.__tablero = Tablero(6,6)
        m = Mochila("M")
        p = Persona("J1")
        l = Lapiz("✎")
        self.__tablero.ponerObjetoPosicion(p,0,0)
        self.__tablero.ponerObjetoPosicion(m,1,1)
        self.__tablero.ponerObjetoPosicion(l,2,2)
        self.__fin = False
    
    def comenzar(self):
        x=0
        while(x<1):
            self.__tablero.mostrarTablero()
            a=str(input("¿A que direccion quieres ir? "))
            if((a=="w") or (a=="a") or (a=="s") or (a=="d")):
                return a
            else:
                print("Elija una tecla valida")



