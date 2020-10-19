from particula import Particula
from algoritmos import distancia_euclidiana

class Particulas:
    def __init__(self):
        self.__particulas = []

    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)

p01 = Particula(id=150, origen_x=50, origen_y=25, destino_x=50, destino_y=25, velocidad=100, red=120, green=150, blue=200, distancia= distancia_euclidiana)
p02 = Particula(id=120, origen_x=143, origen_y=291, destino_x=234, destino_y=67, velocidad=200, red=45, green=50, blue=92, distancia=distancia_euclidiana)
particulas = Particulas()
particulas.agregar_final(p01)
particulas.agregar_inicio(p02)
particulas.agregar_inicio(p01)
particulas.mostrar()

