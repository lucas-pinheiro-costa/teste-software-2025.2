print("\n=== CLASSIFICAÇÃO DE TRIÂNGULOS ===\n")

try:
    L1 = int(input("\tDigite o valor do primeiro lado: "))
    L2 = int(input("\tDigite o valor do segundo lado: "))
    L3 = int(input("\tDigite o valor do terceiro lado: "))

    # --- Verificação da condição de existência de um triângulo ---
    # A soma de dois lados quaisquer deve ser sempre maior que o terceiro lado.
    if ((L1 + L2) > L3) and ((L1 + L3) > L2) and ((L2 + L3) > L1):
        
        print("\n--- Classificação ---")
        # --- Lógica de classificação ---
        if  L1 == L2 and L2 != L3:  #Mutante aqui
            print("O triângulo é EQUILÁTERO (todos os lados são iguais).")
        elif    L1 == L2 or L1 == L3 or L2 == L3:
            print("O triângulo é ISÓSCELES (possui dois lados iguais).")
        else:
            print("O triângulo é ESCALENO (todos os lados são diferentes).")

    else:
        print("\nERRO: Os valores fornecidos não podem formar um triângulo.")

except ValueError:
    print("\nERRO: Por favor, insira apenas números inteiros válidos.")