print("\n=== CLASSIFICAÇÃO DE TRIÂNGULOS ===\n")

try:
    L1 = int(input("\tDigite o valor do primeiro lado: "))
    L2 = int(input("\tDigite o valor do segundo lado: "))
    L3 = int(input("\tDigite o valor do terceiro lado: "))
    # Verificações feitas: 

    # --- Verificação da condição de existência de um triângulo ---
    # A soma de dois lados quaisquer deve ser sempre maior que o terceiro lado.
    if ((L1 + L2) > L3) and ((L1 + L3) > L2) and ((L2 + L3) > L1):
        
        print("\n--- Classificação ---")
        # --- Lógica de classificação ---
        if  L1 == L2 and L2 == L3:
            print("O triângulo é EQUILÁTERO (todos os lados são iguais).")
        elif    L1 == L2 or L1 == L3 or L2 == L3:
            print("O triângulo é ISÓSCELES (possui dois lados iguais).")
        else:
            print("O triângulo é ESCALENO (todos os lados são diferentes).")

    else:
        print("\nERRO: Os valores fornecidos não podem formar um triângulo.")

except ValueError:
    print("\nERRO: Por favor, insira apenas números inteiros válidos.")




'''
Fazer uma lista de testes para validar cada um dos pontos abordados anteriormente:

1. Há um teste para identificar um triângulo escaleno válido?
2. Há um teste para identificar um triângulo equilátero válido?
3. Há um teste para identificar um triângulo isósceles válido?
4. Para o triângulo isósceles, foi testado a permutação dos dois valores iguais? Ex. um teste como (3, 3, 4); (3, 4, 3); (4, 3, 3).
5. Foi testado uma ocorrência em que um dos valores é zero?
6. Foi testado uma ocorrência em que um dos valores é negativo?
7. Foi testado uma ocorrência em que os três lados são positivos e a soma de dois dos lados é igual ao terceiro lado? Houve uma permutação desses valores?
8. Foi testado uma ocorrência em que os três lados são positivos e a soma de dois dos lados é menor do que o terceiro lado? Houve uma permutação desses valores?
9. Foi testado uma ocorrência em que houveram menos entradas do que o esperado?
10. Para cada teste você especificou a saída esperada do programa?

'''