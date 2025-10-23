def main():
    print("\n=== CLASSIFICAÇÃO DE TRIÂNGULOS ===\n")

    try:
        l1 = int(input("\tDigite o valor do primeiro lado: "))
        l2 = int(input("\tDigite o valor do segundo lado: "))
        l3 = int(input("\tDigite o valor do terceiro lado: "))

        # --- Validação de valores negativos e zeros ---
        if l1 <= 0 or l2 <= 0 or l3 <= 0:
            print("\nERRO: Os lados do triângulo devem ser números inteiros positivos e maiores que zero.")
        # --- Verificação da condição de existência de um triângulo ---
        # A soma de dois lados quaisquer deve ser sempre maior que o terceiro lado.
        elif ((l1 + l2) > l3) and ((l1 + l3) > l2) and ((l2 + l3) > l1):
            print("\n--- Classificação ---")
            if l1 == l2 and l2 == l3:
                print("O triângulo é EQUILÁTERO (todos os lados são iguais).")
            elif l1 == l2 or l1 == l3 or l2 == l3:
                print("O triângulo é ISÓSCELES (possui dois lados iguais).")
            else:
                print("O triângulo é ESCALENO (todos os lados são diferentes).")
        else:
            print("\nERRO: Os valores fornecidos não podem formar um triângulo.")
    except ValueError:
        print("\nERRO: Por favor, insira apenas números inteiros válidos.")

'''Exemplos de condições favoráveis (entradas válidas) para cada critério:
1. Triângulo escaleno válido:
    (2, 3, 4)  # Todos os lados diferentes, usando o número inteiro mínimo (2)

2. Triângulo equilátero válido:
    (1, 1, 1)  # Todos os lados iguais, usando o número inteiro mínimo (1)

3. Triângulo isósceles válido:
    (2, 2, 3)  # Dois lados iguais, usando o número inteiro mínimo (2)

4. Permutação dos lados iguais do isósceles:
    (2, 2, 3), (3, 2, 2), (2, 3, 2) # usando o número inteiro mínimo (2)

5. Um dos valores está abaixo do mínimo (não forma triângulo):
    (1, 4, 6) # 1 (um) é o valor abaixo do mínimo para o triângulo escaleno

6. Soma de dois lados igual ao terceiro (não forma triângulo):
    (2, 2, 4), (4, 2, 2), (2, 4, 2)

7. Soma de dois lados menor que o terceiro (não forma triângulo):
    (1, 2, 4), (4, 1, 2), (2, 4, 1)

8. Menos entradas do que o esperado (erro de entrada):
    (3, 4) ou (3,)'''