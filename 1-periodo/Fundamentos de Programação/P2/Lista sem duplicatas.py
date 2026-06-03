lista = [1, 5, 2, 8, 3, 5, 1, 9, 2]

nova_lista = []

for numero in lista:

    if numero not in nova_lista:

        nova_lista.append(numero)

print("Lista original:", lista)
print("Lista sem duplicatas:", nova_lista)