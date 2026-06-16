# Guia de Contribuição

Leia este documento **antes** de abrir issues, criar branches ou enviar pull requests.
As regras abaixo são extraídas diretamente do enunciado do Trabalho Prático GCS 2026.1 (§4.2 e §4.3).

---

## Fluxo de trabalho (GitHub Flow — §4.2)

Existe apenas uma branch permanente: **`main`**, que deve estar sempre em estado estável e auditável.

| Prefixo | Uso | Exemplo |
|---------|-----|---------|
| `feature/<slug>` | Nova funcionalidade | `feature/jstring-substring` |
| `fix/<slug>` | Correção de bug | `fix/jinteger-parseint-radix` |
| `docs/<slug>` | Documentação | `docs/adaptacao-intern` |
| `ci/<slug>` | Alterações de pipeline | `ci/adicionar-cobertura` |

### Regras obrigatórias (§4.2)

1. A branch `main` deve estar protegida em **Settings → Branches**.
2. Nenhum commit direto em `main` é permitido após o primeiro sprint.
3. Toda funcionalidade nasce de uma **issue** e é desenvolvida em um branch com nome descritivo.
4. Commits devem referenciar a issue que os originou (ver formato abaixo).
5. Cada PR requer **pelo menos 1 aprovação** de outro membro além do autor. Auto-aprovação é vedada.
6. Ao longo do projeto, pelo menos **3 conflitos de merge reais** devem ser resolvidos e evidenciados no histórico.

```bash
git checkout main
git pull origin main
git checkout -b feature/minha-feature
# ... trabalhe ...
git push origin feature/minha-feature
# Abra PR de feature/minha-feature → main
```

---

## Padrão de commits (Conventional Commits + refs de issue — §4.2)

```
<tipo>(<escopo>): <descrição curta> — refs #<número da issue>

[corpo opcional]
```

**Tipos aceitos:** `feat`, `fix`, `refactor`, `test`, `docs`, `chore`, `ci`

**Exemplos exatos do enunciado:**

```
feat: add JString.substring(int) — refs #14
fix: corrigir overflow em JInteger.parseInt com valor negativo — refs #22
docs: registrar adaptação de String.intern() — refs #9
```

### Limites obrigatórios (§10, regra 34)

- Um commit **não pode ter mais de 3 métodos implementados**.
- Um PR **não pode conter mais de 7 métodos implementados**.
- Regra análoga vale para casos de teste.

---

## Controle de mudanças — rastreabilidade completa (§4.3)

1. Toda mudança não-trivial nasce em uma **issue específica** — não genérica.
   - ❌ "implementar string"
   - ✅ "implementar JString.substring(int, int) e seus casos-limite"
2. Cada issue recebe **labels** apropriadas: `feature`, `bug`, `docs`, `decision`, `good-first-issue`, `refactor`.
3. Cada issue é atribuída a um **responsável** (assignee) e a um **milestone** (baseline correspondente).
4. O PR que resolve a issue deve conter `Closes #N` na descrição, além de resumo do impacto.
5. O **code review deve produzir discussão registrada** — PRs aprovados sem comentários substantivos serão investigados.

---

## Configuração do ambiente local

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
# Com cobertura:
pytest --cov=javalang --cov-report=term-missing
```

---

## Lint e formatação

```bash
ruff check .
ruff format .
```

O CI rejeita PRs com erros de lint ou testes em vermelho.

---

## Uso de IA generativa (§10, regra 33)

Uso de IA é permitido, desde que declarado em [`docs/uso-de-ia.md`](docs/uso-de-ia.md) **antes do merge do PR**.
Uso não declarado, se identificado, será tratado como omissão grave.

---

## Anti-atalhos (§10)

| Regra | Descrição |
|-------|-----------|
| §10/28 | Histórico concentrado em ≤ 72 h antes da entrega → penalização severa |
| §10/29 | Force push em `main` → vedado |
| §10/30 | Auto-aprovação de PR → não conta para avaliação |
| §10/32 | PR único com milhares de linhas perto da entrega → tratado como ausência de processo |
| §10/34 | Mais de 3 métodos por commit / mais de 7 por PR → vedado |
