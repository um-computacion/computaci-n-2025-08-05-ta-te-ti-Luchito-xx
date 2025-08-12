import unittest
from src.jugador import Jugador

class TestJugador(unittest.TestCase):
    def test_jugador_init(self):
        j = Jugador("messi", "X")
        self.assertEqual(j.nombre, "messi")
        self.assertEqual(j.ficha, "X")

if __name__ == '__main__':
    unittest.main()

