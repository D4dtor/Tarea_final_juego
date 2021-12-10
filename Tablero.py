from Vacio import Vacio

class Tablero(object):

  """
  :version:
  :author:
  """

  def __init__(self, filas, columnas):
    self.__filas = filas
    self.__columnas = columnas
    self.__celdas =  [[Vacio("_")  for x in range(filas)] for i in range(columnas)]

  
  def get_celdas(self):
        return self.__celdas 

  def mostrarTablero(self):
        str = ""
        for i in range(self.__filas):
              for j in range(self.__columnas):
                  str+=(self.__celdas[i][j].mostrarImagen())
                  if(j == self.__columnas-1):
                        str += "\n"
        print(str)

  def ponerObjetoPosicion(self, obj, i, j):
        if((i < self.__filas) and (j < self.__columnas)):
              self.__celdas[i][j] = obj
        else:
              print("Esta fuera de rango")

  def moverObjeto(self, i_inicial, j_inicial, i_final, j_final):
        self.comenzar():
        if(a=="w"):
              """No nos ha dado tiempo terminar de implementar la version de tablero a POO"""

              """ Esta es nuestra version con funciones"""
"""
def pi(x):
    for i in range(5):
        for c in range(5):
            n=juego[i][c]
            if (n==x):
                
                return i
def pc(x):
    for i in range(5):
        for c in range(5):
            n=juego[i][c]
            if (n==x):
                
                return c


def movimiento(J1):

    x=0
    while(x<1):
        mostrar(juego)
        a=str(input("¿A que direccion quieres ir? "))
        if((a=="w") or (a=="a") or (a=="s") or (a=="d")):
            l=pi(J1)
            c=pc(J1)
            if(a=="w"):
                if(l-1<0):
                    os.system ("cls")
                    print("Elige otra direccion")
                else:
                    juego[l-1][c]=J1
                    juego[l][c]=" "
                    os.system ("cls")
                    
            if(a=="s"):
                if(l+1>4):
                    os.system ("cls")
                    print("Elige otra direccion")
                else:
                    juego[l+1][c]=J1
                    juego[l][c]=" "
                    os.system ("cls")
                    
            if(a=="a"):
                if(c-1<0):
                    os.system ("cls")
                    print("Elige otra direccion")
                else:
                    juego[l][c-1]=J1
                    juego[l][c]=" "
                    os.system ("cls")
                    
            if(a=="d"):
                if(c+1>4):
                    os.system ("cls")
                    print("Elige otra direccion")
                else:
                    juego[l][c+1]=J1
                    juego[l][c]=" "
                    os.system ("cls")
                    
        else:
            os.system ("cls")
            print("Elija una tecla valida")"""
              if(i_final<0):
                  print("Elige otra direccion")
              else:
                  juego[i_final][j_final]=J1
                  juego[i_inicial][j_inicial]=" "
        if(a=="s"):
              if(i_final>4):
                  print("Elige otra direccion")
               else:
                  juego[i_final][j_final]=J1
                  juego[i_inicial][j_inicial]=" "
                     
        if(a=="a"):
               if(j_final<0):
                              
                  print("Elige otra direccion")
               else:
                  juego[i_final][j_final]=J1
                  juego[i_inicial][j_inicial]=" "
                                
            if(a=="d"):
               if(j_final>4):
                  print("Elige otra direccion")
               else:
                  juego[i_inicial][j_final]=J1
                  juego[i_inicial][j_inicial]=" "

      """Funcion creada con el fin de cambiar la posicion del personaje 
      avanzando a la direccion elegida y cambiando la posicion anterior 
      por un espacion en blanco,no nos ha dado tiempo a terminar de implementarlo"""
 
     

    @param Objeto estado_inicial : 
    @param Objeto estado_final : 
    @return  :
    @author
    """
    pass



