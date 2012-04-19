import unittest
from code import *

class DojoTest(unittest.TestCase):
    def test_convert_um(self):
        self.assertEquals(1, convert('I'))

    def test_convert_dois(self):
        self.assertEquals(2, convert('II'))

    def test_convert_tres(self):
        self.assertEquals(3, convert('III'))

    def test_convert_cinco(self):
        self.assertEquals(5, convert('V'))

    def test_convert_dez(self):
        self.assertEquals(10, convert('X'))

    def test_convert_seis(self):
        self.assertEquals(6, convert('VI'))

    def test_convert_quatro(self):
        self.assertEquals(4, convert('IV'))

    def test_valida_caract(self):
        self.assertRaises(CaracterInvalido, convert, ('Z',))

    def test_convert_sete(self):
        self.assertEquals(7, convert('VII'))

    def test_convert_nove(self):
        self.assertEquals(9, convert('IX'))

    def test_convert_vinte_um(self):
        self.assertEquals(21, convert('XXI'))

    def test_convert_mil_cento_e_cinquenta_e_quatro(self):
        self.assertEquals(1154, convert('MCLIV'))

    def test_convert_iiid(self):
        self.assertRaises(SequenciaInvalida, convert, 'IIID') 

    def test_convert_noventa(self):
        self.assertEquals(90,convert('XC'))

    def test_convert_quarenta(self):
        self.assertEquals(40, convert('XL'))

    def test_convert_iiii(self):
        self.assertRaises(SequenciaInvalida, convert, 'IIII')            