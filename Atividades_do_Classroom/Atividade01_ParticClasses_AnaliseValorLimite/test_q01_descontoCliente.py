import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from q01_descontoCliente import calcula_desconto

class TestDescontoCliente(unittest.TestCase):
    # Cliente A
    def test_cliente_a_sem_desconto_limite_inferior(self):
        self.assertEqual(calcula_desconto('A', 1), 0.0)
    def test_cliente_a_sem_desconto_limite_superior(self):
        self.assertEqual(calcula_desconto('A', 9), 0.0)
    def test_cliente_a_5_porcento_limite_inferior(self):
        self.assertEqual(calcula_desconto('A', 10), 0.05)
    def test_cliente_a_5_porcento_limite_superior(self):
        self.assertEqual(calcula_desconto('A', 99), 0.05)
    def test_cliente_a_10_porcento_limite_inferior(self):
        self.assertEqual(calcula_desconto('A', 100), 0.10)
    def test_cliente_a_10_porcento_limite_superior(self):
        self.assertEqual(calcula_desconto('A', 1000), 0.10)

    # Cliente B
    def test_cliente_b_5_porcento_limite_inferior(self):
        self.assertEqual(calcula_desconto('B', 1), 0.05)
    def test_cliente_b_5_porcento_limite_superior(self):
        self.assertEqual(calcula_desconto('B', 9), 0.05)
    def test_cliente_b_15_porcento_limite_inferior(self):
        self.assertEqual(calcula_desconto('B', 10), 0.15)
    def test_cliente_b_15_porcento_limite_superior(self):
        self.assertEqual(calcula_desconto('B', 99), 0.15)
    def test_cliente_b_25_porcento_limite_inferior(self):
        self.assertEqual(calcula_desconto('B', 100), 0.25)
    def test_cliente_b_25_porcento_limite_superior(self):
        self.assertEqual(calcula_desconto('B', 1000), 0.25)

    # Cliente C
    def test_cliente_c_sem_desconto_limite_inferior(self):
        self.assertEqual(calcula_desconto('C', 1), 0.0)
    def test_cliente_c_sem_desconto_limite_superior(self):
        self.assertEqual(calcula_desconto('C', 9), 0.0)
    def test_cliente_c_20_porcento_limite_inferior(self):
        self.assertEqual(calcula_desconto('C', 10), 0.20)
    def test_cliente_c_20_porcento_limite_superior(self):
        self.assertEqual(calcula_desconto('C', 99), 0.20)
    def test_cliente_c_25_porcento_limite_inferior(self):
        self.assertEqual(calcula_desconto('C', 100), 0.25)
    def test_cliente_c_25_porcento_limite_superior(self):
        self.assertEqual(calcula_desconto('C', 1000), 0.25)

if __name__ == '__main__':
    unittest.main()
