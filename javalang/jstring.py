from __future__ import annotations


def _coerce_str(value) -> str:
    if isinstance(value, JString):
        return value.value
    return str(value)


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

    # compareToIgnoreCase(String str)
    # contentEquals(CharSequence cs)
    # regionMatches(int toffset, String other, int ooffset, int len)
    # regionMatches(boolean ignoreCase, int toffset,
    #               String other, int ooffset, int len)
    # hashCode()

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
