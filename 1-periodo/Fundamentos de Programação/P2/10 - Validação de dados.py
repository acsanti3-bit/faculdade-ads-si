nome = input("Digite o nome: ")

if len(nome) <= 3:
    print("Nome inválido")

idade = int(input("Digite a idade: "))

if idade < 0 or idade > 150:
    print("Idade inválida")

salario = float(input("Digite o salário: "))

if salario <= 0:
    print("Salário inválido")

sexo = input("Digite o sexo (f/m): ").lower()

if sexo not in ["f", "m"]:
    print("Sexo inválido")

estado = input("Digite o estado civil (s/c/v/d): ").lower()

if estado not in ["s", "c", "v", "d"]:
    print("Estado civil inválido")

print("Dados cadastrados!")