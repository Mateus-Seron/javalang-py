"""Testes para JFloat."""

import sys
import pytest

from javalang.jfloat import JFloat

# ── CONSTANTES ─────────────────────────────────────────────────────────────


class TestConstantes:
    def test_max_value(self):
        assert JFloat.MAX_VALUE == sys.float_info.max

    def test_min_normal(self):
        assert JFloat.MIN_NORMAL == sys.float_info.min

    def test_min_value(self):
        assert JFloat.MIN_VALUE == 5e-324