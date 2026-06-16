"""Smoke test — verifica que o pacote pode ser importado."""

import javalang


def test_pacote_importavel():
    assert javalang is not None


def test_versao_definida():
    assert hasattr(javalang, "__version__")
    assert isinstance(javalang.__version__, str)
    assert len(javalang.__version__) > 0
