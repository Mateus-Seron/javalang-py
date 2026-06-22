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

class TestOffsetByCodePoints:

    def test_forward_offset(self):
        s = JString("abcdef")
        assert s.offsetByCodePoints(2, 3) == 5

    def test_backward_offset(self):
        s = JString("abcdef")
        assert s.offsetByCodePoints(5, -2) == 3

    def test_zero_offset(self):
        s = JString("abcdef")
        assert s.offsetByCodePoints(3, 0) == 3

    def test_invalid_index_negative(self):
        s = JString("abcdef")

        with pytest.raises(IndexError):
            s.offsetByCodePoints(-1, 1)

    def test_invalid_index_too_large(self):
        s = JString("abcdef")

        with pytest.raises(IndexError):
            s.offsetByCodePoints(7, 1)

    def test_offset_beyond_end(self):
        s = JString("abcdef")

        with pytest.raises(IndexError):
            s.offsetByCodePoints(5, 2)

    def test_offset_before_start(self):
        s = JString("abcdef")

        with pytest.raises(IndexError):
            s.offsetByCodePoints(1, -2)

class TestGetChars:

    def test_copy_middle(self):
        s = JString("abcdef")

        dst = [""] * 10

        s.getChars(1, 4, dst, 2)

        assert dst[2:5] == ["b", "c", "d"]

    def test_copy_full_string(self):
        s = JString("abc")

        dst = [""] * 3

        s.getChars(0, 3, dst, 0)

        assert dst == ["a", "b", "c"]

    def test_invalid_src_begin(self):
        s = JString("abc")

        with pytest.raises(IndexError):
            s.getChars(-1, 2, [""] * 5, 0)

    def test_src_begin_greater_than_src_end(self):
        s = JString("abc")

        with pytest.raises(IndexError):
            s.getChars(2, 1, [""] * 5, 0)

    def test_src_end_too_large(self):
        s = JString("abc")

        with pytest.raises(IndexError):
            s.getChars(0, 4, [""] * 5, 0)

    def test_negative_dst_begin(self):
        s = JString("abc")

        with pytest.raises(IndexError):
            s.getChars(0, 2, [""] * 5, -1)

    def test_destination_too_small(self):
        s = JString("abcdef")

        with pytest.raises(IndexError):
            s.getChars(0, 6, [""] * 3, 0)

class TestToCharArray:

    def test_to_char_array(self):
        s = JString("abc")

        assert s.toCharArray() == ["a", "b", "c"]

    def test_empty_string(self):
        s = JString("")

        assert s.toCharArray() == []

class TestGetBytes:

    def test_default_encoding(self):
        s = JString("abc")

        assert isinstance(s.getBytes(), bytes)

    def test_utf8(self):
        s = JString("Olá")

        assert s.getBytes("utf-8") == "Olá".encode("utf-8")

    def test_ascii(self):
        s = JString("abc")

        assert s.getBytes("ascii") == b"abc"

    def test_invalid_charset(self):
        s = JString("abc")

        with pytest.raises(ValueError):
            s.getBytes("charset-inexistente")