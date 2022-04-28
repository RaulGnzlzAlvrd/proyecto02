from unittest import TestCase
import os

import numpy as np

from src.pkg.io.imagen import *

class TestImagen(TestCase):
    def setUp(self):
        self.pixeles = np.array(
                [  [[186, 157,   2],
                    [ 83, 152, 117],
                    [117, 150,  62],
                    [ 29, 119, 158]],

                   [[136,  27, 187],
                    [207, 213, 162],
                    [212, 194, 210],
                    [200,  25, 169]],

                   [[232, 222,  10],
                    [193,  70,  96],
                    [236,  79,  80],
                    [159, 131, 196]]], dtype="uint8")
        base_dir = "./tests/assets/"
        self.img_path = base_dir + "img4x3.png"
        self.img_copy_path = base_dir + "img4x3_copy.png"
        if os.path.exists(self.img_copy_path):
            os.remove(self.img_copy_path)

    def test_get_pixeles_imagen(self):
        pixeles_leidos = get_pixeles_imagen(self.img_path)
        resultado = np.testing.assert_array_equal(self.pixeles, pixeles_leidos)
        self.assertIsNone(resultado)

    def test_crea_imagen(self):
        try:
            crea_imagen(self.pixeles, self.img_copy_path)
            self.assertTrue(os.path.exists(self.img_copy_path))
            with Image.open(self.img_copy_path) as img_copy:
                self.assertEqual(img_copy.size, self.pixeles.shape[-2::-1])
        finally:
            if os.path.exists(self.img_copy_path):
                os.remove(self.img_copy_path)
