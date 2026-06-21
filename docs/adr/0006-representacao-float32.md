# ADR-0006 — Representação IEEE 754 em `JFloat`

**Status:** Aceito | **Data:** 2026-06-19 | **Autores:** Equipe GCS 2026.1

---

## Contexto

`Float.compare`, `Float.max` e `Float.min` em Java SE 8 não usam apenas `<` e `>=`. A especificação
trata `-0.0` e `+0.0` como valores distintos, propaga `NaN` e compara bits quando os valores
numéricos empataam.

Em Python, `-0.0 == 0.0` e comparações com `NaN` não reproduzem esse comportamento sozinhas.

## Decisão

Helpers internos em `javalang/jfloat.py`, via `struct` (big-endian, 32 bits):

| Função | Papel |
|--------|-------|
| `_float_to_int_bits` | Emula `Float.floatToIntBits` — bits como `int` com sinal; usado em `compare` |
| `_float_to_raw_bits` | Mesmos bits como unsigned; usado em `max`/`min` quando ambos operandos são zero |
| `_int_bits_to_float` | Emula `Float.intBitsToFloat` — reconverte bits em `float` |

Regras aplicadas:

- **`compare`:** após empate numérico, compara bits com sinal (`-0.0` < `+0.0`).
- **`max` / `min`:** se o primeiro operando é `NaN`, retorna `NaN`; se ambos são zero, usa `&` ou `|` nos bits brutos (como `Math.max`/`Math.min` em Java).
- Novos métodos de `JFloat` que dependam de semântica IEEE 754 devem reutilizar esses helpers.
