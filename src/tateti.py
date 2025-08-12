from tablero import Tablero
from jugador import Jugador

class Tateti:
    def __init__(self, nombre1="Elpro", nombre2="Elcrack"):
        self.jugadores = [
            Jugador(nombre1, "X"),
            Jugador(nombre2, "O")
        ]
        self.turno_index = 0
        self.tablero = Tablero()
        self.finalizar = False

    def jugador(self):
        return self.jugadores[self.turno_index]

    def ocupar_casilla(self, fil, col):

        self.tablero.poner_la_ficha(fil, col, self.jugador().ficha)

        ganador = self.ganador()
        if ganador:
            self.finalizar = True
            raise Exception(f"\nVictoria de: {self.jugador().nombre}")

        if self.esta_lleno():
            self.finalizar = True
            raise Exception("\nEmpate")

        self.turno_index = 1 - self.turno_index

    def ganador(self):

        tabla = self.tablero.contenedor

        combinaciones = [

            # fila
            ((0,0),(0,1),(0,2)),
            ((1,0),(1,1),(1,2)),
            ((2,0),(2,1),(2,2)),
            # columna
            ((0,0),(1,0),(2,0)),
            ((0,1),(1,1),(2,1)),
            ((0,2),(1,2),(2,2)),
            # diagonal
            ((0,0),(1,1),(2,2)),
            ((0,2),(1,1),(2,0)),

        ]

        for x in combinaciones:
            casilla = tabla[x[0][0]][x[0][1]]

            if casilla == "":
                continue

            if casilla == tabla[x[1][0]][x[1][1]] == tabla[x[2][0]][x[2][1]]:
                return x

        return None


    def esta_lleno(self):

        for fila in self.tablero.contenedor:
            for celda in fila:
                if celda == "":
                    return False
        return True
