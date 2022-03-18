class Estacionamento:
  def __init__ (self, vaga, local, acao):
    self.vaga = vaga
    self.local = local
    self.acao = acao

  def print(self):
    print(f'A vaga {self.vaga} do {self.local} foi {self.acao}')

  def change(self, new_vaga, new_local, new_acao):
    self.vaga = new_vaga
    self.local = new_local
    self.acao = new_acao