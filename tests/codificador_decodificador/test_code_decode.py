from unittest import TestCase

from src.pkg.codificador_decodificador.code_decode import *

class TestCodeDecode(TestCase):
    def test_get_bits(self):
        mensaje = "AH SI SOY"
        esperado = "00000001111101010010010001101010010011101100011011"
        obtenido = get_bits(mensaje)
        self.assertEqual(obtenido, esperado)

    def test_mensaje(self):
        bits = "00000001111101010010010001101010010011101100011011"
        esperado = "AH SI SOY"
        obtenido = get_mensaje(bits)
        self.assertEqual(obtenido, esperado)
        bits2 = "00000001111101010010010001101010010011101100011011010101111"
        esperado2 = "AH SI SOY"
        obtenido2 = get_mensaje(bits2)
        self.assertEqual(obtenido2, esperado2)

    def test_valida_tamanio(self):
        mensaje = "AH SI SOY"
        limite_valido = 50
        obtenido = valida_tamanio(mensaje, limite_valido)
        self.assertTrue(obtenido)
        limite_no_valido = 45
        obtenido = valida_tamanio(mensaje, limite_no_valido)
        self.assertFalse(obtenido)
