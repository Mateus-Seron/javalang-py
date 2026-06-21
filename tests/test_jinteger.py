"""Testes para JInteger."""

import pytest

from javalang.jinteger import JInteger

# ── Parsing ────────────────────────────────────────────────────────────────


class TestParseInt:
    def test_parseInt_zero(self):
        assert JInteger.parseInt("0") == 0

    def test_parseInt_positive_decimal(self):
        assert JInteger.parseInt("473") == 473

    def test_parseInt_plus_prefix(self):
        assert JInteger.parseInt("+42") == 42

    def test_parseInt_negative_zero(self):
        assert JInteger.parseInt("-0") == 0

    def test_parseInt_max_value(self):
        assert JInteger.parseInt("2147483647") == 2_147_483_647

    def test_parseInt_min_value(self):
        assert JInteger.parseInt("-2147483648") == -2_147_483_648

    def test_parseInt_overflow_raises(self):
        with pytest.raises(ValueError):
            JInteger.parseInt("2147483648")

    def test_parseInt_null_raises(self):
        with pytest.raises(ValueError):
            JInteger.parseInt(None)  # type: ignore

    def test_parseInt_empty_raises(self):
        with pytest.raises(ValueError):
            JInteger.parseInt("")

    def test_parseInt_only_minus_raises(self):
        with pytest.raises(ValueError):
            JInteger.parseInt("-")

    def test_parseInt_only_plus_raises(self):
        with pytest.raises(ValueError):
            JInteger.parseInt("+")

    def test_parseInt_invalid_chars_raises(self):
        with pytest.raises(ValueError):
            JInteger.parseInt("Kona", 10)


# ── parseInt com radix ─────────────────────────────────


class TestParseIntWithRadix:
    def test_parseInt_radix_10(self):
        assert JInteger.parseInt("473", 10) == 473

    def test_parseInt_hex(self):
        assert JInteger.parseInt("-FF", 16) == -255

    def test_parseInt_binary(self):
        assert JInteger.parseInt("1100110", 2) == 102

    def test_parseInt_radix_27_kona(self):
        assert JInteger.parseInt("Kona", 27) == 411_787

    def test_parseInt_radix_8_invalid_digit_raises(self):
        with pytest.raises(ValueError):
            JInteger.parseInt("99", 8)

    def test_parseInt_radix_below_min_raises(self):
        with pytest.raises(ValueError):
            JInteger.parseInt("10", 1)

    def test_parseInt_radix_above_max_raises(self):
        with pytest.raises(ValueError):
            JInteger.parseInt("10", 37)

    def test_parseInt_hex_max(self):
        assert JInteger.parseInt("7FFFFFFF", 16) == JInteger.MAX_VALUE

    def test_parseInt_hex_min(self):
        assert JInteger.parseInt("-80000000", 16) == JInteger.MIN_VALUE


# ── parseUnsignedInt ───────────────────────────────────


class TestParseUnsignedInt:
    def test_parseUnsignedInt_zero(self):
        assert JInteger.parseUnsignedInt("0") == 0

    def test_parseUnsignedInt_positive(self):
        assert JInteger.parseUnsignedInt("42") == 42

    def test_parseUnsignedInt_plus_prefix(self):
        assert JInteger.parseUnsignedInt("+100") == 100

    def test_parseUnsignedInt_max_unsigned(self):
        assert JInteger.parseUnsignedInt("4294967295") == JInteger.MAX_UNSIGNED_VALUE

    def test_parseUnsignedInt_beyond_signed_max(self):
        # valores entre 2^31 e 2^32-1 são válidos para unsigned
        assert JInteger.parseUnsignedInt("2147483648") == 2_147_483_648

    def test_parseUnsignedInt_exceeds_max_raises(self):
        with pytest.raises(ValueError):
            JInteger.parseUnsignedInt("4294967296")

    def test_parseUnsignedInt_minus_raises(self):
        with pytest.raises(ValueError):
            JInteger.parseUnsignedInt("-1")

    def test_parseUnsignedInt_empty_raises(self):
        with pytest.raises(ValueError):
            JInteger.parseUnsignedInt("")

    def test_parseUnsignedInt_null_raises(self):
        with pytest.raises(ValueError):
            JInteger.parseUnsignedInt(None)  # type: ignore[arg-type]

    def test_parseUnsignedInt_invalid_char_raises(self):
        with pytest.raises(ValueError):
            JInteger.parseUnsignedInt("XYZ")


# ── parseUnsignedInt com radix ─────────────────────────


class TestParseUnsignedIntWithRadix:
    def test_parseUnsignedInt_hex(self):
        assert JInteger.parseUnsignedInt("FF", 16) == 255

    def test_parseUnsignedInt_binary(self):
        assert JInteger.parseUnsignedInt("11111111", 2) == 255

    def test_parseUnsignedInt_max_unsigned_hex(self):
        assert JInteger.parseUnsignedInt("FFFFFFFF", 16) == JInteger.MAX_UNSIGNED_VALUE

    def test_parseUnsignedInt_radix_below_min_raises(self):
        with pytest.raises(ValueError):
            JInteger.parseUnsignedInt("10", 1)

    def test_parseUnsignedInt_radix_above_max_raises(self):
        with pytest.raises(ValueError):
            JInteger.parseUnsignedInt("10", 37)

    def test_parseUnsignedInt_invalid_digit_for_radix_raises(self):
        with pytest.raises(ValueError):
            JInteger.parseUnsignedInt("99", 8)


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


# ── signum ───────────────────────────────────────────────────────────────────


class TestSignum:
    def test_zero(self):
        assert JInteger.signum(0) == 0

    def test_positivo(self, valores_bit):
        assert JInteger.signum(valores_bit["dez"]) == 1

    def test_negativo(self, valores_bit):
        assert JInteger.signum(valores_bit["negativo"]) == -1

    def test_min_value(self):
        assert JInteger.signum(JInteger.MIN_VALUE) == -1

    def test_max_value(self, valores_bit):
        assert JInteger.signum(valores_bit["max"]) == 1


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


# ── floatValue ────────────────────────────────────────────────────────


class TestFloatValue:
    def test_floatValue_positive(self):
        assert JInterger.floatValue(2) == 2.0

    def test_floatValue_negative(self):
        assert JInterger.floatValue(-2) == -2.0

    def test_floatValue_zero(self):
        assert JInterger.floatValue(0) == 0.0


# ── toString ────────────────────────────────────────────────────────


class TestToString:
    def test_toString_positive_number(self):
        assert JInteger.toString(2) == "2"
    
    def test_toString_negative_number(self):
        assert JInteger.toString(-2) == "-2"

    def test_toString_float_number(self):
        assert JInteger.toString(2.5) == "2.5"


# ── equals ────────────────────────────────────────────────────────


class TestEquals:
    def test_equals_number_true(self):
        assert JInteger.equals(2, 2) is True

    def test_equals_float_true(self):
        assert JInteger.equals("igual", "igual") is True

    def test_equals_number_false(self):
        assert JInteger.equals(2, 3) is False

    def test_equals_float_false(self):
        assert JInteger.equals("igual", "igual") is False


# ── doubleValue ────────────────────────────────────────────────────────


class TestDoubleValue:
    def test_doubleValue_positive(self):
        assert JInteger.doubleValue(2) == 2.0

    def test_doubleValue_negative(self):
        assert JInteger.doubleValue(-2) == -2.0

    def test_doubleValue_zero(self):
        assert JInteger.doubleValue(0) == 0.0


# ── hashCode ────────────────────────────────────────────────────────


class TestHashCode:
    def test_hashCode_same(self):
        assert JInteger.hashCode(2) == JInteger.hashCode(2)

    def test_hashCode_different(self):
        assert JInteger.hashCode(2) != JInteger.hashCode(3)


# ── compareTo ────────────────────────────────────────────────────────


class TestcompareTo:
    def test_compareTo_positive(self):
        assert JInteger.compareTo(2, 1) > 0

    def test_compareTo_negative(self):
        assert JInteger.compareTo(-2, -1) < 0

    def test_compareTo_equal(self):
        assert JInteger.compareTo(2, 2) == 0