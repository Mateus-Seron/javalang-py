# Declaração de Uso de IA Generativa

> Conforme §10, regra 33 do enunciado do Trabalho Prático GCS 2026.1:
> _"Uso de IA generativa — Permitido para auxílio em implementação técnica, desde que declarado abertamente
> em docs/uso-de-ia.md, com listagem dos métodos onde foi utilizada e dos prompts representativos."_

---

## Política da equipe

A equipe declara abertamente o uso de ferramentas de IA generativa como auxílio. Todo uso deve ser registrado
neste documento antes do merge do PR correspondente. O membro responsável pelo código deve ser capaz de
explicar oralmente qualquer trecho gerado com auxílio de IA.

---

## Registro de uso

| Sprint        | Artefato                         | Membro      | Ferramenta | Descrição do uso                                                                                                       | PR                      |
| ------------- | -------------------------------- | ----------- | ---------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| Setup         | Estrutura inicial do repositório | Mateus Seron |     | Geração da estrutura inicial do projeto, documentação de processo, templates e configuração de CI                      | —                       |
| v0.2-jinteger | Classe JInteger                  | Enzo Euvine | Claude    | Apoio na implementação dos métodos da API Java Integer em Python, elaboração de testes e revisão de código             | #32, #37, #40           |
| v0.2-jinteger | Documentação                     | Enzo Euvine | ChatGPT    | Revisão e atualização de README, templates de issue e documentação do projeto                                          | #36                     |
| v0.3-jfloat   | Classe JFloat                    | Enzo Euvine | ChatGPT    | Apoio na implementação dos métodos da API Java Float, constantes, parsing, formatação e verificações IEEE-754          | #44, #45, #46           |
| v0.4-jstring  | Classe JString                   | Enzo Euvine | ChatGPT    | Apoio na modelagem da classe, organização dos métodos, implementação e revisão de operações de acesso, tamanho e busca | #52, #55, #57, #60, #63 |

---

## Prompts representativos

### Setup — Estrutura inicial

```
Crie a estrutura mínima de um repositório Python para o projeto javalang-py,
conforme o enunciado GCS 2026.1, incluindo pyproject.toml, ci.yml, templates
de issue e PR, ADRs e documentação de itens de configuração.
```

---

## Métodos implementados com auxílio de IA

> _Esta seção será preenchida conforme o desenvolvimento avançar._

| Classe   | Método                                                           | Membro      | Observação                      |
| -------- | ---------------------------------------------------------------- | ----------- | ------------------------------- |
| JInteger | Métodos de operação Aritmetica Estatica e operações de parsing          | Enzo Euvine | Implementação com auxílio de IA |
| JFloat   | Métodos de operações de verificações e pacote de operações de parsing e formatação        | Enzo Euvine | Implementação com auxílio de IA |
| JString  | Métodos de pacote de operações de acesso e tamanho e de operações de busca | Enzo Euvine | Implementação com auxílio de IA |

---

## Compromisso

Nenhum código gerado por IA será submetido sem revisão e compreensão do membro responsável.
A ausência de declaração, se identificada, será tratada como omissão grave conforme o enunciado.
