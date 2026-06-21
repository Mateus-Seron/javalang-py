# ADR-0005 — Unificação de sobrecargas com `radix` em `JInteger`

**Status:** Aceito | **Data:** 2026-06-18 | **Autores:** Equipe GCS 2026.1

---

## Contexto

Java define pares de sobrecargas em `java.lang.Integer`:

- `toString(int)` e `toString(int, int radix)`
- `toUnsignedString(int)` e `toUnsignedString(int, int radix)`

Python não permite dois métodos com o mesmo nome — o segundo sobrescreveria o primeiro.

## Decisão

Um único método por par, com parâmetro opcional `radix=10`:

```python
def toString(i: int, radix: int = 10) -> str:
def toUnsignedString(i: int, radix: int = 10) -> str:
```

Exemplos:

- `JInteger.toString(42)` / `JInteger.toString(255, 16)` → decimal com sinal / base 16.
- `JInteger.toUnsignedString(-1)` → `"4294967295"`; `JInteger.toUnsignedString(-1, 16)` → `"ffffffff"`.

Mesmo padrão valerá para futuras sobrecargas da API Java (`valueOf`, `parseInt`, etc.).
