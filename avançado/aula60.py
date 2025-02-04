class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, quantia):
        self.saldo += quantia
        return self.saldo
    
    def sacar(self, quantia):
        if quantia <= self.saldo:
            self.saldo -= quantia
            return self.saldo
        else:
            return "Saldo insuficiente"
    
    def exibir_saldo(self):
        return f"Saldo atual: {self.saldo}"

# Criando uma instância da classe ContaBancaria
conta = ContaBancaria("Maria", 1000)

# Realizando operações
print(conta.depositar(500))
print(conta.sacar(200))
print(conta.exibir_saldo())