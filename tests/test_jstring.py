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


# ── Pacote de Operações de Expressões Regulares ──────────────────────────────


class TestPacoteDeOperacoesDeExpressoesRegulares:
    def test_matches_true(self):
        assert JString("abc").matches("a.c") is True

    def test_matches_false(self):
        assert JString("abc").matches("a") is False

    def test_matches_invalid_regex(self):
        with pytest.raises(ValueError, match="PatternSyntaxException"):
            JString("abc").matches("[")

    def test_replaceFirst_single(self):
        assert JString("aaa").replaceFirst("a", "b").value == "baa"

    def test_replaceFirst_no_match(self):
        assert JString("abc").replaceFirst("x", "y").value == "abc"

    def test_replaceFirst_invalid_regex(self):
        with pytest.raises(ValueError, match="PatternSyntaxException"):
            JString("abc").replaceFirst("[", "x")

    def test_replaceAll_all(self):
        assert JString("aaa").replaceAll("a", "b").value == "bbb"

    def test_replaceAll_no_match(self):
        assert JString("abc").replaceAll("x", "y").value == "abc"

    def test_replaceAll_invalid_regex(self):
        with pytest.raises(ValueError, match="PatternSyntaxException"):
            JString("abc").replaceAll("[", "x")

    def test_split_basic(self):
        parts = JString("a,b,c").split(",")
        assert [part.value for part in parts] == ["a", "b", "c"]

    def test_split_discards_trailing_empty(self):
        parts = JString("a,b,").split(",")
        assert [part.value for part in parts] == ["a", "b"]

    def test_split_invalid_regex(self):
        with pytest.raises(ValueError, match="PatternSyntaxException"):
            JString("a,b").split("[")

    def test_split_with_limit(self):
        parts = JString("a,b,c").split(",", 2)
        assert [part.value for part in parts] == ["a", "b,c"]

    def test_split_with_limit_keeps_trailing_empty(self):
        parts = JString("a,b,").split(",", -1)
        assert [part.value for part in parts] == ["a", "b", ""]

    def test_split_with_limit_one(self):
        parts = JString("a,b,c").split(",", 1)
        assert [part.value for part in parts] == ["a,b,c"]
