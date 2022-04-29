from unittest import TestCase
import numpy as np
import os

from src.pkg.logica.ocultar import *
from src.pkg.logica.develar import *
from src.pkg.io.texto import leer
from src.pkg.io.imagen import get_pixeles_imagen

class TestOcultarDevelar(TestCase):
    def setUp(self):
        base_dir = "./tests/assets/"
        self.msg_path = base_dir + "msg.txt"
        self.img_path = base_dir + "img.jpg"
        self.modified_img_path = base_dir + "modified_img.png"
        self.msg_revealed_path = base_dir + "msg_revealed.txt"
        if os.path.exists(self.modified_img_path):
            os.remove(self.modified_img_path)
        if os.path.exists(self.msg_revealed_path):
            os.remove(self.msg_revealed_path)

    def test_oculta_devela(self):
        try:
            ocultar(self.msg_path, self.img_path, self.modified_img_path)
            develar(self.modified_img_path, self.msg_revealed_path)
            original_msg = leer(self.msg_path)
            develed_msg = leer(self.msg_revealed_path)
            self.assertEqual(original_msg, develed_msg)
        finally:
            if os.path.exists(self.modified_img_path):
                os.remove(self.modified_img_path)
            if os.path.exists(self.msg_revealed_path):
                os.remove(self.msg_revealed_path)

    def test_matriz_imperceptible(self):
        try:
            ocultar(self.msg_path, self.img_path, self.modified_img_path)
            pixels = get_pixeles_imagen(self.img_path)
            modified_pixels = get_pixeles_imagen(self.modified_img_path)
            result = np.testing.assert_allclose(pixels, modified_pixels, 1)
            self.assertIsNone(result)
        finally:
            if os.path.exists(self.msg_revealed_path):
                os.remove(self.msg_revealed_path)
