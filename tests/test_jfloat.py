"""Testes para JFloat."""

import math

import pytest

from javalang.jfloat import JFloat

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


# ── Construtor ──────────────────────────────────────────────────────────────


class TestJFloatInit:
    def test_init_com_float(self):
        assert JFloat(3.14).value == 3.14

    def test_init_com_int(self):
        assert JFloat(10).value == 10.0

    def test_init_com_string(self):
        assert JFloat("2.5").value == 2.5

    def test_init_com_string_negativa(self):
        assert JFloat("-7.25").value == -7.25

    def test_init_com_zero(self):
        assert JFloat(0).value == 0.0

    def test_init_string_invalida_levanta_excecao(self):
        with pytest.raises(ValueError):
            JFloat("abc")


# ── byteValue ───────────────────────────────────────────────────────────────


class TestByteValue:
    def test_bytevalue_zero(self):
        assert JFloat(0.0).byteValue() == 0

    def test_bytevalue_um(self):
        assert JFloat(1.9).byteValue() == 1

    def test_bytevalue_maximo_positivo(self):
        assert JFloat(127.9).byteValue() == 127

    def test_bytevalue_128_vira_negativo(self):
        assert JFloat(128.0).byteValue() == -128

    def test_bytevalue_255_vira_menos_um(self):
        assert JFloat(255.99).byteValue() == -1

    def test_bytevalue_256_reinicia_para_zero(self):
        assert JFloat(256.0).byteValue() == 0

    def test_bytevalue_negativo_menos_1(self):
        assert JFloat(-1.5).byteValue() == -1

    def test_bytevalue_negativo_menos_128(self):
        assert JFloat(-128.0).byteValue() == -128

    def test_bytevalue_negativo_menos_129(self):
        assert JFloat(-129.0).byteValue() == 127

    def test_bytevalue_grande_positivo(self):
        assert JFloat(300.75).byteValue() == 44

    def test_bytevalue_retorna_int(self):
        assert isinstance(JFloat(10.5).byteValue(), int)


# ── shortValue ──────────────────────────────────────────────────────────────


class TestShortValue:
    def test_shortvalue_zero(self):
        assert JFloat(0.0).shortValue() == 0

    def test_shortvalue_positivo(self):
        assert JFloat(32767.99).shortValue() == 32767

    def test_shortvalue_negativo(self):
        assert JFloat(-32768.99).shortValue() == -32768

    def test_shortvalue_32768_vira_negativo(self):
        assert JFloat(32768.0).shortValue() == -32768

    def test_shortvalue_65535_vira_menos_um(self):
        assert JFloat(65535.0).shortValue() == -1

    def test_shortvalue_65536_reinicia(self):
        assert JFloat(65536.0).shortValue() == 0

    def test_shortvalue_negativo_menos_32769(self):
        assert JFloat(-32769.0).shortValue() == 32767

    def test_shortvalue_retorna_int(self):
        assert isinstance(JFloat(5.5).shortValue(), int)


# ── intValue ────────────────────────────────────────────────────────────────


class TestIntValue:
    def test_intvalue_positivo(self):
        assert JFloat(100.99).intValue() == 100

    def test_intvalue_negativo(self):
        assert JFloat(-50.99).intValue() == -50

    def test_intvalue_zero(self):
        assert JFloat(0.0).intValue() == 0

    def test_intvalue_trunca_decimal(self):
        assert JFloat(123.999).intValue() == 123

    def test_intvalue_retorna_int(self):
        assert isinstance(JFloat(7.7).intValue(), int)


# ── longValue ───────────────────────────────────────────────────────────────


class TestLongValue:
    def test_longvalue_positivo(self):
        assert JFloat(1_000_000.9).longValue() == 1_000_000

    def test_longvalue_negativo(self):
        assert JFloat(-1_000_000.9).longValue() == -1_000_000

    def test_longvalue_zero(self):
        assert JFloat(0.0).longValue() == 0

    def test_longvalue_grande(self):
        valor = 2**53
        assert JFloat(float(valor)).longValue() == valor

    def test_longvalue_retorna_int(self):
        assert isinstance(JFloat(5.5).longValue(), int)
