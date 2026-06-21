# ADR-0007 — Unificação de `toString` instância/estático em `JFloat`

**Status:** Aceito | **Data:** 2026-06-19 | **Autores:** Equipe GCS 2026.1

---

## Contexto

Em Java SE 8, `java.lang.Float` expõe duas formas de `toString`:

- `toString()` — método de instância no wrapper `Float`
- `toString(float)` — método estático de formatação

Python não permite dois métodos com o mesmo nome na classe. Definir ambos como funções normais
faz o segundo sobrescrever o primeiro (erro **F811** no Ruff). `@staticmethod` com parâmetro
opcional não resolve chamadas zero-arg na instância (`JFloat.valueOf(2.5).toString()`).

O padrão do [ADR-0005](0005-unificacao-tostring.md) (parâmetro opcional) funciona em `JInteger`
porque a API estática não exige método de instância com a mesma assinatura.

## Decisão

Descriptor `_ToString` em `javalang/jfloat.py`:

- **`JFloat.toString(f)`** (acesso via classe) → delega a `_float_to_string_static` (estático Java)
- **`obj.toString()`** (acesso via instância) → delega a `_float_to_string` no valor encapsulado

Implementação resumida:

```python
class _ToString:
    def __get__(self, obj, owner):
        if obj is None:
            return owner._toString_static
        return lambda: _float_to_string(obj._value)

class JFloat:
    _toString_static = staticmethod(_float_to_string_static)
    toString = _ToString()
```

O estático distingue `-0.0` de `+0.0` na saída (`"-0.0"` / `"0.0"`); o de instância usa
formatação decimal simples para valores finitos.

`valueOf(float)` e `valueOf(String)` permanecem unificados em um único `@staticmethod`, conforme
previsto no ADR-0005.
