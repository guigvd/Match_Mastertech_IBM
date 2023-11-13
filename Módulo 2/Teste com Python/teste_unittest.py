import unittest
from unittest2 import calcArea
from math import pi

class TestCalcArea(unittest.TestCase):
    def test_area(self):
        print('--Teste de valores de resultados conhecidos--')
        self.assertRaises(ValueError, calcArea, -1)
        self.assertAlmostEqual(calcArea(1),pi)
        self.assertAlmostEqual(calcArea(0),0)
        self.assertAlmostEqual(calcArea(1),pi*(3**2))

    def test_tipos(self):
        print('--Teste de tipos compativeis--')
        self.assertRaises(TypeError, calcArea, True)
        self.assertRaises(TypeError, calcArea, 'ola')
        self.assertRaises(TypeError, calcArea, 2+3j)