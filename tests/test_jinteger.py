from javalang.jinteger import JInteger

# ======================================================
# Métodos de Arimética Estática: testes para os métodos
# ── sum ────────────────────────────────────────────────


class TestSum:
    def test_sum_positive(self):
        assert JInteger.sum(3, 4) == 7

    def test_sum_negative(self):
        assert JInteger.sum(-3, -4) == -7

    def test_sum_mixed(self):
        assert JInteger.sum(-10, 5) == -5

    def test_sum_zero(self):
        assert JInteger.sum(0, 0) == 0

    def test_sum_with_zero(self):
        assert JInteger.sum(42, 0) == 42


# ── max ────────────────────────────────────────────────


class TestMax:
    def test_max_first_greater(self):
        assert JInteger.max(10, 3) == 10

    def test_max_second_greater(self):
        assert JInteger.max(3, 10) == 10

    def test_max_equal(self):
        assert JInteger.max(5, 5) == 5

    def test_max_negative(self):
        assert JInteger.max(-1, -5) == -1

    def test_max_mixed_sign(self):
        assert JInteger.max(-1, 1) == 1


# ── min ────────────────────────────────────────────────


class TestMin:
    def test_min_first_smaller(self):
        assert JInteger.min(2, 9) == 2

    def test_min_second_smaller(self):
        assert JInteger.min(9, 2) == 2

    def test_min_equal(self):
        assert JInteger.min(7, 7) == 7

    def test_min_negative(self):
        assert JInteger.min(-3, -1) == -3

    def test_min_mixed_sign(self):
        assert JInteger.min(-1, 1) == -1


# ── compare ────────────────────────────────────────────────


class TestCompare:
    def test_compare_equal(self):
        assert JInteger.compare(5, 5) == 0

    def test_compare_less(self):
        assert JInteger.compare(3, 7) < 0

    def test_compare_greater(self):
        assert JInteger.compare(7, 3) > 0

    def test_compare_negative_values(self):
        assert JInteger.compare(-10, -5) < 0

    def test_compare_negative_and_positive(self):
        assert JInteger.compare(-1, 1) < 0


# ── compareUnsigned ────────────────────────────────────────────────


class TestCompareUnsigned:
    def test_compareUnsigned_equal(self):
        assert JInteger.compareUnsigned(5, 5) == 0

    def test_compareUnsigned_positive_less(self):
        assert JInteger.compareUnsigned(3, 7) < 0

    def test_compareUnsigned_positive_greater(self):
        assert JInteger.compareUnsigned(7, 3) > 0

    def test_compareUnsigned_negative_treated_as_large(self):
        # -1 como unsigned 32 bits == 0xFFFFFFFF (maior que qualquer positivo)
        assert JInteger.compareUnsigned(-1, 1) > 0

    def test_compareUnsigned_both_negative(self):
        # -1 (0xFFFFFFFF) > -2 (0xFFFFFFFE) como unsigned
        assert JInteger.compareUnsigned(-1, -2) > 0


# ── divideUnsigned ────────────────────────────────────────────────


class TestDivideUnsigned:
    def test_divideUnsigned_simple(self):
        assert JInteger.divideUnsigned(10, 2) == 5

    def test_divideUnsigned_truncates(self):
        assert JInteger.divideUnsigned(7, 2) == 3

    def test_divideUnsigned_negative_dividend_as_large_unsigned(self):
        # -1 unsigned == 0xFFFFFFFF; 0xFFFFFFFF // 2 == 2147483647
        assert JInteger.divideUnsigned(-1, 2) == 2_147_483_647

    def test_divideUnsigned_dividend_zero(self):
        assert JInteger.divideUnsigned(0, 5) == 0

    def test_divideUnsigned_divisor_one(self):
        assert JInteger.divideUnsigned(100, 1) == 100


# ── remainderUnsigned ────────────────────────────────────────────────


class TestRemainderUnsigned:
    def test_remainderUnsigned_simple(self):
        assert JInteger.remainderUnsigned(10, 3) == 1

    def test_remainderUnsigned_exact_division(self):
        assert JInteger.remainderUnsigned(10, 2) == 0

    def test_remainderUnsigned_negative_dividend_as_large_unsigned(self):
        # 0xFFFFFFFF % 3
        assert JInteger.remainderUnsigned(-1, 3) == 0xFFFFFFFF % 3

    def test_remainderUnsigned_dividend_zero(self):
        assert JInteger.remainderUnsigned(0, 7) == 0

    def test_remainderUnsigned_divisor_one(self):
        assert JInteger.remainderUnsigned(99, 1) == 0
