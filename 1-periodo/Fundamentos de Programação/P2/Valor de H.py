n = int(input("Digite o número de termos: "))

h = 0

for i in range(1, n + 1):

    h = h + (1 / i)

print("Valor de H:", h)