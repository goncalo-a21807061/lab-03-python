import os
import csv
from matplotlib import pyplot as plt


def pede_pasta():
    pasta_dir = input("Insira o caminho para uma pasta:")
    if not os.path.isdir(pasta_dir):
        print("o ficheiro que inseriu nao é uma pasta!")
    return pasta_dir


def faz_calculos(nome_ficheiro):
    dict = {}
    for nome in os.listdir(nome_ficheiro):
        nome = os.path.splitext(nome)

        if nome[1] not in dict:
            dict[nome[1]] = {'quantidade': 1, 'volume': int(os.path.getsize(nome_ficheiro + nome[0] + nome[1]) / (1024))}
        else:
            dict[nome[1]]['quantidade'] += 1
            dict[nome[1]]['volume'] += int(os.path.getsize(nome_ficheiro + nome[0] + nome[1]) / (1024))
    print('Os resultados foram guardados no ficheiro `varios.csv`')
    return dict


def guarda_resultados():
    nome_ficheiro = input('Nome do Ficheiro: ')
    with open(f"{nome_ficheiro}.csv", 'w', newline='') as ficheiro:
        campos = ['Extensao','Quantidade','Tamanho[kByte]']
        writer = csv.DictWriter(ficheiro, fieldnames=campos)
        writer.writeheader()
        for chave in faz_calculos().keys():
            writer.writerow({'Extensao': chave,
                             'Quantidade':faz_calculos().get(chave)['quantidade'],
                             'Tamanho[kByte]':faz_calculos().get(chave)['volume']})


def faz_grafico_queijos(titulo, lista_chaves, lista_valores):
    plt.pie(lista_valores, labels=lista_chaves, autopct='%1.0f%%')
    plt.title(titulo)
    plt.show()


def faz_grafico_barras(titulo, lista_chaves, lista_valores):
    plt.bar(lista_chaves, lista_valores)
    plt.title(titulo)
    plt.show()