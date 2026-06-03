A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

linhas_A = len(A)
colunas_A = len(A[0])

linhas_B = len(B)
colunas_B = len(B[0])

if colunas_A != linhas_B:

    print("Não é possível multiplicar")

else:

    resultado = []

    for i in range(linhas_A):

        linha = []

        for j in range(colunas_B):

            soma = 0

            for k in range(colunas_A):

                soma = soma + (A[i][k] * B[k][j])

            linha.append(soma)

        resultado.append(linha)

    print(resultado)