from unittest import TestCase
import numpy as np
import os

from src.pkg.logica.ocultar import *
from src.pkg.logica.develar import *
from src.pkg.io.texto import leer
from src.pkg.io.imagen import get_pixeles_imagen

class TestOcultarDevelar(TestCase):
    def test_oculta_devela(self):
        img_path = "../test_oculta.jpg"
        msg_path = "../msg_test.txt"
        dest_path = "../msg_oculto.jpg"
        develed_path = "../msg_develado.txt"
        try:
            ocultar(img_path, msg_path, dest_path)
            develar(dest_path, develed_path)
            msg_original = leer(msg_path)
            msg_develado = leer(develed_path)
            self.assertEqual(msg_original, msg_develado)
        finally:
            if os.path.exists(dest_path):
                os.remove(dest_path)
            if os.path.exists(develed_path):
                os.remove(develed_path)

    def test_matriz_imperceptible(self):
        img_path = "../test_oculta.jpg"
        msg_path = "../msg_test.txt"
        dest_path = "../msg_oculto.jpg"
        try:
            ocultar(img_path, msg_path, dest_path)
            pixeles = get_pixeles_imagen(img_path)
            modificados = get_pixeles_imagen(dest_path)
            res = np.testing.assert_allclose(pixeles, modificados, 1)
            self.assertIsNone(res)
        finally:
            if os.path.exists(dest_path):
                os.remove(dest_path)
