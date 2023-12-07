# Inicializa os vetores
numeros = []
pares = []
impares = []


for _ in range(20):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

    # Classifica os números em pares e ímpares
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# Imprime os vetores
print("\nTodos os números:", numeros)
print("Números pares:", pares)
print("Números ímpares:", impares)
