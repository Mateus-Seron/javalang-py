from __future__ import annotations

## class JString:
"""Wrapper imutável equivalente a java.lang.String (Java SE 8)."""


def _coerce_str(value) -> str:
    if value is None:
        return None
    if isinstance(value, JString):
        return value.value
    if isinstance(value, str):
        return value
    raise TypeError(f"Tipo inválido: {type(value).__name__}")


def _chars_region_match(c1: str, c2: str, ignore_case: bool) -> bool:
    if c1 == c2:
        return True
    if not ignore_case:
        return False
    u1 = c1.upper()
    u2 = c2.upper()
    if u1 != u2:
        return False
    return c1.lower() == c2.lower()


def _java_string_hash(value: str) -> int:
    """Equivalente a String.hashCode() — polinômio 31 sobre code units."""
    h = 0
    for char in value:
        h = (31 * h + ord(char)) & 0xFFFFFFFF
    if h >= 2**31:
        h -= 2**32
    return h


class JString:
    def __init__(self, value: str = ""):
        self.value = str(value)

    # ----------------------------------------------------------
    # UTILITÁRIO: converte string Python para UTF-16 code units
    # ----------------------------------------------------------
    def _code_units(self):
        b = self.value.encode("utf-16-le")
        return [b[i] + (b[i + 1] << 8) for i in range(0, len(b), 2)]

    def _from_code_unit(self, cu: int):
        return chr(cu)

    # ==========================================================
    # CONSTRUTORES
    # ==========================================================

    # String()
    @staticmethod
    def string(self) -> str:
        return ""

    # String(char[] value)
    @staticmethod
    def stringCharArray(value: list[str]) -> str:
        return "".join(value)

    # String(byte[] bytes)
    @staticmethod
    def stringBytes(byte: bytes) -> str:
        return byte.decode()

    # String(byte[], int offset, int length)
    # String(StringBuilder builder)
    # String(String original)
    @staticmethod
    def stringOriginal(original: str) -> str:
        return str(original)

    # String(char[] value, int offset, int count)
    @staticmethod
    def stringCharArrayOffsetCount(value: list[str], offset: int, count: int) -> str:
        return "".join(value[offset : offset + count])

    # String(byte[] bytes, String charset)
    # String(int[] codePoints, int offset, int count)

    # String()
    # String(char[] value)
    # String(byte[] bytes)
    # String(byte[], int offset, int length)
    # String(StringBuilder builder)
    # String(String original)
    # String(char[] value, int offset, int count)
    # String(byte[] bytes, String charset)
    # String(int[] codePoints, int offset, int count)

    # ==========================================================
    # ACESSO E TAMANHO
    # ==========================================================

    def length(self) -> int:
        return len(self._code_units())

    def isEmpty(self) -> bool:
        return self.length() == 0

    def charAt(self, index: int) -> str:
        units = self._code_units()
        if index < 0 or index >= len(units):
            raise IndexError("String index out of range")
        return chr(units[index])

    def codePointAt(self, index: int) -> int:
        units = self._code_units()

        if index < 0 or index >= len(units):
            raise IndexError("Index out of range")

        cu1 = units[index]

        # high surrogate
        if 0xD800 <= cu1 <= 0xDBFF and index + 1 < len(units):
            cu2 = units[index + 1]
            if 0xDC00 <= cu2 <= 0xDFFF:
                return 0x10000 + ((cu1 - 0xD800) << 10) + (cu2 - 0xDC00)

        return cu1

    def codePointBefore(self, index: int) -> int:
        units = self._code_units()

        if index <= 0 or index > len(units):
            raise IndexError("Index out of range")

        cu1 = units[index - 1]

        # low surrogate
        if 0xDC00 <= cu1 <= 0xDFFF and index - 2 >= 0:
            cu2 = units[index - 2]
            if 0xD800 <= cu2 <= 0xDBFF:
                return 0x10000 + ((cu2 - 0xD800) << 10) + (cu1 - 0xDC00)

        return cu1

    def codePointCount(self, beginIndex: int, endIndex: int) -> int:
        units = self._code_units()

        if beginIndex < 0 or endIndex > len(units) or beginIndex > endIndex:
            raise IndexError("Index out of range")

        i = beginIndex
        count = 0

        while i < endIndex:
            cu1 = units[i]

            if 0xD800 <= cu1 <= 0xDBFF and i + 1 < endIndex and 0xDC00 <= units[i + 1] <= 0xDFFF:
                i += 2
            else:
                i += 1

            count += 1

        return count

    def offsetByCodePoints(self, index: int, codePointOffset: int) -> int:
        length = len(self.value)

        if index < 0 or index > length:
            raise IndexError("index out of bounds")

        result = index + codePointOffset

        if result < 0 or result > length:
            raise IndexError("codePointOffset out of bounds")

        return result

    def getChars(self, srcBegin: int, srcEnd: int, dst: list, dstBegin: int) -> None:

        length = len(self.value)

        if srcBegin < 0:
            raise IndexError("srcBegin out of bounds")

        if srcBegin > srcEnd:
            raise IndexError("srcBegin greater than srcEnd")

        if srcEnd > length:
            raise IndexError("srcEnd out of bounds")

        if dstBegin < 0:
            raise IndexError("dstBegin out of bounds")

        copy_len = srcEnd - srcBegin

        if dstBegin + copy_len > len(dst):
            raise IndexError("destination array too small")

        for i in range(copy_len):
            dst[dstBegin + i] = self.value[srcBegin + i]

    def toCharArray(self) -> list:
        return list(self.value)

    def getBytes(self, charsetName: str = None) -> bytes:  # type: ignore
        if charsetName is None:
            return self.value.encode()

        try:
            return self.value.encode(charsetName)
        except LookupError:
            raise ValueError(f"Unsupported encoding: {charsetName}")

    # ==========================================================
    # COMPARAÇÃO
    # ==========================================================

    def equals(self, other) -> bool:
        """String.equals(Object obj)."""
        if self is other:
            return True
        if not isinstance(other, JString):
            return False
        return self.value == other.value

    def equalsIgnoreCase(self, other) -> bool:
        """String.equalsIgnoreCase(String anotherString)."""
        if other is None:
            return False
        return self.value.casefold() == _coerce_str(other).casefold()

    def compareTo(self, other) -> int:
        """String.compareTo(String anotherString)."""
        other_str = _coerce_str(other)
        limit = min(len(self.value), len(other_str))
        for i in range(limit):
            c1 = self.value[i]
            c2 = other_str[i]
            if c1 != c2:
                return ord(c1) - ord(c2)
        return len(self.value) - len(other_str)

    def compareToIgnoreCase(self, other) -> int:
        """String.compareToIgnoreCase(String str)."""
        other_str = _coerce_str(other)
        limit = min(len(self.value), len(other_str))
        for i in range(limit):
            c1 = self.value[i]
            c2 = other_str[i]
            if c1 != c2:
                u1 = c1.upper()
                u2 = c2.upper()
                if u1 != u2:
                    return ord(u1) - ord(u2)
                l1 = c1.lower()
                l2 = c2.lower()
                if l1 != l2:
                    return ord(l1) - ord(l2)
        return len(self.value) - len(other_str)

    def contentEquals(self, cs) -> bool:
        """String.contentEquals(CharSequence cs)."""
        if cs is None:
            return False
        return self.value == _coerce_str(cs)

    def regionMatches(
        self,
        toffset_or_ignore,
        other=None,
        ooffset=None,
        length=None,
        maybe_length=None,
    ) -> bool:
        """String.regionMatches(...) — sobrecargas com e sem ignoreCase."""
        if isinstance(toffset_or_ignore, bool):
            ignore_case = toffset_or_ignore
            toffset, other, ooffset, length = other, ooffset, length, maybe_length
        else:
            ignore_case = False
            toffset, other, ooffset, length = toffset_or_ignore, other, ooffset, length

        other_str = _coerce_str(other)
        if ooffset < 0 or toffset < 0 or length < 0:
            return False
        if toffset > len(self.value) - length or ooffset > len(other_str) - length:
            return False

        for i in range(length):
            if not _chars_region_match(
                self.value[toffset + i],
                other_str[ooffset + i],
                ignore_case,
            ):
                return False
        return True

    def hashCode(self) -> int:
        """String.hashCode()."""
        return _java_string_hash(self.value)

    # ==========================================================
    # BUSCA
    # ==========================================================

    # indexOf(int ch)
    # indexOf(int ch, int fromIndex)
    # indexOf(String str)
    # indexOf(String str, int fromIndex)

    # lastIndexOf(int ch)
    # lastIndexOf(int ch, int fromIndex)
    # lastIndexOf(String str)
    # lastIndexOf(String str, int fromIndex)

    # contains(CharSequence s)
    # startsWith(String prefix)
    # startsWith(String prefix, int toffset)
    # endsWith(String suffix)

    # ==========================================================
    # TRANSFORMAÇÃO
    # ==========================================================

    # substring(int beginIndex)
    # substring(int beginIndex, int endIndex)
    # subSequence(int beginIndex, int endIndex)

    # concat(String str)

    # replace(char oldChar, char newChar)
    # replace(CharSequence target, CharSequence replacement)

    # toLowerCase()
    # toUpperCase()
    # trim()

    # intern()

    # ==========================================================
    # EXPRESSÕES REGULARES
    # ==========================================================

    # matches(String regex)
    # replaceAll(String regex, String replacement)
    # replaceFirst(String regex, String replacement)

    # split(String regex)
    # split(String regex, int limit)

    # ==========================================================
    # MÉTODOS ESTÁTICOS
    # ==========================================================

    # String.valueOf(int value)
    # String.valueOf(long value)
    # String.valueOf(float value)
    # String.valueOf(double value)
    # String.valueOf(boolean value)
    # String.valueOf(char value)
    # String.valueOf(char[] value)
    # String.valueOf(Object obj)

    # String.copyValueOf(char[] value)

    # String.format(String format, Object... args)

    # String.join(...)
