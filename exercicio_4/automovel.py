class Automovel():

    __MENSAGEM_ERRO = "ERRO: Capacidade Maxima Atingida!"

    def __init__(self,cap_dep,quant_comb,consumo):
        self.cap_dep = cap_dep
        self.quant_comb = quant_comb
        self.consumo = consumo

    def combustivel(self):
        return self.quant_comb

    def autonomia(self):
        return (int)((self.quant_comb / self.consumo ) * 100)

    def abastece(self,n_litros):
        self.quant_comb += n_litros

        if self.quant_comb > self.cap_dep:
            self.quant_comb -= n_litros
            return self.__MENSAGEM_ERRO


        return self.autonomia()

    def percorre(self,n_km):
        litros_necessarios = n_km / self.consumo

        if litros_necessarios < self.consumo:
            return self.autonomia() - n_km
        else:
            return -1

    @classmethod
    def cria_automovel(cls,cap,qtd,consumo):
        return cls(cap,qtd,consumo)