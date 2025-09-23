# Determine os casos de teste para o problema abaixo usando a análise do valor limite:
# o cálculo do desconto por dependente é feito da seguinte forma: a entrada é a idade do dependente que deve estar restrita ao intervalo [0..24]. Para dependentes até 12 anos (inclusive) o desconto é de 15%. Entre 13 e 18 (inclusive) o desconto é de 12%. Dos 19 aos 21 (inclusive) o desconto é de 5% e dos 22 aos 24 de 3%...

# Casos favoráveis (dentro dos limites)
# Idade = 0 (limite inferior absoluto): desconto = 15%
# Idade = 12 (limite superior do primeiro intervalo): desconto = 15%
# Idade = 13 (limite inferior do segundo intervalo): desconto = 12%
# Idade = 18 (limite superior do segundo intervalo): desconto = 12%
# Idade = 19 (limite inferior do terceiro intervalo): desconto = 5%
# Idade = 21 (limite superior do terceiro intervalo): desconto = 5%
# Idade = 22 (limite inferior do quarto intervalo): desconto = 3%
# Idade = 24 (limite superior absoluto): desconto = 3%

# Casos desfavoráveis (fora dos limites)
# Idade = -1 (abaixo do limite inferior): erro
# Idade = 25 (acima do limite superior): erro

# --- Casos nos pontos de transição ---
# Idade = 12 (15%) e 13 (12%) — transição de faixa
# Idade = 18 (12%) e 19 (5%) — transição de faixa
# Idade = 21 (5%) e 22 (3%) — transição de faixa

def desconto_dependente(idade):
    if 0 <= idade <= 12:
        return 15
    elif 13 <= idade <= 18:
        return 12
    elif 19 <= idade <= 21:
        return 5
    elif 22 <= idade <= 24:
        return 3
    else:
        return 'erro'

# Casos de teste de valor limite
casos_teste = [
    # Favoráveis
    (0, 15),
    (12, 15),
    (13, 12),
    (18, 12),
    (19, 5),
    (21, 5),
    (22, 3),
    (24, 3),
    # Desfavoráveis
    (-1, 'erro'),
    (25, 'erro'),
    # Pontos de transição
    (12, 15),
    (13, 12),
    (18, 12),
    (19, 5),
    (21, 5),
    (22, 3),
]

def rodar_testes():
    print("Testes de valor limite para desconto por dependente:")
    for idade, esperado in casos_teste:
        resultado = desconto_dependente(idade)
        status = 'OK' if resultado == esperado else 'FALHA'
        print(f"Idade: {idade:>2} | Esperado: {esperado}% | Resultado: {resultado}% | {status}")

if __name__ == "__main__":
    rodar_testes()