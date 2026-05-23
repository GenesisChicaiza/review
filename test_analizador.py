"""Tests del AnalizadorTexto."""
import unittest

from src.analizador import AnalizadorTexto


class TestContarLineas(unittest.TestCase):

    def test_cuenta_lineas_no_vacias(self):
        texto = "hola mundo\n\nbuenos dias\n   \nadios\n"
        a = AnalizadorTexto(texto)
        self.assertEqual(a.contar_lineas(), 3)

    def test_texto_vacio_tiene_cero_lineas(self):
        self.assertEqual(AnalizadorTexto("").contar_lineas(), 0)


class TestContarPalabras(unittest.TestCase):

    def test_cuenta_palabras_separadas_por_espacios_y_saltos(self):
        texto = "hola mundo\nbuenos dias amigos\nadios"
        a = AnalizadorTexto(texto)
        self.assertEqual(a.contar_palabras(), 6)

    def test_texto_vacio_tiene_cero_palabras(self):
        self.assertEqual(AnalizadorTexto("   \n\n").contar_palabras(), 0)


if __name__ == "__main__":
    unittest.main()

