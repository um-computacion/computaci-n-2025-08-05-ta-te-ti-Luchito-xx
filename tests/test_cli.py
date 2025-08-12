import unittest
from src.cli import mostrar_tablero

class TestCLI(unittest.TestCase):
    
    def test_mostrar_tablero(self):
        tablero = [
            ["X", "O", ""],
            ["", "X", "O"],
            ["O", "", "X"]
        ]
        try:
            mostrar_tablero(tablero)
        except Exception as e:
            self.fail(f"mostrar_tablero lanzó una excepción: {e}")

if __name__ == '__main__':
    unittest.main()
