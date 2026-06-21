"""Testes para JFloat."""

import math

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


# ── Operações de Construtores e Conversão de Float ───────────────────────────


class TestOperacoesConstrutoresEConversaoDeFloat:
    def test_floatValue_positive(self):
        assert JFloat.valueOf(2.5).floatValue() == 2.5

    def test_floatValue_negative(self):
        assert JFloat.valueOf(-3.0).floatValue() == -3.0

    def test_floatValue_zero(self):
        assert JFloat.valueOf(0.0).floatValue() == 0.0

    def test_doubleValue_positive(self):
        assert JFloat.valueOf(2.5).doubleValue() == 2.5

    def test_doubleValue_negative(self):
        assert JFloat.valueOf(-3.0).doubleValue() == -3.0

    def test_doubleValue_zero(self):
        assert JFloat.valueOf(0.0).doubleValue() == 0.0

    def test_toString_positive(self):
        assert JFloat.valueOf(2.5).toString() == "2.5"

    def test_toString_negative(self):
        assert JFloat.valueOf(-2.0).toString() == "-2.0"

    def test_toString_nan(self):
        assert JFloat.valueOf(float("nan")).toString() == "NaN"
