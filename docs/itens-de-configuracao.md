# Itens de Configuração

Documento produzido no primeiro sprint conforme exigido pelo §4.1 do Trabalho Prático GCS 2026.1.

---

## Critérios de inclusão como IC

Um artefato é tratado como item de configuração quando:

1. É necessário para construir, testar ou documentar o software; **ou**
2. Serve de base para decisões técnicas futuras; **ou**
3. Seu conteúdo precisa ser rastreado entre versões.

---

## Tabela de Itens de Configuração

| ID | Nome do IC | Tipo | Localização | Responsável | Formato | Frequência de mudança | Dependências |
|----|-----------|------|-------------|-------------|---------|----------------------|-------------|
| IC-01 | `pyproject.toml` | Configuração de build | raiz | Mantenedor | TOML | Baixa — apenas em mudanças de dependência ou versão | Nenhuma |
| IC-02 | `javalang/__init__.py` | Código-fonte | `javalang/` | Mantenedor | Python | Baixa — atualizado a cada nova classe integrada | IC-03, IC-04, IC-05 |
| IC-03 | `javalang/jstring.py` | Código-fonte | `javalang/` | Desenvolvedor | Python | Alta — implementação incremental via PRs | IC-02 |
| IC-04 | `javalang/jinteger.py` | Código-fonte | `javalang/` | Desenvolvedor | Python | Alta — implementação incremental via PRs | IC-02 |
| IC-05 | `javalang/jfloat.py` | Código-fonte | `javalang/` | Desenvolvedor | Python | Alta — implementação incremental via PRs | IC-02, IC-04 |
| IC-06 | `tests/test_jstring.py` | Teste | `tests/` | Eng. de Qualidade | Python | Alta — acompanha cada PR de IC-03 | IC-03 |
| IC-07 | `tests/test_jinteger.py` | Teste | `tests/` | Eng. de Qualidade | Python | Alta — acompanha cada PR de IC-04 | IC-04 |
| IC-08 | `tests/test_jfloat.py` | Teste | `tests/` | Eng. de Qualidade | Python | Alta — acompanha cada PR de IC-05 | IC-05 |
| IC-09 | `tests/test_interop.py` | Teste | `tests/` | Eng. de Qualidade | Python | Média — atualizado ao integrar múltiplas classes | IC-03, IC-04, IC-05 |
| IC-10 | `.github/workflows/ci.yml` | CI/CD | `.github/` | Eng. de Qualidade | YAML | Baixa — estável após configuração inicial | IC-01 |
| IC-11 | `docs/adr/` (3 arquivos) | Decisão arquitetural | `docs/adr/` | Gerente de Config. | Markdown | Baixa — nova entrada por decisão formal | Nenhuma |
| IC-12 | `docs/itens-de-configuracao.md` | Documentação de processo | `docs/` | Gerente de Config. | Markdown | Baixa — atualizado a cada novo IC | Todos os ICs |
| IC-13 | `docs/adaptacoes.md` | Documentação de processo | `docs/` | Gerente de Config. | Markdown | Média — atualizado a cada adaptação documentada | IC-11 |
| IC-14 | `README.md` | Documentação | raiz | Mantenedor | Markdown | Média — seção de adaptações e papéis evoluem | IC-11, IC-13 |
| IC-15 | `docs/uso-de-ia.md` | Declaração de processo | `docs/` | Relator | Markdown | Alta — atualizado a cada PR com uso de IA | Todos |
| IC-16 | `CONTRIBUTING.md` | Documentação de processo | raiz | Mantenedor | Markdown | Baixa — estável após o primeiro sprint | Nenhuma |
| IC-17 | `.github/ISSUE_TEMPLATE/` | Processo | `.github/` | Mantenedor | Markdown | Muito baixa | Nenhuma |
| IC-18 | `.github/pull_request_template.md` | Processo | `.github/` | Mantenedor | Markdown | Muito baixa | Nenhuma |

---

## Baselines planejadas

| Baseline | Tag Git | Conteúdo mínimo exigido pelo enunciado | ICs incluídos |
|----------|---------|----------------------------------------|---------------|
| Functional | `v0.1-functional` | Documento de ICs, decisões arquiteturais e plano de implementação aprovados | IC-10 a IC-18 |
| Allocated — JInteger | `v0.2-jinteger` | JInteger completo (ou parcial documentado) + testes verdes | + IC-04, IC-07 |
| Allocated — JFloat | `v0.3-jfloat` | JFloat completo + interoperabilidade com JInteger | + IC-05, IC-08 |
| Allocated — JString | `v0.4-jstring` | JString completo + interoperabilidade com JInteger e JFloat | + IC-03, IC-06, IC-09 |
| Product | `v1.0.0` | Release final, README completo, relatório de status e auditoria | Todos os ICs |

---

## Controle de mudanças

Qualquer alteração em um IC deve:
1. Ser proposta via **issue** com label adequada
2. Referenciar a issue no commit (`refs #N`)
3. Ser implementada em branch dedicado
4. Passar pelo CI e ter **mínimo 1 aprovação** antes do merge
5. Ser documentada no `CHANGELOG.md` após cada baseline
