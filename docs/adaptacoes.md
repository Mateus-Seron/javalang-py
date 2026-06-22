# Adaptações ao Processo e à Estrutura Padrão

Este documento registra as adaptações feitas pela equipe em relação à estrutura mínima recomendada pelo projeto. Cada adaptação deve referenciar o ADR correspondente.

---

## Como registrar uma adaptação

Toda vez que a equipe decide:
- Adicionar, remover ou renomear um arquivo da estrutura padrão
- Mudar um padrão de código, lint ou CI
- Adotar uma convenção diferente da sugerida no `CONTRIBUTING.md`

…o integrante responsável deve:
1. Abrir uma issue com o template `decision.md`
2. Criar o ADR correspondente em `docs/adr/`
3. Registrar o resumo abaixo

---

## Registro de Adaptações

| # | Descrição da adaptação | ADR | Data | Autor |
|---|------------------------|-----|------|-------|
| 1 | Nomenclatura de classes com prefixo `J` em vez de sufixo `Java` | [ADR-0001](adr/0001-nomenclatura-classes.md) | — | — |
| 2 | Uso de GitHub Flow (branch curto → PR → merge em `main`) | [ADR-0002](adr/0002-modelo-ramificacao.md) | — | — |
| 3 | Locale configurável via variável de ambiente `JAVALANG_LOCALE` | [ADR-0003](adr/0003-tratamento-locale.md) | — | — |
| 4 | Normalização de resultados bit a bit para 32 bits em `JInteger` (`_to_int32`) | [ADR-0004](adr/0004-representacao-int32.md) | 2026-06-18 | — |
| 5 | Unificação de `toString` e `toUnsignedString` com `radix=10` (sobrecargas Java) | [ADR-0005](adr/0005-unificacao-tostring.md) | 2026-06-18 | — |
| 6 | Helpers IEEE 754 em `JFloat` para `compare`, `max` e `min` | [ADR-0006](adr/0006-representacao-float32.md) | 2026-06-19 | — |
| 7 | Unificação de `toString` instância/estático em `JFloat` via descriptor | [ADR-0007](adr/0007-unificacao-tostring-jfloat.md) | 2026-06-19 | — |
| 8 | Expressões regulares em `JString` via módulo `re` (não `java.util.regex`) | [ADR-0008](adr/0008-regex-python-re-jstring.md) | 2026-06-19 | — |
| 9 | Unificação de `int`/`long`, `double`/`float`, e `valueOf(Object)` retorna `"null"` no `JString` | [ADR-0009](adr/0009-adapt-metodos-estaticos.md) | 2026-06-21 | — | 

---

> **Nota:** Este arquivo não substitui os ADRs. Serve apenas como índice rápido de consulta.
