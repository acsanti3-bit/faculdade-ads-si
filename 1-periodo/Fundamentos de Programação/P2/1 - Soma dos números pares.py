numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma_pares = 0

for numero in numeros:
    if numero % 2 == 0:
        soma_pares = soma_pares + numero

print("A soma dos números pares é igual a:", soma_pares)