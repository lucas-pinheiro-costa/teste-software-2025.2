import unittest
from io import StringIO
import sys

def classificar_triangulo(L1, L2, L3):
    if not all(isinstance(x, int) for x in [L1, L2, L3]):
        return "ERRO: Por favor, insira apenas números inteiros válidos."
    if ((L1 + L2) > L3) and ((L1 + L3) > L2) and ((L2 + L3) > L1):
        if L1 == L2 and L2 == L3:
            return "O triângulo é EQUILÁTERO (todos os lados são iguais)."
        elif L1 == L2 or L1 == L3 or L2 == L3:
            return "O triângulo é ISÓSCELES (possui dois lados iguais)."
        else:
            return "O triângulo é ESCALENO (todos os lados são diferentes)."
    else:
        return "ERRO: Os valores fornecidos não podem formar um triângulo."

class TestClassificacaoTriangulo(unittest.TestCase):
    def test_escaleno(self):
        self.assertEqual(classificar_triangulo(3, 4, 5), "O triângulo é ESCALENO (todos os lados são diferentes).")

    def test_equilatero(self):
        self.assertEqual(classificar_triangulo(5, 5, 5), "O triângulo é EQUILÁTERO (todos os lados são iguais).")

    def test_isosceles(self):
        self.assertEqual(classificar_triangulo(4, 4, 5), "O triângulo é ISÓSCELES (possui dois lados iguais).")
        self.assertEqual(classificar_triangulo(3, 3, 4), "O triângulo é ISÓSCELES (possui dois lados iguais).")
        self.assertEqual(classificar_triangulo(3, 4, 3), "O triângulo é ISÓSCELES (possui dois lados iguais).")
        self.assertEqual(classificar_triangulo(4, 3, 3), "O triângulo é ISÓSCELES (possui dois lados iguais).")

    def test_zero(self):
        self.assertEqual(classificar_triangulo(0, 4, 5), "ERRO: Os valores fornecidos não podem formar um triângulo.")

    def test_negativo(self):
        self.assertEqual(classificar_triangulo(-3, 4, 5), "ERRO: Os valores fornecidos não podem formar um triângulo.")

    def test_soma_igual_terceiro(self):
        self.assertEqual(classificar_triangulo(2, 2, 4), "ERRO: Os valores fornecidos não podem formar um triângulo.")
        self.assertEqual(classificar_triangulo(4, 2, 2), "ERRO: Os valores fornecidos não podem formar um triângulo.")
        self.assertEqual(classificar_triangulo(2, 4, 2), "ERRO: Os valores fornecidos não podem formar um triângulo.")

    def test_soma_menor_terceiro(self):
        self.assertEqual(classificar_triangulo(1, 2, 4), "ERRO: Os valores fornecidos não podem formar um triângulo.")
        self.assertEqual(classificar_triangulo(4, 1, 2), "ERRO: Os valores fornecidos não podem formar um triângulo.")
        self.assertEqual(classificar_triangulo(2, 4, 1), "ERRO: Os valores fornecidos não podem formar um triângulo.")

    def test_entrada_invalida(self):
        self.assertEqual(classificar_triangulo("a", 4, 5), "ERRO: Por favor, insira apenas números inteiros válidos.")
        self.assertEqual(classificar_triangulo(3, "b", 5), "ERRO: Por favor, insira apenas números inteiros válidos.")
        self.assertEqual(classificar_triangulo(3, 4, "c"), "ERRO: Por favor, insira apenas números inteiros válidos.")

if __name__ == "__main__":
    unittest.main()
