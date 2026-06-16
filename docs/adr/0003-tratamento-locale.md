# ADR-0003 — Tratamento de Locale

**Status:** Aceito  
**Data:** 2026-06-14  
**Autores:** Equipe GCS 2026.1

---

## Contexto

`java.lang.String` possui métodos sensíveis a locale, como `toUpperCase(Locale)`, `toLowerCase(Locale)` e `compareToIgnoreCase`. Em Python, a função `locale.setlocale` é global e não thread-safe.

O projeto precisa definir como lidar com locale para manter comportamento previsível nos testes e permitir personalização.

## Decisão

Adotar a seguinte estratégia em camadas:

1. **Padrão:** `JString` usa a API Python padrão (`str.upper()`, `str.lower()`) sem configurar locale explicitamente — comportamento equivalente ao `Locale.ROOT` do Java.
2. **Configuração por variável de ambiente:** Se a variável `JAVALANG_LOCALE` estiver definida (ex: `pt_BR.UTF-8`), os métodos sensíveis a locale chamarão `locale.setlocale` no início da operação e restaurarão o valor anterior ao final.
3. **Testes:** os testes não devem depender de locale do sistema; usam o padrão (sem `JAVALANG_LOCALE`).

## Alternativas consideradas

| Opção | Prós | Contras |
|-------|------|---------|
| `locale.setlocale` global | Simples | Não thread-safe; afeta toda a aplicação |
| Parâmetro `locale` em cada método | Fiel à API Java | Aumenta a superfície da API; verboso |
| Ignorar locale completamente | Simples | Diverge de comportamentos Java para línguas não-ASCII |
| Variável de ambiente (adotado) | Sem impacto na API; configurável | Requer documentação clara |

## Consequências

- **Positivas:** API limpa; testes determinísticos por padrão; comportamento configurável sem alterar código.
- **Negativas:** operações com locale não são thread-safe quando `JAVALANG_LOCALE` está definida.
- Documentar a limitação de thread-safety no `README.md`.
