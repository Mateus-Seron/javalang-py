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
    
    