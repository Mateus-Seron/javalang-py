import pytest

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

    def test_contentEquals_same_str(self):
        assert JString("abc").contentEquals("abc") is True

    def test_contentEquals_different(self):
        assert JString("abc").contentEquals("abd") is False

    def test_contentEquals_jstring(self):
        assert JString("abc").contentEquals(JString("abc")) is True

    def test_regionMatches_match(self):
        assert JString("hello").regionMatches(1, "ell", 0, 3) is True

    def test_regionMatches_no_match(self):
        assert JString("hello").regionMatches(0, "abc", 0, 3) is False

    def test_regionMatches_out_of_bounds(self):
        assert JString("hello").regionMatches(4, "lo", 0, 3) is False

    def test_regionMatches_ignore_case_match(self):
        assert JString("Hello").regionMatches(True, 0, "hel", 0, 3) is True

    def test_regionMatches_ignore_case_no_match(self):
        assert JString("Hello").regionMatches(True, 0, "abc", 0, 3) is False

    def test_regionMatches_ignore_case_out_of_bounds(self):
        assert JString("Hello").regionMatches(True, 3, "lo", 0, 3) is False

    def test_hashCode_same_string(self):
        assert JString("abc").hashCode() == JString("abc").hashCode()

    def test_hashCode_different_string(self):
        assert JString("abc").hashCode() != JString("abd").hashCode()

    def test_hashCode_empty(self):
        assert JString("").hashCode() == 0


# ── Pacote de Operações de Acesso e Tamanho ──────────────────────────────


class TestLength:
    def test_length_empty(self):
        s = JString("")
        assert s.length() == 0

    def test_length_normal(self):
        s = JString("abc")
        assert s.length() == 3


class TestIsEmpty:
    def test_true(self):
        assert JString("").isEmpty() is True

    def test_false(self):
        assert JString("a").isEmpty() is False


class TestCharAt:
    def test_char_at_basic(self):
        s = JString("abc")
        assert s.charAt(0) == "a"
        assert s.charAt(2) == "c"

    def test_char_at_exception(self):
        s = JString("abc")
        with pytest.raises(IndexError):
            s.charAt(5)


class TestCodePointAt:
    def test_ascii(self):
        s = JString("abc")
        assert s.codePointAt(1) == ord("b")


class TestCodePointBefore:
    def test_ascii(self):
        s = JString("abc")
        assert s.codePointBefore(2) == ord("b")


class TestCodePointCount:
    def test_basic(self):
        s = JString("hello")
        assert s.codePointCount(0, 5) == 5

    def test_partial_range(self):
        s = JString("abcdef")
        assert s.codePointCount(1, 5) == 4
