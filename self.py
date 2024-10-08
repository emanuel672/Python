import datetime
from Extrato import Extrato

class Conta:
    def_init_(self,clientes,numero,saldo)
    self.clientes = clientes
    self.numero = numero
    self.saldo = saldo
    self.sata 
    abertura = datetime.satetime.today()
    self.extrato = Extrato () 

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.trasacoes.append(["DEPOSITO", valor, "Data",datetime.datetime.today ()])

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()]) 
            return True

    def transfereValor(self, contadestino, valor):
        if self.saldo < valor:
            return "Não existe saldo suficiente"
        else:
            contadestino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(["TRANSFERENCIA", valor, "Data", datetime.datetime.today()]) 
            return "Transferencia Realizada"

    def gerarsaldo(self):
        print(f"numero: {self.unmero}\n saldo:{self.saldo}")

"""
class Conta():
    def _init_(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo
        
    def depositar(self, valor):
        self.saldo += valor
        
    def sacar(self,valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True
            
    def gerar_extrato(self):
        print(f"numero: {self.numero}\n cpf: {self.cpf}\nsaldo: {self.saldo}")     
        
def main():
    c1 = Conta(1,1,"Joao",0)
    c1.depositar(300)
    saque = c1.sacar(400)
    c1.gerar_extrato()
    print(f"O saque foi realizado? {saque}")
    

if __name__ == "_main_": 
    main()
"""

"""
class Conta:
    def _init_(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

def main():
    c1 = Conta(1,1,"Joao",1000) # Objeto sendo instanciado
    print (f"Nome do titular da conta: {c1.nomeTitular}")
    print (f"Número da conta: {c1.numero}")
    print (f"CPF do titular da conta: {c1.cpf}")
    print (f"Saldo da conta: {c1.saldo}")
    

# Quando um script python é executado, a variável reservada
# NAME referente a ele tem valor igual a "_main_".
# Nesse caso, a condição do IF a seguir será TRUE.
# Então o que está no corpo do IF será executado. No caso,
# é um chamado ao método main do script

if __name__ == "_main_": 
    main()
"""