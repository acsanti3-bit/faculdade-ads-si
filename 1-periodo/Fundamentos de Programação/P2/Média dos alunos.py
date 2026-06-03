notas = [
    [7.0, 8.5, 6.0],
    [9.0, 9.5, 10.0],
    [5.0, 4.0, 7.5]
]

for i in range(len(notas)):

    soma = sum(notas[i])
    quantidade = len(notas[i])
    media = soma / quantidade

    if media >= 7:
        status = "Aprovado"
    else:
        status = "Reprovado"

    print(f"Aluno {i+1}: Média = {media:.2f} - {status}")