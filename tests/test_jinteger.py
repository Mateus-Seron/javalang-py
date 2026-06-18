import pytest
from javalang.jinteger import JInteger


# ── sum ────────────────────────────────────────────────────────────────────────

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


# ── max ────────────────────────────────────────────────────────────────────────

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


# ── min ────────────────────────────────────────────────────────────────────────

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