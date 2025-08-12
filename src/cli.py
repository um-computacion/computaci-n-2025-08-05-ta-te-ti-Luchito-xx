from tateti import Tateti
from exception import PosOcupadaException, RangosException

def mostrar_tablero(tab):
    print("\n", tab[0],"\n", tab[1], "\n", tab[2], "\n")

def main():
    print("Bienvenidos al Tateti")
    juego = Tateti()

    while True:
        mostrar_tablero(juego.tablero.contenedor)
        jugador = juego.jugador()
        print(f"\nTurno del jugador: {jugador.nombre} \nFicha: {jugador.ficha} \n")

        try:
            fil = int(input("Ingrese fila (0-2): "))
            col = int(input("Ingrese columna (0-2): "))
            if not (0 <= fil <= 2 and 0 <= col <= 2):
                print("\nPor favor ingresa numeros validos (0, 1 o 2)")
                continue
            juego.ocupar_casilla(fil, col)
        except PosOcupadaException as e:
            print(e)
        except Exception as e:
            print(e)
            mostrar_tablero(juego.tablero.contenedor)
            break

if __name__ == '__main__':
    main()