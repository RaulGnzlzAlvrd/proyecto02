from unittest import TestCase
import os

from src.pkg.io.texto import *

class TestTexto(TestCase):
    def setUp(self):
        base_dir = "./tests/assets/"
        self.txt_path = base_dir + "msg.txt"
        self.writed_txt_path = base_dir + "writed.txt"
        self.txt = "HOLA MUNDO COMO ESTAS EL DIA DE HOY"
        if os.path.exists(self.writed_txt_path):
            os.remove(self.writed_txt_path)

    def test_leer(self):
        readed_txt = leer(self.txt_path)
        self.assertEqual(self.txt, readed_txt)

    def test_escribe(self):
        try:
            escribe(self.txt, self.writed_txt_path)
            self.assertTrue(os.path.exists(self.writed_txt_path))
            self.assertEqual(leer(self.writed_txt_path), self.txt)
        finally:
            if os.path.exists(self.writed_txt_path):
                os.remove(self.writed_txt_path)
