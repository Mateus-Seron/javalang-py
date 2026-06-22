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

            if (
                0xD800 <= cu1 <= 0xDBFF
                and i + 1 < endIndex
                and 0xDC00 <= units[i + 1] <= 0xDFFF
            ):
                i += 2
            else:
                i += 1

            count += 1

        return count


# offsetByCodePoints(int index, int codePointOffset)
# getChars(int srcBegin, int srcEnd, char[] dst, int dstBegin)
# toCharArray()
# getBytes()
# getBytes(String charset)

# ==========================================================
# COMPARAÇÃO
# ==========================================================

# equals(Object obj)
# equalsIgnoreCase(String anotherString)
# compareTo(String anotherString)
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
