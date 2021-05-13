from automovel import *

__TEXTO = "1... criar Automovel\n2...abastecer carro\n3... percorrer\n4...mostra autonomia\n5... Sair"


def main():
        carro = None
        print(__TEXTO)
        opcao = eval(input("Escolha a opcão:"))
        while True:
                if opcao == 1:
                        cap = eval(input("Capacidade: "))
                        quant_comb = eval(input("Quantidade do Combustivel: "))
                        consumo = eval(input("Consumo em litros aos 100 km: "))
                        carro = Automovel.cria_automovel(cap,quant_comb,consumo)
                elif opcao == 2:
                        n_litros = eval(input("Litros: "))
                        print(carro.abastece(n_litros))
                elif opcao == 3:
                        n_km = eval(input("Nº de Quilómetros a percorrer: "))
                        print(carro.percorre(n_km))
                elif opcao == 4:
                        print(carro.autonomia())
                elif opcao == 5:
                        break
                else:
                        print("Opcão Inválida, tente novamente!")
                opcao = eval(input("Escolha a opcão:"))



if __name__ == '__main__':
        main()

