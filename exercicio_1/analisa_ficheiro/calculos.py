def calcula_linhas(nome):
    f = open(nome, "r")
    return f.readlines().__len__()


def calcula_carateres(nome):
    f = open(nome, "r")
    return f.read().__len__()


def calcula_palavra_comprida(nome):
    f = open(nome, "r")
    data = f.readlines()
    f.close()
    bigword = ""
    for line in data:
        longest = max(line.split(), key=len)
        if len(longest) > len(bigword):
            bigword = longest
    return bigword


def calcula_ocorrencia_de_letras(nome):
    f = open(nome, "r")
    valor = f.read()
    f.close()

    dict = {}
    for letra in valor:
        if letra not in ['\n', ' ']:
            letra = letra.lower()
            if letra not in dict:
                dict[letra] = 1
            else:
                dict[letra] += 1

    return dict
