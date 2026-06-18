# Constantes úteis para operações unsigned (int Java é 32 bits)
_UINT_MASK = 0xFFFFFFFF


class JInteger:

    # ====== Métodos de Arimética Estática ======

    @staticmethod
    def sum(a: int, b: int) -> int:
        return a + b

    @staticmethod
    def max(a: int, b: int) -> int:
        return a if a >= b else b

    @staticmethod
    def min(a: int, b: int) -> int:
        return a if a <= b else b

    @staticmethod
    def compare(x: int, y: int) -> int:
        if x == y:
            return 0
        return -1 if x < y else 1

    @staticmethod
    def compareUnsigned(x: int, y: int) -> int:
        ux = x & _UINT_MASK
        uy = y & _UINT_MASK
        if ux == uy:
            return 0
        return -1 if ux < uy else 1

    @staticmethod
    def divideUnsigned(dividend: int, divisor: int) -> int:
        return (dividend & _UINT_MASK) // (divisor & _UINT_MASK)
    
    @staticmethod
    def remainderUnsigned(dividend: int, divisor: int) -> int:
        return (dividend & _UINT_MASK) % (divisor & _UINT_MASK)
