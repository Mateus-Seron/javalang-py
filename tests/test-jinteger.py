import unittest

from javalang import JInteger


class TestJIntegerInit(unittest.TestCase):
    """Testes para o construtor __init__"""

    def test_init_com_inteiro_positivo(self):
        j = JInteger(42)
        self.assertEqual(j.value, 42)

    def test_init_com_inteiro_negativo(self):
        j = JInteger(-10)
        self.assertEqual(j.value, -10)

    def test_init_com_zero(self):
        j = JInteger(0)
        self.assertEqual(j.value, 0)

    def test_init_com_string_numerica(self):
        j = JInteger("123")
        self.assertEqual(j.value, 123)

    def test_init_com_string_negativa(self):
        j = JInteger("-99")
        self.assertEqual(j.value, -99)

    def test_init_com_float_trunca(self):
        # int(3.9) == 3, comportamento esperado do int() do Python
        j = JInteger(3.9)
        self.assertEqual(j.value, 3)

    def test_init_string_invalida_levanta_excecao(self):
        with self.assertRaises(ValueError):
            JInteger("abc")


class TestIntValue(unittest.TestCase):
    """Testes para intValue()"""

    def test_intvalue_positivo(self):
        self.assertEqual(JInteger(100).intValue(), 100)

    def test_intvalue_negativo(self):
        self.assertEqual(JInteger(-50).intValue(), -50)

    def test_intvalue_zero(self):
        self.assertEqual(JInteger(0).intValue(), 0)

    def test_intvalue_grande(self):
        self.assertEqual(JInteger(2_147_483_647).intValue(), 2_147_483_647)

    def test_intvalue_retorna_int(self):
        self.assertIsInstance(JInteger(7).intValue(), int)


class TestLongValue(unittest.TestCase):
    """Testes para longValue()"""

    def test_longvalue_positivo(self):
        self.assertEqual(JInteger(1_000_000).longValue(), 1_000_000)

    def test_longvalue_negativo(self):
        self.assertEqual(JInteger(-1_000_000).longValue(), -1_000_000)

    def test_longvalue_zero(self):
        self.assertEqual(JInteger(0).longValue(), 0)

    def test_longvalue_numero_grande(self):
        self.assertEqual(JInteger(9_223_372_036_854_775_807).longValue(), 9_223_372_036_854_775_807)

    def test_longvalue_retorna_int(self):
        self.assertIsInstance(JInteger(5).longValue(), int)


class TestShortValue(unittest.TestCase):
    """Testes para shortValue()"""

    def test_shortvalue_positivo(self):
        self.assertEqual(JInteger(32_767).shortValue(), 32_767)

    def test_shortvalue_negativo(self):
        self.assertEqual(JInteger(-32_768).shortValue(), -32_768)

    def test_shortvalue_zero(self):
        self.assertEqual(JInteger(0).shortValue(), 0)

    def test_shortvalue_retorna_int(self):
        self.assertIsInstance(JInteger(1).shortValue(), int)


class TestByteValue(unittest.TestCase):
    """Testes para byteValue() — faixa esperada: -128 a 127"""

    def test_bytevalue_zero(self):
        self.assertEqual(JInteger(0).byteValue(), 0)

    def test_bytevalue_um(self):
        self.assertEqual(JInteger(1).byteValue(), 1)

    def test_bytevalue_maximo_positivo(self):
        # 127 → sem ajuste → 127
        self.assertEqual(JInteger(127).byteValue(), 127)

    def test_bytevalue_128_vira_negativo(self):
        # 128 & 0xFF = 128 >= 128 → 128 - 256 = -128
        self.assertEqual(JInteger(128).byteValue(), -128)

    def test_bytevalue_255_vira_menos_um(self):
        # 255 & 0xFF = 255 >= 128 → 255 - 256 = -1
        self.assertEqual(JInteger(255).byteValue(), -1)

    def test_bytevalue_256_reinicia_para_zero(self):
        # 256 & 0xFF = 0 → 0
        self.assertEqual(JInteger(256).byteValue(), 0)

    def test_bytevalue_negativo_menos_1(self):
        # -1 & 0xFF = 255 >= 128 → 255 - 256 = -1
        self.assertEqual(JInteger(-1).byteValue(), -1)

    def test_bytevalue_negativo_menos_128(self):
        # -128 & 0xFF = 128 >= 128 → 128 - 256 = -128
        self.assertEqual(JInteger(-128).byteValue(), -128)

    def test_bytevalue_negativo_menos_129(self):
        # -129 & 0xFF = 127 < 128 → 127
        self.assertEqual(JInteger(-129).byteValue(), 127)

    def test_bytevalue_grande_positivo(self):
        # 300 & 0xFF = 44 < 128 → 44
        self.assertEqual(JInteger(300).byteValue(), 44)

    def test_bytevalue_resultado_dentro_da_faixa(self):
        for v in range(-300, 301):
            resultado = JInteger(v).byteValue()
            self.assertGreaterEqual(resultado, -128, f"Falhou para v={v}")
            self.assertLessEqual(resultado, 127, f"Falhou para v={v}")

    def test_bytevalue_retorna_int(self):
        self.assertIsInstance(JInteger(10).byteValue(), int)


if __name__ == "__main__":
    unittest.main(verbosity=2)
