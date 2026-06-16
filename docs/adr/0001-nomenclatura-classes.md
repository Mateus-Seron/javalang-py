# ADR-0001 — Nomenclatura das Classes

**Status:** Aceito  
**Data:** 2026-06-14  
**Autores:** Equipe GCS 2026.1

---

## Contexto

O projeto implementa em Python os tipos `String`, `Integer` e `Float` da especificação Java SE 8. Foi necessário decidir como nomear as classes Python para evitar colisão com os tipos nativos (`str`, `int`, `float`) e com o módulo `string` da biblioteca padrão.

## Decisão

As classes serão nomeadas com o **prefixo `J`**:

- `JString` (em vez de `JavaString`, `StringJ`, `PyString`, etc.)
- `JInteger`
- `JFloat`

## Alternativas consideradas

| Opção | Prós | Contras |
|-------|------|---------|
| Prefixo `J` (adotado) | Curto, reconhecível, sem colisão | Menos autodescritivo sem contexto |
| Sufixo `Java` | Descritivo | Verboso; `StringJava` soa estranho |
| Sufixo `Type` | Neutro | Ambíguo em outros contextos |
| Nome Java direto (`String`) | Fidelidade ao original | Colide com `str` e módulo `string` |

## Consequências

- **Positivas:** código cliente conciso; fácil busca por `J` + nome Java.
- **Negativas:** requer familiaridade com a convenção para novos colaboradores.
- O `README.md` deve mencionar explicitamente a convenção na seção "Adaptações".
