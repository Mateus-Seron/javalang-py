# ADR-0004 — Representação de int de 32 bits em JInteger

**Status:** Aceito  
**Data:** 2026-06-18  
**Autores:** Equipe GCS 2026.1

---

## Contexto

Em Java SE 8, o tipo primitivo `int` ocupa exatamente 32 bits e usa complemento de dois, com intervalo
`[Integer.MIN_VALUE, Integer.MAX_VALUE]` (`-2³¹` a `2³¹ - 1`).

Em Python 3, o tipo `int` nativo tem **precisão arbitrária** — não há truncamento automático para 32 bits.
Operações bit a bit em valores grandes ou negativos podem produzir resultados numericamente corretos em
Python, mas **divergentes da especificação Java**.

Exemplo: `Integer.highestOneBit(-1)` em Java retorna `Integer.MIN_VALUE` (`-2147483648`). Sem
normalização, a mesma operação em Python retornaria `2147483648`.

## Decisão

Adotar uma função auxiliar interna `_to_int32(value: int) -> int` em `javalang/jinteger.py`, aplicada
sempre que o resultado de uma operação bit a bit precisar respeitar a semântica de `int` Java:

1. `value & 0xFFFFFFFF` — mantém apenas os 32 bits menos significativos.
2. Se o bit de sinal (bit 31) estiver ligado, subtrair `2³²` para converter ao valor negativo
   equivalente em complemento de dois.

Esta normalização é usada nos métodos `highestOneBit`, `lowestOneBit` e em qualquer outro método de
`JInteger` cujo contrato Java dependa de overflow/wrap de 32 bits.

## Alternativas consideradas

| Opção | Prós | Contras |
|-------|------|---------|
| Confiar no `int` nativo do Python | Simples | Resultados incorretos para valores fora do intervalo Java |
| Usar `ctypes.c_int32` | Fidelidade automática | Dependência extra; API menos legível |
| Normalização via `_to_int32` (adotado) | Sem dependências; explícito; testável | Requer aplicar manualmente em cada método afetado |

## Consequências

- **Positivas:** métodos bit a bit produzem os mesmos valores que `java.lang.Integer` nos casos-limite
  (`0`, `-1`, `MIN_VALUE`, `MAX_VALUE`).
- **Negativas:** a normalização deve ser lembrada em todo método novo que envolva operações de 32 bits;
  documentado no README e neste ADR.
- **Alternativa para o usuário:** quem precisar de inteiros arbitrários em Python pode usar `int` nativo
  diretamente; `JInteger` existe para emular o contrato Java.
