import unittest
import math
from main import calculadora, calculadora_v2, calculadora_v3, calculadora_v4

class TestCalculadora(unittest.TestCase):

    def executar_bateria_testes(self, func):
        # Teste com operações básicas
        self.assertEqual(func(2, 3, '+'), 5)
        self.assertEqual(func(5, 3, '-'), 2)
        self.assertEqual(func(2, 4, '*'), 8)
        self.assertEqual(func(8, 2, '/'), 4)
        self.assertEqual(func(9, 4, '%'), 1)
        self.assertEqual(func(2, 3, '^'), 8)

        # Teste com divisão por zero e módulo por zero
        self.assertTrue(math.isnan(func(5, 0, '/')))
        self.assertTrue(math.isnan(func(5, 0, '%')))

        # Teste com operadores inválidos
        self.assertTrue(math.isnan(func(2, 3, '$')))
        self.assertTrue(math.isnan(func(2, 5, '#')))
        self.assertTrue(math.isnan(func(0, 2, 'qwe')))

        # Teste com números em ponto flutuante
        self.assertAlmostEqual(func(2.5, 1.5, '+'), 4.0)
        self.assertAlmostEqual(func(4.5, 1.5, '-'), 3.0)
        self.assertAlmostEqual(func(5.5, 1.5, '*'), 8.25)
        self.assertAlmostEqual(func(7.5, 1.5, '/'), 5.0)
        self.assertAlmostEqual(func(7.5, 2.0, '%'), 1.5)
        self.assertAlmostEqual(func(2.0, 3.0, '^'), 8.0)

        # Teste com números negativos
        self.assertEqual(func(-2, 3, '*'), -6)
        self.assertEqual(func(-6, 3, '/'), -2.0)
        self.assertEqual(func(-7, 3, '%'), 2.0)
        self.assertEqual(func(-2, 3, '^'), -8)
        self.assertEqual(func(0, 3, '^'), 0)

        # Chamar as operações das calculadoras (v1 - v4)
    def test_calculadora_v1(self):
        self.executar_bateria_testes(calculadora)

    def test_calculadora_v2(self):
        self.executar_bateria_testes(calculadora_v2)

    def test_calculadora_v3(self):
        self.executar_bateria_testes(calculadora_v3)

    def test_calculadora_v4(self):
        self.executar_bateria_testes(calculadora_v4)


if __name__ == '__main__':
    unittest.main()


# para correr os testes: python -m unittest -v testes_main_alunos.py
