##########################################################################################

import random as rd         # Librería para números random

##########################################################################################

class part:                 # Clase para las partículas
    def __init__(self, ID, masa, carga, radio, posicion, velocidad, aceleracion):
        self.ID=ID
        self.masa= masa
        self.carga=carga
        self.radio=radio
        self.posicion=posicion
        self.velocidad=velocidad
        self.aceleracion=aceleracion
    
    # Funciones para imprimir el valor de dicha característica
    
    def PrintID(self):            
        print(self.ID)

    def Printmasa(self):
        print("masa=",self.masa)
    
    def Printcarga(self):
        print("carga=",self.carga)
    
    def Printradio(self):
        print("radio=",self.radio)
    
    def Printposicion(self):
        print("posición=",self.posicion)
    
    def Printvelocidad(self):
        print("velocidad=",self.velocidad)

    def Printaceleracion(self):
        print("aceleración=",self.aceleracion)

##########################################################################################

# Prueba para obtener y cambiar los datos de un objeto
p1=part(1,2,3,4,5,6,7)    # ejemplo partícula 1

p1.Printmasa()            
p1.masa=1                 # Se cambia el valor de la masa a 1
a=p1.masa                 # Se asigna a una variable el valor de la masa para 
                          # corroborar que el dato obtenido es correcto
print("masa=",a)
p1.Printmasa()

##########################################################################################

Lista=[]                  # Se crea una lista de tamaño arbitrario
N=5                       # Se elige la cantidad de partículas a crear

for i in range(N):
  masa = rd.randint(1,5)  # Se asignan valores aleatorios para cada característica
  carga = rd.randint(1,5)
  radio = rd.randint(1,5)
  posicion = rd.randint(1,5)
  velocidad = rd.randint(1,5)
  aceleracion = rd.randint(1,5)

  # Con los valores asignados se crea una partícula con ID=i
  Lista.append(part(i,masa,carga,radio,posicion,velocidad,aceleracion))

##########################################################################################

for a in Lista:             # Se recorre la lista creada para observar determinadas características
  print("ID=",a.ID,"masa=",a.masa)

def info(ide,Lista):        # Función ver todas las características de una partícula cualquiera
  print("\nID=",Lista[ide].ID,"\nmasa=",Lista[ide].masa,"\ncarga=",Lista[ide].carga)
  print("radio=",Lista[ide].radio,"\nposicion=",Lista[ide].posicion,"\nvelocidad=",Lista[ide].velocidad)
  print("aceleracion=",Lista[ide].aceleracion)

info(1,Lista)               # Se revisa la información de la partícula 1

##########################################################################################