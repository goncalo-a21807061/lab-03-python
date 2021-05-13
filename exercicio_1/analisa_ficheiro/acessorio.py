def pede_nome():
    nome = ""
    while True:
        nome = input("Indique o nome do ficheiro: ")
        try:
            f = open(nome + ".txt")
            break
        except OSError:
            pass
    return nome + ".txt"


def gera_nome(nome, data):
    nome = nome.split(".")
    ficheiro = open(f"{nome[0]}.json", "w")
    ficheiro.write(str(data))
    ficheiro.close()
    return nome[0] + ".json"
