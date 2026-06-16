# ADR-0002 — Modelo de Ramificação (Branching)

**Status:** Aceito  
**Data:** 2026-06-14  
**Autores:** Equipe GCS 2026.1

---

## Contexto

O projeto é de escopo acadêmico, com equipe pequena (≤ 5 integrantes) e ciclo de vida limitado a um semestre. Era necessário escolher um modelo de ramificação que equilibrasse rastreabilidade de mudanças com baixo overhead operacional.

## Decisão

Adotar **GitHub Flow**:

- Existe uma única branch permanente: `main`, que deve sempre estar em estado deployável/auditável.
- Toda mudança (feature, fix, docs, ci) parte de um branch curto criado a partir de `main`.
- O branch é integrado de volta a `main` exclusivamente via **Pull Request** revisado e com CI verde.
- Após o merge, o branch temporário é deletado.

### Convenção de nomenclatura dos branches temporários

| Prefixo | Uso |
|---------|-----|
| `feature/<slug>` | Nova funcionalidade |
| `fix/<slug>` | Correção de bug |
| `docs/<slug>` | Documentação |
| `ci/<slug>` | Alterações de pipeline |

### Regras

1. Nenhum commit direto em `main`.
2. PRs requerem **mínimo 1 aprovação** e CI verde antes do merge.
3. Branches temporários são deletados após o merge.
4. Tags semânticas (`v0.1.0`, `v1.0.0`) marcam baselines diretamente em `main`.

## Alternativas consideradas

| Opção | Motivo de rejeição |
|-------|--------------------|
| Git Flow (com `develop`, `release/`, `hotfix/`) | Overhead de branches permanentes extras desnecessário para equipe pequena e escopo de um semestre |
| Trunk-based development (sem PRs) | Não garante revisão de código; dificulta rastreabilidade exigida pela disciplina |
| GitHub Flow (adotado) | Fluxo simples, amplamente documentado e com suporte nativo no GitHub |

## Consequências

- **Positivas:** fluxo simples, fácil de auditar, integrado com as proteções de branch do GitHub e com o CI.
- **Negativas:** sem branch `develop`, correções urgentes e features seguem o mesmo fluxo — branches de curta duração minimizam esse risco.
