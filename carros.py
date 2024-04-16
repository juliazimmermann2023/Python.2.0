class Carro:
    def __init__(self,marca,modelo,cor,ano):
        self.marca=marca
        self.modelo=modelo
        self.cor=cor
        self.ano=ano

    def exibir_informacoes():
        print("Marca:",self.marca)
        print("Modelo:",self.modelo)
        print("Cor:",self.cor)
        print("Ano:",self.ano)

carro1= Carro("Ranger Rover","Evoque","Prata",2021)
carro2= Carro("Chevrolet","Opala Collectors","Branco", 1979)
carro1.exibir_informacoes()
carro2.exibir_informacoes()
input()
