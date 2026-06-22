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

    def test_from_bytes_ascii(self):
        data = b"hello"
        js = JString.from_bytes(data, "ascii")
        assert js.value == "hello"

    def test_from_bytes_range(self):
        data = b"hello world"
        js = JString.from_bytes_range(data, 6, 5)
        assert js.value == "world"

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

        assert s.getBytes("utf-8") == "Olá".encode()

    def test_ascii(self):
        s = JString("abc")

        assert s.getBytes("ascii") == b"abc"

    def test_invalid_charset(self):
        s = JString("abc")

        with pytest.raises(ValueError):
            s.getBytes("charset-inexistente")


# ── Pacote de busca em String ──────────────────────────────────────────────


class TestPacoteDePesquisaEmString:
    def test_indexOf_char_found(self):
        assert JString("banana").index_of(ord("a")) == 1

    def test_indexOf_char_not_found(self):
        assert JString("banana").index_of(ord("x")) == -1

    def test_indexOf_char_from_index(self):
        assert JString("banana").index_of(ord("a"), 2) == 3

    def test_indexOf_string_found(self):
        assert JString("banana").index_of("na") == 2

    def test_indexOf_string_not_found(self):
        assert JString("banana").index_of("xyz") == -1

    def test_indexOf_string_from(self):
        assert JString("banana").index_of_string_from("na", 3) == 4

    def test_indexOf_string_from_not_found(self):
        assert JString("banana").index_of_string_from("na", 5) == -1

    def test_lastIndexOf_char_found(self):
        assert JString("banana").last_index_of(ord("a")) == 5

    def test_lastIndexOf_char_not_found(self):
        assert JString("banana").last_index_of(ord("x")) == -1

    def test_lastIndexOf_char_from_index(self):
        assert JString("banana").last_index_of(ord("a"), 4) == 3

    def test_lastIndexOf_char_from_index_not_found(self):
        assert JString("banana").last_index_of(ord("a"), 0) == -1


# ── Pacote de Operações de Busca ──────────────────────────────


class TestLastIndexOf:
    def test_last_occurrence(self):
        s = JString("banana")
        assert s.lastIndexOf("na") == 4

    def test_not_found(self):
        s = JString("banana")
        assert s.lastIndexOf("xyz") == -1

    def test_empty_string(self):
        s = JString("banana")
        assert s.lastIndexOf("") == 6

    def test_entire_string(self):
        s = JString("banana")
        assert s.lastIndexOf("banana") == 0


class TestLastIndexOfFromIndex:
    def test_found_before_index(self):
        s = JString("banana")
        assert s.lastIndexOf("na", 3) == 2

    def test_found_exact_index(self):
        s = JString("banana")
        assert s.lastIndexOf("na", 4) == 4

    def test_negative_index(self):
        s = JString("banana")
        assert s.lastIndexOf("na", -1) == -1

    def test_large_index(self):
        s = JString("banana")
        assert s.lastIndexOf("na", 100) == 4

    def test_empty_string(self):
        s = JString("banana")
        assert s.lastIndexOf("", 3) == 3


class TestContains:
    def test_contains_true(self):
        s = JString("banana")
        assert s.contains("nan")

    def test_contains_false(self):
        s = JString("banana")
        assert not s.contains("xyz")

    def test_contains_empty(self):
        s = JString("banana")
        assert s.contains("")

    def test_contains_entire_string(self):
        s = JString("banana")
        assert s.contains("banana")


class TestStartsWith:
    def test_prefix_exists(self):
        s = JString("banana")
        assert s.startsWith("ban")

    def test_prefix_not_exists(self):
        s = JString("banana")
        assert not s.startsWith("nan")

    def test_empty_prefix(self):
        s = JString("banana")
        assert s.startsWith("")

    def test_entire_string(self):
        s = JString("banana")
        assert s.startsWith("banana")


class TestStartsWithOffset:
    def test_valid_offset(self):
        s = JString("banana")
        assert s.startsWith("nan", 2)

    def test_invalid_offset_negative(self):
        s = JString("banana")
        assert not s.startsWith("ban", -1)

    def test_invalid_offset_too_large(self):
        s = JString("banana")
        assert not s.startsWith("ban", 100)

    def test_offset_no_match(self):
        s = JString("banana")
        assert not s.startsWith("ban", 1)

    def test_empty_prefix(self):
        s = JString("banana")
        assert s.startsWith("", 3)


class TestEndsWith:
    def test_suffix_exists(self):
        s = JString("banana")
        assert s.endsWith("ana")

    def test_suffix_not_exists(self):
        s = JString("banana")
        assert not s.endsWith("ban")

    def test_empty_suffix(self):
        s = JString("banana")
        assert s.endsWith("")

    def test_entire_string(self):
        s = JString("banana")
        assert s.endsWith("banana")


# ── Pacote de Operações de Transformação ─────────────────────


class TestReplace:
    def test_replace_basic(self):
        s = JString("banana")
        assert s.replace("a", "o").value == "bonono"

    def test_replace_with_jstring(self):
        s = JString("hello world")
        target = JString("world")
        replacement = JString("python")
        assert s.replace(target, replacement).value == "hello python"

    def test_replace_no_match(self):
        s = JString("abc")
        assert s.replace("x", "y").value == "abc"

    def test_replace_empty_target(self):
        s = JString("abc")
        assert s.replace("", "-").value == "-a-b-c-"


class TestToLowerCase:
    def test_to_lower_case_mixed(self):
        s = JString("JaVa 123")
        assert s.toLowerCase().value == "java 123"

    def test_to_lower_case_already_lower(self):
        s = JString("python")
        assert s.toLowerCase().value == "python"

    def test_to_lower_case_returns_jstring(self):
        s = JString("ABC")
        assert isinstance(s.toLowerCase(), JString)


class TestToUpperCase:
    def test_to_upper_case_mixed(self):
        s = JString("jAvA 123")
        assert s.toUpperCase().value == "JAVA 123"

    def test_to_upper_case_already_upper(self):
        s = JString("PYTHON")
        assert s.toUpperCase().value == "PYTHON"

    def test_to_upper_case_returns_jstring(self):
        s = JString("abc")
        assert isinstance(s.toUpperCase(), JString)


class TestTrim:
    def test_trim_basic_spaces(self):
        s = JString("  hello world  ")
        assert s.trim().value == "hello world"

    def test_trim_control_characters(self):
        s = JString("\t\n\r hello \t\n\r")
        assert s.trim().value == "hello"

    def test_trim_no_spaces(self):
        s = JString("abc")
        assert s.trim().value == "abc"

    def test_trim_only_spaces(self):
        s = JString("   \t   ")
        assert s.trim().value == ""


class TestIntern:
    def test_intern_same_reference(self):
        s1 = JString("teste_intern").intern()
        s2 = JString("teste_intern").intern()
        assert s1.value is s2.value

    def test_intern_value_equivalence(self):
        s = JString("java")
        assert s.intern().value == "java"
