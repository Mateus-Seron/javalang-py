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

| Sprint        | Artefato                         | Membro                                                                | Ferramenta      | Descrição do uso                                                                                                                              |
|---------------|----------------------------------|------------------------------------------------------------------------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Setup         | Estrutura inicial do repositório | Mateus Seron | Composer | Apoio na geração da estrutura inicial, documentação, configuração de ambiente, automações, planejamento e organização dos artefatos do projeto. |
| v0.2-jinteger | Implementação e documentação     | Enzo Euvine, João Braga, Lucas Gabriel, Mateus Seron, Mariana Paulino | ChatGPT, Claude | Apoio à implementação, revisão, documentação, testes, correções e organização dos artefatos produzidos durante a sprint.                       |
| v0.3-jfloat   | Implementação e documentação     | Enzo Euvine, João Braga, Lucas Gabriel, Mateus Seron, Mariana Paulino | ChatGPT, Claude | Apoio à implementação, revisão, documentação, testes, correções e organização dos artefatos produzidos durante a sprint.                       |
| v0.4-jstring  | Implementação e documentação     | Enzo Euvine, João Braga, Lucas Gabriel, Mateus Seron, Mariana Paulino | ChatGPT, Claude | Apoio à implementação, revisão, documentação, testes, correções e organização dos artefatos produzidos durante a sprint.                       |

---

## Prompts representativos

### Planejamento e estruturação

```text
Auxilie na organização do projeto, estrutura do repositório,
documentação, configuração de ferramentas e definição dos artefatos
necessários para atender aos requisitos da disciplina.
```

### Implementação

```text
Auxilie na implementação dos métodos da API Java SE 8 em Python,
preservando o contrato público da especificação e os nomes originais
dos métodos sempre que possível.
```

---

## Métodos implementados com auxílio de IA

| Classe   | Método                                        | Membro                                                                | Observação                                              |
| -------- | --------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------- |
| JInteger | Métodos implementados na sprint v0.2-jinteger | Enzo Euvine, João Braga, Lucas Gabriel, Mateus Seron, Mariana Paulino | Implementação, revisão e documentação com auxílio de IA |
| JFloat   | Métodos implementados na sprint v0.3-jfloat   | Enzo Euvine, João Braga, Lucas Gabriel, Mateus Seron, Mariana Paulino | Implementação, revisão e documentação com auxílio de IA |
| JString  | Métodos implementados na sprint v0.4-jstring  | Enzo Euvine, João Braga, Lucas Gabriel, Mateus Seron, Mariana Paulino | Implementação, revisão e documentação com auxílio de IA |


---

## Compromisso

Nenhum código gerado por IA será submetido sem revisão e compreensão do membro responsável.
A ausência de declaração, se identificada, será tratada como omissão grave conforme o enunciado.
