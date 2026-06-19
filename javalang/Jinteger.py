class JInteger:
    def __init__(self, value):
        "Equivale aos dois contrutores Integer(int) e Integer(String)"
        self.value = int(value)

    def intValue(self):
        return self.value

    def longValue(self):
        return self.value

    def shortValue(self):
        return self.value

    def byteValue(self):
        value = self.value & 0xFF

        if value >= 128:
            value -= 256

        return value
