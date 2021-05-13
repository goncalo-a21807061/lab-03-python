from analise_pasta import *
import os


def calcula_tamanho_pasta(pasta):
    soma = 0
    for entry in os.scandir(pasta):
        if entry.is_file():
            soma += os.path.getsize(entry)
        elif entry.is_dir():
            soma += calcula_tamanho_pasta(entry.path)
    return soma



if __name__=="__main__":
    nome = pede_pasta()
    while not os.path.isdir(nome):
        nome = input("Digite um diretório correto:")
        if os.path.isdir(nome):
            break

    tamanho = calcula_tamanho_pasta(nome)
    print(f"Tamanho Total = {tamanho / 1048576} MBytes")