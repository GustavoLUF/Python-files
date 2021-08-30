class Conta:
    def __init__(self, numero, nome_cliente, saldo, limite=1000.0):
        self.numero = numero
        self.titular = nome_cliente
        self.saldo = saldo
        self.limite = limite

    def get_titular(self):
        return self.titular
    
    def set_titular(self, nome):
        self.titular = nome

    def get_saldo(self):
        return self.saldo
    
    def get_numero(self):
        return self.numero
    
    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if self.saldo + self.limite < valor:
            print("Saldo Insuficiente.")
            return False
        else:
            self.saldo -= valor
            print("Saque realizado.")
            return True

    def transfere_para(self, destino, valor):
        retirou = self.saque(valor)
        if not retirou:
            print("Transferencia não realizada.")
            return False
        else:
            destino.deposito(valor)
            print("Transferencia realizada com sucesso.")
            return True

    def extrato(self):
        print(f"Extrato:\nNome: {self.titular}, Número: {self.numero}, Saldo: {self.saldo}")
        
    def __str__(self):
        return f'''        --Dados conta {self.titular}--
        Número: {self.numero}
        Nome do Cliente: {self.titular}
        Saldo: {self.saldo}
        Limite: {self.limite}
        '''

if __name__ == "__main__":
    
    conta1 = Conta("0001", "Gustavo", 33.50, 1000.0)
    print(conta1)
    print("Nome:", conta1.get_titular())
    print("Número:", conta1.get_numero())
    conta1.set_titular("Gustavo Lopes")
    print("Nome:", conta1.get_titular())
    conta1.deposito(100)
    print("Saldo:", conta1.get_saldo())
    conta1.saque(33)
    print("Novo Saldo:", conta1.get_saldo())
    conta2 = Conta("0002", "Luca", 0, 1000.0)
    print(conta1)
    conta1.transfere_para(conta2, 100)
    conta1.extrato()
    conta2.extrato()
    print(conta1)
    print(conta2)
    print("Métodos especiais:")
    print(conta1.__class__)
    print(conta1.__class__.__name__)
    print(conta1.__dict__)
    print(vars(conta1))