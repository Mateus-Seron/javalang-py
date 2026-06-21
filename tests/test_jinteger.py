"""Testes para JInteger."""

import pytest

from javalang.jinteger import JInteger

# ── bitCount ───────────────────────────────────────────────────────────────


class TestBitCount:
    def test_zero(self):
        assert JInteger.bitCount(0) == 0

    def test_todos_bits_um(self):
        assert JInteger.bitCount(-1) == 32

    def test_sete(self, valores_bit):
        assert JInteger.bitCount(valores_bit["sete"]) == 3  # 0b111

    def test_dez(self, valores_bit):
        assert JInteger.bitCount(valores_bit["dez"]) == 2  # 0b1010

    def test_max_value(self, valores_bit):
        assert JInteger.bitCount(valores_bit["max"]) == 31


# ── highestOneBit ────────────────────────────────────────────────────────────


class TestHighestOneBit:
    def test_zero(self):
        assert JInteger.highestOneBit(0) == 0

    def test_negativo_retorna_min_value(self):
        assert JInteger.highestOneBit(-1) == JInteger.MIN_VALUE

    def test_dez(self, valores_bit):
        assert JInteger.highestOneBit(valores_bit["dez"]) == 8  # 0b1010 -> 0b1000

    def test_potencias_de_dois(self, potencias_de_dois):
        for p in potencias_de_dois:
            assert JInteger.highestOneBit(p) == p

    def test_cem(self, valores_bit):
        assert JInteger.highestOneBit(valores_bit["cem"]) == 64  # 0b1100100 -> 0b1000000


# ── lowestOneBit ─────────────────────────────────────────────────────────────


class TestLowestOneBit:
    def test_zero(self):
        assert JInteger.lowestOneBit(0) == 0

    def test_um(self, valores_bit):
        assert JInteger.lowestOneBit(valores_bit["um"]) == 1

    def test_dez(self, valores_bit):
        assert JInteger.lowestOneBit(valores_bit["dez"]) == 2  # 0b1010 -> 0b0010

    def test_doze(self, valores_bit):
        assert JInteger.lowestOneBit(valores_bit["doze"]) == 4  # 0b1100 -> 0b0100

    def test_potencias_de_dois(self, potencias_de_dois):
        for p in potencias_de_dois:
            assert JInteger.lowestOneBit(p) == p

    def test_min_value(self):
        assert JInteger.lowestOneBit(JInteger.MIN_VALUE) == JInteger.MIN_VALUE


# ── numberOfLeadingZeros ─────────────────────────────────────────────────────


class TestNumberOfLeadingZeros:
    def test_zero(self):
        assert JInteger.numberOfLeadingZeros(0) == 32

    def test_um(self, valores_bit):
        assert JInteger.numberOfLeadingZeros(valores_bit["um"]) == 31

    def test_negativo(self, valores_bit):
        assert JInteger.numberOfLeadingZeros(valores_bit["negativo"]) == 0

    def test_oito(self):
        assert JInteger.numberOfLeadingZeros(8) == 28  # 0b1000

    def test_max_value(self, valores_bit):
        assert JInteger.numberOfLeadingZeros(valores_bit["max"]) == 1

    def test_min_value(self):
        assert JInteger.numberOfLeadingZeros(JInteger.MIN_VALUE) == 0


# ── numberOfTrailingZeros ────────────────────────────────────────────────────


class TestNumberOfTrailingZeros:
    def test_zero(self):
        assert JInteger.numberOfTrailingZeros(0) == 32

    def test_um(self, valores_bit):
        assert JInteger.numberOfTrailingZeros(valores_bit["um"]) == 0

    def test_oito(self):
        assert JInteger.numberOfTrailingZeros(8) == 3  # 0b1000

    def test_doze(self, valores_bit):
        assert JInteger.numberOfTrailingZeros(valores_bit["doze"]) == 2  # 0b1100

    def test_negativo_menos_um(self, valores_bit):
        assert JInteger.numberOfTrailingZeros(valores_bit["negativo"]) == 0  # 0xFFFFFFFF

    def test_min_value(self):
        assert JInteger.numberOfTrailingZeros(JInteger.MIN_VALUE) == 31  # 0x80000000


# ── Operações de Formatação por Base ─────────────────────────────────────────


class TestOperacoesFormatacaoPorBase:

    def test_to_string_decimal_positivo(self, valores_bit):
        assert JInteger.toString(valores_bit["dez"]) == "10"

    def test_to_string_decimal_negativo(self, valores_bit):
        assert JInteger.toString(valores_bit["negativo"]) == "-1"

    def test_to_string_decimal_min_value(self):
        assert JInteger.toString(JInteger.MIN_VALUE) == "-2147483648"

    def test_to_string_radix_hex(self):
        assert JInteger.toString(255, 16) == "ff"

    def test_to_string_radix_binario_negativo(self):
        assert JInteger.toString(-10, 2) == "-1010"

    def test_to_string_radix_fora_do_intervalo(self):
        with pytest.raises(ValueError, match="radix 1 out of range"):
            JInteger.toString(10, 1)

    def test_to_binary_string_zero(self):
        assert JInteger.toBinaryString(0) == "0"

    def test_to_binary_string_positivo(self, valores_bit):
        assert JInteger.toBinaryString(valores_bit["dez"]) == "1010"

    def test_to_binary_string_negativo(self, valores_bit):
        assert JInteger.toBinaryString(valores_bit["negativo"]) == "1" * 32

    def test_to_octal_string_zero(self):
        assert JInteger.toOctalString(0) == "0"

    def test_to_octal_string_positivo(self, valores_bit):
        assert JInteger.toOctalString(valores_bit["dez"]) == "12"

    def test_to_octal_string_negativo(self, valores_bit):
        assert JInteger.toOctalString(valores_bit["negativo"]) == "37777777777"

    def test_to_hex_string_zero(self):
        assert JInteger.toHexString(0) == "0"

    def test_to_hex_string_positivo(self):
        assert JInteger.toHexString(255) == "ff"

    def test_to_hex_string_negativo(self, valores_bit):
        assert JInteger.toHexString(valores_bit["negativo"]) == "ffffffff"

    def test_to_unsigned_string_zero(self):
        assert JInteger.toUnsignedString(0) == "0"

    def test_to_unsigned_string_positivo(self, valores_bit):
        assert JInteger.toUnsignedString(valores_bit["dez"]) == "10"

    def test_to_unsigned_string_negativo(self, valores_bit):
        assert JInteger.toUnsignedString(valores_bit["negativo"]) == "4294967295"

    def test_to_unsigned_string_radix_hex(self, valores_bit):
        assert JInteger.toUnsignedString(valores_bit["negativo"], 16) == "ffffffff"

    def test_to_unsigned_string_radix_binario(self, valores_bit):
        assert JInteger.toUnsignedString(valores_bit["negativo"], 2) == "1" * 32

    def test_to_unsigned_string_radix_fora_do_intervalo(self):
        with pytest.raises(ValueError, match="radix 37 out of range"):
            JInteger.toUnsignedString(10, 37)


# ── sum ──────────────────────────────────────────────────────────────────────


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


# ── max ──────────────────────────────────────────────────────────────────────


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


# ── min ──────────────────────────────────────────────────────────────────────


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


# ── compare ──────────────────────────────────────────────────────────────────


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


# ── compareUnsigned ──────────────────────────────────────────────────────────


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


# ── divideUnsigned ───────────────────────────────────────────────────────────


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


# ── remainderUnsigned ────────────────────────────────────────────────────────


class TestRemainderUnsigned:
    def test_remainderUnsigned_simple(self):
        assert JInteger.remainderUnsigned(10, 3) == 1

    def test_remainderUnsigned_exact_division(self):
        assert JInteger.remainderUnsigned(10, 2) == 0

    def test_remainderUnsigned_negative_dividend_as_large_unsigned(self):
        assert JInteger.remainderUnsigned(-1, 3) == 0xFFFFFFFF % 3

    def test_remainderUnsigned_dividend_zero(self):
        assert JInteger.remainderUnsigned(0, 7) == 0

    def test_remainderUnsigned_divisor_one(self):
        assert JInteger.remainderUnsigned(99, 1) == 0
