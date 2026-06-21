"""Testes para JFloat."""

import math

import pytest

from javalang.jfloat import JFloat

# ── Operações de Verificação IEEE 754 ─────────────────────────────────────────


class TestIsNaN:
    def test_is_nan_instance(self):
        value = JFloat(float("nan"))
        assert value.isNaN() is True

    def test_is_nan_static(self):
        assert JFloat(float("nan")).isNaN() is True

    def test_is_nan_false(self):
        assert JFloat(10.5).isNaN() is False


class TestIsInfinite:
    def test_is_infinite_instance(self):
        value = JFloat(float("inf"))
        assert value.isInfinite() is True

    def test_is_infinite_static(self):
        value = JFloat(float("-inf"))
        assert value.isInfinite() is True

    def test_is_infinite_false(self):
        value = JFloat(100.0)
        assert value.isInfinite() is False


class TestIsFinite:
    def test_is_finite_true(self):
        assert JFloat.isFinite(42.0) is True

    def test_is_finite_infinity(self):
        assert JFloat.isFinite(float("inf")) is False

    def test_is_finite_nan(self):
        assert JFloat.isFinite(float("nan")) is False


# ── Operações de Comparação de Float ─────────────────────────────────────────


class TestOperacoesComparacaoDeFloat:
    def test_compare_less(self):
        assert JFloat.compare(1.0, 2.0) < 0

    def test_compare_greater(self):
        assert JFloat.compare(3.0, 2.0) > 0

    def test_compare_negative_zero(self):
        assert JFloat.compare(-0.0, 0.0) < 0

    def test_max_first_greater(self):
        assert JFloat.max(3.0, 1.0) == 3.0

    def test_max_nan(self):
        assert math.isnan(JFloat.max(float("nan"), 1.0))

    def test_max_zeros(self):
        assert JFloat.max(-0.0, 0.0) == 0.0

    def test_min_first_smaller(self):
        assert JFloat.min(1.0, 3.0) == 1.0

    def test_min_nan(self):
        assert math.isnan(JFloat.min(float("nan"), 1.0))

    def test_min_zeros(self):
        assert math.copysign(1.0, JFloat.min(-0.0, 0.0)) == -1.0

    def test_sum_positive(self):
        assert JFloat.sum(1.5, 2.5) == 4.0

    def test_sum_negative(self):
        assert JFloat.sum(-3.0, -1.0) == -4.0

    def test_sum_mixed(self):
        assert JFloat.sum(-2.0, 5.0) == 3.0


# ── Pacote de Operações de Parsing e Formatação ─────────────────────────────────────────


class TestParseFloat:
    def test_parse_float_valid(self):
        assert JFloat.parseFloat("3.14") == 3.14

    def test_parse_float_whitespace(self):
        assert JFloat.parseFloat("  2.5  ") == 2.5

    def test_parse_float_invalid(self):
        with pytest.raises(ValueError):
            JFloat.parseFloat("abc")


class TestValueOfFloat:
    def test_value_of_positive(self):
        result = JFloat.valueOf(3.14)
        assert result._value == 3.14

    def test_value_of_negative(self):
        result = JFloat.valueOf(-5.5)
        assert result._value == -5.5

    def test_value_of_zero(self):
        result = JFloat.valueOf(0.0)
        assert result._value == 0.0


class TestValueOfString:
    def test_value_of_string_valid(self):
        result = JFloat.valueOf("4.2")
        assert result._value == 4.2

    def test_value_of_string_whitespace(self):
        result = JFloat.valueOf(" 1.5 ")
        assert result._value == 1.5

    def test_value_of_string_invalid(self):
        with pytest.raises(ValueError):
            JFloat.valueOf("abc")


class TestToString:
    def test_to_string_normal(self):
        assert JFloat.toString(3.14) == "3.14"

    def test_to_string_nan(self):
        assert JFloat.toString(float("nan")) == "NaN"

    def test_to_string_infinity(self):
        assert JFloat.toString(float("inf")) == "Infinity"


class TestToHexString:
    def test_to_hex_string_one(self):
        assert JFloat.toHexString(1.0) == "0x1.0000000000000p+0"

    def test_to_hex_string_half(self):
        assert JFloat.toHexString(0.5) == "0x1.0000000000000p-1"

    def test_to_hex_string_nan(self):
        assert JFloat.toHexString(float("nan")) == "NaN"

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