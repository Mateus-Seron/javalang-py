from __future__ import annotations

import math
import struct
import sys


def _to_float32(value: float) -> float:
    """
    Força o valor para precisão IEEE-754 de 32 bits,
    simulando java.lang.Float.
    """
    return struct.unpack(">f", struct.pack(">f", float(value)))[0]


def _float_to_int_bits(value: float) -> int:
    """Equivalente a Float.floatToIntBits(float)."""
    return struct.unpack(">i", struct.pack(">f", value))[0]


def _float_to_raw_bits(value: float) -> int:
    """Bits IEEE-754 brutos (32 bits unsigned)."""
    return struct.unpack(">I", struct.pack(">f", value))[0]


def _int_bits_to_float(bits: int) -> float:
    """Equivalente a Float.intBitsToFloat(int)."""
    return struct.unpack(">f", struct.pack(">I", bits & 0xFFFFFFFF))[0]


class JFloat:
    # ── Constantes Float ──────────────────────────────────────────────

    MAX_VALUE = sys.float_info.max
    MIN_VALUE = sys.float_info.min * sys.float_info.epsilon
    MIN_NORMAL = sys.float_info.min

    POSITIVE_INFINITY = float("inf")
    NEGATIVE_INFINITY = float("-inf")
    NaN = float("nan")

    MAX_EXPONENT = 127
    MIN_EXPONENT = -126

    SIZE = 32
    BYTES = 4
    TYPE = float

    # ── Construtor ────────────────────────────────────────────────────

    def __init__(self, value):
        """
        Equivale aos construtores:
            Float(float value)
            Float(double value)
            Float(String s)
        """
        self.value = _to_float32(float(value))

    # ── Operações de Verificação IEEE 754 ─────────────────────────────

    def isNaN(self):
        return math.isnan(self.value)

    def isInfinite(self):
        return math.isinf(self.value)

    @staticmethod
    def isFinite(f: float) -> bool:
        return math.isfinite(f)

    # ── Operações de Comparação ───────────────────────────────────────

    @staticmethod
    def compare(f1: float, f2: float) -> int:
        if f1 < f2:
            return -1

        if f1 > f2:
            return 1

        bits1 = _float_to_int_bits(f1)
        bits2 = _float_to_int_bits(f2)

        if bits1 == bits2:
            return 0

        return -1 if bits1 < bits2 else 1

    @staticmethod
    def max(a: float, b: float) -> float:
        if math.isnan(a):
            return a

        if a == 0.0 and b == 0.0:
            return _int_bits_to_float(_float_to_raw_bits(a) & _float_to_raw_bits(b) & 0x7FFFFFFF)

        return a if a >= b else b

    @staticmethod
    def min(a: float, b: float) -> float:
        if math.isnan(a):
            return a

        if a == 0.0 and b == 0.0:
            return _int_bits_to_float(_float_to_raw_bits(a) | _float_to_raw_bits(b))

        return a if a <= b else b

    @staticmethod
    def sum(a: float, b: float) -> float:
        return a + b

    # ── Conversões ────────────────────────────────────────────────────

    def byteValue(self) -> int:
        value = int(self.value) & 0xFF

        if value >= 128:
            value -= 256

        return value

    def shortValue(self) -> int:
        value = int(self.value) & 0xFFFF

        if value >= 32768:
            value -= 65536

        return value

    def intValue(self) -> int:
        return int(self.value)

    def longValue(self) -> int:
        return int(self.value)

    def floatValue(self) -> float:
        return self.value

    def doubleValue(self) -> float:
        return float(self.value)

    # ── Parsing e Formatação ──────────────────────────────────────────

    @staticmethod
    def parseFloat(s: str) -> float:
        if s is None:
            raise TypeError("NullPointerException")

        try:
            return _to_float32(float(s.strip()))
        except ValueError:
            raise ValueError("NumberFormatException")

    @staticmethod
    def valueOf(f_or_s):
        if isinstance(f_or_s, str):
            try:
                return JFloat(f_or_s.strip())
            except ValueError:
                raise ValueError("NumberFormatException")

        return JFloat(f_or_s)

    @staticmethod
    def toString(f: float) -> str:
        if math.isnan(f):
            return "NaN"

        if math.isinf(f):
            return "Infinity" if f > 0 else "-Infinity"

        if f == 0.0:
            return "-0.0" if math.copysign(1.0, f) < 0 else "0.0"

        return str(float(f))

    @staticmethod
    def toHexString(f: float) -> str:
        if math.isnan(f):
            return "NaN"

        if math.isinf(f):
            return "Infinity" if f > 0 else "-Infinity"

        return f.hex()
