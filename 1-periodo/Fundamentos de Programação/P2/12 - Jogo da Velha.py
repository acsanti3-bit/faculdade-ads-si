tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def verificar_vitoria(tab):

    for linha in tab:

        if linha[0] == linha[1] == linha[2] != " ":
            return linha[0]

    for i in range(3):

        if tab[0][i] == tab[1][i] == tab[2][i] != " ":
            return tab[0][i]

    if tab[0][0] == tab[1][1] == tab[2][2] != " ":
        return tab[0][0]

    if tab[0][2] == tab[1][1] == tab[2][0] != " ":
        return tab[0][2]

    return None

for jogada in range(9):

    simbolo = input("Digite X ou O: ")

    linha = int(input("Linha: "))
    coluna = int(input("Coluna: "))

    tabuleiro[linha][coluna] = simbolo

    vencedor = verificar_vitoria(tabuleiro)

    for linha_tab in tabuleiro:
        print(linha_tab)

    if vencedor:
        print("Vencedor:", vencedor)
        break