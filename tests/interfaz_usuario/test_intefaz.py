from unittest import TestCase, mock
import sys
import os
import io

from src.pkg.interfaz_usuario.interfaz import main

class TestInterfaz(TestCase):
    def setUp(self):
        base_dir = "./tests/assets/"
        self.msg_path = base_dir + "msg.txt"
        self.img_path = base_dir + "img.jpg"
        self.modified_img_path = base_dir + "modified_img.png"
        self.lsg_img_path = base_dir + "lsb_img.png"
        self.msg_revealed_path = base_dir + "msg_revealed.txt"
        if os.path.exists(self.modified_img_path):
            os.remove(self.modified_img_path)
        if os.path.exists(self.msg_revealed_path):
            os.remove(self.msg_revealed_path)
        self.maxDiff = None

    def test_hide(self):
        sys.argv = ["_", "-h", self.msg_path, self.img_path, self.modified_img_path]
        try:
            self.assertStdout("")
            self.assertTrue(os.path.exists(self.modified_img_path))
        finally:
            if os.path.exists(self.modified_img_path):
                os.remove(self.modified_img_path)

    def test_unhide(self):
        sys.argv = ["_", "-u", self.lsb_img_path, self.msg_revealed_path]
        try:
            self.assertStdout("")
            self.assertTrue(os.path.exists(self.msg_revealed_path))
        finally:
            if os.path.exists(self.msg_revealed_path):
                os.remove(self.msg_revealed_path)

    @mock.patch("sys.stdout", new_callable=io.StringIO)
    def assertStdout(self, expected_output, mock_stdout):
        main()
        actual_output = mock_stdout.getvalue()
        self.assertEqual(expected_output, actual_output)

    def test_unvalid_parameters(self):
        sys.argv = ["_", "-h", self.msg_path, self.img_path]
        esperado = lambda args: f"""Parámetros inválidos {args}

Uso:    python -B src/main.py [option]

Opciones:
    -h msg img dest     Oculta el texto del archivo msg usando la imagen img, el resultado lo guarda en dest
    -u img dest         Extrae el mensaje oculto en img y lo guarda el el archivo dest

Ejemplos:
    Cualquiera de los siguientes ejemplos se pueden ejecutar como demo del programa

    Para ocultar:
    python -B src/main.py -h {self.msg_path} {self.img_path} {self.modified_img_path}

    Para develar
    python -B src/main.py -u {self.lsb_img_path} {self.msg_revealed_path}
"""
        self.assertStdout(esperado(sys.argv[1:]))
        sys.argv = ["_", "-u", self.lsb_img_path, self.msg_revealed_path, self.img_path]
        self.assertStdout(esperado(sys.argv[1:]))
        sys.argv = ["_", "-u"]
        self.assertStdout(esperado(sys.argv[1:]))
