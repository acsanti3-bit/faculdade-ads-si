numeros = []

for i in range(15):

    numero = int(input(f"Digite o {i+1}º número: "))

    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)

print("Maior número:", maior)
print("Posição:", numeros.index(maior))

print("Menor número:", menor)
print("Posição:", numeros.index(menor))