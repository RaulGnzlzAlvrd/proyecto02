from unittest import TestCase
import os

from src.pkg.io.texto import *

class TestTexto(TestCase):
    def test_leer(self):
        mensaje_path = "../msg_test.txt"
        mensaje = "HOLA MUNDO COMO ESTAS EL DIA DE HOY"
        obtenido = leer(mensaje_path)
        self.assertEqual(obtenido, mensaje)

    def test_escribe(self):
        nuevo_path = "../msg_test2.txt"
        mensaje = "HOLA MUNDO COMO ESTAS EL DIA DE HOY"
        try:
            escribe(mensaje, nuevo_path)
            self.assertTrue(os.path.exists(nuevo_path))
            self.assertEqual(leer(nuevo_path), mensaje)
        finally:
            if os.path.exists(nuevo_path):
                os.remove(nuevo_path)
