from __future__ import annotations


def _coerce_str(value) -> str:
    if isinstance(value, JString):
        return value.value
    return str(value)


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
    """Wrapper imutável equivalente a java.lang.String (Java SE 8)."""

    # ==========================================================
    # CONSTRUTORES
    # ==========================================================

    def __init__(self, value: str = ""):
        self.value = str(value)

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

    # length()
    # isEmpty()
    # charAt(int index)
    # codePointAt(int index)
    # codePointBefore(int index)
    # codePointCount(int beginIndex, int endIndex)
    # offsetByCodePoints(int index, int codePointOffset)
    # getChars(int srcBegin, int srcEnd, char[] dst, int dstBegin)
    # toCharArray()
    # getBytes()
    # getBytes(String charset)

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
