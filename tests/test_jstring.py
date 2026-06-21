"""Testes para JString."""

import pytest

from javalang.jstring import JString

# ── Contrutores ─────────────────────────────────────────────────────────────

class TestConstrutores:
    def test_string(self):
        assert JString.string() == ""

    def test_string_original(self):
        assert JString.stringOriginal("teste") == "teste"

    def test_String_char_array(self):
        assert JString.stringCharArray(['a', 'b', 'c']) == "abc" 
