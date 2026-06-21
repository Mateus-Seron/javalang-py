from __future__ import annotations

import math
import struct


def _float_to_int_bits(value: float) -> int:
    """Equivalente a Float.floatToIntBits(float) — bits interpretados como int com sinal."""
    return struct.unpack(">i", struct.pack(">f", value))[0]


def _float_to_canonical_int_bits(value: float) -> int:
    """Equivalente a Float.floatToIntBits(float) — NaN e zeros canônicos."""
    if value != value:
        return 0x7FC00000
    if value == 0.0:
        return 0
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


def _float_to_string_static(f: float) -> str:
    """Equivalente a Float.toString(float)."""
    if math.isnan(f):
        return "NaN"
    if math.isinf(f):
        return "Infinity" if f > 0 else "-Infinity"
    if f == 0.0:
        return "-0.0" if math.copysign(1.0, f) < 0 else "0.0"
    return str(float(f))


class _ToString:
    """Unifica Float.toString() (instância) e Float.toString(float) (estático)."""

    def __get__(self, obj, owner):
        if obj is None:
            return owner._toString_static
        return lambda: _float_to_string(obj._value)


class JFloat:

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

    # ── Operações de Construtores e Conversão de Float ─────────────────────

    def __init__(self, value: float):
        self._value = _to_float32(value)

    @staticmethod
    def valueOf(f_or_s):
        """Float.valueOf(float) e Float.valueOf(String)."""
        if isinstance(f_or_s, str):
            try:
                return JFloat(float(f_or_s.strip()))
            except ValueError:
                raise ValueError("NumberFormatException")
        return JFloat(float(f_or_s))

    def floatValue(self) -> float:
        """Float.floatValue()."""
        return self._value

    def doubleValue(self) -> float:
        """Float.doubleValue()."""
        return float(self._value)

    _toString_static = staticmethod(_float_to_string_static)
    toString = _ToString()

    def hashCode(self) -> int:
        """Float.hashCode()."""
        return _float_to_canonical_int_bits(self._value)

    def equals(self, other) -> bool:
        """Float.equals(Object obj)."""
        if not isinstance(other, JFloat):
            return False
        self_bits = _float_to_canonical_int_bits(self._value)
        other_bits = _float_to_canonical_int_bits(other._value)
        return self_bits == other_bits

    def compareTo(self, other: JFloat) -> int:
        """Float.compareTo(Float anotherFloat)."""
        return JFloat.compare(self._value, other._value)
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
    def toHexString(f: float) -> str:

        if math.isnan(f):
            return "NaN"

        if math.isinf(f):
            return "Infinity" if f > 0 else "-Infinity"

        return f.hex()
