from analise_pasta import *

ficheiro = input('Ficheiro:')
lista_chaves = [*faz_calculos(ficheiro).keys()]
lista_valores = []

for qtd in faz_calculos(ficheiro).values():
    lista_valores.append(qtd['quantidade'])



faz_grafico_barras('quantidade',lista_chaves,lista_valores)
faz_grafico_queijos('quantidade', lista_chaves, lista_valores)