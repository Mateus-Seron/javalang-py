# ADR-0008 — Expressões regulares em `JString` via módulo `re`

**Status:** Aceito | **Data:** 2026-06-19 | **Autores:** Equipe GCS 2026.1

---

## Contexto

Em Java SE 8, `java.lang.String` delega operações com regex a `java.util.regex.Pattern` e
`Matcher` (`matches`, `replaceFirst`, `replaceAll`, `split`).

Python não possui `Pattern`/`Matcher` na stdlib com API idêntica. Reimplementar o motor Java em
Python está fora do escopo acadêmico do projeto.

## Decisão

Os métodos de **Operações de Expressões Regulares** em `javalang/jstring.py` usam o módulo
`re` da biblioteca padrão:

| Método Java | Implementação Python |
|-------------|----------------------|
| `matches(String regex)` | `re.fullmatch(regex, self.value)` |
| `replaceFirst(String, String)` | `re.sub(..., count=1)` → retorna `JString` |
| `replaceAll(String, String)` | `re.sub(...)` → retorna `JString` |
| `split(String regex)` | `split(regex, limit=0)` — ver abaixo |
| `split(String regex, int limit)` | `re.split` + regras de `limit` Java |

Sobrecargas de `split` ficam em um único método com `limit=0` opcional (padrão do
[ADR-0005](0005-unificacao-tostring.md)).

Regras de `split` emuladas além do `re.split`:

- **`limit == 0`:** descarta strings vazias finais (comportamento de `split(regex)` Java).
- **`limit == 1`:** retorna a string inteira em um único elemento.
- **`limit > 1`:** no máximo `limit - 1` divisões (`maxsplit=limit - 1`).
- **`limit < 0`:** divide tudo e mantém vazios finais.

Regex inválida levanta `ValueError("PatternSyntaxException")`, alinhado às demais exceções Java
simuladas no pacote.

## Limitações conhecidas

- Sintaxe de regex e flags podem divergir de `Pattern` em casos avançados.
- Referências de grupo na *replacement* usam convenção Python (`\1`), não `$1` do Java.
- `split` com padrão vazio ou look-behind complexo pode diferir do JDK — testes cobrem casos
  simples (delimitador literal, `limit`, descarte de trailing empty).

## Consequências

- **Positivas:** zero dependência externa; implementação curta e testável.
- **Negativas:** fidelidade 100% ao JDK não garantida fora dos casos documentados nos testes.
