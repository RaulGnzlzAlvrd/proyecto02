from unittest import TestCase
import numpy as np

from src.pkg.lsb.lsb import *

class TestLSB(TestCase):
    def setUp(self):
        self.pixeles = np.array(
                [  [[186, 157,   2],
                    [ 83, 152, 117],
                    [ 29, 119, 158]],

                   [[232, 222,  10],
                    [236,  79,  80],
                    [159, 131, 196]]])
        self.bits = "1001011010011"
        self.pixeles_modificados = np.array(
                [  [[187, 156,   2],
                    [ 83, 152, 117],
                    [ 29, 118, 159]],

                   [[232, 222,  11],
                    [237,  79,  80],
                    [159, 131, 196]]])
        self.bits_extraidos = "100101101001110"

    def test_guarda_bits(self):
        obtenido = guarda_bits(self.bits, self.pixeles)
        resultado = np.testing.assert_array_equal(self.pixeles_modificados, obtenido)
        self.assertIsNone(resultado)

    def test_extrae_bits(self):
        obtenido = extrae_bits(self.pixeles_modificados)
        self.assertEqual(self.bits_extraidos, obtenido)
