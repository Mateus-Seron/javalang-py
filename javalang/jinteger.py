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
    MIN_RADIX = 2
    MAX_RADIX = 36
    MIN_VALUE: int = -(2**31)
    MAX_VALUE: int = 2**31 - 1
    SIZE: int = 32
    BYTES: int = 4
    MAX_UNSIGNED_VALUE: int = 2**32 - 1

    _DIGITS = "0123456789abcdefghijklmnopqrstuvwxyz"
    _valueOf_cache: dict = {i: i for i in range(-128, 128)}

    @staticmethod
    def _check_radix(radix: int) -> None:
        if not (JInteger.MIN_RADIX <= radix <= JInteger.MAX_RADIX):
            raise ValueError(
                f"NumberFormatException: radix {radix} out of range "
                f"[{JInteger.MIN_RADIX}, {JInteger.MAX_RADIX}]"
            )

    @staticmethod
    def _valid_digit_chars(s: str, radix: int) -> bool:
        valid = set(JInteger._DIGITS[:radix])
        return all(ch in valid for ch in s.lower())

    # ── Parsing ────────────────────────────────────────────────────────────
    @staticmethod
    def parseInt(s: str, radix: int = 10) -> int:
        if s is None:
            raise ValueError("NumberFormatException: null")

        if len(s) == 0:
            raise ValueError('NumberFormatException: For input string: ""')

        JInteger._check_radix(radix)

        body = s
        if body[0] in ("+", "-"):
            if len(body) == 1:
                raise ValueError(
                    f'NumberFormatException: For input string: "{s}"'
                )
            body = body[1:]

        if not JInteger._valid_digit_chars(body, radix):
            raise ValueError(
                f'NumberFormatException: For input string: "{s}"'
            )

        result = int(s, radix)

        if not (JInteger.MIN_VALUE <= result <= JInteger.MAX_VALUE):
            raise ValueError(
                f'NumberFormatException: For input string: "{s}"'
            )

        return result

    @staticmethod
    def parseUnsignedInt(s: str, radix: int = 10) -> int:
        if s is None:
            raise ValueError("NumberFormatException: null")

        if len(s) == 0:
            raise ValueError('NumberFormatException: For input string: ""')

        JInteger._check_radix(radix)

        if s[0] == "-":
            raise ValueError(
                f'NumberFormatException: Illegal leading minus sign '
                f'on unsigned string "{s}"'
            )

        body = s
        if body[0] == "+":
            if len(body) == 1:
                raise ValueError(
                    f'NumberFormatException: For input string: "{s}"'
                )
            body = body[1:]

        if not JInteger._valid_digit_chars(body, radix):
            raise ValueError(
                f'NumberFormatException: For input string: "{s}"'
            )

        result = int(body, radix)

        if result > JInteger.MAX_UNSIGNED_VALUE:
            raise ValueError(
                f'NumberFormatException: String value "{s}" '
                f'exceeds range of unsigned int'
            )

        return result
    
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

    @staticmethod
    def numberOfLeadingZeros(i: int) -> int:
        """Integer.numberOfLeadingZeros(int i) — zeros antes do primeiro bit 1."""
        if i == 0:
            return 32
        v = i & _MASK32
        n = 0
        if v <= 0x0000FFFF:
            n += 16
            v <<= 16
        if v <= 0x00FFFFFF:
            n += 8
            v <<= 8
        if v <= 0x0FFFFFFF:
            n += 4
            v <<= 4
        if v <= 0x3FFFFFFF:
            n += 2
            v <<= 2
        if v <= 0x7FFFFFFF:
            n += 1
        return n

    @staticmethod
    def numberOfTrailingZeros(i: int) -> int:
        """Integer.numberOfTrailingZeros(int i) — zeros após o último bit 1."""
        if i == 0:
            return 32
        v = i & _MASK32
        n = 0
        if v & 0x0000FFFF == 0:
            n += 16
            v >>= 16
        if v & 0x000000FF == 0:
            n += 8
            v >>= 8
        if v & 0x0000000F == 0:
            n += 4
            v >>= 4
        if v & 0x00000003 == 0:
            n += 2
            v >>= 2
        if v & 0x00000001 == 0:
            n += 1
        return n

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
