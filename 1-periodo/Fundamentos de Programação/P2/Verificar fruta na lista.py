frutas = ["maçã", "banana", "uva", "laranja", "abacaxi"]
fruta = input("Digite uma fruta: ").lower()

if fruta in frutas:
    print("Fruta encontrada!")
else:
    print("Fruta não encontrada!")