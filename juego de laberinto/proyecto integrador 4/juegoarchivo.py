class Juego:
    def __init__(self, mapa, inicio, fin):
        self.mapa = mapa
        self.inicio = inicio
        self.fin = fin

    # Aquí puedes reescribir tus funciones como métodos de la clase
    # Por ejemplo, si tenías una función para mover al jugador, podría verse así:
    def mover_jugador(self, direccion):
        # Código para mover al jugador
        pass
    import os
import random

class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        nombre_archivo = random.choice(os.listdir(path_a_mapas))
        path_completo = f"{path_a_mapas}/{nombre_archivo}"
        mapa, inicio, fin = self.leer_mapa(path_completo)
        super().__init__(mapa, inicio, fin)

    def leer_mapa(self, path_completo):
        with open(path_completo, 'r') as archivo:
            # Aquí debes leer el archivo y extraer el mapa, inicio y fin
            # Asegúrate de devolver estos valores
            pass

