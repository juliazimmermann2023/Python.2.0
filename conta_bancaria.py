class ContaBancaria:
    def __init__(self, numero, titular,saldo=0):
        self.numero= numero
        self.titular= titular
        self.saldo= saldo
        
    def deposita (self, valor):
        self.saldo += valor
    def exibir_detalhes(self):
        print("Número da conta:", self.numero)
        print("Titular:", self.titular)
        print("Saldo:", self.saldo)
    def sacar(self,valor):
        if self.saldo >=valor:
            self.saldo -=valor
        else: 
            print("Saldo insuficiente")
conta_da_julia = ContaBancaria("1234-5","Júlia",100)
conta_da_julia.deposita(500)
conta_da_julia.sacar(200)
conta_da_julia.exibir_detalhes()
