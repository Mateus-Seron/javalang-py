from __future__ import annotations

import struct


def _float_to_int_bits(value: float) -> int:
    """Equivalente a Float.floatToIntBits(float) — bits interpretados como int com sinal."""
    return struct.unpack(">i", struct.pack(">f", value))[0]


def _float_to_raw_bits(value: float) -> int:
    """Bits IEEE 754 brutos (32 bits unsigned) para operações bitwise."""
    return struct.unpack(">I", struct.pack(">f", value))[0]


def _int_bits_to_float(bits: int) -> float:
    """Equivalente a Float.intBitsToFloat(int)."""
    return struct.unpack(">f", struct.pack(">I", bits & 0xFFFFFFFF))[0]


def _to_float32(value: float) -> float:
    """Normaliza para precisão de float Java (32 bits)."""
    return struct.unpack(">f", struct.pack(">f", value))[0]


def _float_to_string(value: float) -> str:
    """Equivalente a Float.toString(float) para casos especiais."""
    if value != value:
        return "NaN"
    if value == float("inf"):
        return "Infinity"
    if value == float("-inf"):
        return "-Infinity"
    return str(value)


class JFloat:
    """Wrapper imutável equivalente a java.lang.Float (Java SE 8)."""

    # ── Operações de Comparação de Float ───────────────────────────────────────

    @staticmethod
    def compare(f1: float, f2: float) -> int:
        """Float.compare(float f1, float f2)."""
        if f1 < f2:
            return -1
        if f1 > f2:
            return 1
        bits1 = _float_to_int_bits(f1)
        bits2 = _float_to_int_bits(f2)
        if bits1 == bits2:
            return 0
        if bits1 < bits2:
            return -1
        return 1

    @staticmethod
    def max(a: float, b: float) -> float:
        """Float.max(float a, float b)."""
        if a != a:
            return a
        if a == 0.0 and b == 0.0:
            return _int_bits_to_float(_float_to_raw_bits(a) & _float_to_raw_bits(b) & 0x7FFFFFFF)
        return a if a >= b else b

    @staticmethod
    def min(a: float, b: float) -> float:
        """Float.min(float a, float b)."""
        if a != a:
            return a
        if a == 0.0 and b == 0.0:
            return _int_bits_to_float(_float_to_raw_bits(a) | _float_to_raw_bits(b))
        return a if a <= b else b

    @staticmethod
    def sum(a: float, b: float) -> float:
        """Float.sum(float a, float b)."""
        return a + b

    # ── Operações de Construtores e Conversão de Float ─────────────────────

    def __init__(self, value: float):
        self._value = _to_float32(value)

    @staticmethod
    def valueOf(value: float) -> JFloat:
        """Float.valueOf(float f)."""
        return JFloat(value)

    def floatValue(self) -> float:
        """Float.floatValue()."""
        return self._value

    def doubleValue(self) -> float:
        """Float.doubleValue()."""
        return float(self._value)

    def toString(self) -> str:
        """Float.toString() — representação decimal do valor encapsulado."""
        return _float_to_string(self._value)
