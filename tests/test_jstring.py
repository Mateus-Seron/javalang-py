"""Testes para JString."""

from javalang.jstring import JString

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
