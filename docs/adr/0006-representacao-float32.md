# ADR-0006 — Representação IEEE 754 em `JFloat`

**Status:** Aceito | **Data:** 2026-06-19 | **Autores:** Equipe GCS 2026.1

---

## Contexto

`Float.compare`, `Float.max`, `Float.min`, `Float.hashCode` e `Float.equals` em Java SE 8 não
usam apenas `<`, `>=` ou `==`. A especificação trata `-0.0` e `+0.0`, propaga `NaN` e, em alguns
métodos, normaliza bits (zeros e NaN canônicos).

Em Python, `float` é 64 bits, `-0.0 == 0.0` e comparações com `NaN` não reproduzem esse
comportamento sozinhos.

## Decisão

Helpers internos em `javalang/jfloat.py`, via `struct` (big-endian, 32 bits):

| Função | Papel | Usado em |
|--------|-------|----------|
| `_to_float32` | Normaliza valor para precisão `float` Java (32 bits) | `__init__`, `valueOf` |
| `_float_to_int_bits` | Bits brutos IEEE 754 como `int` com sinal (preserva sinal de zero) | `compare`, `compareTo` |
| `_float_to_canonical_int_bits` | Emula `Float.floatToIntBits` (NaN → `0x7fc00000`, zeros → `0`) | `hashCode`, `equals` |
| `_float_to_raw_bits` | Mesmos bits como unsigned | `max` / `min` quando ambos operandos são zero |
| `_int_bits_to_float` | Emula `Float.intBitsToFloat` | reconversão após operações bitwise |

### Valor encapsulado

O construtor `JFloat(value)` armazena `self._value = _to_float32(value)`, garantindo que o wrapper
reflete a precisão de um `float` Java, não a precisão dupla padrão de Python.

### Comparação vs identidade

- **`compare` / `compareTo`:** após empate numérico (`f1 == f2`), compara `_float_to_int_bits`
  (bits brutos). Assim `-0.0` < `+0.0`, alinhado ao desempate por bits da implementação adotada.
- **`hashCode` / `equals`:** usam `_float_to_canonical_int_bits`, como `Float.hashCode` e
  `Float.equals` em Java (`-0.0` e `+0.0` têm o mesmo hash e são iguais).

### Max / min

- Se o primeiro operando é `NaN`, retorna `NaN`.
- Se ambos são zero, usa `&` ou `|` nos bits brutos (como `Math.max` / `Math.min` em Java).

Novos métodos de `JFloat` que dependam de semântica IEEE 754 devem reutilizar estes helpers e
escolher bits brutos ou canônicos conforme a especificação Java do método implementado.
