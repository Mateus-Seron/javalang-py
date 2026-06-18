"""Implementação parcial de java.lang.Integer (Java SE 8) em Python.

Métodos adicionados incrementalmente via PRs.
Referência: https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html
"""

from __future__ import annotations

_MASK32 = 0xFFFFFFFF


def _to_int32(value: int) -> int:
    # Python usa inteiros de precisão arbitrária, sem limite de bits.
    # Java representa int com exatamente 32 bits em complemento de dois,
    # cobrindo o intervalo [-2^31, 2^31 - 1].
    #
    # Esta função simula esse comportamento em duas etapas:
    #   1. & _MASK32 — descarta tudo acima dos 32 bits menos significativos.
    #   2. Se o bit 31 (sinal) estiver ligado, o valor está no intervalo
    #      [2^31, 2^32 - 1] em Python, mas deveria ser negativo em Java.
    #      Subtrair 2^32 faz a conversão correta para complemento de dois.
    #
    # Exemplo: highestOneBit(-1) produz 0x80000000 = 2147483648 em Python.
    # Sem esta função, retornaríamos 2147483648 — correto em bits, mas errado
    # como int Java com sinal, que deve ser -2147483648 (Integer.MIN_VALUE).
    value = value & _MASK32
    if value >= 2**31:
        value -= 2**32
    return value


class JInteger:
    """Wrapper imutável equivalente a java.lang.Integer (Java SE 8)."""

    MIN_VALUE: int = -(2**31)
    MAX_VALUE: int = 2**31 - 1
    SIZE: int = 32
    BYTES: int = 4

    # ── Operações bit a bit ────────────────────────────────────────────────

    @staticmethod
    def bitCount(i: int) -> int:
        """Integer.bitCount(int i) — número de bits 1 na representação de 32 bits."""
        return bin(i & _MASK32).count("1")

    @staticmethod
    def highestOneBit(i: int) -> int:
        """Integer.highestOneBit(int i) — retorna apenas o bit 1 mais à esquerda."""
        if i == 0:
            return 0
        v = i & _MASK32
        # propaga o bit mais alto para todos os bits à direita dele
        v |= v >> 1
        v |= v >> 2
        v |= v >> 4
        v |= v >> 8
        v |= v >> 16
        return _to_int32(v - (v >> 1))

    @staticmethod
    def lowestOneBit(i: int) -> int:
        """Integer.lowestOneBit(int i) — retorna apenas o bit 1 mais à direita."""
        return _to_int32(i & (-i))

    # ── Aritmética estática ────────────────────────────────────────────────

    @staticmethod
    def sum(a: int, b: int) -> int:
        """Integer.sum(int a, int b)"""
        return a + b

    @staticmethod
    def max(a: int, b: int) -> int:
        """Integer.max(int a, int b)"""
        return a if a >= b else b

    @staticmethod
    def min(a: int, b: int) -> int:
        """Integer.min(int a, int b)"""
        return a if a <= b else b

    @staticmethod
    def compare(x: int, y: int) -> int:
        """Integer.compare(int x, int y)"""
        if x == y:
            return 0
        return -1 if x < y else 1

    @staticmethod
    def compareUnsigned(x: int, y: int) -> int:
        """Integer.compareUnsigned(int x, int y)"""
        ux = x & _MASK32
        uy = y & _MASK32
        if ux == uy:
            return 0
        return -1 if ux < uy else 1

    @staticmethod
    def divideUnsigned(dividend: int, divisor: int) -> int:
        """Integer.divideUnsigned(int dividend, int divisor)"""
        return (dividend & _MASK32) // (divisor & _MASK32)

    @staticmethod
    def remainderUnsigned(dividend: int, divisor: int) -> int:
        """Integer.remainderUnsigned(int dividend, int divisor)"""
        return (dividend & _MASK32) % (divisor & _MASK32)
