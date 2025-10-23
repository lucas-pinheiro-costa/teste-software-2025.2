print("\n=== CLASSIFICAÇÃO DE TRIÂNGULOS ===\n")

def classificar_triangulo(L1, L2, L3):
    # Verificações feitas: 
    # --- Verificação da condição de existência de um triângulo ---
    # A soma de dois lados quaisquer deve ser sempre maior que o terceiro lado.
    if not all(isinstance(x, int) for x in [L1, L2, L3]):
        return "ERRO: Por favor, insira apenas números inteiros válidos."
    if L1 <= 0 or L2 <= 0 or L3 <= 0:
        return "ERRO: Os valores fornecidos não podem formar um triângulo."
    if ((L1 + L2) > L3) and ((L1 + L3) > L2) and ((L2 + L3) > L1):
        # --- Lógica de classificação ---
        if  L1 == L2 and L2 == L3:
            return "O triângulo é EQUILÁTERO (todos os lados são iguais)."
        elif L1 == L2 or L1 == L3 or L2 == L3:
            return "O triângulo é ISÓSCELES (possui dois lados iguais)."
        else:
            return "O triângulo é ESCALENO (todos os lados são diferentes)."
    else:
        return "ERRO: Os valores fornecidos não podem formar um triângulo."

# Testes automáticos para cada caso listado

def rodar_testes():
    testes = [
        # 1. Triângulo escaleno válido
        ((3, 4, 5), "O triângulo é ESCALENO (todos os lados são diferentes)."),
        # 2. Triângulo equilátero válido
        ((5, 5, 5), "O triângulo é EQUILÁTERO (todos os lados são iguais)."),
        # 3. Triângulo isósceles válido
        ((4, 4, 5), "O triângulo é ISÓSCELES (possui dois lados iguais)."),
        # 4. Permutação dos lados iguais do isósceles
        ((3, 3, 4), "O triângulo é ISÓSCELES (possui dois lados iguais)."),
        ((3, 4, 3), "O triângulo é ISÓSCELES (possui dois lados iguais)."),
        ((4, 3, 3), "O triângulo é ISÓSCELES (possui dois lados iguais)."),
        # 5. Um dos valores é zero
        ((0, 4, 5), "ERRO: Os valores fornecidos não podem formar um triângulo."),
        # 6. Um dos valores é negativo
        ((-3, 4, 5), "ERRO: Os valores fornecidos não podem formar um triângulo."),
        # 7. Soma de dois lados igual ao terceiro (não forma triângulo)
        ((2, 2, 4), "ERRO: Os valores fornecidos não podem formar um triângulo."),
        ((4, 2, 2), "ERRO: Os valores fornecidos não podem formar um triângulo."),
        ((2, 4, 2), "ERRO: Os valores fornecidos não podem formar um triângulo."),
        # 8. Soma de dois lados menor que o terceiro (não forma triângulo)
        ((1, 2, 4), "ERRO: Os valores fornecidos não podem formar um triângulo."),
        ((4, 1, 2), "ERRO: Os valores fornecidos não podem formar um triângulo."),
        ((2, 4, 1), "ERRO: Os valores fornecidos não podem formar um triângulo."),
        # 9. Menos entradas do que o esperado (simulado por None)
        ((3, 4, None), "ERRO: Por favor, insira apenas números inteiros válidos."),
        # 10. Saída esperada especificada em cada teste
    ]
    for i, (entrada, esperado) in enumerate(testes, 1):
        try:
            resultado = classificar_triangulo(*entrada)
        except Exception:
            resultado = "ERRO: Por favor, insira apenas números inteiros válidos."
        print(f"Teste {i}: entrada={entrada} | esperado={esperado} | resultado={resultado} | {'OK' if resultado == esperado else 'FALHA'}")

if __name__ == "__main__":
    rodar_testes()
