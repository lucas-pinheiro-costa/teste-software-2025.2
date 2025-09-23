'''Exercício – Particionamento em Classes de Equivalência e Análise do Valor Limite

1) Considere uma função com duas variáveis de entrada: 'Cliente' e 'Qtd', e uma variável de saída, 'Desconto'. Cliente pode ser do tipo A, B ou C e Qtd pode variar de 1 a 1000. A função calcula Desconto de acordo com as seguintes regras:
    a. Clientes do tipo A não recebem desconto se no de itens comprados for inferior a 10; recebem 5% desconto para compras entre 10 e 99 itens; 10% de desconto acima de 100 itens.
    b. Clientes do tipo B recebem 5% de desconto para compras abaixo de 10 itens; 15% de desconto entre 10 e 99 itens; 25% de desconto acima de 100 itens.
    c. Clientes do tipo C não recebem desconto se no de itens comprados for inferior a 10; 20% de desconto entre 10 e 99 itens; 25% de desconto acima de 100 itens.
** Elabore os casos de testes necessários para testar a função acima.
'''

def calcula_desconto(cliente, qtd):
    # Validação da quantidade
    '''if not isinstance(qtd, int) or qtd < 1 or qtd > 1000:
        raise ValueError("A quantidade deve ser um inteiro entre 1 e 1000.")'''
    if (qtd < 0):
        raise ValueError("INVÁLIDO: A quantidade não pode ser um valor negativo.")
    elif (qtd == 0):
        raise ValueError("INVÁLIDO: A quantidade não pode ser zero.")
    elif (qtd > 1000):
        raise ValueError("INVÁLIDO: A quantidade não pode ser maior que 1000.")

    # Validação do tipo de cliente
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