from __future__ import annotations

import math
import struct
import sys



def _float_to_int_bits(value: float) -> int:
    """Equivalente a Float.floatToIntBits(float) — bits interpretados como int com sinal."""
    return struct.unpack(">i", struct.pack(">f", value))[0]


def _float_to_raw_bits(value: float) -> int:
    """Bits IEEE 754 brutos (32 bits unsigned) para operações bitwise."""
    return struct.unpack(">I", struct.pack(">f", value))[0]


def _int_bits_to_float(bits: int) -> float:
    """Equivalente a Float.intBitsToFloat(int)."""
    return struct.unpack(">f", struct.pack(">I", bits & 0xFFFFFFFF))[0]


class JFloat:
    def __init__(self, value):
        self._value = float(value)

    # ── Operações de Verificação IEEE 754  ──────────────────────────────────────────────

    def isNaN(self_or_v):
        if isinstance(self_or_v, JFloat):
            return math.isnan(self_or_v._value)

        return math.isnan(self_or_v)

    def isInfinite(self_or_v):
        if isinstance(self_or_v, JFloat):
            return math.isinf(self_or_v._value)

        return math.isinf(self_or_v)

    @staticmethod
    def isFinite(f: float) -> bool:
        return math.isfinite(f)

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

    # ── Pacote de Operações de Parsing e Formatação ──────────────────────────────────────────────

    @staticmethod
    def parseFloat(s: str) -> float:
        if s is None:
            raise TypeError("NullPointerException")

        try:
            return float(s.strip())
        except ValueError:
            raise ValueError("NumberFormatException")

    @staticmethod
    def valueOf(f_or_s):
        if isinstance(f_or_s, str):
            try:
                return JFloat(float(f_or_s.strip()))
            except ValueError:
                raise ValueError("NumberFormatException")

        return JFloat(float(f_or_s))

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

    # ── Constantes ─────────────────────────────────────────────────────────

    MAX_VALUE = sys.float_info.max
    MIN_VALUE = sys.float_info.min * sys.float_info.epsilon
    MIN_NORMAL = sys.float_info.min
    POSITIVE_INFINITY = float('inf')
    NEGATIVE_INFINITY = float('-inf')