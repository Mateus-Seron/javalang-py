# javalang-py

Implementação em Python das classes `String`, `Integer` e `Float` da especificação Java SE 8 — GCS 2026.1.

---

## Visão geral

O pacote `javalang` expõe três classes imutáveis que espelham a API de `java.lang`:

| Classe Python | Equivalente Java | Referência |
|--------------|-----------------|-----------|
| `JString` | `java.lang.String` | [Java SE 8 Docs](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html) |
| `JInteger` | `java.lang.Integer` | [Java SE 8 Docs](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html) |
| `JFloat` | `java.lang.Float` | [Java SE 8 Docs](https://docs.oracle.com/javase/8/docs/api/java/lang/Float.html) |

---

## Instalação (desenvolvimento)

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate

pip install -e ".[dev]"
```

---

## Executando os testes

```bash
pip install -e ".[dev]"    # instala pytest + ruff
ruff check . --fix
ruff format .
ruff check .
ruff format --check .
pytest
```

Para cobertura:

```bash
pytest --cov=javalang --cov-report=term-missing
```

---

## Adaptações

Esta implementação diverge da especificação Java SE 8 nos seguintes pontos, cada um formalizado como ADR:

| ADR | Decisão | Resumo |
|-----|---------|--------|
| [ADR-0001](docs/adr/0001-nomenclatura-classes.md) | Prefixo `J` nas classes | Evita colisão com tipos nativos Python (`str`, `int`, `float`) |
| [ADR-0002](docs/adr/0002-modelo-ramificacao.md) | GitHub Flow | Branch curto → PR → merge em `main`; adequado ao escopo acadêmico |
| [ADR-0003](docs/adr/0003-tratamento-locale.md) | Locale via variável de ambiente | `JAVALANG_LOCALE` configura locale; padrão equivale a `Locale.ROOT` |
| [ADR-0004](docs/adr/0004-representacao-int32.md) | Normalização de 32 bits em `JInteger` | Python `int` é arbitrário; Java `int` é fixo em 32 bits |
| [ADR-0005](docs/adr/0005-unificacao-tostring.md) | Sobrecargas com `radix` em `JInteger` | Python não tem sobrecarga; `toString` e `toUnsignedString` usam `radix=10` |
| [ADR-0006](docs/adr/0006-representacao-float32.md) | Semântica IEEE 754 em `JFloat` | Normalização float32, bits brutos vs canônicos, `compare`/`hashCode`/`equals` |
| [ADR-0007](docs/adr/0007-unificacao-tostring-jfloat.md) | `toString` instância/estático em `JFloat` | Descriptor `_ToString` unifica `toString()` e `toString(float)` |

Veja o índice completo em [`docs/adaptacoes.md`](docs/adaptacoes.md).

### JInteger — representação de 32 bits

Em Java, `int` tem exatamente 32 bits em complemento de dois (`-2³¹` a `2³¹ - 1`).
Em Python, `int` não tem limite de tamanho.

Para métodos bit a bit (`bitCount`, `highestOneBit`, `lowestOneBit`, `numberOfLeadingZeros`,
`numberOfTrailingZeros`), os resultados são normalizados para o intervalo Java via função interna
`_to_int32` em `javalang/jinteger.py`. Sem isso, casos como `highestOneBit(-1)` retornariam
`2147483648` em Python, mas a especificação Java exige `-2147483648` (`Integer.MIN_VALUE`).

Detalhes em [ADR-0004](docs/adr/0004-representacao-int32.md).

### JInteger — sobrecargas unificadas (`toString`, `toUnsignedString`)

Java define `toString(int)` / `toString(int, int radix)` e `toUnsignedString(int)` /
`toUnsignedString(int, int radix)` como métodos distintos. Em Python, cada par fica em um método
com `radix=10` opcional. Detalhes em [ADR-0005](docs/adr/0005-unificacao-tostring.md).

### JFloat — semântica IEEE 754

`Float.compare`, `Float.max`, `Float.min`, `Float.hashCode` e `Float.equals` em Java tratam
`-0.0`, `+0.0` e `NaN` de forma especial. Em `javalang/jfloat.py`:

- `_to_float32` normaliza o valor encapsulado para 32 bits.
- `_float_to_int_bits` (bits brutos) desempata `compare` / `compareTo` (`-0.0` < `+0.0`).
- `_float_to_canonical_int_bits` emula `floatToIntBits` para `hashCode` / `equals` (zeros e NaN
  canônicos).

Detalhes em [ADR-0006](docs/adr/0006-representacao-float32.md).

### JFloat — `toString` instância e estático

Java define `toString()` no wrapper e `toString(float)` como estático. Em Python, o descriptor
`_ToString` expõe ambas as formas sem conflito de nome. Detalhes em
[ADR-0007](docs/adr/0007-unificacao-tostring-jfloat.md).

> **Nota sobre locale e concorrência:** quando `JAVALANG_LOCALE` está definida, operações sensíveis a locale **não são thread-safe** (limitação de `locale.setlocale`). Em cenários multi-thread, deixe a variável não definida.

---

## Estrutura do repositório

```
javalang-py/
├── javalang/               # Pacote principal
├── tests/                  # Testes unitários e de interoperabilidade
├── docs/
│   ├── adr/                # Decisões arquiteturais (ADRs)
│   ├── itens-de-configuracao.md
│   ├── adaptacoes.md
│   └── uso-de-ia.md        # Declaração obrigatória de uso de IA (§10/33)
├── .github/                # CI e templates de issue/PR
├── CONTRIBUTING.md         # Regras de processo (§4.2 e §4.3)
└── pyproject.toml          # Build, dependências e ferramentas
```

---

## Equipe e papéis

| Papel | Responsável |
|-------|-------------|
| Mantenedor | Mateus Miranda Seron |
| Gerente de Configuração | Enzo Euvine Cunha Neves |
| Engenheiro de Qualidade | Mariana Paulino da Silva |
| Desenvolvedor | João Vitor Costa Braga |
| Relator | Lucas Gabriel de Almeida Souza |

---

## Contribuindo

Leia o [`CONTRIBUTING.md`](CONTRIBUTING.md) antes de abrir issues ou pull requests.

---

## Licença

[MIT](LICENSE)
