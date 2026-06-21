import pytest


@pytest.fixture
def zero():
    return 0


@pytest.fixture
def potencias_de_dois():
    """Valores que são potências de 2 — úteis para highestOneBit e lowestOneBit."""
    return [1, 2, 4, 8, 16, 32, 64, 128]


@pytest.fixture
def valores_bit():
    """Conjunto representativo de inteiros para testes de operações bit a bit."""
    return {
        "zero": 0,
        "um": 1,
        "sete": 7,
        "dez": 10,
        "doze": 12,
        "cem": 100,
        "max": 2**31 - 1,
        "negativo": -1,
    }
