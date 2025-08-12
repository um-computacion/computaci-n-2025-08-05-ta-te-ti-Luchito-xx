import unittest
from src.tablero import Tablero
from src.exception import PosOcupadaException

class TestTablero(unittest.TestCase):
    
    def test_poner_ficha_correcta(self):
        t = Tablero()
        t.poner_la_ficha(0, 0, "X")
        self.assertEqual(t.contenedor[0][0], "X")

    def test_poner_ficha_ocupada(self):
        t = Tablero()
        t.poner_la_ficha(0, 0, "X")
        with self.assertRaises(PosOcupadaException):
            t.poner_la_ficha(0, 0, "O")

if __name__ == '__main__':
    unittest.main()
