"""Testes para JString."""

from javalang.jstring import JString

# ── Pacote de Operações de Comparação de String ──────────────────────────────


class TestPacoteDeOperacoesDeComparacaoDeString:
    def test_equals_same_string(self):
        assert JString("abc").equals(JString("abc")) is True

    def test_equals_different_string(self):
        assert JString("abc").equals(JString("abd")) is False

    def test_equals_not_jstring(self):
        assert JString("abc").equals("abc") is False

    def test_equalsIgnoreCase_same(self):
        assert JString("Java").equalsIgnoreCase("java") is True

    def test_equalsIgnoreCase_different(self):
        assert JString("Java").equalsIgnoreCase("Python") is False

    def test_equalsIgnoreCase_none(self):
        assert JString("Java").equalsIgnoreCase(None) is False

    def test_compareTo_greater(self):
        assert JString("b").compareTo("a") > 0

    def test_compareTo_less(self):
        assert JString("a").compareTo("b") < 0

    def test_compareTo_equal(self):
        assert JString("abc").compareTo("abc") == 0

    def test_compareToIgnoreCase_greater(self):
        assert JString("B").compareToIgnoreCase("a") > 0

    def test_compareToIgnoreCase_less(self):
        assert JString("a").compareToIgnoreCase("B") < 0

    def test_compareToIgnoreCase_equal(self):
        assert JString("Java").compareToIgnoreCase("JAVA") == 0


# ── Contrutores ─────────────────────────────────────────────────────────────


class TestConstrutores:
    def test_string(self):
        assert JString.string(self) == ""

    def test_string_original(self):
        assert JString.stringOriginal("teste") == "teste"

    def test_String_char_array(self):
        assert JString.stringCharArray(["a", "b", "c"]) == "abc"

    def test_string_char_array_offset_count(self):
        assert JString.stringCharArrayOffsetCount(["a", "b", "c", "d", "e"], 1, 3) == "bcd"

    def test_String_bytes(self):
        assert JString.stringBytes(b"Hello") == "Hello"
