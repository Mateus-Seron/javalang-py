import math

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
