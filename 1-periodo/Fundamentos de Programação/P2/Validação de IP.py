# Função para validar IP
def ip_valido(ip):

    partes = ip.split(".")

    if len(partes) != 4:
        return False

    for parte in partes:

        if not parte.isdigit():
            return False

        numero = int(parte)

        if numero < 0 or numero > 255:
            return False

    return True

# Abrindo arquivo
with open(r"C:\Users\caroo\OneDrive\Área de Trabalho\Facul\faculdade-ads-si\1-periodo\Fundamentos de Programação\P2\ips.txt", "r") as arquivo:

    ips = arquivo.readlines()

validos = []
invalidos = []

# Verificando IPs
for ip in ips:

    ip = ip.strip()

    if ip_valido(ip):

        validos.append(ip)

    else:

        invalidos.append(ip)

# Criando relatório
with open("relatorio.txt", "w") as arquivo:

    arquivo.write("[Endereços válidos:]\n")

    for ip in validos:
        arquivo.write(ip + "\n")

    arquivo.write("\n[Endereços inválidos:]\n")

    for ip in invalidos:
        arquivo.write(ip + "\n")

print("Relatório criado!")