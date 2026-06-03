def eh_palindromo(palavra):

    return palavra == palavra[::-1]

palavras = []

palindromos = []

for i in range(10):

    palavra = input("Digite uma palavra: ")

    palavras.append(palavra)

for palavra in palavras:

    if eh_palindromo(palavra):

        palindromos.append(palavra)

print("Palíndromos:", palindromos)