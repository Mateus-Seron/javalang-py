# ADR-0009 — Adaptações dos Métodos Estáticos em `JString`

**Status:** Aceito | **Data:** 2026-06-21 | **Autores:** Equipe GCS 2026.1

---

## Contexto

A classe `java.lang.String` possui diversas sobrecargas do método estático `valueOf(...)` para diferentes tipos primitivos e objetos.

Durante a implementação da biblioteca em Python, algumas dessas sobrecargas não puderam ser reproduzidas exatamente devido às diferenças entre os sistemas de tipos das duas linguagens:

* Python não diferencia os tipos inteiros `int` e `long` como ocorre em versões anteriores do Java;
* Python utiliza apenas o tipo `float` para representar números de ponto flutuante, não distinguindo `float` e `double`;
* Em Java, `String.valueOf(Object)` retorna `"null"` quando recebe uma referência nula.

Essas diferenças exigiram adaptações para preservar o comportamento esperado da API Java dentro das limitações da linguagem Python.

## Decisão

Foram adotadas as seguintes adaptações na implementação de `JString.valueOf(...)`:

    * As sobrecargas `valueOf(int)` e `valueOf(long)` foram unificadas em uma única implementação, utilizando o tipo `int` do Python;
    * As sobrecargas `valueOf(float)` e `valueOf(double)` foram unificadas em uma única implementação baseada no tipo `float` do Python;
    * Quando o argumento recebido é `None`, o método retorna a string `"null"`, reproduzindo o comportamento de `String.valueOf(Object)` em Java.

## Implementação resumida:

```python
    @staticmethod
    def valueOfInt(value: int) -> 'JString':
        return JString(str(value))

    @staticmethod
    def valueOfFloat(value: float) -> 'JString':
        return JString(str(value))

    @staticmethod
    def valueOfObject(value: object) -> 'JString':
        if value is None:
            return JString("null")
        return JString(str(value))
```

## Impactos
    * Mantém padrão do Java;
    * Preserva a representação textual esperada para referências nulas;
    * Não é possível distinguir explicitamente chamadas à `int` ou `long` e `float` e `double`.