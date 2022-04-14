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
                    [159, 131, 196]]])
        self.path_file = "../img_test.png"

    def test_get_pixeles_imagen(self):
        obtenido = get_pixeles_imagen(self.path_file)
        resultado = np.testing.assert_array_equal(obtenido, self.pixeles)
        self.assertIsNone(resultado)

    def test_crea_imagen(self):
        path_nuevo = "../img_test2.png"
        try:
            crea_imagen(self.pixeles, path_nuevo)
            self.assertTrue(os.path.exists(path_nuevo))
            with Image.open(path_nuevo) as img:
                self.assertEqual(img.size, self.pixeles.shape[:-1])
        finally:
            if os.path.exists(path_nuevo):
                os.remove(path_nuevo)
