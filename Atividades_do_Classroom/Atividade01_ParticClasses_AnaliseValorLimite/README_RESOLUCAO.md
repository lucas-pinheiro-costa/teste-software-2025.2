# Resolução dos exercícios de Particionamento em Classes de Equivalência e Análise do Valor Limite

## Exercício 1: Desconto para Clientes

```python
def calcula_desconto(cliente, qtd):
    if (qtd < 0):
        raise ValueError("INVÁLIDO: A quantidade não pode ser um valor negativo.")
    elif (qtd == 0):
        raise ValueError("INVÁLIDO: A quantidade não pode ser zero.")
    elif (qtd > 1000):
        raise ValueError("INVÁLIDO: A quantidade não pode ser maior que 1000.")

    if cliente not in ('A', 'B', 'C'):
        raise ValueError("INVÁLIDO: tipo de cliente está incorreto. Aceito apenas 'A', 'B' ou 'C'.")

    if cliente == 'A':
        if qtd < 10:
            return "VÁLIDO: O desconto é de 0%."
        elif 10 <= qtd <= 99:
            return "VÁLIDO: O desconto é de 5%."
        elif qtd >= 100:
            return "VÁLIDO: O desconto é de 10%."
    elif cliente == 'B':
        if qtd < 10:
            return "VÁLIDO: O desconto é de 5%."
        elif 10 <= qtd <= 99:
            return "VÁLIDO: O desconto é de 15%."
        elif qtd >= 100:
            return "VÁLIDO: O desconto é de 25%."
    elif cliente == 'C':
        if qtd < 10:
            return "VÁLIDO: O desconto é de 0%."
        elif 10 <= qtd <= 99:
            return "VÁLIDO: O desconto é de 20%."
        elif qtd >= 100:
            return "VÁLIDO: O desconto é de 25%."
```

A função `calcula_desconto` foi criada para calcular o desconto de acordo com o tipo de cliente e a quantidade de itens comprados. O código realiza validações e retorna mensagens informativas:

### Validação da quantidade
```python
if (qtd < 0):
    raise ValueError("INVÁLIDO: A quantidade não pode ser um valor negativo.")
elif (qtd == 0):
    raise ValueError("INVÁLIDO: A quantidade não pode ser zero.")
elif (qtd > 1000):
    raise ValueError("INVÁLIDO: A quantidade não pode ser maior que 1000.")
```

### Validação do tipo de cliente
```python
if cliente not in ('A', 'B', 'C'):
    raise ValueError("INVÁLIDO: tipo de cliente está incorreto. Aceito apenas 'A', 'B' ou 'C'.")
```

### Cálculo do desconto
```python
if cliente == 'A':
    if qtd < 10:
        return "VÁLIDO: O desconto é de 0%."
    elif 10 <= qtd <= 99:
        return "VÁLIDO: O desconto é de 5%."
    elif qtd >= 100:
        return "VÁLIDO: O desconto é de 10%."
# ...lógica semelhante para B e C...
```

## Exercício 2: Inclusão de contato na agenda telefônica

```python
agenda = []

def incluir_contato(nome, telefone, email):
    if telefone is None or not str(telefone).isdigit():
        raise ValueError("INVÁLIDO: O contato deve possuir um número telefônico apenas com dígitos.")
    if len(str(telefone)) < 8:
        raise ValueError("INVÁLIDO: O número telefônico deve ter entre 8 e 15 dígitos.")
    if len(str(telefone)) > 15:
        raise ValueError("INVÁLIDO: O número telefônico deve ter entre 8 e 15 dígitos.")
    for contato in agenda:
        if contato['telefone'] == telefone:
            raise ValueError("INVÁLIDO: Já existe um contato com esse número telefônico.")

    import re
    email_regex = r'^[A-Za-z0-9]+@[A-Za-z]+\.[A-Za-z]$'
    if not re.match(email_regex, email):
        raise ValueError("INVÁLIDO: O email deve estar no formato texto@dominio.extensão e seguir as regras de formatação.")

    agenda.append({'nome': nome, 'telefone': telefone, 'email': email})
    return "VÁLIDO: Contato adicionado com sucesso."
```

A função `incluir_contato` foi desenvolvida para adicionar contatos à agenda, validando telefone e email conforme as regras do enunciado:

### Validação do telefone
```python
if telefone is None or not str(telefone).isdigit():
    raise ValueError("INVÁLIDO: O contato deve possuir um número telefônico apenas com dígitos.")
if len(str(telefone)) < 8:
    raise ValueError("INVÁLIDO: O número telefônico deve ter pelo menos 8 dígitos.")
if len(str(telefone)) > 15:
    raise ValueError("INVÁLIDO: O número telefônico não pode ter mais que 15 dígitos.")
for contato in agenda:
    if contato['telefone'] == telefone:
        raise ValueError("INVÁLIDO: Já existe um contato com esse número telefônico.")
```

### Validação do email
```python
import re
email_regex = r'^[A-Za-z0-9]+@[A-Za-z]+\.[A-Za-z]{2,6}$'
if not re.match(email_regex, email):
    raise ValueError("INVÁLIDO: O email deve estar no formato texto@dominio.extensão e seguir as regras de formatação.")
```

### Adição do contato
```python
agenda.append({'nome': nome, 'telefone': telefone, 'email': email})
return "VÁLIDO: Contato adicionado com sucesso."
```
