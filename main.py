# class Aluno:
#   def __init__(self, nome, idade):
#     self.nome = nome
#     self.idade = idade

#   def display(self):
#     print(self.nome, self.idade)

# class Fundamental(Aluno):
#   def acrescentar(self):
#     print('Olá Alunos')


# aluno = Fundamental('Carlos',19)

# aluno.display()
# aluno.acrescentar()

#Exercício 4: Crie uma classe chamada Conta_bancaria com um atributo saldo inicializado com 0. Em seguida, crie métodos deposito e saque que atualizem o saldo. Crie um objeto da classe ContaBancaria, faça um depósito e um saque, e imprima o saldo resultante.

from saque import Saque
from deposito import Deposito


class Conta_Bancaria:
  def __init__(self, saldo=0):
    self.saldo = saldo


  def depositar(self, valor):
    deposito = Deposito(valor)
    self.saldo = deposito.executar2(valor)
    print(f'O deposito é R${valor}, e o saldo atual é R${self.saldo}')

  def sacar(self, valor):
    saque = Saque(valor)
    saldo_atual = saque.executar(self.saldo)
    if saldo_atual is not None:
      self.saldo = saldo_atual
      print(f'Saque R${valor}, saldo autal R${self.saldo}')

    else:
      print('Saldo insuficiente')

if __name__ == '__main__':
  conta = Conta_Bancaria(50)
  conta.depositar(20)
  conta.sacar(10)
    
    


    

    