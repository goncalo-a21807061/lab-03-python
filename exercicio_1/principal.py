from analisa_ficheiro import *
import json


def main():
    nome = acessorio.pede_nome()
    data = dict()
    data["nr-linhas"] = calculos.calcula_linhas(nome)
    data["nr-caracteres"] = calculos.calcula_carateres(nome)
    data["ocorrencia-letras"] = calculos.calcula_ocorrencia_de_letras(nome)
    data["palavra-comprida"] = calculos.calcula_palavra_comprida(nome)

    data = json.dumps(data)
    print("Ficheiro JSON: " + acessorio.gera_nome(nome, data))
    return


if __name__ == "__main__":
    main()
