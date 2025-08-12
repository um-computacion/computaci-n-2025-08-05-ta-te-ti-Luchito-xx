import unittest
from src.tateti import Tateti
from src.exception import PosOcupadaException

class TestTateti(unittest.TestCase):

    def test_ocupar_casilla_cambia_turno(self):
        juego = Tateti()
        juego.ocupar_casilla(0, 0)
        self.assertEqual(juego.jugador().ficha, "O")

    def test_ganador(self):
        juego = Tateti()
        juego.tablero.contenedor = [
            ["X", "X", "X"],
            ["", "", ""],
            ["", "", ""]
        ]
        self.assertIsNotNone(juego.ganador())

        juego.tablero.contenedor = [
            ["O", "", ""],
            ["O", "", ""],
            ["O", "", ""]
        ]
        self.assertIsNotNone(juego.ganador())

        juego.tablero.contenedor = [
            ["X", "", ""],
            ["", "X", ""],
            ["", "", "X"]
        ]
        self.assertIsNotNone(juego.ganador())

        juego.tablero.contenedor = [
            ["", "", "O"],
            ["", "O", ""],
            ["O", "", ""]
        ]
        self.assertIsNotNone(juego.ganador())

        juego.tablero.contenedor = [
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["O", "X", "O"]
        ]
        self.assertIsNone(juego.ganador())


    def test_esta_lleno(self):
        juego = Tateti()
        juego.tablero.contenedor = [["X"]*3, ["O"]*3, ["X"]*3]
        self.assertTrue(juego.esta_lleno())

if __name__ == '__main__':
    unittest.main()
