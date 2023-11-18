class Deposito():
  def __init__(self, valor):
    self.valor = valor


  def executar2(self, saldo):
       saldo = saldo + self.valor
       return saldo