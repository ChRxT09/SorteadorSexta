class Jogador(object):
  def __init__(self, nome, posicao):
    self.nome = nome
    self.posicao = posicao

  def getNome(self): return self.nome
  def getPosicao(self): return self.posicao



def dividir(time1, time2):
  for i in range(len(Jogador)):
    if i % 2 == 0:
      time1.append(Jogador[i])
    else:
      time2.append(Jogador[i])


