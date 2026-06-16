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

Veja o índice completo em [`docs/adaptacoes.md`](docs/adaptacoes.md).

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
| Gerente de Configuração | ? |
| Engenheiro de Qualidade | ? |
| Desenvolvedor | ? |
| Relator | ? |

---

## Contribuindo

Leia o [`CONTRIBUTING.md`](CONTRIBUTING.md) antes de abrir issues ou pull requests.

---

## Licença

[MIT](LICENSE)
