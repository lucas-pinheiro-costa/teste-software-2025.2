'''Exercício – Particionamento em Classes de Equivalência e Análise do Valor Limite

1) Considere uma função com duas variáveis de entrada: 'Cliente' e 'Qtd', e uma variável de saída, 'Desconto'. Cliente pode ser do tipo A, B ou C e Qtd pode variar de 1 a 1000. A função calcula Desconto de acordo com as seguintes regras:
    a. Clientes do tipo A não recebem desconto se no de itens comprados for inferior a 10; recebem 5% desconto para compras entre 10 e 99 itens; 10% de desconto acima de 100 itens.
    b. Clientes do tipo B recebem 5% de desconto para compras abaixo de 10 itens; 15% de desconto entre 10 e 99 itens; 25% de desconto acima de 100 itens.
    c. Clientes do tipo C não recebem desconto se no de itens comprados for inferior a 10; 20% de desconto entre 10 e 99 itens; 25% de desconto acima de 100 itens.
** Elabore os casos de testes necessários para testar a função acima.

O comando para rodar os testes é:
```python
python -m unittest test_q01_descontoCliente.py
```

'''

def calcula_desconto(cliente, qtd):
    if cliente == 'A':
        if qtd < 10:
            return 0.0
        elif 10 <= qtd <= 99:
            return 0.05
        elif qtd >= 100:
            return 0.10
    elif cliente == 'B':
        if qtd < 10:
            return 0.05
        elif 10 <= qtd <= 99:
            return 0.15
        elif qtd >= 100:
            return 0.25
    elif cliente == 'C':
        if qtd < 10:
            return 0.0
        elif 10 <= qtd <= 99:
            return 0.20
        elif qtd >= 100:
            return 0.25
    else:
        raise ValueError('Tipo de cliente inválido')

